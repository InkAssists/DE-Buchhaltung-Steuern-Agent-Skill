# Intake Rules V1

## Standard flow
1. Save the original file.
2. Capture the receipt date.
3. Capture counterparty or customer.
4. Capture gross, net, tax amount, and tax rate.
5. Assign category and subcategory.
6. Assign tax treatment.
7. Set review status.

## Review statuses
- auto_logged - recorded automatically or unambiguously
- manually_checked - reviewed on purpose
- needs_review - unclear, special case, or missing information

## Typical tax treatments
- Domestic standard invoice -> de_vat_19
- Domestic reduced rate -> de_vat_7
- Tax free / no VAT -> de_vat_0 or no_vat
- Foreign reverse-charge service -> reverse_charge_inbound
- Foreign VAT not deductible -> foreign_vat_non_deductible
- Unclear case -> needs_review

## Special fields
### Hospitality
- participants
- occasion

### Travel / hotel
- route or destination
- business purpose

### Vehicle costs
- vehicle reference
- trip or job reference

## Rule of thumb
- Prefer needs_review over guessing.
- Do not infer tax treatment from the payment provider alone.
- Keep the raw document and the booking record in sync.

