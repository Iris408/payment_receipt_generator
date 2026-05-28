# Payment Receipt Generator

This is a beginner Python project that generates a PDF payment receipt using ReportLab.

## Current Version - V5.0
Version 5.0 improves the receipt structure and adds automatic payment calculations.

### Features
- Generated receipts are saved inside a `receipts/` folder
- Added automatic item total calculation
- Added VAT calculation at 20%
- Added final total including VAT
- Added multiple item support
- Added payment method + status validation
- Improved EN/JP comments for learning and review

## Version History
### ✅ v1: Basic PDF receipt
### ✅ v2: User input receipt data
### ✅ v3: Multiple item support
### ✅ v4: Payment details + validation
### ✅ v5: Automatic totals, VAT calculation, cleaner receipt layout

## Future Updates

### ⚠️ v6: Email receipt support
### ⚠️ v7: Automated receipt generation
### ⚠️ v8: Docker deployment


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
