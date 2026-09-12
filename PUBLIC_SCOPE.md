# Public showcase boundary

This repository is deliberately a **presentation layer**, not the production
or development source tree.

## Included

- Architectural decisions and system boundaries.
- A standalone, read-only visualization using fabricated data.
- Sanitized diagrams and a reproducible local demonstration.
- High-level testing and reliability approach.

## Excluded

- API credentials, tokens, webhook URLs, account identifiers, Google service
  accounts, and environment files.
- Private source code, exchange signing logic, order routes, runtime database,
  logs, and debug traces.
- Real balances, order IDs, fill history, client IDs, sheet IDs, chat IDs, and
  identifiable screenshots.
- Any component that can create, amend, cancel, or close exchange orders.

The private repository remains the only place for implementation, backups,
tests, operational debugging, and future feature work.
