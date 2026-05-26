# EN: Import tools needed to create a PDF receipt
# JP: PDFレシートを作成するために必要なツールをインポートします

from datetime import datetime

from reportlab.platypus import SimpleDocTemplate, Spacer, Table, Paragraph, TableStyle
from reportlab.lib import colors
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet


# EN: Receipt data stored as a list of lists
# JP: レシートのデータをリストの中のリストとして保存します

receipt_data = [
    ["Item", "Quantity", "Price", "Total"],
    ["Coffee", "2", "£3.00", "£6.00"],
    ["Sandwich", "1", "£5.00", "£5.00"],
    ["Cake", "1", "£4.00", "£4.00"],
    ["", "", "Total", "£15.00"],
]

# EN: Basic receipt information
# JP: 基本的なレシート情報

customer_name = "John Smith"
receipt_number = "REC-001"
receipt_date = datetime.now().date()

# EN: Create the PDF file
# JP: PDFファイルを作成します

pdf = SimpleDocTemplate(
    "payment_receipt.pdf",
    pagesize=A4
)


# EN: Get default text styles from ReportLab
# JP: ReportLabから標準の文字スタイルを取得します

styles = getSampleStyleSheet()


# EN: Create a title style
# JP: タイトル用のスタイルを作成します

title_style = styles["Heading1"]
title_style.alignment = 1 


# EN: Create the receipt title
# JP: レシートのタイトルを作成します

title = Paragraph("Payment Receipt", title_style)

# EN: Create receipt information text
# JP: レシート情報のテキストを作成します

normal_style = styles["Normal"]

receipt_info = Paragraph(
    f"""
    Customer Name: {customer_name}<br/>
    Receipt Number: {receipt_number}<br/>
    Receipt Date: {receipt_date}
    """,
    normal_style
)

# EN: Create table styling
# JP: テーブルのスタイルを作成します

table_style = TableStyle(
    [
        ("BOX", (0, 0), (-1, -1), 1, colors.black),
        ("GRID", (0, 0), (-1, -1), 1, colors.black),
        ("BACKGROUND", (0, 0), (-1, 0), colors.grey),
        ("TEXTCOLOR", (0, 0), (-1, 0), colors.whitesmoke),
        ("ALIGN", (0, 0), (-1, -1), "CENTER"),
        ("BACKGROUND", (0, 1), (-1, -1), colors.beige),
    ]
)


# EN: Create the table and apply the style
# JP: テーブルを作成してスタイルを適用します

receipt_table = Table(receipt_data)
receipt_table.setStyle(table_style)


# EN: Build the final PDF
# JP: 最終的なPDFを作成します

pdf.build([
    title,
    Spacer(1, 20),
    receipt_info,
    Spacer(1, 20),
    receipt_table
])


# EN: Show a success message in the terminal
# JP: ターミナルに成功メッセージを表示します

print("Receipt created successfully: payment_receipt.pdf")