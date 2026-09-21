from typing import Protocol


class TicketModel(Protocol):
    def predict(self, text: str) -> tuple[str, str]:
        """Return the responsible team and urgency."""
        ...


class WafiRuleModel:
    """Deterministic baseline model for helpdesk ticket triage."""

    def predict(self, text: str) -> tuple[str, str]:
        normalized = text.lower()

        outage_keywords = [
            "all employees",
            "everyone",
            "entire system",
            "system is down",
            "full outage",
            "service outage",
            "completely down",
        ]

        if any(keyword in normalized for keyword in outage_keywords):
            return "IT Support", "urgent"

        if any(
            keyword in normalized
            for keyword in ["password", "reset password", "forgot password"]
        ):
            return "IT Support", "low"

        if any(
            keyword in normalized
            for keyword in ["cannot login", "can't login", "login problem", "access"]
        ):
            return "IT Support", "medium"

        return "IT Support", "medium"
