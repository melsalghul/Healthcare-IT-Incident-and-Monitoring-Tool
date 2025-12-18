from app.database import initialize_db
from app.monitor import log_system_status

initialize_db()

# Simulated checks
log_system_status(system_id=1, status="UP")
log_system_status(system_id=2, status="DOWN")

print("System status logged successfully.")
