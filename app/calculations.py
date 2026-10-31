def estimate_1rm(weight, reps):
    return round(weight * (1 + reps/30), 1)

def best_set_1rm(sets):
    estimates = [estimate_1rm(s["weight_lbs"], s["reps"]) for s in sets]
    return max(estimates)
