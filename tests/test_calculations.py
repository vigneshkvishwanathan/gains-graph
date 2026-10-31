from app.calculations import estimate_1rm

def test_estimate_1rm_uses_epley_formula():
    assert estimate_1rm(weight=140, reps=4) == 158.7
