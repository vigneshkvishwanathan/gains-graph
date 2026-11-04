def check_lift_row(row, lift_names):
    problems = []
    if row["lift"] not in lift_names:
        problems.append(f"unknown lift: {row['lift']}")
    return problems
