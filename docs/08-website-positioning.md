# 08 - Website positioning: public claims

Status values: **Implemented** (verifiable in the repository), **Static record** (recorded, not live), **Service** (offered manually, not software), **Planned** (not built).

| Claim on the site | Where | Status | Evidence / note |
|---|---|---|---|
| Cortex Financial Engine is in development | hero eyebrow, `#como` | Implemented | stated as in development |
| Reads CSV and XLSX in Brazilian format, Decimal totals, reproduces the R$ 600,00 divergence, safe CSV export, local and synthetic only | `#como` card "Hoje, em código e com testes"; FAQ | Implemented | `tests/test_engine.py`, 46 tests; code is not deployed on the site |
| Provider interface exists but is simulated; no Claude API call | `#como`; FAQ | Implemented | `engine/provider.py` |
| PDF, Claude API integration, web app with login, client uploads, open pilot do not exist | `#como`; FAQ | Accurate | listed as "Ainda não existe" |
| Demonstration with fictitious data | hero trust line, `#demo`, `/demo/` | Static record | recorded in claude.ai; label kept; not a live run |
| "Claude interpreta documentos; nosso motor confere os números" | hero | Partial | true of the recorded demo; in the engine the provider is a mock |
| "Sem recomendações de investimento" | hero trust line, FAQ | Implemented | no such feature exists |
| "Revisão humana para exceções" | hero trust line | Planned | divergences are listed as exceptions; there is no review interface yet |
| "Divergência sinalizada pelo código" (R$ 600,00) | `#demo`, hero animation | Implemented | `test_r600_discrepancy_and_consolidated_total`; the hero animation is labelled illustrative |
| Security list (API keys on server, minimal access, deletion at end of project, Claude processing may occur outside Brazil) | `#seguranca` | Service | project commitments, not product features; unchanged from `main`; needs legal review |
| Fixed-scope packages R$529, R$897, R$1.497; first version in up to 72h; 20-minute call | `#servicos`, `#oferta`, strip | Service | unchanged from `main`; custom projects, not product pricing |
| Participation in a limited pilot, synthetic files at first | `#piloto`; FAQ | Planned | no open slots; contact only |
| Founder background, no clients or revenue claimed | `#quem` | Implemented | unchanged from `main` |
| "A Cortex Dev é independente e não é afiliada à Anthropic" | footer | Implemented | unchanged |

Cannot be claimed yet: accuracy figures, customers, a live Claude pipeline, encryption or retention periods, regulatory compliance.