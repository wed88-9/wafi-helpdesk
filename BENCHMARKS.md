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



\## Current Test Result



The complete local test suite currently contains:



```text

12 tests passed

Breakdown:

Unit tests:          4 passed

Integration tests:   5 passed

Behavioural tests:   3 passed

\--------------------------------

Total:              12 passed

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

The runtime container:

\- Uses a non-root user

\- Includes only the required runtime dependencies

\- Exposes port 8000

\- Includes a readiness health check

Redis is also included in Docker Compose and is configured with a health check.

API Validation

Example valid request:

{

&#x20; "text": "All employees cannot access the system"

}

Expected classification:

{

&#x20; "team": "IT Support",

&#x20; "urgency": "urgent"

}

Invalid requests are rejected using FastAPI/Pydantic validation.

Performance Notes

The current implementation is a deterministic rule-based baseline.

No formal latency or throughput benchmark has been recorded yet.

Future performance measurements can include:

\- Average request latency

\- Requests per second

\- Container startup time

\- Memory usage

\- CPU usage

Summary

The current validation confirms that:

\- Functional tests pass

\- Behavioural tests pass

\- Ruff checks pass

\- Mypy checks pass

\- Import architecture checks pass

\- Docker image builds successfully

\- The API runs successfully with Docker Compose

