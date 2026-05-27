# Finance V1 Public

This repository is a public, sanitized scaffold for bookkeeping and ELSTER preparation.

It intentionally contains:
- the data model
- intake and review rules
- CSV and report templates
- a small summary script

It intentionally does not contain:
- receipts
- ledgers with real bookings
- taxpayer identifiers
- account numbers
- customer or vendor names from private records
- Google Sheet IDs or other live integration secrets

## Structure

- config/ - categories, intake rules, review checklist, and sheet schema
- templates/ - CSV and markdown templates
- reports/ - human-readable report notes
- scripts/ - local helper scripts

## Quick Start

1. Keep your private ledger and receipts outside the repository, or in ignored paths such as private/ or data/.
2. Copy templates/ledger_v1.csv into your own private working file and fill it with bookings.
3. Use scripts/monthly_elster_summary.py to summarize a month.

Example:

    python3 scripts/monthly_elster_summary.py \
      --ledger /path/to/private-ledger.csv \
      --month 2026-05

Optional output file:

    python3 scripts/monthly_elster_summary.py \
      --ledger /path/to/private-ledger.csv \
      --month 2026-05 \
      --output reports/generated/elster-summary-for-2026-05.json

## Notes

- This is a working template, not tax advice.
- The repository is designed so that the published version stays free of personal data.
- If you add real data locally, make sure it remains ignored before publishing.

