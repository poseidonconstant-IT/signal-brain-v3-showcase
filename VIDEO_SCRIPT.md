# 90-second Upwork showcase video

This video is a portfolio walkthrough of a **fabricated, read-only showcase**.
Do not open BingX, Telegram, a real Google Sheet, a terminal containing logs, or
any account screen while recording.

| Time | Screen | Narration |
| --- | --- | --- |
| 0–10s | README and architecture diagram | “Signal Brain V3 is a demo-first Python automation and reconciliation case study.” |
| 10–25s | Operations overview tab | “The key design choice is explicit authority: the exchange owns execution facts, SQLite preserves application context, and the dashboard is read-only.” |
| 25–42s | Restart and close-event sections | “After a restart, the system reloads positions and protective orders from the exchange. A close is reconciled before it becomes a terminal ledger record.” |
| 42–60s | Reporting boundary tab | “Google Sheets is downstream and rebuildable. Partial or unverifiable records are visibly labelled and excluded from strategy metrics.” |
| 60–75s | Verification evidence tab | “The private baseline passed 31 automated test modules covering reconciliation, safety gates, reporting, and restart recovery.” |
| 75–90s | README safety section | “This portfolio contains fabricated data only. It is an engineering reliability case study, not investment advice or a profitability claim.” |

## Recording checklist

- Use a browser profile without personal bookmarks or notifications.
- Keep the screen to the public showcase and this repository only.
- Record at 1080p; crop browser chrome if it reveals personal data.
- Export MP4, 60–90 seconds, and attach it to the Upwork portfolio item.
- Attach two screenshots: the architecture diagram and the Verification evidence tab.
