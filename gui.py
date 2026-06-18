import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox

from multi_invoice import generate_excel
from vendor_analysis import generate_chart
from ppt_generator import generate_ppt

selected_folder = ""

def select_folder():

    global selected_folder

    selected_folder = filedialog.askdirectory()

    folder_label.config(
        text=selected_folder
    )

def generate_complete_report():

    global selected_folder

    if selected_folder == "":

        messagebox.showerror(
            "Error",
            "Please Select Folder First"
        )

        return

    try:

        generate_excel(selected_folder)

        generate_chart()

        generate_ppt()

        messagebox.showinfo(
            "Success",
            "Report Generated Successfully!\n\nFiles Created:\nall_invoices.xlsx\nvendor_chart.png\nInvoice_Report.pptx"
        )

    except Exception as e:

        messagebox.showerror(
            "Error",
            str(e)
        )

root = tk.Tk()

root.title("Invoice Processor")

root.geometry("600x350")

title = tk.Label(
    root,
    text="Invoice Processor",
    font=("Arial", 20, "bold")
)

title.pack(pady=20)

folder_btn = tk.Button(
    root,
    text="Select Folder",
    command=select_folder,
    width=25
)

folder_btn.pack(pady=10)

folder_label = tk.Label(
    root,
    text="No Folder Selected",
    wraplength=550
)

folder_label.pack(pady=10)

generate_btn = tk.Button(
    root,
    text="Generate Complete Report",
    command=generate_complete_report,
    width=25
)

generate_btn.pack(pady=20)

exit_btn = tk.Button(
    root,
    text="Exit",
    command=root.destroy,
    width=25
)

exit_btn.pack(pady=10)

root.mainloop()