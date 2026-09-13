# Recruiter guide

## What this demonstrates

Signal Brain V3 is a Python automation case study focused on **operational
correctness**, not trading-return claims. It demonstrates how an API workflow
can keep its own record accurate when the external system is slow, returns
partial history, changes protective orders, or the local process restarts.

The public showcase contains only fabricated demo records. It has no keys,
account data, order routes, or executable exchange integration.

## The engineering problem

An exchange is the authority for positions, fills, protective orders, and
realized P&L. However, it does not preserve all application context needed for
analytics: strategy grade, intended risk, confidence, and reporting state.

The solution therefore uses explicit authority boundaries:

| Concern | Source of truth |
| --- | --- |
| Market context | Public market-data adapter |
| Execution facts | Exchange snapshot and close/fill records |
| Strategy metadata and lifecycle audit | SQLite ledger |
| Notifications | Telegram operator surface |
| Reporting | One-way, rebuildable Google Sheets output |

## Reliability behaviours

1. **Restart recovery** — At startup, the system re-reads positions and
   pending orders from the exchange, restores current SL/TP when available,
   then rebuilds local management state.
2. **Reconciliation** — A missing local/exchange match is verified before a
   trade is treated as closed. Delayed or partial history is labelled as such;
   it is not converted into invented P&L, exit price, or exit reason.
3. **Idempotent reporting** — Closed-trade reporting can be rebuilt from the
   ledger. A reporting or notification failure does not become an execution
   failure.
4. **Safety gate** — Diagnostics that could remove an unreconcilable
   demo-only record require an explicit acknowledgement. The dashboard is an
   observer, not a trading control surface.

## Verification evidence

The private baseline preflight executed on **14 September 2026** with
**31 test modules passing and 0 failures**. Coverage includes decision logic,
exchange-resilience handling, reconciliation safety, partial close handling,
SL/TP amendment, restart recovery, ledger persistence, Google Sheets
reporting, production gating, and historical-backfill ambiguity.

That result shows regression coverage of the implemented behaviours. It does
not claim live-market profitability or guarantee uptime.

## Safe interactive walkthrough

Run the read-only showcase locally:

```bash
python -m venv .venv
.venv/bin/pip install -r requirements.txt
.venv/bin/streamlit run showcase_app.py
```

The walkthrough has three views:

- **Operations overview** — component boundaries, a fabricated operator view,
  and the restart/close-event sequence.
- **Reporting boundary** — fabricated, downstream-only reporting examples and
  data-quality labels.
- **Verification evidence** — test result context and the explicit public
  scope guarantees.

For deeper detail, see [architecture.md](architecture.md) and
[PUBLIC_SCOPE.md](../PUBLIC_SCOPE.md).
