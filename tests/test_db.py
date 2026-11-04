from app.db import connect

def test_connect_creates_tables(tmp_path):
    conn = connect(tmp_path / "test.db")
    rows = conn.execute("SELECT name FROM sqlite_master WHERE type='table'")
    names = {r[0] for r in rows}
    assert {"lifts", "days", "day_lifts"} <= names
