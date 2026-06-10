import sqlite3
import pytest

@pytest.fixture

def db_session():
    conn = sqlite3.connect(":memory:")
    cursor = conn.cursor()

    cursor.execute("CREATE TABLE users (id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT NOT NULL, company TEXT NOT NULL)")

    conn.commit()
    yield conn
    conn.close()

def test_insert_users_to_database(db_session):
    cursor = db_session.cursor()

    cursor.execute("INSERT INTO users (name, company) VALUES (?, ?)", ("Test John", "QA Tester"))
    db_session.commit()

    cursor.execute("SELECT * FROM users")
    rows = cursor.fetchall()

    assert len(rows) == 1
    assert rows[0][1] == "Test John"
    assert rows[0][2] == "QA Tester"
