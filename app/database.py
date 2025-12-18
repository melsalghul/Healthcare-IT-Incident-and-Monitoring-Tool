import sqlite3

DB_PATH = "data/hospital_it.db"

def get_connection():
    return sqlite3.connect(DB_PATH)

def initialize_db():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS systems (
        system_id INTEGER PRIMARY KEY AUTOINCREMENT,
        system_name TEXT NOT NULL,
        criticality TEXT NOT NULL
    )
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS incidents (
        incident_id INTEGER PRIMARY KEY AUTOINCREMENT,
        system_id INTEGER,
        severity TEXT,
        start_time TEXT,
        end_time TEXT,
        root_cause TEXT,
        resolution_notes TEXT
    )
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS system_status_logs (
        log_id INTEGER PRIMARY KEY AUTOINCREMENT,
        system_id INTEGER,
        status TEXT,
        timestamp TEXT
    )
    """)

    conn.commit()
    conn.close()
