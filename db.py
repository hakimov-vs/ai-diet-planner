import sqlite3 as sq

DB_NAME = "diet_planner.db"


def init_db():
    with sq.connect(DB_NAME) as conn:
        conn.execute("""
           
        CREATE TABLE IF NOT EXISTS 
            'users'(
                'id' INTEGER PRIMARY KEY AUTOINCREMENT,
                'user_id' INTEGER UNIQUE,
                'username' VARCHAR(100),
                'first_name' VARCHAR(100),
                'last_name' VARCHAR(100),
                'gender' VARCHAR(10),
                'age' INTEGER,
                'weight' REAL,
                'height' REAL,
                'activity_level' VARCHAR(25),
                'goal' VARCHAR(25)
            )         
        """)
        