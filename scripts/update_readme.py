#!/usr/bin/env python3
"""Rebuild the README skill-index tables from skill file frontmatter.

Scans all skills/**/*.md files, parses their YAML frontmatter, and
replaces the content between HTML comment markers in README.md:

    <!-- SKILLS:{category}:START -->
    ...auto-generated table...
    <!-- SKILLS:{category}:END -->
"""

import re
import yaml
from pathlib import Path

REPO_ROOT = Path(__file__).parent.parent
README = REPO_ROOT / "README.md"
SKILLS_DIR = REPO_ROOT / "skills"

CATEGORY_ORDER = [
    "personal-finance",
    "investing",
    "financial-modeling",
    "accounting",
    "trading",
    "data-and-research",
    "tools-and-utilities",
]

CATEGORY_LABELS = {
    "personal-finance": "Personal Finance",
    "investing": "Investing",
    "financial-modeling": "Financial Modeling",
    "accounting": "Accounting",
    "trading": "Trading",
    "data-and-research": "Data & Research",
    "tools-and-utilities": "Tools & Utilities",
}


def parse_frontmatter(filepath: Path) -> dict | None:
    """Return parsed YAML frontmatter dict, or None if not present."""
    text = filepath.read_text(encoding="utf-8")
    if not text.startswith("---"):
        return None
    end = text.find("---", 3)
    if end == -1:
        return None
    try:
        return yaml.safe_load(text[3:end])
    except yaml.YAMLError:
        return None


def collect_skills() -> dict[str, list[dict]]:
    """Return skills grouped by top-level category."""
    groups: dict[str, list[dict]] = {cat: [] for cat in CATEGORY_ORDER}

    for md_file in sorted(SKILLS_DIR.rglob("*.md")):
        if md_file.name == ".gitkeep":
            continue
        fm = parse_frontmatter(md_file)
        if not fm or "category" not in fm:
            continue

        top_cat = fm["category"].split("/")[0]
        if top_cat not in groups:
            groups[top_cat] = []

        tags = fm.get("tags", [])
        tag_str = " ".join(f"`{t}`" for t in tags[:3])  # show max 3 tags
        rel_path = md_file.relative_to(REPO_ROOT)

        groups[top_cat].append(
            {
                "name": fm.get("name", md_file.stem),
                "description": fm.get("description", ""),
                "tags": tag_str,
                "path": str(rel_path).replace("\\", "/"),
            }
        )

    return groups


def build_table(skills: list[dict]) -> str:
    if not skills:
        return "_No skills yet — [contribute one!](CONTRIBUTING.md)_\n"
    lines = [
        "| Skill | Description | Tags |",
        "|---|---|---|",
    ]
    for s in skills:
        lines.append(f"| [{s['name']}]({s['path']}) | {s['description']} | {s['tags']} |")
    return "\n".join(lines) + "\n"


def update_readme(groups: dict[str, list[dict]]) -> None:
    content = README.read_text(encoding="utf-8")

    for cat, skills in groups.items():
        start_marker = f"<!-- SKILLS:{cat}:START -->"
        end_marker = f"<!-- SKILLS:{cat}:END -->"
        table = build_table(skills)
        replacement = f"{start_marker}\n{table}{end_marker}"

        pattern = re.escape(start_marker) + r".*?" + re.escape(end_marker)
        if re.search(pattern, content, flags=re.DOTALL):
            content = re.sub(pattern, replacement, content, flags=re.DOTALL)
        else:
            print(f"  Warning: markers not found for category '{cat}' — skipping.")

    README.write_text(content, encoding="utf-8")
    print("README.md updated.")


def main() -> None:
    print("Scanning skill files…")
    groups = collect_skills()
    total = sum(len(v) for v in groups.values())
    print(f"Found {total} skills across {len(groups)} categories.")
    update_readme(groups)


if __name__ == "__main__":
    main()
