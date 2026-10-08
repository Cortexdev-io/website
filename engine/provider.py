"""Extraction provider interface. Only a mock exists; no network call is ever made here.

The mock replays a recorded extraction keyed by the SHA-256 of the input text, so it can
never be mistaken for a live model call: every result carries is_live=False.
"""
from __future__ import annotations

import hashlib
import json
import os
from dataclasses import dataclass
from datetime import date
from pathlib import Path
from typing import Protocol

from .models import CURRENCY, Position, SourceLocation, Statement
from .numbers import parse_decimal

DEMO_LABEL_DEFAULT = "Modo demonstrativo (resultados reproduzidos)"
DEMO_LABEL_LIVE = "Demonstração ao vivo com Claude API"
FIXTURES = Path(__file__).resolve().parent.parent / "fixtures"


class ProviderError(RuntimeError):
    pass


@dataclass(frozen=True)
class ExtractionResult:
    statement: Statement
    provider: str
    is_live: bool
    cost_usd: float


class ExtractionProvider(Protocol):
    name: str
    is_live: bool

    def extract_statement(self, text: str, filename: str) -> ExtractionResult: ...


class MockProvider:
    name = "mock"
    is_live = False

    def __init__(self, recordings: Path = FIXTURES / "gama_capital_extraction.json"):
        self._recordings = json.loads(recordings.read_text(encoding="utf-8-sig"))

    def extract_statement(self, text: str, filename: str) -> ExtractionResult:
        digest = hashlib.sha256(text.encode("utf-8")).hexdigest()
        rec = self._recordings.get(digest)
        if rec is None:
            raise ProviderError(f"mock provider has no recording for {filename} (sha256 {digest[:12]}…)")
        positions = [
            Position(
                broker=rec["broker"], ticker=p["ticker"],
                quantity=parse_decimal(p["quantity"], "en-US"),
                avg_price=parse_decimal(p["avg_price"], "en-US"),
                declared_value=parse_decimal(p["declared_value"], "en-US"),
                source=SourceLocation(file=filename, line=p["line"], excerpt=p["excerpt"]),
            )
            for p in rec["positions"]
        ]
        stmt = Statement(
            rec["broker"], rec["account"], date.fromisoformat(rec["as_of"]), CURRENCY,
            parse_decimal(rec["declared_total"], "en-US"), positions, filename,
            extracted_by="mock-provider",
        )
        return ExtractionResult(stmt, self.name, False, 0.0)


def live_enabled(env: dict[str, str] | None = None) -> bool:
    """True only if key present, live endpoint enabled, kill switch off and ceiling > 0."""
    e = os.environ if env is None else env
    try:
        ceiling = float(e.get("CORTEX_DAILY_SPEND_CEILING_USD", "0") or 0)
    except ValueError:
        ceiling = 0.0
    return bool(
        e.get("ANTHROPIC_API_KEY", "").strip()
        and e.get("CORTEX_LIVE_ENDPOINT_ENABLED", "false").lower() == "true"
        and e.get("CORTEX_API_KILL_SWITCH", "true").lower() == "false"
        and ceiling > 0
    )


def demo_label(provider: ExtractionProvider, env: dict[str, str] | None = None) -> str:
    """The live label requires a live provider AND live_enabled(); mock output never gets it."""
    return DEMO_LABEL_LIVE if provider.is_live and live_enabled(env) else DEMO_LABEL_DEFAULT


def get_provider(env: dict[str, str] | None = None) -> ExtractionProvider:
    """Always the mock for now. A real Anthropic adapter is not implemented in this slice."""
    return MockProvider()
