.PHONY: install test lint image smoke

install:
pip install -r requirements.txt

test:
docker compose run --rm wafi-api pytest

lint:
docker compose run --rm wafi-api ruff check src tests
docker compose run --rm wafi-api mypy src
docker compose run --rm wafi-api lint-imports

image:
docker compose build wafi-api

smoke:
docker compose up -d
Invoke-RestMethod http://localhost:8000/ready
