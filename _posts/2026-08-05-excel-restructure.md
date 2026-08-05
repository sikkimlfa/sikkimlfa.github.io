---
title: "Restructuring Multi-Year Excel Data into a Single Year-Wise Table with Microsoft Excel"
date: 2026-08-05 13:00:00 +0000
categories: [excel]
tags: [excel, data-cleaning, data-transformation, power-query, pivot-table, fiscal-year, spreadsheets, productivity]
---

# Restructuring Multi-Year Excel Data into a Single Year-Wise Table with Microsoft Excel

Business reports often store data for different Financial Years (FY) in separate tables within the same worksheet or across multiple worksheets. While this layout is convenient for preparing annual reports, it becomes difficult when you need to analyze trends, create dashboards, generate PivotTables, or import data into Power BI.

In this conversation, the objective was simple:

> Convert multiple FY-wise tables into a single consolidated table and arrange the data year-wise.

Although the uploaded Excel file could not be processed because of a temporary tool limitation, the approach remains the same regardless of the workbook's size.

---

# The Problem

Suppose an Excel workbook contains data like this:

## FY 2021-22

| Department | Revenue | Expenditure |
| ---------- | ------- | ----------- |
| A          | 120     | 100         |
| B          | 80      | 70          |

---

## FY 2022-23

| Department | Revenue | Expenditure |
| ---------- | ------- | ----------- |
| A          | 140     | 110         |
| B          | 95      | 82          |

---

## FY 2023-24

| Department | Revenue | Expenditure |
| ---------- | ------- | ----------- |
| A          | 155     | 120         |
| B          | 110     | 90          |

Each Financial Year is stored as a separate table.

While visually appealing, this structure is not suitable for:

* Trend analysis
* PivotTables
* Charts
* Power BI
* Power Query
* SQL databases
* Python analysis

---

# Desired Output

Instead of maintaining separate tables, the data should be combined into one master table.

| Financial Year | Department | Revenue | Expenditure |
| -------------- | ---------- | ------- | ----------- |
| 2021-22        | A          | 120     | 100         |
| 2021-22        | B          | 80      | 70          |
| 2022-23        | A          | 140     | 110         |
| 2022-23        | B          | 95      | 82          |
| 2023-24        | A          | 155     | 120         |
| 2023-24        | B          | 110     | 90          |

This format is called **normalized** or **long-format data**.

---

# Benefits of a Consolidated Table

A single table offers numerous advantages.

## Easier Filtering

You can filter records for any Financial Year instantly.

Example:

```
FY = 2023-24
```

returns only the required records.

---

## Better PivotTables

Instead of creating separate PivotTables for each FY, one PivotTable can compare all years.

Example:

| Department | 2021-22 | 2022-23 | 2023-24 |
| ---------- | ------- | ------- | ------- |
| A          | 120     | 140     | 155     |
| B          | 80      | 95      | 110     |

---

## Faster Chart Creation

Excel charts work best when all data is stored in one table.

Examples include:

* Line charts
* Trend analysis
* Bar charts
* Comparative dashboards

---

## Compatible with Power BI

Power BI expects normalized data.

Separate tables require additional transformation before analysis.

---

## Easier Formula Management

Instead of writing formulas repeatedly for each FY table, formulas automatically extend when using an Excel Table.

Example:

```excel
=SUMIFS(Table1[Revenue],Table1[Financial Year],"2023-24")
```

---

# Typical Workflow

The restructuring process generally follows these steps.

```text
Existing Workbook
        │
        ▼
Locate Each FY Table
        │
        ▼
Identify Common Columns
        │
        ▼
Insert Financial Year Column
        │
        ▼
Append All Records
        │
        ▼
Create Master Table
        │
        ▼
Analysis / Dashboard / PivotTable
```

---

# Best Practices

## Keep Column Names Identical

Instead of:

```
Revenue
Income
Receipt
```

use one consistent heading.

```
Revenue
```

---

## Add Financial Year Column

Never rely on table titles.

Instead include:

| Financial Year |
| -------------- |
| 2021-22        |
| 2022-23        |
| 2023-24        |

This makes filtering effortless.

---

## Convert to Excel Table

Press

```
Ctrl + T
```

Benefits include:

* Dynamic ranges
* Automatic formatting
* Structured references
* Easier PivotTables

---

## Avoid Blank Rows

Blank rows interrupt:

* Power Query
* PivotTables
* Sorting
* Filtering

Keep the dataset continuous.

---

# Using Power Query

Power Query is the preferred method for combining multiple tables.

Typical workflow:

1. Import each table.
2. Standardize column names.
3. Add a Financial Year column.
4. Append all tables.
5. Load the combined data back into Excel.

Advantages:

* Repeatable process
* Minimal manual effort
* Easy to refresh when new data is added

---

# Common Challenges

## Different Column Names

Example:

```
Amount
```

versus

```
Total Amount
```

These should be standardized before combining.

---

## Missing Columns

Some FY tables may contain additional or missing fields.

A consistent structure is necessary for accurate consolidation.

---

## Merged Cells

Merged cells interfere with sorting, filtering, and Power Query.

They should be removed before transformation.

---

## Totals Inside Data

Rows such as:

```
Grand Total
```

should be excluded from the master dataset.

Totals should be calculated separately using PivotTables or formulas.

---

# Ideal Structure for Analysis

A well-designed dataset resembles the following:

| FY      | Department | Scheme   | Amount | Remarks   |
| ------- | ---------- | -------- | ------ | --------- |
| 2021-22 | A          | Scheme A | 120    | Completed |
| 2021-22 | B          | Scheme B | 90     | Pending   |
| 2022-23 | A          | Scheme A | 140    | Completed |
| 2022-23 | B          | Scheme B | 95     | Completed |
| 2023-24 | A          | Scheme A | 155    | Completed |

This layout is ideal for:

* Excel formulas
* PivotTables
* Power Query
* Power BI
* SQL
* Python
* Data visualization

---

# Temporary Limitation Encountered

During this conversation, an Excel workbook (`CARR.xlsx`) was uploaded for restructuring. The intended workflow was to inspect the workbook, identify FY-wise tables, and consolidate them into a single year-wise master table.

However, a temporary limitation prevented the spreadsheet from being processed at that time. As a result, the file could not be analyzed or transformed during the session.

---

# Next Steps

When the workbook can be processed successfully, the restructuring would involve:

1. Reading all worksheets.
2. Detecting individual FY tables.
3. Standardizing column names.
4. Adding a **Financial Year** column where required.
5. Appending all records into one master dataset.
6. Delivering:

   * A cleaned Excel workbook.
   * A consolidated master table.
   * Year-wise sorted data.
   * Pivot-ready format.
   * Optional Power Query solution for future refreshes.

---

# Conclusion

Keeping each Financial Year in a separate table is suitable for presentation but inefficient for analysis. Consolidating all records into a single normalized table simplifies reporting, enables powerful analytical tools such as PivotTables and Power BI, reduces manual work, and makes future updates significantly easier.

Whether the dataset contains three years or thirty, a well-structured master table provides a scalable foundation for reporting, auditing, dashboard creation, and data-driven decision making.
