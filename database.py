import sqlite3
import os

DATABASE = 'database.db'

def get_db():
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row
    return conn

def init_db():
    if os.path.exists(DATABASE):
        os.remove(DATABASE)

    conn = get_db()
    cursor = conn.cursor()

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT NOT NULL UNIQUE,
            password TEXT NOT NULL,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    ''')

    demo_users = [
        ('admin', 'admin123'),
        ('user1', 'pass123'),
        ('user2', 'test456'),
        ('demo', 'demo123'),
        ('student', 'project2024'),
        ('test', 'test123')
    ]

    cursor.executemany(
        'INSERT INTO users (username, password) VALUES (?, ?)',
        demo_users
    )

    conn.commit()
    conn.close()

    print("Database initialized successfully!")
    print(f"Inserted {len(demo_users)} demo users")

if __name__ == '__main__':
    init_db()
