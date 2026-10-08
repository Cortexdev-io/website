# 04 - Financial data model (as implemented)

- Amounts are `Decimal`; floats from spreadsheets are converted through `repr`.
- Number parsing (`engine/numbers.py`): `1.234,56`, `R$ 1.234,56`, `1,234.56`, `(10,00)`, `-5`. A single separator followed by exactly three digits (`1.200`, `1,500`) is **ambiguous** and raises unless the locale (`pt-BR` or `en-US`) is given. Each parser passes the locale of its source.
- A position line holds a cost value (quantity x average price). Market value is not modelled and is never added to cost.
- Line check: `|declared_value - quantity x avg_price| <= R$ 0.01`, else `line_mismatch`.
- Statement check: `|declared_total - sum(positions)| <= R$ 0.01`, else `total_mismatch`. The source is never altered.
- Consolidated cost total = sum of the **computed** sums per statement (not the declared totals).
- Two statements with the same broker, account and as-of date: the second is excluded with a `duplicate_snapshot` warning.
- Mixed currencies raise an error; no conversion exists.
- Every issue records `detected_by = "deterministic-code"`.

## Canonical fixture (synthetic)
| Source | Declared | Computed |
|---|---|---|
| Corretora Alfa (CSV) | 54.220,00 | 54.220,00 |
| Beta Invest (XLSX) | 52.185,00 | 52.185,00 |
| Gama Capital (email, mock extraction) | 43.220,00 | 42.620,00 (difference 600,00) |
| Consolidated cost total | | 149.025,00 |

Tests: `tests/test_engine.py`.