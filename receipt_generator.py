# EN: Import tools needed to create a PDF receipt
# JP: PDFレシートを作成するために必要なツールをインポートします

from datetime import datetime

from reportlab.platypus import SimpleDocTemplate, Spacer, Table, Paragraph, TableStyle
from reportlab.lib import colors
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet


# EN: Create an empty list to store receipt items
# JP: レシートの商品データを保存するための空のリストを作成します

items = []

# EN: Ask the user how many items they want to add
# JP: 追加したい商品の数をユーザーに尋ねます

num_items = int(input("How many items do you want to add? "))

# EN: Repeat the question for each item
# JP: 各商品について質問を繰り返します

for item_number in range(num_items):
    print(f"Item {item_number + 1}:")

    item_name = input("Enter item name: ")
    quantity = int(input("Enter quantity: "))
    price = float(input("Enter price: "))
    
    items.append([item_name, quantity, price])

# EN: Create the receipt table header
# JP: レシートテーブルの見出しを作成します

receipt_data = [
    ["Item", "Quantity", "Price", "Total"]
]


# EN: Start the total amount at 0
# JP: 合計金額を0から開始します

total_amount = 0


# EN: Loop through each item and calculate the item total
# JP: 各商品をループして商品の合計金額を計算します

for item in items:
    item_name = item[0]
    quantity = item[1]
    price = item[2]

    item_total = quantity * price
    total_amount = total_amount + item_total

    receipt_data.append(
        [
            item_name,
            quantity,
            f"£{price:.2f}",
            f"£{item_total:.2f}"
        ]
    )


# EN: Add the final total row to the receipt table
# JP: 最終的な合計行をレシートテーブルに追加します

receipt_data.append(
    ["", "", "Total", f"£{total_amount:.2f}"]
)

# EN: Basic receipt information
# JP: 基本的なレシート情報

customer_name = "John Smith"

# EN: Get the current date and time for the receipt
# JP: レシートの現在の日付と時間を取得します

current_datetime = datetime.now()
receipt_date = current_datetime.strftime("REC-%Y-%m-%d - %H:%M:%S")

# EN: Create a unique receipt number using the current timestamp
# JP: 現在のタイムスタンプを使用して一意のレシート番号を作成します

receipt_number = f"{current_datetime.strftime("REC-%Y%m%d-%H%M%S")}"

# EN: Create a readable receipt date and time
# JP: 読みやすいレシートの日付と時間を作成します

receipt_date = current_datetime.strftime("%Y-%m-%d %H:%M:%S")


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