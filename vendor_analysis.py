import pandas as pd
import matplotlib.pyplot as plt

def generate_chart():

    df = pd.read_excel("all_invoices.xlsx")

    vendor_data = df.groupby(
        "Vendor"
    )["Amount"].sum()

    vendor_data.plot(kind="bar")

    plt.title("Vendor Wise Spending")
    plt.xlabel("Vendor")
    plt.ylabel("Amount")

    plt.tight_layout()

    plt.savefig("vendor_chart.png")

    print("Chart Generated")

if __name__ == "__main__":
    generate_chart()