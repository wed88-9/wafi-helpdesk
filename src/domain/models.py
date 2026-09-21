from pydantic import BaseModel, ConfigDict, Field


class TicketRequest(BaseModel):
    model_config = ConfigDict(extra="forbid")

    text: str = Field(min_length=3, max_length=1000)


class TicketResponse(BaseModel):
    team: str
    urgency: str


class ErrorResponse(BaseModel):
    trace_id: str
    error: str
