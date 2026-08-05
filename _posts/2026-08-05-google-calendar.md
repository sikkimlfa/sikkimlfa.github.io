---
title: "Creating a Google Calendar (.ICS) from a Holiday List: A Practical Guide"
date: 2026-08-05 18:31:00 +0530
categories: [productivity]
tags: [google-calendar, ics, calendar, holidays, csv, scheduling, github-pages]
---

# Creating a Google Calendar (.ICS) from a Holiday List: A Practical Guide

Managing public holidays is much easier when they are available directly in your digital calendar. During this project, the objective was to convert a tabular holiday notification into a format that could be imported into Google Calendar while also supporting recurring weekly holidays such as second and fourth Saturdays.

This post documents the complete workflow, from extracting holidays from an image to preparing data for ICS, VCS, and CSV formats.

---

# Project Goal

The objective was to:

* Extract holidays from a holiday notification image.
* Create a Google Calendar compatible **ICS** file.
* Create a **VCS** calendar file for older calendar applications.
* Include recurring holidays such as:

  * Second Saturday
  * Fourth Saturday
* Identify holidays whose dates change every year.
* Convert the holiday list into structured CSV format.

---

# Source Data

The source was a holiday notification containing:

* Fixed national holidays
* State holidays
* Religious festivals
* Multi-day holidays
* Bank closing days

---

# Fixed Date Holidays

These holidays occur on the same calendar date every year.

| Holiday                    | Date        |
| -------------------------- | ----------- |
| New Year's Day             | 1 January   |
| Republic Day               | 26 January  |
| Dr. B. R. Ambedkar Jayanti | 14 April    |
| State Day                  | 16 May      |
| Independence Day           | 15 August   |
| Gandhi Jayanti             | 2 October   |
| Christmas                  | 25 December |

These are ideal candidates for annual recurring events in an ICS calendar.

---

# Variable Date Holidays

The following holidays do **not** occur on the same Gregorian calendar date every year because they are determined using lunar, Tibetan, Buddhist, or ecclesiastical calendars.

| Holiday                   |
| ------------------------- |
| Maghe Sankranti           |
| Losar                     |
| Holi                      |
| Good Friday               |
| Ramnawami (Chaite Dasain) |
| Drukpa Tshe-zi            |
| Tendong Lho Rum Faat      |
| Janmashtami               |
| Indrajatra                |
| Pang-Lhabsol              |
| Durga Puja (Dasain)       |
| Laxmi Puja (Deepawali)    |
| Losoong / Namsoong        |

These events must generally be updated each year rather than using a simple yearly recurrence rule.

---

# Multi-Day Holidays

Some holidays span multiple days.

| Holiday                | Start           | End             |
| ---------------------- | --------------- | --------------- |
| Durga Puja (Dasain)    | 11 October 2024 | 14 October 2024 |
| Laxmi Puja (Deepawali) | 1 November 2024 | 3 November 2024 |

ICS files represent these using a start date and an end date.

---

# Monthly Recurring Holidays

Apart from public holidays, recurring weekends were also included.

These are:

* Second Saturday
* Fourth Saturday

Instead of creating twelve separate entries manually, an ICS file can use recurrence rules (RRULE) such as:

```text
Second Saturday:
FREQ=MONTHLY;BYDAY=2SA

Fourth Saturday:
FREQ=MONTHLY;BYDAY=4SA
```

This greatly reduces the number of calendar entries.

---

# Additional Bank Holidays

The notification also contained bank-specific holidays.

| Holiday                              | Date      |
| ------------------------------------ | --------- |
| Yearly Closing of Bank Accounts      | 1 April   |
| Half-Yearly Closing of Bank Accounts | 1 October |

These can be included as annual recurring events.

---

# Preparing Data for CSV

A structured CSV makes it easy to generate calendars automatically.

Example:

```csv
Holiday Name,Start Date,End Date
Maghe Sankranti,2024-01-15,2024-01-15
Losar,2024-02-10,2024-02-10
Holi,2024-03-25,2024-03-25
Good Friday,2024-03-29,2024-03-29
Ramnawami (Chaite Dasain),2024-04-17,2024-04-17
Drukpa Tshe-zi,2024-07-09,2024-07-09
Tendong Lho Rum Faat,2024-08-08,2024-08-08
Janmashtami,2024-08-26,2024-08-26
Indrajatra,2024-09-17,2024-09-17
Pang-Lhabsol,2024-09-18,2024-09-18
Durga Puja (Dasain),2024-10-11,2024-10-14
Laxmi Puja (Deepawali),2024-11-01,2024-11-03
Losoong/Namsoong,2024-12-31,2024-12-31
```

This structure works well for:

* Google Calendar generators
* Python scripts
* Excel
* Power Query
* JavaScript applications

---

# ICS File Structure

An ICS calendar is a plain text file following the iCalendar specification.

A simplified event looks like this:

```text
BEGIN:VEVENT
SUMMARY:Republic Day
DTSTART;VALUE=DATE:20240126
DTEND;VALUE=DATE:20240127
END:VEVENT
```

Multi-day events include a later `DTEND` date.

Recurring events additionally include an `RRULE`.

---

# Why Use ICS Instead of Manual Entry?

Using ICS files offers several advantages.

* One-click import into Google Calendar
* Compatible with Outlook
* Compatible with Apple Calendar
* Compatible with Thunderbird
* Easy sharing with colleagues
* Can be regenerated automatically every year

---

# Creating a Complete Holiday Calendar

A complete holiday calendar should contain:

* National holidays
* State holidays
* Religious holidays
* Multi-day festivals
* Bank closing days
* Weekly recurring holidays
* Annual recurrence rules where appropriate

This provides a single calendar that can be imported into nearly every modern calendar application.

---

# Lessons Learned

Several practical observations emerged from this exercise.

* Fixed-date holidays should use yearly recurrence rules.
* Lunar and religious festivals should be updated annually.
* Multi-day holidays require both start and end dates.
* Monthly recurring Saturdays are best represented using RRULE rather than creating separate events.
* CSV serves as an excellent intermediate format for generating ICS files programmatically.

---

# Future Improvements

Possible enhancements include:

* Automatic generation of annual ICS files from government notifications.
* PDF-to-calendar conversion using OCR.
* Automatic holiday extraction using AI.
* Support for multiple Indian state holiday calendars.
* GitHub Actions workflow to regenerate calendars annually.
* Web application for importing government holiday notifications and exporting ICS files.

---

# Conclusion

Converting government holiday notifications into structured calendar formats significantly improves productivity. By organizing holidays into CSV, ICS, and recurring calendar events, the same dataset can be reused across multiple platforms, reducing manual effort and ensuring consistency.

This workflow also provides a solid foundation for building automated holiday management systems, organizational calendars, and public holiday repositories that can be updated and distributed with minimal effort.
