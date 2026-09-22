import json
from pathlib import Path

from src.adapters.model import WafiRuleModel


def load_golden_cases():
    path = Path("tests/fixtures/golden_cases.json")
    return json.loads(path.read_text(encoding="utf-8"))


def test_invariance_case_and_whitespace():
    model = WafiRuleModel()

    result_1 = model.predict("All employees cannot access the system")
    result_2 = model.predict("ALL EMPLOYEES CANNOT ACCESS THE SYSTEM")

    assert result_1 == result_2


def test_directional_full_outage_must_be_urgent():
    model = WafiRuleModel()

    _, normal_urgency = model.predict("I cannot login to the system")
    _, outage_urgency = model.predict("All employees cannot access the system")

    assert normal_urgency == "medium"
    assert outage_urgency == "urgent"


def test_golden_reference_cases():
    model = WafiRuleModel()

    for case in load_golden_cases():
        team, urgency = model.predict(case["text"])

        assert team == case["team"]
        assert urgency == case["urgency"]
