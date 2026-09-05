# Windows 11 / 10 & VSCodium Development Environment Setup

This document provides a setup guide for working on `sikkimlfa.github.io` on a Windows system using VSCodium.

---

## 1. Toolchain Installation

Open **PowerShell as Administrator** and install the required tools using Windows Package Manager (`winget`):

```powershell
# Install Git version control
winget install Git.Git -e

# Install GitHub Command Line Interface
winget install GitHub.cli -e

# Install Hugo Extended Engine (Required for PaperMod SCSS processing)
winget install Hugo.Hugo.Extended -e

# Install Python 3 (For data migrations and pipeline scripts)
winget install Python.Python.3.12 -e

# Install VSCodium (Free/Libre Open Source Software binaries of VS Code)
winget install VSCodium.VSCodium -e

```

> **Important:** Close and restart PowerShell after running these commands to refresh your system `PATH`.

---

## 2. GitHub Identity & Account Switching

If you manage multiple GitHub accounts on your Windows machine, ensure Windows Credential Manager does not lock you to an incorrect user.

### Step 2.1: Clear Cached Windows Credentials

1. Press `Win + S`, type **Credential Manager**, and press Enter.
2. Select **Windows Credentials**.
3. Under **Generic Credentials**, find all items starting with `git:https://github.com`.
4. Click **Remove**.

### Step 2.2: Authenticate GitHub CLI

In your PowerShell terminal:

```powershell
gh auth login

```

Select the following options during the interactive prompt:

* **What account do you want to log in to?** `GitHub.com`
* **What is your preferred protocol for Git operations on this machine?** `HTTPS`
* **Authenticate Git with your GitHub credentials?** `Yes`
* **How would you like to authenticate GitHub CLI?** `Login with a web browser`

Complete the browser sign-in using your `sikkimlfa` organization account.

### Step 2.3: Verify Setup

```powershell
gh auth status
git config --global user.name "Sikkim LFA"
git config --global user.email "contact@sikkimlfa.gov.in"

```

---

## 3. Cloning and Initializing the Workspace

```powershell
# Navigate to your preferred projects directory
cd "$HOME\Desktop"

# Clone with submodules (pulls PaperMod theme files automatically)
git clone --recurse-submodules [https://github.com/sikkimlfa/sikkimlfa.github.io.git](https://github.com/sikkimlfa/sikkimlfa.github.io.git) sikkimlfa-portal
cd sikkimlfa-portal

```

If the repository was cloned without `--recurse-submodules`, initialize the theme manually:

```powershell
git submodule update --init --recursive

```

---

## 4. Configuring VSCodium

1. Launch VSCodium.
2. Click **File** > **Open Folder...** and select `C:\Users\<YourUsername>\Desktop\sikkimlfa-portal`.
3. Press `Ctrl + Shift + X` to open the Extensions view and install:
* **Hugo Language Support** (`budparr.language-hugo-html`)
* **Front Matter CMS** (`eliostruyf.vscode-front-matter`)
* **Markdown All in One** (`yzhang.markdown-all-in-one`)



---

## 5. Daily Development Workflow

Open the built-in terminal in VSCodium by pressing `Ctrl + ` `.

### Run Local Development Server

```powershell
hugo server -D --disableFastRender

```

* Open `http://localhost:1313/` in your browser.
* Hugo watches for file edits and hot-reloads the browser automatically upon save.

### Draft a New Article / Notification

```powershell
hugo new posts/2026-10-15-quarterly-audit-circular.md

```

Open the newly created file in `content/posts/`, edit the content, and toggle:

```yaml
draft: false

```

### Commit and Deploy Changes

```powershell
# Review unstaged modifications
git status

# Stage all changes
git add .

# Commit with a descriptive message
git commit -m "Add quarterly audit circular for October 2026"

# Push directly to GitHub Pages pipeline
git push origin main

```

---

## 6. Project Shortcuts Reference

| Task | PowerShell Command |
| --- | --- |
| **Start Local Preview** | `hugo server -D` |
| **Strict Production Build Check** | `hugo --gc --minify` |
| **Check Remote Action Status** | `gh run list --limit 1` |
| **Follow Remote Deployment Log** | `gh run watch` |
| **Pull Remote Updates** | `git pull origin main` |

---

[← Return to Main README](https://www.google.com/search?q=../README.md) · [View Troubleshooting Runbook →](https://www.google.com/search?q=TROUBLESHOOTING.md)
