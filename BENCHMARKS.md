\# Benchmarks



\## Purpose



This document records the basic validation and performance checks performed on the Wafi Helpdesk Ticket Triage service.



\## Environment



\- Python: 3.12

\- API framework: FastAPI

\- Runtime: Docker

\- Container orchestration: Docker Compose

\- Model: Deterministic rule-based classifier



\## Functional Test Results



The project includes three test groups:



\### Unit Tests



Unit tests verify the ticket classification rules.



Covered cases include:



\- Full system outage → urgent

\- Password issue → low

\- Login problem → medium

\- Unknown ticket → medium



\### Integration Tests



Integration tests verify the FastAPI endpoints and request validation.



Covered endpoints and behaviours include:



\- `GET /health`

\- `GET /ready`

\- `POST /v1/predict`

\- Invalid short text

\- Unknown request fields



\### Behavioural Tests



Behavioural tests verify important model behaviours, including:



\- Case and whitespace invariance

\- Full outage classification

\- Golden reference cases



## Current Test Result

The complete local test suite currently contains:

```text
13 tests passed
Branch coverage: 91%

Breakdown:
Unit tests:          4 passed
Integration tests:   6 passed
Behavioural tests:   3 passed
--------------------------------
Total:              13 passed
Static Analysis
Ruff
Command:
docker compose run --rm wafi-api ruff check src tests
Result:
All checks passed!
Mypy
Command:
docker compose run --rm wafi-api mypy src
Result:
Success: no issues found in 9 source files
Import Linter
Command:
docker compose run --rm wafi-api lint-imports
Result:
Contracts: 1 kept, 0 broken
Architecture contract:
Domain must not depend on API
Docker Validation
The application is packaged using a multi-stage Docker build.
Measured Docker image size:
395 MB
Build time:
1.25 seconds
The runtime container:
- Uses a non-root user
- Includes only the required runtime dependencies
- Exposes port 8000
- Includes a readiness health check
Redis is also included in Docker Compose and is configured with a health check.
Test Performance
Measured complete test and coverage execution time:
3.21 seconds
This run completed with:
13 tests passed
Branch coverage: 91%
API Validation
Example valid request:
{
  "text": "All employees cannot access the system"
}
Expected classification:
{
  "team": "IT Support",
  "urgency": "urgent"
}
Invalid requests are rejected using FastAPI/Pydantic validation.
Performance Notes
The current implementation is a deterministic rule-based baseline.
Measured results from the local environment:
Metric	Result
Docker image size	395 MB
Docker build time	1.25 seconds
Test + coverage time	3.21 seconds
Branch coverage	91%
Tests passed

Summary

The current validation confirms that:

\- Functional tests pass

\- Behavioural tests pass

\- Ruff checks pass

\- Mypy checks pass

\- Import architecture checks pass

\- Docker image builds successfully

\- The API runs successfully with Docker Compose

