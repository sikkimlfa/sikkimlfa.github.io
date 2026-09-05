# Sikkim LFA Portal & Documentation Hub

[![Deploy Hugo site to Pages](https://github.com/sikkimlfa/sikkimlfa.github.io/actions/workflows/hugo.yaml/badge.svg)](https://github.com/sikkimlfa/sikkimlfa.github.io/actions/workflows/hugo.yaml)
[![Hugo Version](https://img.shields.io/badge/Hugo-v0.165.0%2BExtended-blue.svg?logo=hugo)](https://gohugo.io/)
[![Theme: PaperMod](https://img.shields.io/badge/Theme-PaperMod-green.svg?logo=github)](https://github.com/adityatelange/hugo-PaperMod)
[![Hosting: GitHub Pages](https://img.shields.io/badge/Host-GitHub%20Pages-181717.svg?logo=github)](https://sikkimlfa.github.io/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

*The central public record and statutory communication portal for the Directorate of Local Fund Audit, Finance Department, Government of Sikkim.*

[**Explore Live Portal »**](https://sikkimlfa.github.io/) · [Windows Setup Guide](WINDOWS_SETUP.md) · [Troubleshooting Runbook](TROUBLESHOOTING.md)

</div>

---

## 📌 Project Overview

This repository powers **[sikkimlfa.github.io](https://sikkimlfa.github.io/)**, an ultra-fast, zero-maintenance static portal dedicated to hosting statutory audit reports, state financial rules, circulars, notifications, and departmental publications.

Originally deployed using **Jekyll (Chirpy Theme)** via Ruby, the site underwent an architectural migration to **Hugo (PaperMod Theme)**. The modern implementation replaces dependency-heavy gem environments with a self-contained Go binary and an automated in-runner sanitization pipeline.

### Core Capabilities

- **Instant Full-Text Search:** Client-side indexing powered by Fuse.js with zero server overhead.
- **Dynamic Cloud Repository:** Direct integration with Google Drive for browsable PDF acts, regulations, and circulars.
- **Automated CI/CD Sanitization:** Python-driven ingestion step inside GitHub Actions that normalizes front matter, rewrites image URLs, and removes rogue template syntax before Hugo compiles.
- **Categorical & Chronological Browsing:** Built-in Taxonomies (Categories, Tags) and an Archive index without arbitrary hierarchy locks.
- **Adaptive UI:** Light/Dark automatic toggle respecting system preference, responsive mobile embeds, and reading-time indicators.

---

## 📊 Architecture & Migration Benchmark

### Jekyll + Chirpy vs. Hugo + PaperMod


```

Legacy Pipeline (Chirpy)                Modern Pipeline (Hugo PaperMod)
┌───────────────────────────┐           ┌───────────────────────────┐
│ Git Push (Markdown)       │           │ Git Push (Markdown)       │
└─────────────┬─────────────┘           └─────────────┬─────────────┘
▼                                       ▼
┌───────────────────────────┐           ┌───────────────────────────┐
│ Ruby Gems / Bundler Lock  │ (Frequent)│ Python In-Runner Sanitize │ (Zero failure)
│ html-proofer Strict Check │ (Fails)   │ Hugo Extended Engine      │ (Single Binary)
└─────────────┬─────────────┘           └─────────────┬─────────────┘
▼                                       ▼
┌───────────────────────────┐           ┌───────────────────────────┐
│ Build Time: 4-6 Minutes   │           │ Build Time: 12-25 Seconds │
└───────────────────────────┘           └───────────────────────────┘

```

| Metric / Dimension | Legacy Platform (Chirpy) | Modern Platform (Hugo) | Improvement / Impact |
| :--- | :--- | :--- | :--- |
| **Engine Core** | Ruby + Jekyll Runtime | Go (Hugo Extended Binary) | Standalone executable; zero dependency drift |
| **Local OS Support** | Fragile native C extensions on Win32 | Native Windows `.exe` via `winget` | 100% stable in VSCodium / PowerShell |
| **Category Limit** | Strict 2-level hierarchy limit | Arbitrary multidimensional taxonomies | No ceiling on categorizing state records |
| **Average Build Time** | 240s – 360s | 0.04s local / 18s GitHub Actions | **>90% faster pipeline execution** |
| **Deployment Mode** | Jekyll branch deployment (`gh-pages`) | Custom GitHub Actions artifact | Direct control over output artifact |
| **Front Matter Fragility** | Unquoted colons crash entire build | Automated validation pipeline | Graceful fallbacks and auto-wrapping |

---

## 🗂️ Site Map & Navigation Hierarchy

The portal is organized for easy access to official and administrative content:


```

sikkimlfa.github.io/
├── / ............................ Search Bar, Top Priority Pages & Recent Updates
├── /about/ ...................... Statutory Mandate, Department Hierarchy & Office Inquiries
├── /documents/ .................. Live Google Drive Acts, Rules & PDF Directory
├── /posts/ ...................... Comprehensive Chronological Post Archive
├── /categories/ ................. Thematic Classification (Audit, Notifications, Rules)
├── /tags/ ....................... Granular Search Keywords
├── /archives/ ................... Year-by-Year Historical Records
└── /search/ ..................... Dedicated Full-Page Fuse.js Search Portal

```

---

## 🛠️ Repository File Tree

```bash
sikkimlfa-new/
├── .github/
│   └── workflows/
│       └── hugo.yaml              # GitHub Actions deploy pipeline with embedded sanitizer
├── assets/
│   └── css/
│       └── extended/
│           └── custom.css         # Responsive mobile styling for PDF & Drive embeds
├── content/
│   ├── posts/                     # Markdown articles, notices, circulars
│   ├── about.md                   # Directorate overview and statutory scope
│   ├── archives.md                # PaperMod chronological index
│   ├── documents.md               # Google Drive folder embed and document table
│   └── search.md                  # Fuse.js search landing page
├── layouts/
│   ├── index.html                 # Custom landing layout: Search + Featured + Updates
│   └── shortcodes/
│       ├── gdrive-doc.html        # Single responsive PDF reader shortcode
│       └── gdrive-folder.html     # Browsable Google Drive iframe shortcode
├── static/
│   ├── img/                       # Static images, logos, banners
│   └── docs/                      # Local PDF fallbacks
├── themes/
│   └── PaperMod/                  # Submodule: Fast, accessible Hugo theme
└── hugo.yaml                      # Core site configuration and parameters

```

---

## 🚀 Quick Setup & Management

### Prerequisites

* **OS:** Windows 10/11, macOS, or Linux
* **IDE:** VSCodium / VS Code
* **Core CLI:** `winget`, `git`, `python` (3.8+), and `gh`

Detailed, step-by-step local machine preparation is documented in:
👉 **[Read the Windows & VSCodium Setup Guide](./WINDOWS_SETUP.md)**

### Local Development Flow

```powershell
# 1. Clone the project along with theme submodules
git clone --recurse-submodules [https://github.com/sikkimlfa/sikkimlfa.github.io.git](https://github.com/sikkimlfa/sikkimlfa.github.io.git)
cd sikkimlfa.github.io

# 2. Launch real-time local server
hugo server -D

# 3. Open in browser: http://localhost:1313/

```

### Publishing New Updates

```powershell
# Generate a new article with correct front matter
hugo new posts/2026-09-05-annual-audit-circular.md

# Stage, commit, and push
git add .
git commit -m "Publish annual audit circular 2026"
git push origin main

```

---

## 🔧 Self-Healing Pipeline: In-Runner Sanitizer

To guarantee zero build errors, our GitHub Action `.github/workflows/hugo.yaml` includes a custom Python sanitization step running before Hugo builds:

```yaml
- name: Sanitize and Validate Markdown Posts
  run: |
    python -c "
    # Validates and cleans front matter on the fly:
    # 1. Encloses raw titles containing colons in quotes.
    # 2. Normalizes non-standard dates to ISO 8601 (YYYY-MM-DDTHH:MM:SS+05:30).
    # 3. Flattens comma-separated categories/tags into clean lists.
    # 4. Converts Chirpy 'pin: true' -> Hugo 'weight: 1'.
    # 5. Maps Chirpy 'image: {path, alt}' blocks to PaperMod 'cover'.
    # 6. Strips legacy Kramdown tags ({: .prompt-info }) & Liquid tags.
    "

```

If something goes wrong during a build or push:
👉 **[Read the Troubleshooting & Recovery Runbook](./TROUBLESHOOTING.md)**

---

## 🏛️ Portal Standard Details

* **Administrative Authority:** Directorate of Local Fund Audit, Government of Sikkim
* **Headquarters:** Gangtok, Sikkim – 737101
* **Official Contact:** `sikkimlfa@gmail.com`
* **Cloud Document Storage:** [Google Drive Shared Repository](https://drive.google.com/drive/folders/1WFikN4k7GVZCjR5VYlYk1IJ6d5v1oJqd?usp=sharing)
