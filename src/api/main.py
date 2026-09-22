import logging
from collections.abc import AsyncIterator
from contextlib import asynccontextmanager
from uuid import uuid4

from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse

from src.adapters.model import WafiRuleModel
from src.api.routes.batch import router as batch_router
from src.domain.models import TicketRequest
from src.logging_config import configure_logging
from src.service.ticket_service import TicketService

configure_logging()
logger = logging.getLogger(__name__)


@asynccontextmanager
async def lifespan(app: FastAPI) -> AsyncIterator[None]:
    app.state.service = TicketService(WafiRuleModel())
    logger.info("Wafi Helpdesk service started")
    yield
    logger.info("Wafi Helpdesk service stopped")


app = FastAPI(
    title="Wafi Helpdesk Ticket Triage",
    version="1.0.0",
    lifespan=lifespan,
)

app.include_router(batch_router)


@app.get("/health")
def health() -> dict[str, str]:
    return {"status": "ok"}


@app.get("/ready")
def ready(request: Request) -> dict[str, str]:
    if not hasattr(request.app.state, "service"):
        return {"status": "not_ready"}

    return {"status": "ready"}


@app.post("/v1/predict")
def predict(
    ticket: TicketRequest,
    request: Request,
) -> dict[str, object]:
    trace_id = str(uuid4())

    team, urgency = request.app.state.service.classify(ticket.text)

    logger.info(
        "Ticket classified",
        extra={
            "trace_id": trace_id,
            "team": team,
            "urgency": urgency,
        },
    )

    return {
        "trace_id": trace_id,
        "data": {
            "team": team,
            "urgency": urgency,
        },
    }


@app.exception_handler(Exception)
async def handle_error(
    request: Request,
    exc: Exception,
) -> JSONResponse:
    trace_id = str(uuid4())

    logger.exception(
        "Unhandled application error",
        extra={"trace_id": trace_id},
    )

    return JSONResponse(
        status_code=500,
        content={
            "trace_id": trace_id,
            "error": "Internal server error",
        },
    )

