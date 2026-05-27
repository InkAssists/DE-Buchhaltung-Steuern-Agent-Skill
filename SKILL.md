---
name: bookkeeping-tax-helper
description: Public bookkeeping and tax helper for German entrepreneurs with safe, anonymized ledgers, receipts, and monthly summaries.
---

# Bookkeeping and Tax Helper

Use this OpenClaw/Hermes skill for bookkeeping, receipt archiving, and ELSTER preparation for German entrepreneurs.

## Prerequisites

- gog must be available if you want to connect to Gmail, Drive, or Sheets.

## When to use

- Capture receipts, income, expenses, and booking months
- Review VAT and tax treatment
- Prepare a month for ELSTER
- Archive receipts and supporting documents without exposing private folder IDs or account data
- Use public templates and review rules for bookkeeping and tax prep
- Use gog for Gmail, Drive, and Sheets when real Google data is involved

## Use only public-safe data

- Keep real receipts, private ledgers, account numbers, sheet IDs, taxpayer IDs, names, and other personal data out of the skill package.
- If you need to work with real data locally, keep it in ignored paths such as private/ or data/.

## Core workflow

1. Capture or import the booking row with receipt date, counterparty, amounts, VAT, currency, and file path.
2. Assign category, subcategory, tax treatment, and review status.
3. Prefer needs_review over guessing when tax treatment is unclear.
4. Summarize the ledger month with scripts/monthly_elster_summary.py.
5. Archive receipts or supporting documents using the generic archiving workflow when needed.
6. Inspect the checklist before finalizing anything that is ambiguous or high-risk.

## Key references

- config/intake-rules.md for the intake flow and tax-treatment rules
- config/review-checklist.md for common review checks
- references/drive-archiving.md for the generic document archiving workflow
- config/sheets-schema-v1.md for the column model
- templates/ledger_v1.csv for the ledger format
- templates/intake_message_template.md for intake prompts
- templates/monthly_report_template.md for month report notes
- scripts/monthly_elster_summary.py for the summary generator

## Output rules

- Keep the public package free of personal data.
- Do not infer missing tax facts from payment providers alone.
- Use needs_review for unclear foreign VAT, reverse charge, hospitality, travel, or vehicle cases.
- Keep archiving instructions generic in the public package; resolve any private destination mapping outside the skill.
- Treat the script output as a prep artifact, not tax advice.
