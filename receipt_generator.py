# EN: Import
# JP: インポート
import os
from datetime import datetime

from reportlab.platypus import SimpleDocTemplate, Spacer, Table, Paragraph, TableStyle
from reportlab.lib import colors
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import inch
from reportlab.lib.styles import getSampleStyleSheet

# =========================================
# EN: Text input helper functions
# JP: テキスト入力用のヘルパー関数
# =========================================

def get_required_text(prompt):
    # EN: Keep asking until the user enters text
    # JP: ユーザーがテキストを入力するまで繰り返します

    while True:
        value = input(prompt).strip()

        if value:
            return value

        print("This field cannot be empty.")

def get_optional_text(prompt, default_value):
    # EN: Use default value if the user leaves the field blank
    # JP: 入力が空の場合はデフォルト値を使用します

    value = input(f"{prompt} [{default_value}]: ").strip()

    if value:
        return value

    return default_value

# =========================================
# EN: Number input validation helper functions
# JP: 数値入力チェック用のヘルパー関数
# =========================================

def get_valid_number_of_items():
    # EN: Keep asking until the user enters a valid whole number
    # JP: ユーザーが有効な整数を入力するまで繰り返します

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
    # EN: Keep asking until the user enters a valid quantity
    # JP: ユーザーが有効な数量を入力するまで繰り返します

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
    # EN: Keep asking until the user enters a valid price
    # JP: ユーザーが有効な価格を入力するまで繰り返します

    while True:
        try:
            price = float(input("Enter price: "))

            if price <= 0:
                print("Please enter a price greater than 0.")

            else:
                return price

        except ValueError:
            print("Invalid input. Please enter a number.")

# =========================================
# EN: Payment helper functions
# JP: 支払い用のヘルパー関数
# =========================================

def get_payment_method():
    # EN: Let the user choose a valid payment method
    # JP: ユーザーが有効な支払い方法を選択できるようにします

    valid_payment_methods = ["Debit Card", "Credit Card", "Gift Card"]

    while True:
        payment_method = input(
            "Enter payment method (Debit Card, Credit Card, Gift Card) [Debit Card]: "
        ).strip()

        if payment_method == "":
            return "Debit Card"

        for valid_method in valid_payment_methods:
            if payment_method.lower() == valid_method.lower():
                return valid_method

        print("Invalid payment method. Please enter Debit Card, Credit Card, or Gift Card.")

def get_payment_status():
    # EN: Let the user confirm whether the payment was approved or declined
    # JP: 支払いが承認されたか拒否されたかを確認します

    valid_payment_statuses = ["Approved", "Declined"]

    while True:
        payment_status = input(
            "Enter payment status (Approved, Declined) [Approved]: "
        ).strip()

        if payment_status == "":
            return "Approved"

        for valid_status in valid_payment_statuses:
            if payment_status.lower() == valid_status.lower():
                return valid_status

        print("Invalid payment status. Please enter Approved or Declined.")

# =========================================
# EN: Collect company, customer, and payment details
# JP: 会社・顧客・支払い情報を取得
# =========================================

type_of_receipt = get_optional_text(
    "Enter type of receipt",
    "Payment Receipt"
)

company_name = get_optional_text(
    "Enter company/shop name",
    "Python Coffee Shop"
)

company_address = get_optional_text(
    "Enter company/shop address",
    "123 Python Street"
)

company_email = get_optional_text(
    "Enter company/shop email",
    "contact@pythonshop.com"
)

company_phone = get_optional_text(
    "Enter company/shop phone",
    "01234 567890"

)

customer_name = get_required_text("Enter customer name: ")

payment_method = get_payment_method()

payment_status = get_payment_status()

footer_message = "Thank you for your purchase."


# =========================================
# EN: Create receipt date, receipt number, and PDF filename
# JP: レシート日付・レシート番号・PDFファイル名を作成
# =========================================

current_datetime = datetime.now()

receipt_number = current_datetime.strftime("REC-%Y%m%d-%H%M%S")

receipt_date = current_datetime.strftime("%Y-%m-%d %H:%M:%S")

# EN: Create receipts folder if it does not exist
# JP: receipts フォルダが存在しない場合は作成します

os.makedirs("receipts", exist_ok=True)

# EN: Save generated PDFs inside the receipts folder
# JP: 作成されたPDFをreceiptsフォルダ内に保存します

pdf_filename = os.path.join(
    "receipts",
    f"receipt_{receipt_number}.pdf"
)

# EN: Create the PDF file
# JP: PDFファイルを作成します

pdf = SimpleDocTemplate(
    pdf_filename,
    pagesize=A4
)

# =========================================
# EN: Collect receipt items from user input
# JP: ユーザー入力からレシート商品データを取得
# =========================================

items = []

number_of_items = get_valid_number_of_items()

for item_number in range(number_of_items):
    print(f"\nItem {item_number + 1}")

    item_name = get_required_text("Enter item name: ")
    quantity = get_valid_quantity()
    price = get_valid_price()

    items.append([item_name, quantity, price])

# =========================================
# EN: Create receipt table data
# JP: レシートテーブルデータを作成
# =========================================

receipt_data = [
    ["Item", "Quantity", "Price", "Total"]
]

subtotal_ex_vat = 0

vat_rate = 0.20

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

# =========================================
# EN: Create PDF text styles
# JP: PDFテキストスタイルを作成
# =========================================

styles = getSampleStyleSheet()

title_style = styles["Heading1"].clone("TitleStyle")
title_style.alignment = 1
title_style.fontSize = 22
title_style.spaceAfter = 20

company_style = styles["Normal"].clone("CompanyStyle")
company_style.alignment = 1
company_style.fontSize = 10
company_style.leading = 14

receipt_info_style = styles["Normal"].clone("ReceiptInfoStyle")
receipt_info_style.fontSize = 10
receipt_info_style.leading = 14

footer_style = styles["Normal"].clone("FooterStyle")
footer_style.alignment = 1
footer_style.fontSize = 10
footer_style.leading = 14
footer_style.spaceBefore = 20

# =========================================
# EN: Create PDF text sections
# JP: PDFテキストセクションを作成
# =========================================

title = Paragraph(type_of_receipt, title_style)

company_info = Paragraph(
    f"""
    <b>{company_name}</b><br/>
    {company_address}<br/>
    Email: {company_email}<br/>
    Phone: {company_phone}
    """,
    company_style
)

receipt_info = Paragraph(
    f"""
    <b>Customer Name:</b> {customer_name}<br/>
    <b>Receipt Number:</b> {receipt_number}<br/>
    <b>Receipt Date:</b> {receipt_date}<br/>
    <b>Payment Method:</b> {payment_method}<br/>
    <b>Payment Status:</b> {payment_status}
    """,
    receipt_info_style

)

footer_info = Paragraph(
    f"<b>{footer_message}</b>",
    footer_style
)

# =========================================
# EN: Create receipt table styling
# JP: レシートテーブルのスタイルを作成
# =========================================

table_style = TableStyle(
    [
        # EN: Main table border and grid lines
        # JP: テーブル全体の枠線とグリッド線
        ("BOX", (0, 0), (-1, -1), 1, colors.black),
        ("GRID", (0, 0), (-1, -1), 0.5, colors.black),

        # EN: Header row styling
        # JP: ヘッダー行のスタイル
        ("BACKGROUND", (0, 0), (-1, 0), colors.grey),
        ("TEXTCOLOR", (0, 0), (-1, 0), colors.white),
        ("FONTNAME", (0, 0), (-1, 0), "Helvetica-Bold"),

        # EN: Body row styling
        # JP: 本文行のスタイル
        ("BACKGROUND", (0, 1), (-1, -4), colors.white),
        ("FONTNAME", (0, 1), (-1, -1), "Helvetica"),
        ("FONTSIZE", (0, 0), (-1, -1), 10),

        # EN: Summary row styling for Price and Total columns only
        # JP: Price列とTotal列だけに集計行のスタイルを適用します
        ("BACKGROUND", (2, -3), (-1, -1), colors.white),
        ("FONTNAME", (2, -3), (-1, -1), "Helvetica-Bold"),
        ("BOX", (2, -3), (-1, -1), 1, colors.white),
        ("GRID", (2, -3), (-1, -1), 0.5, colors.black),

        # EN: Keep table text centered
        # JP: テーブル内のテキストを中央揃えにします
        ("ALIGN", (0, 0), (-1, -1), "CENTER"),

        # EN: Add spacing inside each cell
        # JP: 各セルに余白を追加します
        ("LEFTPADDING", (0, 0), (-1, -1), 6),
        ("RIGHTPADDING", (0, 0), (-1, -1), 6),
        ("TOPPADDING", (0, 0), (-1, -1), 8),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 8),

        # EN: Keep text vertically centered
        # JP: テキストを縦方向の中央に配置
        ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
    ]
)

# =========================================
# EN: Create the receipt table
# JP: レシートテーブルを作成
# =========================================

receipt_table = Table(
    receipt_data,
    colWidths=[
        2.5 * inch,
        1.0 * inch,
        1.2 * inch,
        1.2 * inch

    ]

)

receipt_table.setStyle(table_style)

# =========================================
# EN: Build the final PDF
# JP: 最終的なPDFを作成
# =========================================

pdf.build([
    title,
    Spacer(1, 20),
    company_info,
    Spacer(1, 20),
    receipt_info,
    Spacer(1, 20),
    receipt_table,
    Spacer(1, 20),
    footer_info

])

# =========================================
# EN: Show a success message in the terminal
# JP: ターミナルに成功メッセージを表示
# =========================================

print(f"Receipt created successfully: {pdf_filename}")