---
name: finance-v1-public
description: Public bookkeeping and ELSTER prep helper for sanitized ledgers, receipts, and month summaries.
---

# Finance V1 Public

Use this skill for sanitized bookkeeping workflows and ELSTER preparation.

## When to use

- Classifying receipts, ledger rows, and booking months
- Reviewing VAT treatment and review status
- Summarizing a month for ELSTER prep
- Preparing public-friendly bookkeeping templates and checks

## Use only public-safe data

- Keep real receipts, private ledgers, account numbers, sheet IDs, taxpayer IDs, names, and other personal data out of the skill package.
- If you need to work with real data locally, keep it in ignored paths such as private/ or data/.

## Core workflow

1. Capture or import the booking row with receipt date, counterparty, amounts, VAT, currency, and file path.
2. Assign category, subcategory, tax treatment, and review status.
3. Prefer needs_review over guessing when tax treatment is unclear.
4. Summarize the ledger month with scripts/monthly_elster_summary.py.
5. Inspect the checklist before finalizing anything that is ambiguous or high-risk.

## Key references

- config/intake-rules.md for the intake flow and tax-treatment rules
- config/review-checklist.md for common review checks
- config/sheets-schema-v1.md for the column model
- templates/ledger_v1.csv for the ledger format
- templates/intake_message_template.md for intake prompts
- templates/monthly_report_template.md for month report notes
- scripts/monthly_elster_summary.py for the summary generator

## Output rules

- Keep the public package free of personal data.
- Do not infer missing tax facts from payment providers alone.
- Use needs_review for unclear foreign VAT, reverse charge, hospitality, travel, or vehicle cases.
- Treat the script output as a prep artifact, not tax advice.
