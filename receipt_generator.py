# EN: Import tools needed to create a PDF receipt
# JP: PDFレシートを作成するために必要なツールをインポートします

from datetime import datetime

from reportlab.platypus import SimpleDocTemplate, Spacer, Table, Paragraph, TableStyle
from reportlab.lib import colors
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import inch
from reportlab.lib.styles import getSampleStyleSheet


# EN: Input validation helper function
# JP: 入力チェックのヘルパー関数

def get_valid_number_of_items():
    # EN: Keep asking the user until they provide a valid number of items
    # JP: ユーザーが有効な商品の数を提供するまで、繰り返し尋ねます

    while True:
        try:
            number_of_items = int(input("How many items do you want to add? "))

            if number_of_items <= 0:
                print("Please enter a number greater than 0.")
            else:
                return number_of_items
            
        except ValueError:
            print("Invalid input. Please enter a whole number.")

def get_valid_quantity():
    # EN: Keep asking the user until they provide a valid quantity
    # JP: ユーザーが有効な数量を提供するまで、繰り返し尋ねます

    while True:
        try:
            quantity = int(input("Enter quantity: "))

            if quantity <= 0:
                print("Please enter a quantity greater than 0.")
            else:
                return quantity
            
        except ValueError:
            print("Invalid input. Please enter a whole number.")         

def get_valid_price():
    # EN: Keep asking the user until they provide a valid price
    # JP: ユーザーが有効な価格を提供するまで、繰り返し尋ねます

    while True:
        try:
            price = float(input("Enter price: "))

            if price <= 0:
                print("Please enter a price greater than 0.")
            else:
                return price
            
        except ValueError:
            print("Invalid input. Please enter a number.")

# EN: Create an empty list to store receipt items

# JP: レシートの商品データを保存するための空のリストを作成します

items = []

# EN: Ask the user how many items they want to add
# JP: 追加したい商品の数をユーザーに尋ねます

num_items = get_valid_number_of_items()

# EN: Repeat the question for each item
# JP: 各商品について質問を繰り返します

for item_number in range(num_items):
    print(f"Item {item_number + 1}:")

    item_name = input("Enter item name: ")
    quantity = get_valid_quantity()
    price = get_valid_price()
    
    items.append([item_name, quantity, price])

# EN: Create the receipt table header
# JP: レシートテーブルの見出しを作成します

receipt_data = [
    ["Item", "Quantity", "Price", "Total"]
]

# EN: Start the subtotal amount at 0
# JP: 小計金額を0から開始します

subtotal_ex_vat = 0

# EN: VAT rate used for receipt calculation
# JP: レシート計算に使用するVAT率

vat_rate = 0.20


# EN: Loop through each item and calculate the item total
# JP: 各商品をループして商品の合計金額を計算します

for item in items:
    item_name = item[0]
    quantity = item[1]
    price = item[2]

    item_total = quantity * price
    subtotal_ex_vat = subtotal_ex_vat + item_total

    receipt_data.append(
        [
            item_name,
            quantity,
            f"£{price:.2f}",
            f"£{item_total:.2f}"
        ]
    )

# EN: Calculate VAT and final total
# JP: VATと最終合計金額を計算します

vat_amount = subtotal_ex_vat * vat_rate
total_inc_vat = subtotal_ex_vat + vat_amount


# EN: Add summary rows under Price and Total columns only
# JP: Price列とTotal列の下だけに集計行を追加します

receipt_data.append(["", "", "Total ex VAT", f"£{subtotal_ex_vat:.2f}"])
receipt_data.append(["", "", "VAT 20%", f"£{vat_amount:.2f}"])
receipt_data.append(["", "", "Total inc VAT", f"£{total_inc_vat:.2f}"])

# EN: Company/shop information shown at the top of the receipt
# JP: レシートの上部に表示される会社/店舗情報

type_of_receipt = "Sales Receipt"
company_address = "123 Python Street, Python City, London, UK"
company_email = "contact@pythoncoffeeshop.com"
company_phone = "01234 567890"

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

# EN: Create a unique PDF filename using the receipt number
# JP: レシート番号を使用して一意のPDFファイル名を作成します

pdf_filename = f"receipt_{receipt_number}.pdf"

# EN: Create the PDF file
# JP: PDFファイルを作成します

pdf = SimpleDocTemplate(
    pdf_filename,
    pagesize=A4
)


# EN: Get default text styles from ReportLab
# JP: ReportLabから標準の文字スタイルを取得します

styles = getSampleStyleSheet()


# EN: Create a clean centered title style
# JP: 中央揃えのきれいなタイトルスタイルを作成します

title_style = styles["Heading1"]
title_style.alignment = 1 
title_style.fontSize = 22
title_style.spaceAfter = 20


# EN: Create the receipt title
# JP: レシートのタイトルを作成します

title = Paragraph("Python Coffee Shop", title_style)

# EN: Create receipt information text
# JP: レシート情報のテキストを作成します

normal_style = styles["Normal"]

# EN: Create centered company information style
# JP: 中央揃えの会社情報スタイルを作成します

company_style = styles["Normal"]
company_style.alignment = 1
company_style.fontSize = 10
company_style.leading = 14

# EN: Create receipt information style
# JP: レシート情報のスタイルを作成します

receipt_info_style = styles["Normal"]
receipt_info_style.fontSize = 10
receipt_info_style.leading = 14

# EN: Create company/shop information text
# JP: 会社・店舗情報のテキストを作成します

company_info = Paragraph(
    f"""
    <b>{type_of_receipt}</b><br/>
    {company_address}<br/>
    Email: {company_email}<br/>
    Phone: {company_phone}
    """,
    company_style
)

# EN: Create receipt information text
# JP: レシート情報のテキストを作成します

receipt_info = Paragraph(
    f"""
    <b>Customer Name:</b> {customer_name}<br/>
    <b>Receipt Number:</b> {receipt_number}<br/>
    <b>Receipt Date:</b> {receipt_date}
    """,
    receipt_info_style
)

# EN: Create table styling
# JP: テーブルのスタイルを作成します

table_style = TableStyle(
    [
        # EN: Main table border and grid lines
        # JP: テーブル全体の枠線とグリッド線
        ("BOX", (0, 0), (-1, -1), 1, colors.lightgrey),
        ("GRID", (0, 0), (-1, -1), 0.5, colors.lightgrey),

        # EN: Header row styling
        # JP: ヘッダ行のスタイル
        ("BACKGROUND", (0, 0), (-1, 0), colors.gainsboro),
        ("TEXTCOLOR", (0, 0), (-1, 0), colors.black),
        ("FONTNAME", (0, 0), (-1, 0), "Helvetica-Bold"),

        # EN: Body row styling
        # JP: 本文行のスタイル
        ("BACKGROUND", (0, 1), (-1, -2), colors.white),
        ("FONTNAME", (0, 1), (-1, -1), "Helvetica"),
        ("FONTSIZE", (0, 0), (-1, -1), 10),

        # EN: Summary row styling for Price and Total columns only
        # JP: Price列とTotal列だけに集計行のスタイルを適用します
        ("BACKGROUND", (0, 1), (-1, -4), colors.white),
        ("FONTNAME", (2, -3), (-1, -1), "Helvetica-Bold"),
        ("BOX", (2, -3), (-1, -1), 1, colors.lightgrey),
        ("GRID", (2, -3), (-1, -1), 0.5, colors.lightgrey),
        
        # EN: Alignment
        # JP: 配置
        ("ALIGN", (0, 0), (-1, -1), "CENTER"),

        # EN: Padding for cleaner spacing
        # JP: 読みやすくするための余白
        ("LEFTPADDING", (0, 0), (-1, -1), 6),
        ("RIGHTPADDING", (0, 0), (-1, -1), 6),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 6),

        # EN: Keep text vertically centered
        # JP: テキストを縦方向の中央に配置
        ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
    ]
)


# EN: Create the receipt table with fixed column widths
# JP: 固定された列幅でレシートテーブルを作成します

receipt_table = Table(
    receipt_data,
    colWidths=[2.0 * inch, 1.0 * inch, 1.2 * inch, 1.2 * inch]
)

receipt_table.setStyle(table_style)


# EN: Build the final PDF
# JP: 最終的なPDFを作成します

pdf.build([
    title,
    Spacer(1, 20),
    company_info,
    Spacer(1, 20),
    receipt_info,
    Spacer(1, 20),
    receipt_table
])


# EN: Show a success message in the terminal
# JP: ターミナルに成功メッセージを表示します

print(f"Receipt created successfully: {pdf_filename}")