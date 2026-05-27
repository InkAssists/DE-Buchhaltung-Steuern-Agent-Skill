---
name: buchhaltungs-steuerhelfer
description: Öffentlicher Buchhaltungs- und Steuerhelfer für deutsche Unternehmer mit sicheren, anonymisierten Ledgern, Belegen und Monatsauswertungen.
---

# Buchhaltungs- und Steuerhelfer

Use this OpenClaw/Hermes skill for Buchhaltung, Belegarchivierung und ELSTER-Vorbereitung für deutsche Unternehmer.

## Prerequisites

- gog must be available if you want to connect to Gmail, Drive, or Sheets.

## When to use

- Belege, Einnahmen, Ausgaben und Buchungsmonate erfassen
- VAT-/USt-Behandlung und Review-Status prüfen
- Einen Monat für ELSTER aufbereiten
- Belege und unterstützende Dokumente archivieren, ohne private Ordner-IDs oder Kontodaten offenzulegen
- Öffentliche Vorlagen und Prüfregeln für Buchhaltung und Steuerhilfe nutzen
- gog für Gmail, Drive und Sheets verwenden, wenn echte Google-Daten eingebunden werden

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
