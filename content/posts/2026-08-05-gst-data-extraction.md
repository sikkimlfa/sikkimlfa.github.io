---
title: "Building a Python Toolkit for GST Return PDF Auditing"
date: 2026-08-05 08:40:00 +0530
categories: [python, gst, auditing]
tags: [python, gst, pdf, csv, pdfplumber, camelot, tabula, pandas, github, automation]
---

# Building a Python Toolkit for GST Return PDF Auditing

GST return PDFs contain valuable information for auditors, but extracting that information manually is slow, repetitive, and error-prone. This project documents the process of building an open-source Python toolkit that converts GST return PDFs into structured data suitable for audit analysis.

The goal is to create a reusable toolkit that can process hundreds of GST returns with minimal manual effort.

---

# Project Objectives

The toolkit should be able to:

- Process multiple GST PDF files automatically
- Extract tables into CSV files
- Extract text into structured text files
- Preserve page structure
- Handle complex GST tables
- Produce outputs suitable for Excel, Power BI, Pandas, and SQL
- Be easy to use from the command line
- Be hosted on GitHub

---

# Understanding GST Return PDFs

GST returns are generated in several formats including:

- GSTR-1
- GSTR-2A
- GSTR-2B
- GSTR-3B
- GSTR-9
- GSTR-9C

These PDFs generally contain:

- GSTIN
- Legal Name
- Return Period
- Invoice Details
- HSN Summary
- Taxable Value
- CGST
- SGST
- IGST
- Cess
- Place of Supply
- Tax Paid
- ITC Claimed

Most GST PDFs contain:

- Multi-line cells
- Split tables
- Repeated headers
- Nested tables
- Rotated pages
- Mixed text and tables

These characteristics make extraction challenging.

---

# Choosing the Right PDF Libraries

Initially, the project used:

- tabula-py
- pdfplumber

These work well for many GST reports but struggle with highly formatted documents.

After evaluating several libraries, a better toolkit emerged.

| Library | Purpose | Rating |
|----------|----------|--------|
| pdfplumber | Text extraction | ⭐⭐⭐⭐⭐ |
| Camelot | Table extraction | ⭐⭐⭐⭐⭐ |
| PyMuPDF | Fast page reading | ⭐⭐⭐⭐⭐ |
| pdfminer.six | Low-level text extraction | ⭐⭐⭐⭐ |
| Tabula | Simple table extraction | ⭐⭐⭐⭐ |
| OCR (Tesseract) | Scanned PDFs | ⭐⭐⭐⭐⭐ |

The toolkit can later combine these libraries to maximize extraction accuracy.

---

# First Utility: PDF to CSV

The first utility scans the current folder for every PDF.

Example:

```
invoice1.pdf
invoice2.pdf
gstr3b.pdf
```

It automatically generates:

```
csv_output/

invoice1.csv
invoice2.csv
gstr3b.csv
```

Main features include:

- Batch processing
- Automatic output folder creation
- Error handling
- Empty table detection
- Logging
- UTF-8 compatibility

---

# Second Utility: PDF to Structured Text

CSV extraction works well for tables.

However, GST PDFs also contain:

- Headings
- Notes
- Return summaries
- Footer information
- Legal declarations

The second utility extracts:

- Page-wise text
- Tables
- Page separators
- Structured output

Example output:

```
---------------------------------
Page 1
---------------------------------

GSTIN
11ABCDE1234F1Z5

Return Period
April 2025

---------------------------------

Table

Invoice No    Date      Taxable
INV001        ...
```

This structured format is ideal for:

- LLMs
- RAG systems
- Search engines
- Audit evidence

---

# Repository Structure

The project was organized into a clean GitHub repository.

```
gst-pdf-audit-tools/

│
├── pdf_to_csv.py
├── pdf_to_text.py
├── requirements.txt
├── README.md
│
├── csv_output/
│
├── text_output/
│
└── .github/
    └── workflows/
        python-test.yml
```

Keeping outputs separate from source code simplifies maintenance.

---

# Dependency Management

A simple `requirements.txt` was created.

```
camelot-py[cv]
pdfplumber
PyMuPDF
pdfminer.six
pandas
openpyxl
tabulate
```

Installation:

```bash
pip install -r requirements.txt
```

---

# Windows Installation Warnings

During installation, Windows displayed warnings similar to:

```
WARNING:
The script camelot.exe is installed in ...

which is not on PATH.
```

These warnings are **not installation failures**.

They simply indicate that executable scripts are installed in a directory that Windows cannot access from the command prompt.

Python libraries continue to function normally when imported.

Adding the Scripts directory to the Windows PATH removes these warnings for future command-line use.

---

# Why Camelot Is Better Than Tabula

Both libraries extract tables.

However, Camelot offers several advantages.

## Stream Mode

Useful for tables without borders.

```python
camelot.read_pdf(
    pdf,
    flavor="stream"
)
```

---

## Lattice Mode

Useful when PDFs have visible grid lines.

```python
camelot.read_pdf(
    pdf,
    flavor="lattice"
)
```

---

## Accuracy Metrics

Camelot reports:

- Accuracy
- Whitespace
- Parsing quality

This allows automatic rejection of poor-quality tables.

---

# Why pdfplumber Is Excellent

pdfplumber provides:

- Character-level extraction
- Word coordinates
- Table detection
- Image positions
- Bounding boxes

This makes it valuable for GST reports where layouts vary significantly.

---

# Future Improvements

The toolkit can evolve into a comprehensive GST audit platform.

Possible enhancements include:

## Data Cleaning

Automatically remove:

- Blank rows
- Duplicate headers
- Empty columns

---

## GST Validation

Validate:

- GSTIN format
- Invoice numbers
- HSN codes
- Dates

---

## Tax Recalculation

Automatically compute:

- CGST
- SGST
- IGST

and compare with reported values.

---

## Cross Verification

Compare:

- GSTR-1
- GSTR-3B
- GSTR-2B
- Books of Accounts

to identify mismatches.

---

## Audit Flags

Generate observations such as:

- Missing invoices
- Duplicate invoices
- Incorrect tax rates
- ITC mismatches
- Negative taxable values
- Invalid GSTINs

---

## Export Formats

Support additional outputs:

- CSV
- Excel
- SQLite
- JSON
- Markdown

---

## OCR Support

Many GST returns are scanned.

Integrating:

- Tesseract OCR
- OCRmyPDF

would allow extraction from scanned documents.

---

# GitHub Automation

GitHub Actions can automatically:

- Check Python syntax
- Install dependencies
- Run unit tests
- Build documentation
- Publish releases

This keeps the repository reliable for contributors.

---

# Long-Term Vision

The toolkit is intended to become a complete GST audit automation framework.

Future modules may include:

- PDF ingestion
- OCR preprocessing
- Table extraction
- Data normalization
- GSTIN validation
- HSN validation
- Return reconciliation
- Risk scoring
- Exception reporting
- Dashboard generation
- AI-assisted audit observations

Ultimately, auditors should be able to place hundreds of GST return PDFs into a folder and receive clean, structured datasets along with exception reports that significantly reduce manual effort.

---

# Conclusion

Processing GST return PDFs is one of the most time-consuming aspects of GST auditing. By combining modern Python libraries such as Camelot, pdfplumber, PyMuPDF, and pandas, it is possible to automate much of this work.

A well-designed toolkit not only saves time but also improves consistency, enables large-scale analysis, and provides a strong foundation for advanced audit analytics, reconciliation, and AI-assisted compliance review.
