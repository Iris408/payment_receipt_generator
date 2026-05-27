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

### Version 7.0

Added input validation.

This version prevents the program from crashing when an invalid value is input.

Validation was added for:

- Number of receipt items
- Item quantity and price

### Version 8.0

Improved PDF layout and styling and added VAT summary.

This version improves the design of the generated receipt by adding:

- Cleaner title formatting
- Company/shop section styling
- Fixed table column widths
- Improved table spacing
- Styled header and summary rows
- VAT summary rows
  - Total ex VAT
  - VAT 20%
  - Total inc VAT

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
- Version 9.0: Add receipt folder storage
- Version 10.0: Add customer name input
- Version 11.0: Add company details input
- Version 12.0: Add payment method failed
```