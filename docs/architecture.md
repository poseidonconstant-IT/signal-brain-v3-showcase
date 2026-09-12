# Architecture and reliability model

## Components

| Component | Responsibility | Authority boundary |
| --- | --- | --- |
| Market-data adapter | Obtains public candles and market context | Input only; never execution truth |
| Signal and risk engine | Creates a trade decision with grade, confidence, and risk intent | Strategy context |
| Exchange adapter | Submits and reads demo/VST orders and positions | Execution facts |
| Reconciliation layer | Compares tracked state with exchange state after restart and close events | Corrects local lifecycle state |
| SQLite ledger | Persists intent, context, lifecycle, and reporting status | Durable application audit trail |
| Telegram layer | Operator-facing status and notifications | Read/command surface; not ledger authority |
| Google Sheets reporter | Rebuildable closed-trade and period reporting | Downstream only |

## Close-event flow

```text
Exchange reports no matching open position
  -> reconcile cautiously and verify the disappearance
  -> query the close/fill evidence when unambiguous
  -> write the SQLite terminal record
  -> notify the operator
  -> rebuild downstream reporting
```

The reporter labels a record as complete only when its strategy context and
exchange-close details are available. Older or incomplete data remains visible
as legacy/partial rather than being silently included in strategy statistics.

## Restart flow

```text
process starts
  -> read exchange positions and open orders
  -> restore actual SL / TP where available
  -> reconstruct the safe local management state
  -> resume reconciliation and monitoring
```

This approach treats a restart as an operational event to recover from, not an
assumption that local memory is still accurate.

## Reporting model

- `Lenh`: closed trades, prices, quantity, P&L, funding where known, R multiple,
  close reason, and data-quality flag.
- `Ngay`, `Thang`, `Nam`: summaries keyed by the close timestamp in the
  configured business timezone.
- Values are rebuilt from the SQLite ledger. Google Sheets never controls
  execution and never becomes the source of truth.
