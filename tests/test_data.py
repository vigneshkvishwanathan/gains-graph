from app.data import load_lifts

def test_load_lifts_converts_numbers(tmp_path):
    csv_file = tmp_path/"lifts.csv"
    csv_file.write_text(
        "data,lift,weight_lbs,reps,partials\n"
        "2026-10-30,smith machine overhead press,140,4,1\n"
    )
    
    rows = load_lifts(csv_file)
    
    assert rows[0]["weight_lbs"] == 140
    assert rows[0]["reps"] == 4
    assert rows[0]["partials"] == 1
