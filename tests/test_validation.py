from app.validation import check_lift_row

LIFT_NAMES = ["smith machine overhead press", "t bar row"]

def test_valid_row_has_no_problems():
    row = {"date": "2026-10-30", "lift": "t bar row", "weight_lbs": "80", "reps": "6", "partials": "1"}
    assert check_lift_row(row, LIFT_NAMES) == []

def test_unknown_lift_is_reported():
    row = {"date": "2026-10-30", "lift": "t bar rwo", "weight_lbs": "80", "reps": "6", "partials": "1"}
    assert check_lift_row(row, LIFT_NAMES) == ["unknown lift: t bar rwo"]
