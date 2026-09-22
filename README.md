\# Wafi Helpdesk Ticket Triage



A FastAPI-based helpdesk ticket triage service that classifies support tickets by responsible team and urgency.



\## Overview



Wafi Helpdesk receives a ticket description and returns:



\- The responsible support team

\- The ticket urgency

\- A unique trace ID for request tracking



The current implementation uses a deterministic rule-based model as a baseline.



\## Tech Stack



\- Python 3.12

\- FastAPI

\- Pydantic

\- Uvicorn

\- Docker / Docker Compose

\- Redis

\- Pytest

\- Ruff

\- Mypy

\- Import Linter



\## Project Structure



```text

wafi-helpdesk/

├── src/

│   ├── adapters/

│   │   └── model.py

│   ├── api/

│   │   └── main.py

│   ├── domain/

│   │   └── models.py

│   └── service/

│       └── ticket\_service.py

├── tests/

│   ├── unit/

│   ├── integration/

│   ├── behavioural/

│   └── fixtures/

├── Dockerfile

├── docker-compose.yml

├── pyproject.toml

├── pytest.ini

├── requirements.txt

└── README.md

API Endpoints

Health Check

GET /health

Response:

{

&#x20; "status": "ok"

}

Readiness Check

GET /ready

Response:

{

&#x20; "status": "ready"

}

Ticket Prediction

POST /v1/predict

Request:

{

&#x20; "text": "All employees cannot access the system"

}

Response:

{

&#x20; "trace\_id": "generated-uuid",

&#x20; "data": {

&#x20;   "team": "IT Support",

&#x20;   "urgency": "urgent"

&#x20; }

}

Validation

Ticket text must contain between 3 and 1000 characters.

Unknown request fields are rejected.

Example of an invalid request:

{

&#x20; "text": ""

}

The API returns HTTP 422.

Running with Docker Compose

Build the API image:

docker compose build wafi-api

Start the services:

docker compose up

The API runs on:

http://localhost:8000

FastAPI Swagger documentation:

http://localhost:8000/docs

Testing

Run all tests:

docker compose run --rm wafi-api pytest

Run Ruff:

docker compose run --rm wafi-api ruff check src tests

Run Mypy:

docker compose run --rm wafi-api mypy src

Run Import Linter:

docker compose run --rm wafi-api lint-imports

Quality Checks

The project includes:

\- Unit tests for ticket classification

\- Integration tests for the FastAPI endpoints

\- Behavioural tests for model behaviour

\- Golden reference tests

\- Ruff linting

\- Mypy static type checking

\- Import Linter architecture checks

Current checks verify that the domain layer does not depend on the API layer.

Docker Security

The Docker image uses a multi-stage build to separate dependency installation from the runtime image.

The application runs as a non-root user:

wafi

Python source files are also given non-executable permissions inside the image.

Model Behaviour

The baseline model applies deterministic rules to classify tickets.

Examples:

Ticket	Team	Urgency

All employees cannot access the system	IT Support	urgent

Forgot password	IT Support	low

Cannot login	IT Support	medium

Unknown ticket	IT Support	medium





Development

The project is structured into separate layers:

\- api — HTTP endpoints

\- service — application/service logic

\- domain — request and response models

\- adapters — model implementation

This separation makes the model implementation replaceable without changing the API layer.

License

This project was developed as part of a software engineering project.

## Training Program

This project was completed as part of the **SDA-AIE-113 — Software Engineering Practices for AI Systems** training program at **SDAIA Academy**, under the supervision of **Abdullah Khalid AlShahrani**.

The portfolio demonstrates the practical application of software engineering practices for AI systems — building a production-style AI/ML service through:

- Clean architecture
- A well-defined API contract
- Containerization
- A layered automated testing suite
- CI/CD with branch protection
- Safe configuration, secrets, and logging management

### Official SDAIA Academy GitHub

https://github.com/SDAIAAcademy