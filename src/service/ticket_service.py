from src.adapters.model import TicketModel


class TicketService:
    def __init__(self, model: TicketModel) -> None:
        self._model = model

    def classify(self, text: str) -> tuple[str, str]:
        return self._model.predict(text)
