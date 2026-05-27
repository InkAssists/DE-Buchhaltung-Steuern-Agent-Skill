# Google Sheets Schema V1

## Suggested tabs
1. Ledger
2. Categories
3. MonthlySummary
4. ReviewQueue

## Tab: Ledger
Columns in this exact order:
- receipt_id
- entry_type
- receipt_date
- booking_month
- counterparty
- description
- main_category
- sub_category
- gross_amount
- net_amount
- tax_amount
- tax_rate
- tax_treatment
- currency
- country
- payment_method
- file_path
- review_status
- business_purpose
- trip_route
- vehicle_reference
- hospitality_participants
- hospitality_occasion
- invoice_number
- customer_name
- notes

## Tab: Categories
- main_category
- sub_category
- entry_type
- default_tax_treatment
- requires_review_hint

## Tab: MonthlySummary
At least one row per month:
- month
- income_net
- output_vat
- expense_net
- input_vat
- vat_payable_estimate
- reverse_charge_base
- reverse_charge_tax
- zero_vat_income
- zero_vat_expense
- open_reviews
- notes

## Tab: ReviewQueue
Filter on review_status = needs_review

