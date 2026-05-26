# Payment Receipt Generator

A beginner Python project that generates a PDF payment receipt using ReportLab.

## Version History

### Version 1.0

Created a static PDF payment receipt with:

- Receipt title
- Customer name
- Receipt number
- Receipt date
- Static item table
- Sample PDF output

### Version 2.0

Added automatic receipt calculation.

This version calculates:

- Item total
- Final receipt total

Example:

```text
quantity x price = item total

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

```markdown
## Future Improvements

- Version 3.0: Add user input for receipt items
- Version 4.0: Generate unique receipt numbers
- Version 5.0: Save receipts with unique filenames
- Version 6.0: Add company/shop details
```