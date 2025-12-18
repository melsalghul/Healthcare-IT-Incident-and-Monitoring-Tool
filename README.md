# Healthcare IT Incident & Systems Monitoring Tool

## Overview
This project simulates a hospital IT operations tool used to monitor uptime, track incidents, and generate SLA-style reporting for critical clinical systems such as EHR, lab, imaging, and pharmacy systems.

The goal of this project is to demonstrate practical healthcare IT skills including system monitoring, incident management, database design, and HIPAA-aware data handling using synthetic data only.

---

## Key Features
- Monitors availability of critical hospital systems
- Logs system uptime and downtime events
- Tracks IT incidents with severity, root cause, and resolution time
- Stores structured data using a relational SQL database
- Designed with role-based access and auditability in mind
- HIPAA-aware design using synthetic, non-PHI data

---

## Tech Stack
- Python
- SQLite
- SQL
- Git
- (Optional) Power BI for operational dashboards

---

## Project Structure
healthcare-it-monitoring/
├── app/ # Core application logic
├── data/ # SQLite database
├── scripts/ # Utility scripts
├── docs/ # Documentation
├── run_monitor.py # Entry point
└── README.md

---

## How to Run
1. Clone the repository
2. Create a virtual environment (optional)
3. Install dependencies: pip install -r requirements.txt
4. Run the monitoring script: python run_monitor.py

---

## Example Use Cases
- Hospital IT teams tracking EHR uptime
- Incident trend analysis and SLA reporting
- IT operations documentation and auditing

---

## HIPAA & Data Privacy
This project uses **synthetic data only** and contains **no patient health information (PHI)**. Design considerations include least-privilege access, audit logging, and secure handling of operational data.

---

## Future Enhancements
- Web-based incident management UI
- Automated alerting
- Integration with Power BI dashboards
- PostgreSQL support
