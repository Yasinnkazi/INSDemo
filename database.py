import sqlite3
import os

_is_vercel = os.environ.get("VERCEL", "").lower() == "1"
DATABASE = "/tmp/database.db" if _is_vercel else "database.db"


def get_db():
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row
    _ensure_init(conn)
    return conn


def _ensure_init(conn):
    cur = conn.execute(
        "SELECT count(*) FROM sqlite_master WHERE type='table' AND name='users'"
    )
    if cur.fetchone()[0] == 0:
        _create_tables(conn)


def _create_tables(conn):
    conn.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT NOT NULL UNIQUE,
            password TEXT NOT NULL,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    """)
    demo_users = [
        ("admin", "admin123"),
        ("user1", "pass123"),
        ("user2", "test456"),
        ("demo", "demo123"),
        ("student", "project2024"),
        ("test", "test123"),
    ]
    conn.executemany(
        "INSERT INTO users (username, password) VALUES (?, ?)", demo_users
    )
    conn.commit()


def init_db():
    if os.path.exists(DATABASE):
        os.remove(DATABASE)
    conn = get_db()
    conn.close()
    print(f"Database initialized at {DATABASE}")


if __name__ == "__main__":
    init_db()
