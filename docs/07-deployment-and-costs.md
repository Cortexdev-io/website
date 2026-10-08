# 07 - Deployment and costs (checklist only; nothing is deployed)

## Defaults (proposals for the founder to confirm; read from environment with safe fallbacks)
| Variable | Default | Meaning |
|---|---|---|
| `CORTEX_MAX_FILE_BYTES` | 5242880 | max upload, 5 MB |
| `CORTEX_MAX_PAGES` | 20 | max pages per document |
| `CORTEX_DEMO_CALLS_PER_IP_PER_HOUR` | 5 | public demo quota |
| `CORTEX_DAILY_SPEND_CEILING_USD` | 0 | no real API calls unless raised |
| `CORTEX_API_KILL_SWITCH` | true | blocks API calls |
| `CORTEX_LIVE_ENDPOINT_ENABLED` | false | live endpoint off |

Implemented today: only the live-label gate (`engine/provider.py: live_enabled`). The limits above are declared in `.env.example` but **not yet enforced by code** (no upload or API endpoint exists).

## Static site (Cloudflare Worker `cortexdev`)
- [ ] `uv run pytest -q` green, including `tests/test_repo_exposure.py`
- [ ] Review the branch diff; merge to `main` only with founder approval (deploys from `main`)
- [ ] After deploy, check `/`, `/demo/`, `/demo/resultado/`, `/privacidade/`, `/termos/`, 404
- [ ] Rollback: revert the merge commit on `main`

## Not covered yet
Backend hosting, database, object storage, secrets store, domain `app.`/`api.` subdomains (need DNS approval), cost projections for the Claude API (no measured usage; measured cost so far US$ 0).