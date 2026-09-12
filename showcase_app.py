"""Read-only, fabricated-data portfolio walkthrough for Signal Brain V3."""

from __future__ import annotations

import streamlit as st


st.set_page_config(page_title="Signal Brain V3 Showcase", page_icon="🛡️", layout="wide")

st.title("Signal Brain V3")
st.caption("Trading Automation & Reconciliation — public, demo-first engineering showcase")

st.warning(
    "This visualization uses fabricated sample data. It has no credentials, network calls, "
    "or exchange-execution capability. It is not investment advice."
)

st.image("docs/system-overview.svg", use_container_width=True)

st.header("What the system is designed to solve")
left, middle, right = st.columns(3)
left.metric("Execution authority", "Exchange")
middle.metric("Strategy context", "SQLite ledger")
right.metric("Reporting direction", "One-way downstream")

st.markdown(
    "A reliable API workflow has to survive late fills, external closes, protective-order changes, "
    "and restarts. The design restores facts from the exchange, preserves application context "
    "durably, and rebuilds reporting without letting a dashboard control execution."
)

st.header("Fabricated closed-trade record")
sample_trade = {
    "Symbol": "DEMO-USDT",
    "Side": "LONG",
    "Grade": "A",
    "Data quality": "COMPLETE",
    "Entry": "100.00",
    "Exit": "102.40",
    "Risk at SL": "$12.00",
    "Realized P&L": "$18.20",
    "Funding fee": "-$0.35",
    "P&L incl. funding": "$17.85",
    "Close reason": "TP / reconciliation verified",
}
st.dataframe([sample_trade], hide_index=True, use_container_width=True)
st.caption("Values above are fabricated; the example demonstrates field separation, not performance.")

st.header("Safety and recovery behavior")
col1, col2 = st.columns(2)
with col1:
    st.subheader("On restart")
    st.markdown(
        "1. Read demo-exchange positions and open orders.\n"
        "2. Restore actual protective levels where available.\n"
        "3. Reconstruct safe local management state.\n"
        "4. Resume monitoring and reconciliation."
    )
with col2:
    st.subheader("On close event")
    st.markdown(
        "1. Confirm the exchange state carefully.\n"
        "2. Persist terminal context in SQLite.\n"
        "3. Notify the operator.\n"
        "4. Rebuild Google Sheets reporting downstream."
    )

st.header("Portfolio evidence")
st.markdown(
    "The private implementation is tested across signal/risk logic, lifecycle state transitions, "
    "reconciliation safety, partial closes, SL/TP updates, reporting, and historical backfill ambiguity. "
    "The public repository intentionally exposes the design and safe walkthrough only."
)

st.divider()
st.caption("Signal Brain V3 · Python automation, reconciliation, durable audit trails, and operational reporting")
