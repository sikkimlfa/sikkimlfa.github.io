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

                # Fix inline bracket arrays: tags: [2025, audit] -> tags: ["2025", "audit"]
                def clean_inline_taxonomies(match):
                    prefix = match.group(1)
                    raw_vals = match.group(2)
                    items = [x.strip().strip("\"'").strip() for x in raw_vals.split(",") if x.strip()]
                    cleaned = []
                    seen = set()
                    for item in items:
                        lowered = item.lower()
                        if lowered and lowered not in seen:
                            seen.add(lowered)
                            cleaned.append(f'"{lowered}"')
                    sep = ", "
                    joined = sep.join(cleaned)
                    return f"{prefix}: [{joined}]"

                # Fix bulleted list items: - 2025 -> - "2025"
                def clean_bullet_items(match):
                    indent = match.group(1)
                    val = match.group(2).strip().strip("\"'").strip()
                    if val.isdigit():
                        return f'{indent}- "{val}"'
                    return match.group(0)

                new_content = re.sub(r"^(categories|tags):\s*\[(.*?)\]", clean_inline_taxonomies, content, flags=re.MULTILINE)
                new_content = re.sub(r"^(\s*)-\s+(.*)$", clean_bullet_items, new_content, flags=re.MULTILINE)

                if new_content != content:
                    with open(path, "w", encoding="utf-8") as f:
                        f.write(new_content)

print("Taxonomies sanitized successfully.")
