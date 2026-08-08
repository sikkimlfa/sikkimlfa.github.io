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
                        # Normalize: replace '&' with 'and', clean whitespace
                        normalized = item.replace("&", "and").strip()
                        lowered = normalized.lower()
                        if lowered and lowered not in seen:
                            seen.add(lowered)
                            cleaned.append(f'"{lowered}"')
                    
                    # Cap categories at max depth of 2 for Chirpy compatibility
                    if key == "categories" and len(cleaned) > 2:
                        cleaned = cleaned[:2]

                    sep = ", "
                    joined = sep.join(cleaned)
                    return f"{key}: [{joined}]"

                new_content = re.sub(r"^(categories|tags):\s*\[(.*?)\]", clean_taxonomies, content, flags=re.MULTILINE)

                if new_content != content:
                    with open(path, "w", encoding="utf-8") as f:
                        f.write(new_content)

print("Taxonomies sanitized successfully.")
