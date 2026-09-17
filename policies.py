import uuid

def generate_ticket():
    return f"ESC-{str(uuid.uuid4())[:8].upper()}"

def detect_sentiment(text):

    angry_words = [
        "angry",
        "worst",
        "terrible",
        "frustrated",
        "ridiculous",
        "unacceptable"
    ]

    if any(word in text.lower() for word in angry_words):
        return "angry"

    return "neutral"

def resolve_request(customer, message, session_state):

    text = message.lower()

    if detect_sentiment(text) == "angry":
        return """
I understand your frustration and apologize for the inconvenience.

Let me help you resolve this quickly.

Available options:
• Refund
• Rebooking
• Compensation
"""

    if "legal" in text or "court" in text:
        return f"""
🚨 ESCALATION REQUIRED

Ticket Number:
{generate_ticket()}

Your request has been forwarded to a specialist support team.
"""

    status = customer["status"]

    if status == "Cancelled":

        if "refund" in text:
            return """
✅ REFUND APPROVED

Reason:
Flight cancelled by airline

Timeline:
7 business days
"""

        if "rebook" in text:
            return """
✅ REBOOKING APPROVED

Benefits:
• No fare difference
• Next available flight
"""

        if "upgrade" in text:
            return f"""
🚨 ESCALATION REQUIRED

Ticket:
{generate_ticket()}

Business-class upgrades require supervisor approval.
"""

        return """
Your flight has been cancelled.

Would you like:

1. Refund
2. Rebooking
"""

    if status == "Delayed4":

        if "hotel" in text:
            return """
❌ REQUEST DENIED

Policy:
Hotel accommodation is not available for delays under 6 hours.

Available Benefits:
• Meal Voucher
• Lounge Access
"""

        return """
✅ COMPENSATION APPROVED

Benefits:
• Meal Voucher
• Lounge Access
"""

    if status == "Delayed6":

        if "fare difference" in text:
            return f"""
🚨 ESCALATION REQUIRED

Reason:
Fare difference waiver exceeds agent authority.

Ticket:
{generate_ticket()}
"""

        return """
✅ COMPENSATION APPROVED

Benefits:
• Meal Voucher
• Lounge Access
• Hotel Accommodation
"""

    return "Please provide additional details."
