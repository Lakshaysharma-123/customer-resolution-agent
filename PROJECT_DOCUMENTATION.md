# PROJECT DOCUMENTATION

## Assignment Title

Customer-Facing Resolution Agent

## Domain

Airline Disruption Management

## Objective

To develop an AI-assisted customer service agent capable of handling airline disruption scenarios including cancellations, delays, refunds, rebooking, compensation requests, and escalations.

---

## Functional Requirements

1. Identify customer intent.
2. Apply airline policies.
3. Recommend valid actions.
4. Escalate requests beyond authority.
5. Handle frustrated customers.
6. Maintain audit records.

---

## Components

### User Interface

Implemented using Streamlit.

### Customer Database

Contains passenger information and flight status.

### Policy Engine

Applies airline compensation and service policies.

### Escalation Module

Generates escalation tickets for exceptional requests.

### Audit Logging

Stores all customer interactions.

---

## Test Scenarios

### Scenario 1

Customer: SK4821X

Issue: Refund Request

Expected Result: Refund Approved

---

### Scenario 2

Customer: TR1190B

Issue: Hotel Request

Expected Result: Request Denied

---

### Scenario 3

Customer: WL7742

Issue: Compensation Request

Expected Result: Hotel + Lounge + Meal Benefits

---

### Scenario 4

Customer uses words such as:
- angry
- frustrated
- terrible

Expected Result:
Empathetic response generated.

---

## Conclusion

The solution successfully demonstrates a customer-facing resolution workflow that aligns with the assignment requirements.
