"""Local end-to-end run on the synthetic fixtures. Usage: uv run python -m engine.cli demo"""
from __future__ import annotations

import sys
from decimal import Decimal

from .parsers import parse_alfa_csv, parse_beta_xlsx
from .provider import FIXTURES, demo_label, get_provider
from .reconcile import Reconciliation, reconcile


def brl(v: Decimal) -> str:
    s = f"{v:,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")
    return f"R$ {s}"


def run_demo() -> Reconciliation:
    provider = get_provider()
    email = (FIXTURES / "gama_capital_email.txt").read_text(encoding="utf-8")
    statements = [
        parse_alfa_csv(FIXTURES / "corretora_alfa.csv"),
        parse_beta_xlsx(FIXTURES / "beta_invest.xlsx"),
        provider.extract_statement(email, "gama_capital_email.txt").statement,
    ]
    rec = reconcile(statements)
    print(f"[{demo_label(provider)}] provedor={provider.name} ao_vivo={provider.is_live} custo=US$ 0")
    for r in rec.results:
        s = r.statement
        print(f"{s.broker}: declarado {brl(s.declared_total)} | calculado {brl(r.computed_total)} ({s.extracted_by})")
    print(f"Custo total consolidado: {brl(rec.consolidated_cost_total)}")
    for i in rec.issues:
        print(f"DIVERGÊNCIA [{i.type}] {i.message} (detectada por: {i.detected_by})")
    return rec


if __name__ == "__main__":
    if sys.argv[1:] != ["demo"]:
        sys.exit("uso: python -m engine.cli demo")
    run_demo()
