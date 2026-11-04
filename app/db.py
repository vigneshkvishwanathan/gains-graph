import sqlite3

SCHEMA = """
CREATE TABLE IF NOT EXISTS lifts (
    id   INTEGER PRIMARY KEY,
    name TEXT UNIQUE NOT NULL
);
CREATE TABLE IF NOT EXISTS days (
    id   INTEGER PRIMARY KEY,
    name TEXT UNIQUE NOT NULL
);
CREATE TABLE IF NOT EXISTS day_lifts (
    day_id   INTEGER NOT NULL REFERENCES days(id),
    lift_id  INTEGER NOT NULL REFERENCES lifts(id),
    position INTEGER NOT NULL,
    sets     INTEGER NOT NULL,
    rep_min  INTEGER NOT NULL,
    rep_max  INTEGER NOT NULL,
    PRIMARY KEY (day_id, position)
);
"""

def connect(path):
    conn = sqlite3.connect(path)
    conn.executescript(SCHEMA)
    return conn
