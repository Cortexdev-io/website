"""Safe CSV export. Cells starting with a formula trigger are neutralised."""
from __future__ import annotations

import csv
import io

from .reconcile import Reconciliation

_TRIGGERS = ("=", "+", "-", "@", "\t", "\r")


def safe_cell(value) -> str:
    """Prefix a single quote when a text cell could be run as a formula by a spreadsheet.

    Numbers are passed as Decimal strings by the callers; a leading '-' on a real negative
    number is therefore also prefixed, which is the conservative (OWASP) behaviour.
    """
    text = "" if value is None else str(value)
    return "'" + text if text.startswith(_TRIGGERS) else text


def positions_csv(rec: Reconciliation) -> str:
    buf = io.StringIO()
    w = csv.writer(buf, lineterminator="\n")
    w.writerow(["broker", "ticker", "quantity", "avg_price", "declared_value", "currency", "source"])
    for r in rec.results:
        for p in r.statement.positions:
            loc = p.source
            where = f"{loc.file}:{loc.sheet + '!' if loc.sheet else ''}{'row ' + str(loc.row) if loc.row else 'line ' + str(loc.line)}"
            w.writerow([safe_cell(x) for x in (p.broker, p.ticker, p.quantity, p.avg_price,
                                               p.declared_value, r.statement.currency, where)])
    return buf.getvalue()
