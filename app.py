from flask import Flask, render_template, request, send_from_directory
from datetime import datetime
import os

app = Flask(__name__)

def generate_receipt(customer_name, amount, payment_method, invoice_date, invoice_number, sale_date,
                     buyer_name, buyer_address, billing_address, seller_name, business_name, siren_number,
                     registered_office_address, purchase_order_number, vat_number):
    receipt_content = f"""
    ╔════════════════════════════╗
          Modern Receipt
    ╚════════════════════════════╝

    Date: {datetime.now().strftime("%Y-%m-%d %H:%M:%S")}
    ──────────────────────────────
    Customer Name: {customer_name}
    Amount: ${amount}
    Payment Method: {payment_method}
    ──────────────────────────────

    Additional Information
    ──────────────────────────────
    Date of Invoice Issue: {invoice_date}
    Invoice Number: {invoice_number}
    Date of Sale or Service Provision: {sale_date}
    ──────────────────────────────
    Buyer Name: {buyer_name}
    Buyer Address: {buyer_address}
    Billing Address: {billing_address}
    ──────────────────────────────
    Seller Name: {seller_name}
    Business Name: {business_name}
    Siren Number: {siren_number}
    Address of Registered Office: {registered_office_address}
    Purchase Order Number: {purchase_order_number}
    VAT Identification Number of the Seller: {vat_number}
    ──────────────────────────────
    Thank you for your business!
    ╔════════════════════════════╗
    """

    receipt_filename = f"receipt_{datetime.now().strftime('%Y%m%d%H%M%S')}.txt"
    with open(os.path.join("receipts", receipt_filename), 'w') as file:
        file.write(receipt_content)

    return receipt_content, receipt_filename




@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        customer_name = request.form['customer_name']
        amount = request.form['amount']
        payment_method = request.form['payment_method']
        invoice_date = request.form['invoice_date']
        invoice_number = request.form['invoice_number']
        sale_date = request.form['sale_date']
        buyer_name = request.form['buyer_name']
        buyer_address = request.form['buyer_address']
        billing_address = request.form['billing_address']
        seller_name = request.form['seller_name']
        business_name = request.form['business_name']
        siren_number = request.form['siren_number']
        registered_office_address = request.form['registered_office_address']
        purchase_order_number = request.form['purchase_order_number']
        vat_number = request.form['vat_number']

        receipt_content, receipt_filename = generate_receipt(customer_name, amount, payment_method,
                                                             invoice_date, invoice_number, sale_date,
                                                             buyer_name, buyer_address, billing_address,
                                                             seller_name, business_name, siren_number,
                                                             registered_office_address, purchase_order_number, vat_number)

        return render_template('index.html', receipt_content=receipt_content, receipt_filename=receipt_filename)

    return render_template('index.html', receipt_content=None, receipt_filename=None)

@app.route('/download/<filename>')
def download(filename):
    return send_from_directory('receipts', filename)

if __name__ == '__main__':
    app.run(debug=True, port=5001)
