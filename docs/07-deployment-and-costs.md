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

## Release to production (prepared only; nothing has been done)
**What changes on `main`:** `assets/css/style.css` (the `/demo/` overflow fix and a few new rules), `index.html` (homepage repositioning; copy pending founder approval in `docs/review-home-copy-diff.md`), and new non-public folders and files (`engine/`, `tests/`, `fixtures/`, `docs/`, `scripts/`, `pyproject.toml`, `uv.lock`, `.env.example`) all listed in `.assetsignore`. `.assetsignore` also drops two entries for files that do not exist.

**What Cloudflare does on push:** the Worker `cortexdev` is deployed from `main`, so a push to `main` rebuilds and publishes it. This branch must not be pushed to `main` before approval.

**Before merging:** founder approves the copy table; `uv run pytest -q` shows 46 passed; link checker shows no new problems (one pre-existing, inactive reference to `assets/img/demo-hero.png`, only loaded if `demoImagem` is true in `config.js`).

**After release, measure** (Playwright, `scrollWidth` against `clientWidth`) on `https://cortexdev.io/demo/`: at 768 px and 800 px expect 768 and 800 (before: 952 on both); also 320, 390, 1024 and 1440 px unchanged. Check `/`, `/demo/resultado/`, `/privacidade/`, `/termos/` and the 404 page load without console errors, and that `https://cortexdev.io/engine/`, `/docs/`, `/fixtures/`, `/tests/`, `/pyproject.toml` and `/.env.example` return 404.

**Rollback (only after the founder approves a push):** `git revert -m 1 <merge-commit>` on `main`, then `git push origin main`. Use `-m 1` only if the merge was a merge commit; for a fast-forward or squash, revert the commit range or the squash commit instead.
