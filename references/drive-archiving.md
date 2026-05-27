# Generic Document Archiving

Use this workflow when a receipt, letter, invoice, or supporting document needs to be archived without exposing private infrastructure details in the public skill.

## Principles

- Keep folder IDs, account IDs, and personal archive paths out of the skill package.
- Resolve the actual destination from a private local configuration or a user-provided target at runtime.
- Prefer deterministic, human-auditable naming.
- Keep the original file and the booking record in sync.

## Suggested flow

1. Identify the document type.
2. Extract the minimum safe metadata: date, counterparty, amount, subject, and category.
3. Choose the archive bucket from the generic business context.
4. Store or move the file using the user's private destination mapping.
5. Record the archive path or reference in the ledger or intake note.

## Naming pattern

Use stable, descriptive filenames such as:

- YYYY-MM-DD_counterparty_subject_amount_currency.pdf
- YYYY-MM-DD_subject_category_needs_review.jpg

## When to defer

- The destination mapping is missing.
- The document contains unclear personal or business boundaries.
- The file looks duplicated, corrupted, or unrelated to bookkeeping.
