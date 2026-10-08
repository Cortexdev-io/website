from __future__ import annotations

from dataclasses import dataclass, field
from datetime import date
from decimal import Decimal

CURRENCY = "BRL"


@dataclass(frozen=True)
class SourceLocation:
    """Where a value came from. Only set what is really known; never invent coordinates."""
    file: str
    sheet: str | None = None
    row: int | None = None
    column: str | None = None
    line: int | None = None
    excerpt: str | None = None


@dataclass(frozen=True)
class Position:
    broker: str
    ticker: str
    quantity: Decimal
    avg_price: Decimal
    declared_value: Decimal  # cost value as written in the source (cost basis, not market value)
    source: SourceLocation


@dataclass
class Statement:
    broker: str
    account: str
    as_of: date
    currency: str
    declared_total: Decimal | None
    positions: list[Position] = field(default_factory=list)
    source_file: str = ""
    extracted_by: str = "deterministic-parser"  # or "mock-provider" / a live model id


@dataclass(frozen=True)
class Issue:
    type: str
    severity: str  # "error" | "warning"
    broker: str
    expected: Decimal
    observed: Decimal
    difference: Decimal
    message: str
    detected_by: str = "deterministic-code"
