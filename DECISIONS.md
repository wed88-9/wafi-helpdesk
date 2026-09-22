\# Architecture and Engineering Decisions



This document records the main technical decisions made for the Wafi Helpdesk Ticket Triage project.



\## Decision 1 — Use FastAPI



\### Decision



Use FastAPI as the API framework.



\### Reason



FastAPI provides:



\- Clear API endpoint definitions

\- Automatic request validation

\- OpenAPI/Swagger documentation

\- Good support for Python type annotations

\- Simple integration with automated tests



\---



\## Decision 2 — Use a Rule-Based Baseline Model



\### Decision



Use a deterministic rule-based classifier as the initial ticket triage model.



\### Reason



The project requires predictable and reproducible behaviour.



A rule-based baseline makes it easy to:



\- Test expected outcomes

\- Explain classification decisions

\- Create behavioural tests

\- Establish golden reference cases



The model can be replaced with a more advanced machine-learning model later.



\---



\## Decision 3 — Separate the Application into Layers



\### Decision



Separate the application into API, service, domain, and adapter layers.



\### Structure



```text

API

&#x20;↓

Service

&#x20;↓

Adapter / Model



Domain models are shared by the application layers.

Reason

This separation improves maintainability and makes individual components easier to replace or test.

An Import Linter contract also ensures that the domain layer does not depend on the API layer.

Decision 4 — Use Docker Multi-Stage Builds

Decision

Use a multi-stage Docker build with a separate builder and runtime stage.

Reason

The builder stage installs project dependencies, while the runtime stage contains the application and required dependencies.

The runtime container also runs using a non-root user.

This provides a cleaner and more secure container setup.

Decision 5 — Use Automated Quality Checks

Decision

Use automated tests and static analysis as part of the development workflow.

Tools

\- Pytest for testing

\- Ruff for linting

\- Mypy for type checking

\- Import Linter for architecture validation

Reason

These checks help detect:

\- Functional regressions

\- Code quality problems

\- Type errors

\- Unwanted architectural dependencies

The checks can also be integrated into CI/CD so that changes are validated automatically.

