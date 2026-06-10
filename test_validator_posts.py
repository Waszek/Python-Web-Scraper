import pytest
import sqlite3
from validator_posts import validate_post_title

@pytest.fixture
def db_create():
    conn = sqlite3.connect(":memory:")
    cursor = conn.cursor()

    cursor.execute("CREATE TABLE posts (id INTEGER PRIMARY KEY AUTOINCREMENT, title TEXT NOT NULL)")

    conn.commit()
    yield conn
    conn.close()

def test_title_validation_success():
    title = "Good Title"
    assert validate_post_title(title) == True

def test_title_validation_failed():
    title = "ABC"
    with pytest.raises(ValueError):
        validate_post_title(title)

def test_add_post_integration(db_create):
    title = "Good Title"
    cursor = db_create.cursor()

    assert validate_post_title(title) == True

    cursor.execute("INSERT INTO posts (title) VALUES (?)", (title,))
    db_create.commit()

    cursor.execute("SELECT * FROM posts")
    posts = cursor.fetchall()

    assert len(posts) == 1 
    assert posts[0][1] == "Good Title"
    