"""Read-only, fabricated-data portfolio walkthrough for Signal Brain V3."""

from __future__ import annotations

import streamlit as st


st.set_page_config(page_title="Signal Brain V3 Showcase", page_icon="🛡️", layout="wide")

st.title("Signal Brain V3")
st.caption("Trading Automation & Reconciliation — public, demo-first engineering showcase")
st.warning(
    "All figures, identifiers, notifications, and records on this page are fabricated. "
    "This application has no credentials, network calls, or exchange-execution capability."
)

overview, reporting, verification = st.tabs(
    ["Operations overview", "Reporting boundary", "Verification evidence"]
)

with overview:
    st.image("docs/system-overview.svg", width="stretch")
    st.subheader("What the system is designed to solve")
    left, middle, right = st.columns(3)
    left.metric("Execution authority", "Exchange")
    middle.metric("Strategy context", "SQLite ledger")
    right.metric("Reporting direction", "One-way downstream")
    st.markdown(
        "A reliable API workflow has to survive late fills, external closes, protective-order "
        "changes, and restarts. The design restores facts from the exchange, preserves "
        "application context durably, and rebuilds reporting without letting a dashboard "
        "control execution."
    )

    st.subheader("Fabricated operator dashboard")
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
    st.caption("A dashboard is an operator view only. It cannot place, amend, cancel, or close an order.")

    left, right = st.columns(2)
    with left:
        st.subheader("On restart")
        st.markdown(
            "1. Read demo-exchange positions and open orders.\n"
            "2. Restore actual protective levels where available.\n"
            "3. Reconstruct safe local management state.\n"
            "4. Resume monitoring and reconciliation."
        )
    with right:
        st.subheader("On close event")
        st.markdown(
            "1. Confirm the exchange state carefully.\n"
            "2. Persist terminal context in SQLite.\n"
            "3. Notify the operator once.\n"
            "4. Rebuild Google Sheets reporting."
        )

with reporting:
    st.subheader("Fabricated downstream report")
    st.caption("Mock `Lenh` rows demonstrate provenance and data-quality labels, not returns.")
    st.dataframe(
        [
            {
                "Trade reference": "DEMO-001",
                "Data quality": "BINGX_VERIFIED",
                "Exit classification": "TAKE_PROFIT",
                "P&L": "$18.20 (fabricated)",
                "Funding": "-$0.35 (fabricated)",
                "Report status": "Synced",
            },
            {
                "Trade reference": "DEMO-002",
                "Data quality": "LEGACY_PARTIAL",
                "Exit classification": "UNKNOWN_EXIT",
                "P&L": "Excluded from metrics",
                "Funding": "Not available",
                "Report status": "Visible with label",
            },
        ],
        hide_index=True,
        width="stretch",
    )
    st.info(
        "SQLite is the durable audit ledger. Google Sheets is rebuildable downstream reporting; "
        "it never becomes execution authority."
    )
    st.subheader("Notification audit example")
    st.code(
        "TRADE_CLOSED · DEMO-001 · exchange-verified\n"
        "outbox status: sent once\n"
        "reporting status: synced\n"
        "operator action: none required",
        language="text",
    )

with verification:
    st.subheader("Private-baseline verification")
    st.metric("Automated test modules", "31 / 31 PASS")
    st.caption("Result captured from the private baseline preflight on 14 September 2026.")
    st.markdown(
        "**Coverage areas:** decision logic, exchange resilience, reconciliation safety, "
        "partial closes, SL/TP amendment, restart recovery, ledger persistence, Google Sheets "
        "reporting, production gating, and historical-backfill ambiguity."
    )
    st.subheader("Public-scope guarantees")
    st.markdown(
        "- No API keys, account balances, order IDs, chat IDs, sheet IDs, or screenshots from live accounts.\n"
        "- No exchange signing code or order route is included.\n"
        "- No profitability claim is made.\n"
        "- Demo/VST is the only portfolio scope."
    )
    st.link_button(
        "Read the architecture notes",
        "https://github.com/poseidonconstant-IT/signal-brain-v3-showcase/blob/main/docs/architecture.md",
    )

st.divider()
st.caption("Signal Brain V3 · Python automation, reconciliation, durable audit trails, and operational reporting")
