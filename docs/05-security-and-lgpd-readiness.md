# 05 - Security and LGPD readiness

**This is a readiness note, not a compliance statement. Legal review is still required before any real client data is processed.**

## Implemented (verifiable in the repository)
| Item | Evidence |
|---|---|
| Only synthetic data is used | `fixtures/`; all names and tickers are fictitious |
| No secrets committed | manual pattern scan before each commit (no scanner installed); `.env` is in `.gitignore` and `.assetsignore`; only `.env.example` with empty placeholders exists |
| Non-public paths are not served by the Worker | `.assetsignore` plus `tests/test_repo_exposure.py` fails if a root entry is neither ignored nor declared public |
| No network calls in the engine | `engine/` has no HTTP or SDK imports; the only provider is `MockProvider` (`is_live=False`) |
| The live label cannot be shown for mock output | `engine/provider.py` `demo_label`, tested |
| Spreadsheets are read without evaluating formulas | `openpyxl` read-only, `data_only=True` |
| CSV export neutralises formula triggers | `engine/export.py`, tested |

## Missing (not started)
- Authentication, authorization and tenant isolation.
- Private file storage, upload validation (type, size, signature, pages), rate limits and CORS.
- Retention, deletion and backup policies, and code that enforces them.
- Audit log and structured logs without personal data.
- Data processing agreement with Anthropic and any hosting provider; list of sub-processors; position on international transfer.
- Controller or processor role definition and a privacy notice for the product (the current `/privacidade/` page covers the website and services and needs review).
- Prompt-injection tests against a real model (no real model is called yet).
- The limits in `.env.example` are declared but not enforced, because no endpoint exists.

## Open legal question (for a Brazilian lawyer; unanswered)
Does a service for independent investment advisory firms touch CVM rules, including confidentiality duties, handling of client data, and the boundary between data processing and investment advice? Record the question and the answer here once obtained.

## Gate
No real client or personal financial data until the missing items above are done and the legal question is answered.