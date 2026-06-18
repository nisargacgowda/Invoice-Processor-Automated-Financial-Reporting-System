import os
import re
import pdfplumber
import pandas as pd

def generate_excel(folder_path):

    all_invoices = []

    for file in os.listdir(folder_path):

        if file.endswith(".pdf"):

            path = os.path.join(folder_path, file)

            text = ""

            with pdfplumber.open(path) as pdf:

                for page in pdf.pages:

                    page_text = page.extract_text()

                    if page_text:
                        text += page_text

            invoice_no = re.search(
                r"Invoice No:\s*(\S+)",
                text
            ).group(1)

            vendor = re.search(
                r"Vendor:\s*(.*)",
                text
            ).group(1)

            date = re.search(
                r"Date:\s*(.*)",
                text
            ).group(1)

            amount = re.search(
                r"Amount:\s*(\d+)",
                text
            ).group(1)

            gst = re.search(
                r"GST:\s*(\d+)",
                text
            ).group(1)

            all_invoices.append({
                "Invoice No": invoice_no,
                "Vendor": vendor,
                "Date": date,
                "Amount": int(amount),
                "GST": int(gst)
            })

    df = pd.DataFrame(all_invoices)

    df.to_excel(
        "all_invoices.xlsx",
        index=False
    )

    print("Excel Generated")

if __name__ == "__main__":
    folder = input("Enter Folder Path: ")
    generate_excel(folder)