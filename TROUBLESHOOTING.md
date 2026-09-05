# Sikkim LFA Portal — Diagnostics & Troubleshooting Runbook

This guide covers common issues, failure indicators, and resolutions for `sikkimlfa.github.io`.

---

## 🚨 Quick Diagnostic Checklist

Run these diagnostic commands inside your VSCodium terminal:

```powershell
# 1. Test local Hugo build sanity
hugo --gc --minify

# 2. Check GitHub remote connection
git remote -v

# 3. View the latest remote deployment status
gh run list --limit 3

# 4. View failure logs if an action run failed
gh run view --log-failed

```

---

## Issue 1: Live Site Still Shows the Old Chirpy Site

### Symptoms

You pushed modern Hugo code to the `main` branch, but loading `https://sikkimlfa.github.io/` displays the old Chirpy blog layout.

### Root Causes

1. **GitHub Pages is still configured for branch deployment (`gh-pages`)** instead of the GitHub Actions build pipeline.
2. **Old Chirpy Service Worker / PWA caching** is running in your local browser.

### Resolution

#### Step 1: Switch Source to GitHub Actions

1. Navigate to: `https://github.com/sikkimlfa/sikkimlfa.github.io/settings/pages`.
2. Under **Build and deployment** > **Source**, change the dropdown to **GitHub Actions**.

#### Step 2: Purge Legacy Deployment Branches

Delete any leftover deployment branches that Chirpy used:

```powershell
git push origin --delete gh-pages

```

*(Ignore errors if the remote branch does not exist).*

#### Step 3: Unregister Browser Service Worker

1. Open `https://sikkimlfa.github.io/` in your browser.
2. Press `F12` to open Developer Tools.
3. Select the **Application** tab (or **Storage** tab in Firefox).
4. Click **Service Workers** in the left sidebar.
5. Click **Unregister** on any registered service workers for this domain.
6. Click **Clear Site Data** and force-refresh the page (`Ctrl + Shift + R`).

---

## Issue 2: `hugo --gc --minify` Fails Locally

### Common Errors and Fixes

### A. Shortcode Not Found

```text
ERROR failed to extract shortcode: template for shortcode "gdrive-folder" not found

```

* **Cause:** Hugo cannot locate `layouts/shortcodes/gdrive-folder.html`.
* **Fix:** Ensure shortcodes reside in `layouts/shortcodes/` at the root of your project:
```powershell
Test-Path "layouts\shortcodes\gdrive-folder.html"
```

If missing, recreate the shortcode using the implementation in `README.md`.

### B. YAML Unquoted Colon Exception

```text
ERROR failed to read front matter: yaml: line 2: mapping values are not allowed in this context

```

* **Cause:** A post title contains a colon without enclosing quotes (e.g., `title: Notice: Audit Report 2026`).
* **Fix:** Enclose the title string in double quotes:
```yaml
title: "Notice: Audit Report 2026"
```

### C. Deprecated `languageCode` Warning

```text
WARN deprecated: project config key languageCode was deprecated in Hugo v0.158.0 and will be removed in a future release. Use locale instead.

```

* **Cause:** Legacy configuration format in `hugo.yaml`.
* **Fix:** Open `hugo.yaml` and change `languageCode: "en-us"` to `locale: "en-us"`.

---

## Issue 3: GitHub Actions Pipeline Fails (`Deploy Hugo site to Pages`)

### How to Inspect Remote Logs

Run in PowerShell:

```powershell
gh run list --limit 1
gh run view --log-failed

```

### Case 1: `submodule: themes/PaperMod not found`

* **Cause:** Git was pushed without the theme submodule configuration.
* **Fix:** Run the following in your terminal:
```powershell
git submodule add --depth=1 [https://github.com/adityatelange/hugo-PaperMod.git](https://github.com/adityatelange/hugo-PaperMod.git) themes/PaperMod
git add .gitmodules themes/PaperMod
git commit -m "Fix PaperMod submodule configuration"
git push origin main
```

### Case 2: `Permission to sikkimlfa/sikkimlfa.github.io denied`

* **Cause:** The GitHub Actions runner lacks authorization to publish to Pages.
* **Fix:**
1. Open `https://github.com/sikkimlfa/sikkimlfa.github.io/settings/actions`.
2. Under **Workflow permissions**, select **Read and write permissions**.
3. Ensure the workflow file (`.github/workflows/hugo.yaml`) includes:
```yaml
permissions:
  contents: read
  pages: write
  id-token: write
```
---

## Issue 4: Google Drive PDF / Folder Embed Shows Blank Box

### Symptoms

The `/documents/` page renders an empty container or displays an error saying *Google Drive refused to connect*.

### Resolution Checklist

1. **Folder / File Sharing Level:**
* Open Google Drive.
* Right-click the folder/file > **Share** > **General access**.
* Ensure the permission is set to **"Anyone with the link"** and the role is **"Viewer"**.


2. **Correct Embed URL Format:**
* **Folders:** Must use the embedded endpoint:
```text
[https://drive.google.com/embeddedfolderview?id=FOLDER_ID#list](https://drive.google.com/embeddedfolderview?id=FOLDER_ID#list)
```

* **Individual Files:** Must use the preview endpoint:
```text
[https://drive.google.com/file/d/FILE_ID/preview](https://drive.google.com/file/d/FILE_ID/preview)
```

3. **Shortcode Arguments:** Verify that you passed only the ID string, not the full URL:
```markdown
<!-- CORRECT -->
{{< gdrive-folder id="1WFikN4k7GVZCjR5VYlYk1IJ6d5v1oJqd" title="Official Records" >}}

<!-- INCORRECT -->
{{< gdrive-folder id="[https://drive.google.com/drive/folders/1WFikN4k](https://drive.google.com/drive/folders/1WFikN4k)..." >}}

---
## Issue 5: Search Page Returns No Matches

### Symptoms

Navigating to `/search/` renders an input box, but typing keywords yields no results.

### Fix
1. Open `hugo.yaml` and verify that the `JSON` output format is enabled for the home section:
```yaml
outputs:
  home:
    - HTML
    - RSS
    - JSON
```

2. Confirm that `content/search.md` has `layout: "search"`:

```markdown
---
title: "Search"
layout: "search"
summary: "search"
placeholder: "Search articles..."
---
```

3. Rebuild locally using `hugo server -D` and verify that `index.json` is generated at `http://localhost:1313/index.json`.
---

[← Return to Main README](https://www.google.com/search?q=../README.md) · [View Windows Setup Guide →](https://www.google.com/search?q=WINDOWS_SETUP.md)

---

### How to Commit These Files to Your Repository

Run these commands in your VSCodium PowerShell terminal to write the documentation structure, stage it, and deploy:

```powershell
# 1. Create docs directory if it doesn't exist
New-Item -ItemType Directory -Force -Path "docs"

# 2. Add the files to git
git add README.md docs/WINDOWS_SETUP.md docs/TROUBLESHOOTING.md

# 3. Commit and push
git commit -m "Add comprehensive README, Windows setup guide, and troubleshooting runbook"
git push origin main

```
