# 02 - Architecture decision (ADR)

**Status:** accepted for the vertical slice. **Date:** 2026-10-08.

## Context
The public site is static (Cloudflare Worker with static assets, `wrangler.jsonc`, `assets.directory = ./`). The product needs deterministic financial logic that cannot run in that Worker. The founder works on Windows/PowerShell, with no API key and no spend.

## Decision
- Keep the marketing site untouched as static files.
- Put the engine in a separate Python package (`engine/`) in the same repository, with `uv` and `pytest`; no `make`, Bash or Docker.
- Python owns every number (`Decimal`). The model only interprets documents, behind an `ExtractionProvider` interface. The only implementation is `MockProvider`, which replays a recorded extraction keyed by SHA-256 and reports `is_live=False`.
- Regular formats (CSV, XLSX) are parsed deterministically; free text (the Gama email) goes through the provider.
- All non-public folders are listed in `.assetsignore`; a test fails if a root entry is neither ignored nor declared public.

## Consequences
- Done: parse, totals, reconciliation, safe CSV export, mock provider, demo label flag.
- Not done: FastAPI, database, auth, real Anthropic adapter, PDF, evaluation dataset. The backend must be hosted outside the Worker (see future `docs/07`).
- Fixtures were rebuilt from `/demo/` because `demo_dados` was not in the repository; they reproduce every figure in the brief.

## Trade-offs
Keeping the engine in the public repo is cheap and simple but means everything committed is public: synthetic data only, no secrets.