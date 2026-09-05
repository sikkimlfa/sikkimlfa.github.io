---
title: "Extracting Numbers in Excel and Converting PDFs to Markdown on Ubuntu"
date: 2026-08-05 10:55:00 +0000
categories: [tech]
tags: [excel, ubuntu, linux, pdf, markdown, pandoc, pdftotext]
---

# Extracting Numbers in Excel and Converting PDF Files to Markdown on Ubuntu

Recently, I worked on two common productivity tasks:

1. Extracting only numeric values from text strings in Microsoft Excel.
2. Converting multiple PDF files into Markdown format on Ubuntu and merging them into a single document.

This post documents the solutions and commands that worked.

---

# Part 1: Extract Only Numbers from Text in Excel

Suppose a cell contains the following text:

```text
Main Plan (5082755)
```

The objective is to extract only:

```text
5082755
```

## Initial Formula

I initially used:

```excel
=RIGHT(D5, LEN(D5) - MIN(SEARCH({0,1,2,3,4,5,6,7,8,9}, D5 & "0123456789"))+2)
```

However, the result was:

```text
5082755)
```

The closing parenthesis was also included.

After modifying the formula, the result became:

```text
082755)
```

which still wasn't correct.

---

## Working Solution

The following formula successfully extracted only the number enclosed within parentheses.

```excel
=SUBSTITUTE(SUBSTITUTE(MID(D5, FIND("(", D5)+1, FIND(")", D5)-FIND("(", D5)-1),"(",""),")","")
```

### How it Works

- Finds the opening parenthesis.
- Finds the closing parenthesis.
- Extracts the text between them.
- Removes any remaining parentheses.

### Result

| Original Text | Output |
|--------------|--------|
| Main Plan (5082755) | 5082755 |

This method is simple, reliable, and works whenever the number is enclosed in parentheses.

---

# Part 2: Convert All PDFs to Markdown on Ubuntu

The next task was converting multiple PDF files in a directory into Markdown files.

## Required Packages

Install the necessary tools:

```bash
sudo apt install poppler-utils pandoc
```

Verify installation:

```bash
pdftotext -v
pandoc --version
```

---

# Convert Every PDF to Markdown

Run the following command directly in the terminal:

```bash
for file in *.pdf; do pdftotext "$file" - | pandoc -f text -t markdown -o "${file%.pdf}.md"; done
```

This command:

- Loops through every PDF.
- Extracts text using `pdftotext`.
- Pipes the output directly into Pandoc.
- Saves each document as a Markdown file.

Example:

```
Report1.pdf
Report2.pdf
Report3.pdf
```

becomes

```
Report1.md
Report2.md
Report3.md
```

---

# Merge All Markdown Files

Once all Markdown files have been generated, merge them into one file:

```bash
cat *.md > merged_output.md
```

The result:

```
merged_output.md
```

contains the contents of every Markdown file.

---

# Complete Workflow

Convert all PDFs:

```bash
for file in *.pdf; do pdftotext "$file" - | pandoc -f text -t markdown -o "${file%.pdf}.md"; done
```

Merge them:

```bash
cat *.md > merged_output.md
```

---

# Why Use This Method?

This approach offers several advantages:

- No temporary text files are created.
- Processes every PDF automatically.
- Produces individual Markdown files for each PDF.
- Easily merges all files into a single Markdown document.
- Works well for documentation, note-taking, GitHub repositories, and knowledge bases.

---

# Limitations

This workflow is best suited for text-based PDFs.

Scanned PDFs require Optical Character Recognition (OCR) before conversion.

For scanned documents, consider:

- OCRmyPDF
- Tesseract OCR

These tools can generate searchable PDFs before converting them to Markdown.

---

# Conclusion

In this session, two practical problems were solved:

- Extracting numeric values enclosed in parentheses in Excel.
- Automating the conversion of multiple PDF files into Markdown on Ubuntu.

The Excel formula provided a clean way to extract only the required numbers, while the Ubuntu commands enabled efficient batch conversion and merging of Markdown files with minimal effort.

These techniques are useful for anyone working with spreadsheets, technical documentation, GitHub Pages, or document automation.

Happy automating!
