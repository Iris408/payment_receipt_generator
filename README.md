# Payment Receipt Generator

This is a beginner Python project that generates a PDF payment receipt using ReportLab.

## Version History

### v1.0.0 — Static PDF Receipt Generator

Created the first version of this project. This version generated a basic PDF receipt with static receipt data.

### v2.0.0 – v4.0.0 — Core Receipt Logic

Added automatic calculation of item totals and final receipt totals. Added terminal input for receipt items, and unique receipt numbers.

### v5.0.0 – v8.0.0 — PDF Improvements

Added unique PDF filenames, company details, input validation, improved PDF layout, and VAT summary rows.

### v9.0.0 — Final Receipt Workflow Upgrade

Combined several workflow improvements into one release:

- Receipts are saved inside a `receipts/` folder
- Customer name can be entered in the terminal
- Company/shop details can be entered in the terminal
- Payment method can be selected from Debit Card, Credit Card and Gift Card
- Payment status can be shown as Approved or Declined
- A static footer message is shown at the bottom of each receipt
- Default company details are available if the user leaves fields blank

## Tech Stack

- Python
- ReportLab
- PDF generation

## Project Structure

```text
payment_receipt_generator/
├── receipt_generator.py
├── payment_receipt.pdf
├── requirements.txt
├── README.md
└── .gitignore
```

## Future Improvements

- Export receipt data to CSV
- Add receipt search/history
- Add a simple web UI interface
- Add automated tests
- Package the project for easier setup
