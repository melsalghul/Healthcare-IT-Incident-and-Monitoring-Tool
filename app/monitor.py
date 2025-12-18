import datetime
from app.database import get_connection

def log_system_status(system_id, status):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
    INSERT INTO system_status_logs (system_id, status, timestamp)
    VALUES (?, ?, ?)
    """, (system_id, status, datetime.datetime.now().isoformat()))

    conn.commit()
    conn.close()
