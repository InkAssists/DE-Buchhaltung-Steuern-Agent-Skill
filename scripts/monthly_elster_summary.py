#!/usr/bin/env python3
import argparse
import csv
import json
from decimal import Decimal, ROUND_HALF_UP
from pathlib import Path

Q = Decimal("0.01")


def dec(value):
    if value is None:
        return Decimal("0.00")
    text = str(value).strip()
    if not text:
        return Decimal("0.00")
    return Decimal(text.replace(",", ".")).quantize(Q, rounding=ROUND_HALF_UP)


def previous_month(target):
    year, month = map(int, target.split("-"))
    month -= 1
    if month == 0:
        year -= 1
        month = 12
    return f"{year:04d}-{month:02d}"


def parse_months(args):
    if args.months:
        return [month.strip() for month in args.months.split(",") if month.strip()]
    return [previous_month(args.month)]


def summarize(rows, months, reverse_charge_rate):
    summary = {
        "monthsIncluded": months,
        "incomeNet": Decimal("0.00"),
        "outputVat": Decimal("0.00"),
        "expenseGross": Decimal("0.00"),
        "expenseNet": Decimal("0.00"),
        "inputVatDeductible": Decimal("0.00"),
        "reverseChargeBase": Decimal("0.00"),
        "reverseChargeTax": Decimal("0.00"),
        "reverseChargeInputVatDeductible": Decimal("0.00"),
        "zeroVatExpense": Decimal("0.00"),
        "foreignVatExpenseGross": Decimal("0.00"),
        "foreignVatExpenseTax": Decimal("0.00"),
        "openReviews": [],
        "details": [],
    }

    for row in rows:
        if row.get("booking_month") not in months:
            continue

        entry_type = row.get("entry_type", "")
        tax_treatment = row.get("tax_treatment", "")
        review_status = row.get("review_status", "")
        gross = dec(row.get("gross_amount"))
        net = dec(row.get("net_amount"))
        tax = dec(row.get("tax_amount"))

        item = {
            "receipt_id": row.get("receipt_id"),
            "date": row.get("receipt_date"),
            "counterparty": row.get("counterparty"),
            "description": row.get("description"),
            "gross": f"{gross:.2f}",
            "net": f"{net:.2f}",
            "tax": f"{tax:.2f}",
            "tax_treatment": tax_treatment,
            "review_status": review_status,
        }
        summary["details"].append(item)
        if review_status == "needs_review":
            summary["openReviews"].append(item)

        if entry_type == "income":
            summary["incomeNet"] += net
            if tax_treatment in {"de_vat_19", "de_vat_7"}:
                summary["outputVat"] += tax
            continue

        summary["expenseGross"] += gross
        summary["expenseNet"] += net

        if tax_treatment in {"de_vat_19", "de_vat_7"}:
            summary["inputVatDeductible"] += tax
        elif tax_treatment == "reverse_charge_inbound":
            rc_tax = (net * reverse_charge_rate).quantize(Q, rounding=ROUND_HALF_UP)
            summary["reverseChargeBase"] += net
            summary["reverseChargeTax"] += rc_tax
            summary["reverseChargeInputVatDeductible"] += rc_tax
        elif tax_treatment in {
            "de_vat_0",
            "no_vat",
            "government_fee_no_vat",
            "domestic_postal_vat_exempt",
        }:
            summary["zeroVatExpense"] += gross
        elif tax_treatment == "foreign_vat_non_deductible":
            summary["foreignVatExpenseGross"] += gross
            summary["foreignVatExpenseTax"] += tax

    summary["vatPayableEstimate"] = (
        summary["outputVat"]
        + summary["reverseChargeTax"]
        - summary["inputVatDeductible"]
        - summary["reverseChargeInputVatDeductible"]
    ).quantize(Q, rounding=ROUND_HALF_UP)
    return summary


def to_jsonable(summary, filing_month):
    payload = {"filingMonth": filing_month}
    for key, value in summary.items():
        if isinstance(value, Decimal):
            payload[key] = f"{value:.2f}"
        else:
            payload[key] = value
    return payload


def main():
    parser = argparse.ArgumentParser(description="Summarize a bookkeeping ledger for ELSTER prep.")
    parser.add_argument("--ledger", required=True, help="Path to the CSV ledger.")
    parser.add_argument("--month", required=True, help="Filing month in YYYY-MM format.")
    parser.add_argument("--months", help="Comma-separated months to include instead of the default previous month.")
    parser.add_argument("--output", help="Optional output JSON path.")
    parser.add_argument(
        "--reverse-charge-rate",
        default="0.19",
        help="Reverse-charge VAT rate, default: 0.19",
    )
    args = parser.parse_args()

    ledger_path = Path(args.ledger)
    if not ledger_path.exists():
        raise SystemExit(f"Ledger not found: {ledger_path}")

    months = parse_months(args)
    reverse_charge_rate = Decimal(args.reverse_charge_rate)

    with ledger_path.open(newline="", encoding="utf-8") as handle:
        rows = list(csv.DictReader(handle))

    summary = summarize(rows, months, reverse_charge_rate)
    payload = to_jsonable(summary, args.month)
    output = json.dumps(payload, indent=2, ensure_ascii=False) + "\n"

    if args.output:
        output_path = Path(args.output)
        output_path.parent.mkdir(parents=True, exist_ok=True)
        output_path.write_text(output, encoding="utf-8")

    print(output, end="")


if __name__ == "__main__":
    main()

