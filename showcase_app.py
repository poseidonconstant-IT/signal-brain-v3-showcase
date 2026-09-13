"""Read-only, fabricated-data portfolio dashboard for Signal Brain V3."""

from __future__ import annotations

import streamlit as st


st.set_page_config(page_title="Signal Brain V3 Showcase", page_icon="🛡️", layout="wide")

st.title("Signal Brain V3")
st.caption("Trading Automation & Reconciliation — public, demo-first engineering showcase")
st.warning(
    "All figures, identifiers, notifications, and records on this page are fabricated. "
    "This dashboard has no credentials, network calls, or exchange-execution capability."
)

st.image("docs/system-overview.svg", width="stretch")

st.subheader("Operator dashboard · fabricated demo state")
first, second, third, fourth = st.columns(4)
first.metric("Mode", "DEMO / VST")
second.metric("Open positions", "1")
third.metric("Pending orders", "0")
fourth.metric("Risk guard", "CLEAR")

st.dataframe(
    [{
        "Symbol": "DEMO-USDT",
        "State": "MANAGING",
        "Side": "LONG",
        "Protection": "Exchange-held SL / TP",
        "Data authority": "Exchange snapshot",
    }],
    hide_index=True,
    width="stretch",
)
st.caption("Observer only — this dashboard cannot place, amend, cancel, or close an order.")

left, middle, right = st.columns(3)
left.metric("Execution authority", "Exchange")
middle.metric("Strategy context", "SQLite ledger")
right.metric("Reporting direction", "One-way downstream")

st.info(
    "The engineering detail, recovery flow, reporting boundary, and verification evidence "
    "are documented in the GitHub README and Recruiter Guide."
)
st.link_button(
    "Read the recruiter guide",
    "https://github.com/poseidonconstant-IT/signal-brain-v3-showcase/blob/main/docs/RECRUITER_GUIDE.md",
)

st.divider()
st.caption("Signal Brain V3 · Python automation, reconciliation, durable audit trails, and operational reporting")
