# Beleg Intake Message Template

Use this pattern when a receipt, photo, or PDF arrives:

## 1. Confirm briefly
- receipt recognized
- will store and record it

## 2. Extract
Minimum fields:
- date
- counterparty or issuer
- gross amount
- tax amount or tax rate, if visible
- document type
- payment method, if visible

## 3. Classify
- entry_type: expense or income
- main_category
- sub_category
- tax_treatment
- review_status

## 4. Store
Filename:
YYYY-MM-DD_counterparty_amount_category_country.ext

Paths:
- expenses: receipts/YYYY/MM/expense/
- income: receipts/YYYY/MM/income/

## 5. Reply
Keep it short and concrete:
- what was recognized
- how it was classified
- whether anything is uncertain

## 6. If unclear
Ask one short question, for example:
- Was this business related?
- Which payment method was used?
- Hospitality with whom and for what occasion?
- Reverse charge or domestic invoice?

