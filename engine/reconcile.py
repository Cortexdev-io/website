"""Deterministic totals and reconciliation. Python owns every number; the model never does arithmetic."""
from __future__ import annotations

from dataclasses import dataclass, field
from decimal import Decimal

from .models import Issue, Position, Statement

TOLERANCE = Decimal("0.01")  # one centavo, for rounding of unit prices
ZERO = Decimal("0")


@dataclass
class StatementResult:
    statement: Statement
    computed_total: Decimal
    issues: list[Issue] = field(default_factory=list)


@dataclass
class Reconciliation:
    results: list[StatementResult]
    consolidated_cost_total: Decimal
    issues: list[Issue]
    excluded: list[str]  # statements dropped as duplicate snapshots
    currency: str = "BRL"
    algorithm_version: str = "1"


def computed_total(positions: list[Position]) -> Decimal:
    return sum((p.declared_value for p in positions), ZERO)


def check_line(p: Position) -> Issue | None:
    """quantity x avg price vs the line value; both are cost values at the same date."""
    expected = p.quantity * p.avg_price
    diff = p.declared_value - expected
    if abs(diff) <= TOLERANCE:
        return None
    return Issue("line_mismatch", "error", p.broker, expected, p.declared_value, diff,
                 f"{p.broker}/{p.ticker}: quantidade × preço médio = {expected}, mas o valor informado é {p.declared_value}.")


def reconcile(statements: list[Statement]) -> Reconciliation:
    seen: set[tuple] = set()
    results: list[StatementResult] = []
    excluded: list[str] = []
    all_issues: list[Issue] = []
    currencies = {s.currency for s in statements}
    if len(currencies) > 1:
        raise ValueError(f"mixed currencies {sorted(currencies)}: totals must be reported per currency")

    for s in statements:
        key = (s.broker, s.account, s.as_of)
        if key in seen:  # never add two snapshots of the same account and date
            excluded.append(s.source_file)
            all_issues.append(Issue("duplicate_snapshot", "warning", s.broker, ZERO, ZERO, ZERO,
                                    f"{s.source_file}: snapshot repetido de {s.broker}/{s.account} em {s.as_of}; excluído da soma."))
            continue
        seen.add(key)
        total = computed_total(s.positions)
        res = StatementResult(s, total)
        for p in s.positions:
            issue = check_line(p)
            if issue:
                res.issues.append(issue)
        if s.declared_total is not None:
            diff = s.declared_total - total
            if abs(diff) > TOLERANCE:
                res.issues.append(Issue(
                    "total_mismatch", "error", s.broker, total, s.declared_total, diff,
                    f"{s.broker}: total declarado {s.declared_total} difere da soma das posições {total} em {diff}."))
        results.append(res)
        all_issues.extend(res.issues)

    # The consolidated total uses the computed sum of positions, never the declared total.
    consolidated = sum((r.computed_total for r in results), ZERO)
    return Reconciliation(results, consolidated, all_issues, excluded)
