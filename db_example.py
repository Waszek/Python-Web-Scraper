import sqlite3

def init_database():
    conn = sqlite3.connect("my_database.db")
    cursor = conn.cursor()

    cursor.execute(
        "CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT NOT NULL, company TEXT NOT NULL)"
    )

    cursor.execute(
        "CREATE TABLE IF NOT EXISTS posts (id INTEGER PRIMARY KEY AUTOINCREMENT, title TEXT NOT NULL, body TEXT NOT NULL, user_id INTEGER, FOREIGN KEY (user_id) REFERENCES users (id))"
    )

    conn.commit()
    conn.close()
    print("Database and table was successfully created!")

def add_user(name, company):
    conn = sqlite3.connect("my_database.db")
    cursor = conn.cursor()

    query = "INSERT INTO users(name, company) VALUES (?, ?)"
    values = (name, company)

    cursor.execute(query, values)
    conn.commit()
    conn.close()


def add_post(title, body, user_id):
    conn = sqlite3.connect("my_database.db")
    cursor = conn.cursor()

    query = "INSERT INTO posts (title, body, user_id) VALUES (?, ?, ?)"
    values = (title, body, user_id)

    cursor.execute(query, values)
    conn.commit()
    conn.close()

def get_all_users():    
    conn = sqlite3.connect("my_database.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users")

    rows = cursor.fetchall()
    for row in rows:
        print(row)

    conn.close()

def get_all_posts():
    conn = sqlite3.connect("my_database.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM posts")

    rows = cursor.fetchall()
    for row in rows:
        print(row)

    conn.close()

def get_users_with_posts():
    conn = sqlite3.connect("my_database.db")
    cursor = conn.cursor()

    cursor.execute("SELECT users.name, posts.title FROM posts INNER JOIN users ON posts.user_id = users.id LIMIT 10")
    rows = cursor.fetchall()
    print("\n=== REPORT: USERS AND THEIR POSTS ===")
    for row in rows:
        print(f"Author: {row[0]} | Title: {row[1]}")

    conn.close()

if __name__ == "__main__":
    # init_database()
    # get_all_users()
    # get_all_posts()
    get_users_with_posts()