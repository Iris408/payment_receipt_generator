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

### Version 5.0

Added unique PDF filenames.

This version save each generated receipt with a unique filename using the receipt number, date and time.

Example
```text
receipt_REC-20260527-174505.pdf
```

### Version 6.0

Added company/shop details to the receipt.

This version shows the business information near the top of the PDF receipt, including:

- Company/ shop name
- Address
- Email address
- Phone number

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
```text
- Version 7.0: Add input validation for incorrect values
- Version 8.0: Improve PDF layout and styling
- Version 9.0: Add receipt folder storage
- Version 10.0: Add customer name input
```