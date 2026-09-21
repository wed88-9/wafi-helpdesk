from contextlib import asynccontextmanager
from uuid import uuid4

from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse

from src.adapters.model import WafiRuleModel
from src.domain.models import TicketRequest
from src.service.ticket_service import TicketService


@asynccontextmanager
async def lifespan(app: FastAPI):
    app.state.service = TicketService(WafiRuleModel())
    yield


app = FastAPI(
    title="Wafi Helpdesk Ticket Triage",
    version="1.0.0",
    lifespan=lifespan,
)


@app.get("/health")
def health() -> dict[str, str]:
    return {"status": "ok"}


@app.get("/ready")
def ready(request: Request) -> dict[str, str]:
    if not hasattr(request.app.state, "service"):
        return {"status": "not_ready"}
    return {"status": "ready"}


@app.post("/v1/predict")
def predict(ticket: TicketRequest, request: Request) -> dict:
    trace_id = str(uuid4())
    team, urgency = request.app.state.service.classify(ticket.text)

    return {
        "trace_id": trace_id,
        "data": {
            "team": team,
            "urgency": urgency,
        },
    }


@app.exception_handler(Exception)
async def handle_error(request: Request, exc: Exception) -> JSONResponse:
    trace_id = str(uuid4())

    return JSONResponse(
        status_code=500,
        content={
            "trace_id": trace_id,
            "error": "Internal server error",
        },
    )
