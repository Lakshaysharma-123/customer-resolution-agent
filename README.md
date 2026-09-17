# Customer Resolution Agent

## AIONOS Assignment 3

Customer-Facing Resolution Agent for Airline Disruption Management.

### Overview

This project simulates a customer support agent that helps airline passengers during disruptions such as:

- Flight Cancellation
- Flight Delays
- Refund Requests
- Rebooking Requests
- Escalation Requests

The system understands customer intent, applies airline policies, recommends actions, and maintains an audit trail.

---

## Features

### Intent Detection
- Refund Requests
- Rebooking Requests
- Compensation Requests
- Escalation Requests

### Policy Engine
Automatically applies airline policies based on flight status.

### Customer Sentiment Handling
Detects frustrated customers and responds professionally.

### Escalation Workflow
Generates escalation tickets when agent authority is exceeded.

### Audit Logging
Maintains complete conversation and action records.

---

## Technology Stack

- Python
- Streamlit
- JSON
- GitHub

---

## Project Structure

customer-resolution-agent/

├── app.py

├── data.py

├── policies.py

├── requirements.txt

├── audit_log.json

└── README.md

---

## Sample Customers

| Customer | Booking Reference |
|-----------|------------------|
| Priya Nair | SK4821X |
| Arvind Kulkarni | TR1190B |
| Meher Kaur | WL7742 |

---

## Run Locally

```bash
pip install -r requirements.txt
streamlit run app.py
```

---

## Assignment Requirements Covered

✔ Understand customer intent

✔ Ask only necessary questions

✔ Use supplied data and policies

✔ Recommend correct next action

✔ Handle angry customers

✔ Escalate when authority is missing

✔ Preserve conversation records
