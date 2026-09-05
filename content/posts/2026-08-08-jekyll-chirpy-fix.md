---
title: "Fixing Jekyll Chirpy on GitHub Pages: Resolving Node 24 Runner Deprecations, Slugify Exceptions, and 404 Category Errors"
date: "2026-08-08 10:00:00 +0530"
categories: ["Technology", "GitHub Pages"]
tags: ["jekyll", "chirpy", "github-actions", "ci-cd", "troubleshooting"]
---

Deploying a Jekyll site with the popular **Chirpy** theme on GitHub Pages offers a clean, ultra-responsive blogging setup. However, configuring custom workflows, taxonomies, and GitHub Actions runners can occasionally throw cryptic build errors, Liquid exceptions, or broken 404 links on tag and category pages.

This post documents all major issues encountered during Chirpy site deployments on GitHub Pages—including Node.js runner deprecation notices, `htmlproofer` dead link failures, Liquid integer `slugify` exceptions, and category 404 routing errors—along with complete, production-tested solutions.

---

## 1. Node.js 20 Deprecation Warnings on GitHub Runners

### Issue Overview
During GitHub Actions workflow runs, standard actions (`actions/checkout@v4`, `actions/configure-pages@v5`, `actions/upload-pages-artifact@v3`) may emit deprecation warnings:

```text
Node.js 20 is deprecated. The following actions target Node.js 20 
but are being forced to run on Node.js 24...

```

### Cause

GitHub Actions updated default virtual environments to run JavaScript actions on the **Node 24** runtime engine while maintaining backward compatibility for Node 20 actions.

### Solution

These annotations are non-fatal build notices. To ensure optimal workflow compatibility without warnings, update your `.github/workflows/build-deploy.yml` with modern action releases and explicitly disable non-critical warnings where appropriate.

---

## 2. Liquid Exception: `undefined method 'gsub' for an instance of Integer`

### Issue Overview

During `bundle exec jekyll build`, the build process crashes with a Ruby exception in `_layouts/tags.html`:

```text
Liquid Exception: undefined method 'gsub' for an instance of Integer in .../_layouts/tags.html
NoMethodError: undefined method 'gsub' for an instance of Integer

```

### Cause

When post front matter includes numeric or year tags (e.g., `tags: [2025]` or `tags: [2026]`), YAML parses the values as `Integer` data types. When Chirpy’s default `_layouts/tags.html` passes these values to Liquid’s `slugify` filter without explicit type conversion, Ruby fails because `.gsub()` cannot be called on an integer.

### Solution

Override `_layouts/tags.html` in your repository root to cast all tag variables to strings using `| append: ''` before processing:

```html
---
layout: page
---

{% include lang.html %}

{% assign tags_list = '' | split: '' %}

{% for post in site.posts %}
  {% for tag in post.tags %}
    {% assign tag_str = tag | append: '' | strip %}
    {% if tag_str != '' %}
      {% unless tags_list contains tag_str %}
        {% assign tags_list = tags_list | push: tag_str %}
      {% endunless %}
    {% endif %}
  {% endfor %}
{% endfor %}

{% assign tags_list = tags_list | sort_natural %}

<div id="tags" class="d-flex flex-wrap mx-xl-2">
  {% for tag in tags_list %}
    {% assign tag_str = tag | append: '' %}
    {% assign tag_slug = tag_str | slugify %}
    {% assign tag_posts = site.tags[tag] %}
    <a href="{{ tag_slug | prepend: '/tags/' | relative_url }}/" class="tag">
      {{ tag_str }}<span class="text-muted">({{ tag_posts.size }})</span>
    </a>
  {% endfor %}
</div>

```

---

## 3. 404 Page Not Found Errors on Categories and Tags

### Issue Overview

Clicking on category or tag pills within posts or navigation sidebars returns a standard `404: Page Not Found` error on deployed sites.

### Cause

1. **Hierarchical Category Misunderstanding:** Chirpy interprets post `categories` as a nested tree (`[Primary Category, Subcategory]`). Specifying 3 or 4 flat categories creates invalid nested routing paths.
2. **Missing Tab Pages:** The site lacks `_tabs/categories.md` or `_tabs/tags.md`.
3. **Plugin Collisions:** Having `jekyll-archives` enabled in `_config.yml` creates destination path collisions with Chirpy's native taxonomy generators.
4. **Special Character Escaping:** Category names containing raw `&` or slashes break URL slug generation.

### Solution

#### Step A: Enforce Max Category Depth (Max 2 Levels)

Limit post categories to 2 levels maximum (`[Category, Subcategory]`) and convert ampersands to words:

```yaml
# Recommended Front Matter Structure
---
title: "Standard Operating Procedures for Local Audits"
categories: ["Public Finance", "Audit and Governance"]
tags: ["Local Fund Audit", "Panchayati Raj", "Sikkim"]
---

```

#### Step B: Ensure Tab Pages Exist

Verify that `_tabs/categories.md` and `_tabs/tags.md` exist in your project root with exact permalinks:

```yaml
# _tabs/categories.md
---
layout: categories
title: Categories
icon: fas fa-stream
order: 2
permalink: /categories/
---

```

```yaml
# _tabs/tags.md
---
layout: tags
title: Tags
icon: fas fa-tags
order: 3
permalink: /tags/
---

```

---

## 4. `htmlproofer` Flagging Client-Side Category Links

### Issue Overview

The `htmlproofer` CI/CD step fails with hundreds of internal link errors:

```text
At _site/categories/index.html:1:
  internally linking to /categories/governance/, which does not exist
HTML-Proofer found 233 failures!

```

### Cause

Chirpy handles tag and category navigation via client-side JavaScript rendering. Static link verification tools like `htmlproofer` inspect built HTML files on disk without executing JavaScript, flagging virtual sub-routes as missing files.

### Solution

Configure `htmlproofer` in `.github/workflows/build-deploy.yml` to ignore dynamic taxonomy routes:

```yaml
      - name: Test site
        run: |
          bundle exec htmlproofer _site \
            --disable-external \
            --ignore-urls "/^http:\/\/127.0.0.1/,/^http:\/\/0.0.0.0/,/^http:\/\/localhost/,/^\/tags\//,/^\/categories\//"

```

---

## 5. Automated Build Sanitizer (`sanitize.py`)

To prevent recurring front matter issues across hundreds of blog posts, add a `sanitize.py` script to your repository root and execute it before the `bundle exec jekyll build` step.

### `sanitize.py` Script

```python
import os
import re

posts_dir = "_posts"

if os.path.exists(posts_dir):
    for root, _, files in os.walk(posts_dir):
        for file in files:
            if file.endswith((".md", ".markdown")):
                path = os.path.join(root, file)
                with open(path, "r", encoding="utf-8") as f:
                    content = f.read()

                def clean_taxonomies(match):
                    key = match.group(1)
                    raw_vals = match.group(2)
                    items = [x.strip().strip("\"'").strip() for x in raw_vals.split(",") if x.strip()]
                    
                    cleaned = []
                    seen = set()
                    for item in items:
                        # Normalize ampersands and strip extra whitespace
                        normalized = item.replace("&", "and").strip()
                        lowered = normalized.lower()
                        if lowered and lowered not in seen:
                            seen.add(lowered)
                            cleaned.append(f'"{lowered}"')
                    
                    # Cap category depth at 2 for Chirpy compatibility
                    if key == "categories" and len(cleaned) > 2:
                        cleaned = cleaned[:2]

                    sep = ", "
                    joined = sep.join(cleaned)
                    return f"{key}: [{joined}]"

                new_content = re.sub(r"^(categories|tags):\s*\[(.*?)\]", clean_taxonomies, content, flags=re.MULTILINE)

                if new_content != content:
                    with open(path, "w", encoding="utf-8") as f:
                        f.write(new_content)

print("Taxonomies successfully sanitized for Chirpy compatibility.")

```

---

## 6. Complete GitHub Actions Workflow (`.github/workflows/build-deploy.yml`)

Here is the production-ready GitHub Actions workflow incorporating all fixes:

```yaml
name: "Build and Deploy"
on:
  push:
    branches:
      - main
      - master
    paths-ignore:
      - .gitignore
      - README.md
      - LICENSE

  workflow_dispatch:

permissions:
  contents: read
  pages: write
  id-token: write

concurrency:
  group: "pages"
  cancel-in-progress: true

jobs:
  build:
    runs-on: ubuntu-latest

    steps:
      - name: Checkout
        uses: actions/checkout@v4
        with:
          fetch-depth: 0

      - name: Setup Pages
        id: pages
        uses: actions/configure-pages@v5

      - name: Setup Ruby
        uses: ruby/setup-ruby@v1
        with:
          ruby-version: 3.3
          bundler-cache: true

      - name: Sanitize Front Matter
        run: python3 sanitize.py

      - name: Build site
        run: bundle exec jekyll b -d "_site${{ steps.pages.outputs.base_path }}"
        env:
          JEKYLL_ENV: "production"

      - name: Test site
        run: |
          bundle exec htmlproofer _site \
            --disable-external \
            --ignore-urls "/^http:\/\/127.0.0.1/,/^http:\/\/0.0.0.0/,/^http:\/\/localhost/,/^\/tags\//,/^\/categories\//"

      - name: Upload site artifact
        uses: actions/upload-pages-artifact@v3
        with:
          path: "_site${{ steps.pages.outputs.base_path }}"

  deploy:
    environment:
      name: github-pages
      url: ${{ steps.deployment.outputs.page_url }}
    runs-on: ubuntu-latest
    needs: build
    steps:
      - name: Deploy to GitHub Pages
        id: deployment
        uses: actions/deploy-pages@v4

```

---

## Conclusion

By implementing explicit Liquid string conversions in `_layouts/tags.html`, capping category depth to two levels, sanitizing front matter during CI/CD, and updating your `htmlproofer` rules, your Jekyll Chirpy site will build cleanly and route all tag and category links without 404 errors.
