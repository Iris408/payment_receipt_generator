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

### Version 3.0

Added user input for receipt items.

This version allows the user to enter:

- Number of items
- Item name
- Quantity
- Price

Python then calculates each item total and the final total automatically before generating the PDF.

### Version 4.0

Added automatic unique receipt numbers.

This version generated a receipt number using the current date and time.

Example
```text
REC-YYYYMMDD-HHMMSS
```

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

- Version 5.0: Save receipts with unique filenames
- Version 6.0: Add company/shop details
- Version 7.0: Add input validation for incorrect values
- Version 8.0: Improve PDF layout and styling
```