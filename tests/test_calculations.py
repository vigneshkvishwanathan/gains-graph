from app.calculations import estimate_1rm, best_set_1rm

def test_estimate_1rm_uses_epley_formula():
    assert estimate_1rm(weight=140, reps=4) == 158.7

def test_best_set_1rm_returns_highest_estimate():
    sets = [
        {"weight_lbs": 125, "reps": 7, "partials": 1},
        {"weight_lbs": 140, "reps": 4, "partials": 1},
    ]
    assert best_set_1rm(sets) == 158.7

def test_best_set_1rm_ignores_partials():
    no_partials = [{"weight_lbs": 140, "reps": 4, "partials": 0}]
    many_partials = [{"weight_lbs": 140, "reps": 4, "partials": 5}]
    assert best_set_1rm(no_partials) == best_set_1rm(many_partials)
