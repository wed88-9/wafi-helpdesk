FROM python:3.12-slim AS builder

WORKDIR /build
COPY pyproject.toml .
COPY requirements.txt .

RUN pip install --no-cache-dir --prefix=/install -r requirements.txt


FROM python:3.12-slim AS runtime

WORKDIR /app

COPY --from=builder /install /usr/local

COPY src ./src
COPY tests ./tests
RUN find /app -type f -name "*.py" -exec chmod 644 {} +
COPY pytest.ini .
COPY pyproject.toml .

RUN useradd --create-home --uid 10001 wafi \
    && chown -R wafi:wafi /app

USER wafi

EXPOSE 8000

HEALTHCHECK --interval=30s --timeout=5s --start-period=10s --retries=3 \
    CMD python -c "import urllib.request; urllib.request.urlopen('http://localhost:8000/ready')"

CMD ["uvicorn", "src.api.main:app", "--host", "0.0.0.0", "--port", "8000"]
