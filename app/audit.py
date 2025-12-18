import datetime
from app.database import get_connection

def log_audit_event(user_id, action):
    """
    Records an audit log entry for system activity.

    Args:
        user_id (int): ID of the user performing the action
        action (str): Description of the action performed
    """
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
    INSERT INTO audit_logs (user_id, action, timestamp)
    VALUES (?, ?, ?)
    """, (
        user_id,
        action,
        datetime.datetime.now().isoformat()
    ))

    conn.commit()
    conn.close()


def get_audit_logs(limit=50):
    """
    Retrieves recent audit log entries.

    Args:
        limit (int): Number of recent logs to return

    Returns:
        list of tuples: Audit log records
    """
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
    SELECT 
        a.audit_id,
        u.username,
        a.action,
        a.timestamp
    FROM audit_logs a
    LEFT JOIN users u ON a.user_id = u.user_id
    ORDER BY a.timestamp DESC
    LIMIT ?
    """, (limit,))

    logs = cursor.fetchall()
    c
