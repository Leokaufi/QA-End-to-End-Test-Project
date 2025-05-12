import sqlite3
import os

BASE_DIR = os.path.dirname(os.path.dirname(__file__))
DB_PATH = os.path.join(BASE_DIR, "db", "todo.db")

def test_task_insert_and_read():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS tasks (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT NOT NULL,
        done BOOLEAN NOT NULL
    );
    """)
    conn.commit()

    # Testdaten
    test_title = "pytest DB-test"
    test_done = 0

    # Einfügen
    cursor.execute("INSERT INTO tasks (title, done) VALUES (?, ?)", (test_title, test_done))
    conn.commit()

    # Abfragen
    cursor.execute("SELECT * FROM tasks WHERE title = ?", (test_title,))
    result = cursor.fetchone()

    conn.close()

    assert result is not None, "No entry found"
    assert result[1] == test_title
    assert result[2] == test_done
