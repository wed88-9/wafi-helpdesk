from fastapi import APIRouter, Request

from src.domain.models import TicketRequest

router = APIRouter(prefix="/v1", tags=["batch"])


@router.post("/predict-batch")
def predict_batch(
    tickets: list[TicketRequest],
    request: Request,
) -> dict[str, object]:
    service = request.app.state.service

    results = []
    for ticket in tickets:
        team, urgency = service.classify(ticket.text)
        results.append(
            {
                "team": team,
                "urgency": urgency,
            }
        )

    return {
        "count": len(results),
        "data": results,
    }
