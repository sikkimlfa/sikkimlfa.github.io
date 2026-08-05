---
title: "Building an Audit Report Analysis System with GitHub Pages, JavaScript, GitHub Actions, and Python"
date: 2026-08-05 03:09:00 +0000
categories: [tech, github]
tags: [audit, github-pages, javascript, python, markdown, github-actions, automation, data-analysis, jekyll]
---

# Building an Audit Report Analysis System with GitHub Pages

Managing hundreds of audit reports becomes increasingly difficult as the number of local bodies, audit years, and observations grows. Traditional document storage makes searching, comparing, and analyzing reports time-consuming.

This project aims to transform audit reports into a searchable knowledge base using GitHub Pages, GitHub Actions, JavaScript, and a small amount of Python.

The result is a completely free system that automatically converts reports, builds an index, and provides an interactive website for browsing audit reports.

---

# Project Goals

The objectives are:

- Store audit reports in a GitHub repository
- Automatically convert DOCX and PDF reports into Markdown
- Generate metadata for every report
- Build a searchable website
- Allow future statistical analysis
- Keep hosting completely free using GitHub Pages

---

# Overall Architecture

```
Audit Report
     │
     ▼
DOCX / PDF
     │
     ▼
GitHub Repository
     │
     ▼
GitHub Actions
     │
     ▼
Python Conversion
     │
     ├── Markdown Files
     ├── JSON Database
     └── Statistics
            │
            ▼
GitHub Pages
            │
            ▼
Interactive Website
```

---

# Why GitHub Pages?

GitHub Pages offers several advantages.

- Completely free
- No server maintenance
- Automatic deployment
- Excellent version control
- Easy collaboration
- Fast global CDN

The limitation is that GitHub Pages only serves static files.

There is no backend.

Therefore, document conversion must happen before deployment.

---

# Why Use Markdown?

Markdown is an excellent storage format for audit reports.

Example:

```markdown
# Audit Report

## Observation 1

Improper maintenance of cash book.

## Observation 2

Utilization certificates not submitted.
```

Advantages include:

- Human readable
- Git friendly
- Small file size
- Easy searching
- Easy rendering
- Works directly with GitHub Pages

---

# Markdown vs JSON vs XML

## Markdown

Best for reading.

Example:

```markdown
## Observation 12

Stock Register not maintained.
```

Advantages

- Very readable
- Git diff friendly
- Easy editing
- Works with Markdown renderers

Disadvantages

- Harder to perform analytics

---

## JSON

Best for applications.

Example

```json
{
  "unit":"Gangtok Municipal Corporation",
  "year":2025,
  "observations":24
}
```

Advantages

- Fast searching
- Structured
- Easy filtering
- Great for dashboards

Disadvantages

- Not pleasant to read manually

---

## XML

Mostly useful when exchanging data between software.

Example

```xml
<report>
  <unit>Gangtok</unit>
</report>
```

Advantages

- Standardized
- Validation support

Disadvantages

- Verbose
- Difficult to read
- Rarely needed for this project

---

# Recommended Storage Strategy

Store both formats.

```
report.md
report.json
```

Markdown is for reading.

JSON is for searching and analytics.

---

# Why Not Use Only JavaScript?

Initially it seems possible.

Unfortunately browsers cannot reliably convert DOCX and PDF.

They have several limitations.

## JavaScript Can

- Read Markdown
- Read JSON
- Search data
- Render reports
- Create dashboards
- Export CSV
- Filter reports

## JavaScript Cannot Reliably

- Parse complicated PDFs
- Preserve Word formatting
- Extract tables accurately
- Read scanned PDFs
- Perform OCR

That is why preprocessing is required.

---

# Hybrid Workflow

The recommended workflow is:

```
Python
↓

Convert documents

↓

Markdown + JSON

↓

GitHub Repository

↓

GitHub Pages

↓

JavaScript Viewer
```

Python runs only during preprocessing.

The website itself contains no Python.

---

# Repository Structure

```
audit-report-viewer/

.github/
    workflows/

css/

js/

data/

database/

templates/

input/

output/

docs/

README.md

LICENSE

index.html

files.json

localbodies.csv
```

Everything remains organized.

---

# Processing Workflow

```
Upload

↓

DOCX/PDF

↓

Python

↓

Extract Text

↓

Identify Unit

↓

Identify Audit Year

↓

Count Observations

↓

Normalize Unit

↓

Generate Markdown

↓

Generate JSON

↓

Generate files.json

↓

GitHub Pages
```

---

# Observation Detection

Every report contains audit observations.

Typical headings include:

- Audit Findings
- Observation
- Audit Para
- Para
- Irregularities
- Compliance Issues

The converter counts these automatically.

Example

```
Observation 1

Observation 2

Observation 3
```

Result

```
Observation Count = 3
```

---

# Standardizing Local Body Names

Different reports often use different spellings.

Example

```
Gangtok Municipal Council

Gangtok MC

GMC

Gangtok Municipality
```

All should become

```
Gangtok Municipal Corporation
```

This is achieved using

```
localbodies.csv
```

Example

| Variant | Standard |
|----------|----------|
| GMC | Gangtok Municipal Corporation |
| Gangtok MC | Gangtok Municipal Corporation |

---

# Automatic File Naming

Each converted report is renamed.

```
gangtok-municipal-corporation-2025-18.md
```

Format

```
Unit-Year-ObservationCount
```

Advantages

- Easy sorting
- Easy searching
- Unique filenames

---

# Metadata Database

Each report also generates JSON metadata.

Example

```json
{
  "unit_name":"Gangtok Municipal Corporation",
  "audit_year":2025,
  "observations":18,
  "filename":"gangtok-2025-18.md"
}
```

These entries become

```
files.json
```

---

# Why Dynamic files.json?

Instead of maintaining JavaScript arrays manually:

```javascript
const files = [...]
```

GitHub Actions generates

```
files.json
```

JavaScript simply fetches it.

```javascript
fetch("files.json")
```

Advantages

- No manual updates
- Automatically synchronized
- Easier maintenance

---

# GitHub Actions

Whenever new reports are uploaded:

```
Push

↓

Workflow

↓

Python

↓

Markdown

↓

JSON

↓

Commit

↓

GitHub Pages Updated
```

Everything is automatic.

---

# Website Features

The frontend includes:

- Search
- Filters
- Sort by year
- Sort by unit
- Markdown preview
- Responsive layout
- Floating navigation
- Error handling

No backend required.

---

# Search Features

Users can search by

- Unit
- Year
- Observation count
- Keywords

Instant filtering occurs in the browser.

---

# Sorting

Reports can be sorted by

- Audit Year
- Unit Name
- Observation Count

Future additions include

- District
- Department
- Risk Level

---

# Markdown Rendering

Instead of showing raw Markdown

```
# Heading
```

The site renders

# Heading

using **marked.js**.

Reports become pleasant to read.

---

# Future Dashboard Ideas

Once metadata exists, dashboards become straightforward.

Examples include

- Reports by Year
- Reports by District
- Observation Trends
- High Risk Departments
- Observation Frequency
- Compliance Percentage

Libraries

- Chart.js
- Apache ECharts
- D3.js

---

# Error Handling

The application should gracefully handle:

- Missing reports
- Corrupted PDFs
- Duplicate filenames
- Invalid years
- Unknown local bodies

Rather than crashing.

---

# Documentation

The repository should include

- README
- CONTRIBUTING
- LICENSE
- Issue Templates
- Pull Request Templates

This encourages collaboration.

---

# Why GitHub Actions Instead of Running Python Locally?

Advantages

- Fully automated
- Consistent environment
- No manual steps
- Always up to date
- Easy collaboration

Only uploading reports is required.

Everything else happens automatically.

---

# Technologies Used

| Technology | Purpose |
|------------|---------|
| HTML | Website |
| CSS | Styling |
| JavaScript | Frontend |
| GitHub Pages | Hosting |
| GitHub Actions | Automation |
| Python | Document conversion |
| Markdown | Report storage |
| JSON | Metadata |
| Marked.js | Markdown rendering |
| PyMuPDF | PDF extraction |
| python-docx | DOCX extraction |

---

# Future Roadmap

## Phase 1

- Convert reports
- Generate Markdown
- Generate JSON

---

## Phase 2

- Search
- Filters
- Sorting
- Responsive interface

---

## Phase 3

- Dashboards
- Statistics
- Observation categorization

---

## Phase 4

- AI-assisted observation summarization
- Similar observation detection
- Duplicate observation identification
- Recommendation generation
- Trend analysis across years

---

# Final Thoughts

This architecture combines the strengths of static hosting and automated preprocessing.

Python is used only where it excels—extracting structured information from DOCX and PDF documents. Once preprocessing is complete, GitHub Pages serves a fast, secure, and maintenance-free website powered entirely by HTML, CSS, and JavaScript.

The approach keeps infrastructure simple while remaining scalable enough to manage thousands of audit reports, making it a practical long-term solution for creating a searchable digital audit archive and enabling future analytical capabilities such as dashboards, trend analysis, and AI-assisted insights.
