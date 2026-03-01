import sqlite3 as sq

DB_NAME = "diet_planner.db"

def init_db():
    with sq.connect(DB_NAME) as conn:
        conn.execute("""   
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER,
            username TEXT,
            first_name TEXT,
            last_name TEXT,
            gender TEXT,
            age INTEGER,
            weight REAL,
            height REAL,
            activity TEXT,
            goal TEXT,
            bmr REAL,
            tdee REAL,
            calories REAL
        )         
        """)

def set_user(user_id, username, first_name, last_name, gender, age, weight, height, activity, goal, bmr, tdee, calories):
    with sq.connect(DB_NAME) as conn:
        conn.execute("""
            INSERT INTO users (
                user_id, username, first_name, last_name,
                gender, age, weight, height,
                activity, goal, bmr, tdee, calories
            )
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        """, (
            user_id, username, first_name, last_name,
            gender, age, weight, height,
            activity, goal, bmr, tdee, calories
        ))


def get_user(user_id):
    with sq.connect(DB_NAME) as conn:
        conn.row_factory = sq.Row
        cursor = conn.execute("""
            SELECT * FROM users WHERE user_id = ?
        """, (user_id, ))
        return cursor.fetchone()