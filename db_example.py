import sqlite3

def init_database():
    conn = sqlite3.connect("my_database.db")
    cursor = conn.cursor()

    cursor.execute(
        "CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT NOT NULL, company TEXT NOT NULL)"
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

def get_all_users():
    conn = sqlite3.connect("my_database.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users")

    rows = cursor.fetchall()
    for row in rows:
        print(row)

    conn.close()

if __name__ == "__main__":
    init_database()
    add_user("John Doe", "Facebook")
    add_user("Alejadro Ferrero", "Police")
    get_all_users()