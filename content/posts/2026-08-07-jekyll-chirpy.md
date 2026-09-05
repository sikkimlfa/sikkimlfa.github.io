---
layout: post
title: "How to Write and Publish Blog Posts on GitHub Pages Using Jekyll Chirpy"
date: 2026-08-07 19:30:00 +0530
categories: [Blogging, GitHub Pages]
tags: [jekyll, chirpy, markdown, github-pages, workflow, documentation]
description: "A complete guide on authoring and publishing blog posts on GitHub Pages using the Chirpy theme, including front matter rules and build error prevention."
---

# Writing for Jekyll Chirpy on GitHub Pages

Publishing content with GitHub Pages and the **Jekyll Chirpy** theme offers a fast, clean, and developer-friendly blogging experience. However, because Chirpy relies on strict layout conventions and automated Ruby/Liquid compilation, a simple formatting oversight in your front matter or Markdown can fail your GitHub Actions build.

This guide provides a standardized workflow, key syntax rules to prevent build errors, and a reusable post template.

---

# Key Rules for Chirpy Front Matter

The top section of every Markdown file contains **YAML front matter** wrapped between `---` lines. Adhering to these structural rules ensures smooth deployment.

* **Explicit Layout:** Always include `layout: post` in the front matter.
* **Category Limits:** Chirpy supports a maximum of **two category levels** (e.g., `[Primary, Secondary]`). Passing three or more items in the categories array breaks layout rendering.
* **Quote Special Characters:** Always wrap titles and descriptions in double quotes (`"..."`), especially if they contain colons (`:`), dashes, or numbers.
* **String Tags:** Ensure numeric tags (e.g., years) are quoted (`"2026"` instead of `2026`) so YAML parses them as strings rather than integers.

---

# Best Practices for Body Markdown

To maintain proper rendering and avoidLiquid parsing crashes:

* **Clean Markdown Tables:** Ensure table header delimiters use standard ASCII characters (`| --- | --- |`). Avoid copying hidden non-breaking spaces (`\u00a0`) from word processors.
* **Flows and Arrows:** Instead of placing standalone arrow symbols (`↓` or `→`) on isolated empty lines, write process flows inline using code formatting (e.g., `Input` → `Process` → `Output`).
* **Fenced Code Blocks:** Always specify a language identifier for code blocks (```yaml, ```bash, ```text) to ensure syntax highlighting works cleanly.

---

# Reusable Chirpy Post Template

Save your new post files inside the `_posts/` directory using the mandatory naming format: `YYYY-MM-DD-your-file-title.md`.

```markdown
---
layout: post
title: "Your Post Title: Include Subtitle Here"
date: 2026-08-07 10:00:00 +0530
categories: [Category, Subcategory]
tags: [tag1, tag2, tag3]
description: "A concise 1-2 sentence summary of what this article covers."
---

# Introduction

Provide a direct overview of the topic. Explain what problem this post solves or what the reader will learn.

---

# Core Concepts

Explain the primary background or rules using concise bullet points:

* **Key Point 1:** Clear explanation of the concept.
* **Key Point 2:** Clear explanation of the concept.

---

# Process or Workflow

Demonstrate procedures using inline sequence flows or numbered steps:

* **Step 1:** `Data Collection` → `Verification` → `Processing`
* **Step 2:** Final execution and review.

---

# Comparative Summary

| Attribute | Option A | Option B |
| --- | --- | --- |
| **Setup Time** | Fast | Moderate |
| **Complexity** | Low | High |

---

# Code or Syntax Example

```bash
# Example terminal command
bundle exec jekyll serve

```

---

# Conclusion

Summarize the key takeaways and suggest practical next steps for the reader.

```

---

# Publishing Checklist

1. **File Name:** Verify the filename follows `YYYY-MM-DD-title-slug.md` inside `_posts/`.
2. **Front Matter Check:** Confirm `layout: post` is set and `categories` has 1 or 2 items max.
3. **Local Preview:** Test locally with `bundle exec jekyll serve` before committing.
4. **Git Push:** Commit and push to your main branch to trigger the GitHub Actions workflow.
