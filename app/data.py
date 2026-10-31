import csv

def load_lifts(path):
    with open(path) as f:
        rows = list(csv.DictReader(f))
    for row in rows:
        row["weight_lbs"] = float(row["weight_lbs"])
        row["reps"] = int(row["reps"])
        row["partials"] = int(row["partials"])
    return rows
    