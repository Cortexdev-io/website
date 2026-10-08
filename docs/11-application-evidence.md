# 11 - Application evidence

## Status of the Claude Startups application
Submitted by the founder around 7 October 2026 using contato@cortexdev.io. **Decision pending; no outcome confirmed.** This file is not a new application and nothing here was submitted.

## Project stage
Prototype. A static website with a recorded demonstration (synthetic data) and a local deterministic engine. No production deployment of the engine.

## What exists (same facts as the README)
- Public site: https://cortexdev.io (the homepage reposition is on a local branch, not yet published at the time of writing). Recorded demo: https://cortexdev.io/demo/ and /demo/resultado/ (a static record of a run done in claude.ai, not a live API execution).
- Engine in `engine/`: Brazilian-locale parsing of CSV and XLSX, `Decimal` totals, reconciliation that reproduces the R$ 600,00 divergence (declared R$ 43.220,00 against computed R$ 42.620,00; consolidated cost R$ 149.025,00), safe CSV export. 46 automated tests pass (`uv run pytest -q`).
- Division of work: Claude interprets free-text documents; deterministic code does all arithmetic and comparison. In the engine this is currently only a design: the provider is a mock replaying a recorded extraction.

## What does not exist
Real Claude API integration (no API call has ever been made by this code; measured spend US$ 0), PDF reading, web app, login, database, evaluation dataset, accuracy measurements, pilots.

## Not stated
Revenue, customers, funding and legal incorporation: none are claimed. Whether a company is legally incorporated and the founding date are for the founder to clarify; owning the domain does not establish either.