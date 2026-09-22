from src.adapters.model import WafiRuleModel


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

    golden_cases = [
        ("All employees cannot access the system", "IT Support", "urgent"),
        ("I forgot my password", "IT Support", "low"),
        ("I cannot login to the system", "IT Support", "medium"),
        ("My monitor is not working", "IT Support", "medium"),
    ]

    for text, expected_team, expected_urgency in golden_cases:
        team, urgency = model.predict(text)

        assert team == expected_team
        assert urgency == expected_urgency
