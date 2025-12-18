from app.database import get_connection
import datetime

def create_incident(system_id, severity, root_cause):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
    INSERT INTO incidents (system_id, severity, start_time, root_cause)
    VALUES (?, ?, ?, ?)
    """, (system_id, severity, datetime.datetime.now().isoformat(), root_cause))

    conn.commit()
    conn.close()
