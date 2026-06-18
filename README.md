# Invoice Processor & Automated Financial Reporting System

## Overview

Invoice Processor is a Python-based desktop application that automates invoice data extraction and financial reporting. The system processes multiple PDF invoices, extracts important invoice details, generates Excel reports, performs vendor-wise spending analysis, creates visual charts, and automatically generates PowerPoint reports through a user-friendly Tkinter GUI.

## Features

* Process multiple PDF invoices automatically
* Extract invoice number, vendor name, date, amount, and GST
* Generate Excel reports using Pandas
* Perform vendor-wise spending analysis
* Create graphical reports using Matplotlib
* Generate PowerPoint presentations automatically
* User-friendly Tkinter desktop interface
* One-click report generation

## Technologies Used

* Python
* Pandas
* Tkinter
* pdfplumber
* Regular Expressions (Regex)
* Matplotlib
* OpenPyXL
* Python-PPTX

## Project Structure

InvoiceProcessor/
│
├── invoices/
│   ├── invoice1.pdf
│   ├── invoice2.pdf
│   └── invoice3.pdf
│
├── gui.py
├── multi_invoice.py
├── vendor_analysis.py
├── ppt_generator.py
├── requirements.txt
└── README.md

## Installation

### Clone the Repository

```bash
git clone https://github.com/nisargacgowda/Invoice-Processor-Automated-Financial-Reporting-System.git
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

## Usage

Run the application:

```bash
python gui.py
```

### Steps

1. Click **Select Folder**
2. Choose a folder containing PDF invoices
3. Click **Generate Complete Report**
4. The application automatically generates:

   * all_invoices.xlsx
   * vendor_chart.png
   * Invoice_Report.pptx

## Workflow

PDF Invoices
↓
Data Extraction
↓
Excel Report Generation
↓
Vendor-wise Analysis
↓
Chart Generation
↓
PowerPoint Report Generation

## Future Enhancements

* OCR Support for Scanned Invoices
* Email Report Automation
* Advanced Analytics and Insights
