import streamlit as st
import json
from datetime import datetime

from data import CUSTOMERS
from policies import resolve_request

# ==========================================
# PAGE CONFIG
# ==========================================

st.set_page_config(
    page_title="Customer Resolution Agent",
    page_icon="✈️",
    layout="wide"
)

# ==========================================
# CUSTOM CSS
# ==========================================

st.markdown("""
<style>

.main-title {
    text-align:center;
    font-size:40px;
    font-weight:bold;
    color:#0E6EFD;
}

.subtitle {
    text-align:center;
    color:gray;
    margin-bottom:20px;
}

.info-card {
    padding:15px;
    border-radius:10px;
    background-color:#f7f7f7;
    border:1px solid #ddd;
}

.success-box {
    padding:10px;
    border-radius:8px;
    background:#e8f5e9;
}

</style>
""", unsafe_allow_html=True)

# ==========================================
# SESSION STATE
# ==========================================

if "messages" not in st.session_state:
    st.session_state.messages = []

if "customer_loaded" not in st.session_state:
    st.session_state.customer_loaded = None

# ==========================================
# AUDIT LOGGER
# ==========================================

def save_log(customer_name, user_message, response):

    record = {
        "customer": customer_name,
        "user_message": user_message,
        "response": response,
        "timestamp": str(datetime.now())
    }

    try:
        with open("audit_log.json", "r") as f:
            data = json.load(f)

    except:
        data = []

    data.append(record)

    with open("audit_log.json", "w") as f:
        json.dump(data, f, indent=4)

# ==========================================
# HEADER
# ==========================================

st.markdown(
    "<div class='main-title'>✈️ Customer Resolution Agent</div>",
    unsafe_allow_html=True
)

st.markdown(
    "<div class='subtitle'>AIONOS Assignment 3 - Airline Disruption Support</div>",
    unsafe_allow_html=True
)

# ==========================================
# SIDEBAR
# ==========================================

with st.sidebar:

    st.header("📋 Sample Customers")

    st.info("""
Priya Nair

PNR: SK4821X

Status: Cancelled
""")

    st.info("""
Arvind Kulkarni

PNR: TR1190B

Status: Delayed4
""")

    st.info("""
Meher Kaur

PNR: WL7742

Status: Delayed6
""")

    st.divider()

    st.markdown("### Features")

    st.markdown("""
✅ Intent Detection

✅ Policy Engine

✅ Escalation Handling

✅ Audit Logging

✅ Sentiment Handling
""")

# ==========================================
# CUSTOMER LOOKUP
# ==========================================

st.subheader("🔎 Customer Lookup")

pnr = st.text_input(
    "Enter Booking Reference",
    placeholder="Example: SK4821X"
)

if pnr:

    pnr = pnr.strip().upper()

    if pnr in CUSTOMERS:

        customer = CUSTOMERS[pnr]

        st.session_state.customer_loaded = customer

        st.success("Customer Found")

        col1, col2 = st.columns(2)

        with col1:

            st.markdown("### 👤 Customer Details")

            st.markdown(f"""
**Name:** {customer['name']}

**Tier:** {customer['tier']}
""")

        with col2:

            st.markdown("### ✈️ Flight Details")

            st.markdown(f"""
**Flight:** {customer['flight']}

**Route:** {customer['route']}

**Status:** {customer['status']}
""")

        st.divider()

        st.subheader("💬 Customer Support Chat")

        # Display history

        for msg in st.session_state.messages:

            with st.chat_message(msg["role"]):
                st.markdown(msg["content"])

        # User input

        prompt = st.chat_input(
            "Describe your issue..."
        )

        if prompt:

            st.session_state.messages.append(
                {
                    "role": "user",
                    "content": prompt
                }
            )

            response = resolve_request(
                customer,
                prompt,
                st.session_state
            )

            st.session_state.messages.append(
                {
                    "role": "assistant",
                    "content": response
                }
            )

            save_log(
                customer["name"],
                prompt,
                response
            )

            st.rerun()

    else:

        st.error(
            "❌ Booking Reference Not Found"
        )

# ==========================================
# AUDIT TRAIL
# ==========================================

st.divider()

st.subheader("📑 Conversation & Action Record")

try:

    with open("audit_log.json", "r") as f:

        logs = json.load(f)

    if len(logs) > 0:

        for item in reversed(logs[-10:]):

            with st.expander(
                f"{item['customer']} | {item['timestamp']}"
            ):

                st.write(
                    "**Customer Message:**",
                    item["user_message"]
                )

                st.write(
                    "**Agent Response:**",
                    item["response"]
                )

    else:

        st.info("No conversation history available.")

except:

    st.info("No audit records available.")

# ==========================================
# FOOTER
# ==========================================

st.divider()

st.caption(
    "Built for AIONOS Assignment 3 | Customer-Facing Resolution Agent"
)
