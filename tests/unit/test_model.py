from src.adapters.model import WafiRuleModel


def test_full_outage_is_urgent():
    model = WafiRuleModel()
    team, urgency = model.predict("All employees cannot access the system")
    assert team == "IT Support"
    assert urgency == "urgent"


def test_password_issue_is_low():
    model = WafiRuleModel()
    team, urgency = model.predict("I forgot my password")
    assert team == "IT Support"
    assert urgency == "low"


def test_login_problem_is_medium():
    model = WafiRuleModel()
    team, urgency = model.predict("I cannot login to the system")
    assert team == "IT Support"
    assert urgency == "medium"


def test_unknown_ticket_defaults_to_medium():
    model = WafiRuleModel()
    team, urgency = model.predict("My monitor is not working")
    assert team == "IT Support"
    assert urgency == "medium"
