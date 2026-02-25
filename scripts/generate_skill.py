#!/usr/bin/env python3
"""Generate a new finance skill using the Anthropic API.

Reads the next pending topic from scripts/skill_queue.yaml,
calls Claude to generate a complete skill file, saves it,
and marks the topic as completed in the queue.
"""

import os
import re
import sys
import yaml
from pathlib import Path
from datetime import date

import anthropic

REPO_ROOT = Path(__file__).parent.parent
QUEUE_FILE = Path(__file__).parent / "skill_queue.yaml"

SYSTEM_PROMPT = """\
You are an expert finance writer creating Claude Code skill files for an open-source \
repository called "Awesome Finance Skills".

Each skill file you produce must follow this EXACT format — output ONLY the raw file \
content with no surrounding text, no code fences, no preamble:

---
name: [Human-readable skill name]
description: [One clear sentence describing what this skill does]
category: [category/subcategory — exactly as given]
tags: [tag1, tag2, tag3]
author: community
source:
license: MIT
claude_version: ">=claude-sonnet-4-6"
date_added: [YYYY-MM-DD as given]
---

## Description

[2–4 sentences: what the skill does, who it's for, and what it produces.]

> **Disclaimer:** This skill is for informational and educational purposes only.
> It does not constitute financial advice. Always consult a qualified financial
> professional before making investment or financial decisions.

## Usage

[How to invoke the skill. What inputs does the user provide? What format?]

## Example

**Input:**
[A realistic sample user prompt]

**Output:**
[Representative output — include key sections; abbreviate where necessary]

## Skill Prompt

```
[The actual Claude Code skill prompt — detailed, specific instructions with formulas, \
frameworks, or methodologies. This is what Claude will follow when the skill is invoked.]
```

## Notes

[Data requirements, known limitations, caveats, and related skills in the repo.]
"""


def load_queue() -> dict:
    with open(QUEUE_FILE) as f:
        return yaml.safe_load(f)


def save_queue(data: dict) -> None:
    with open(QUEUE_FILE, "w") as f:
        yaml.dump(data, f, default_flow_style=False, allow_unicode=True, sort_keys=False)


def slugify(text: str) -> str:
    text = text.lower()
    text = re.sub(r"[^a-z0-9\s-]", "", text)
    text = re.sub(r"[\s-]+", "-", text.strip())
    return text


def strip_code_fences(content: str) -> str:
    """Remove any accidental markdown code-fence wrappers around the output."""
    content = content.strip()
    # If Claude wrapped the whole thing in ```markdown ... ```
    if content.startswith("```"):
        content = re.sub(r"^```[a-z]*\n?", "", content)
        content = re.sub(r"\n?```$", "", content)
    return content.strip()


def generate_skill(topic: str, category: str, tags: list, today: str) -> str:
    client = anthropic.Anthropic()
    user_prompt = (
        f"Create a complete finance skill file for the following topic:\n\n"
        f"Topic: {topic}\n"
        f"Category: {category}\n"
        f"Tags: {tags}\n"
        f"Date: {today}\n\n"
        f"Output ONLY the raw file content starting with the YAML frontmatter (---). "
        f"No preamble, no code fences wrapping the entire output, no trailing commentary."
    )

    message = client.messages.create(
        model="claude-sonnet-4-6",
        max_tokens=4096,
        system=SYSTEM_PROMPT,
        messages=[{"role": "user", "content": user_prompt}],
    )
    return strip_code_fences(message.content[0].text)


def save_skill(content: str, category: str, topic: str) -> Path:
    parts = category.split("/")
    subdir = REPO_ROOT / "skills" / Path(*parts)
    subdir.mkdir(parents=True, exist_ok=True)
    filepath = subdir / (slugify(topic) + ".md")
    filepath.write_text(content, encoding="utf-8")
    return filepath


def set_output(name: str, value: str) -> None:
    """Write a GitHub Actions output variable."""
    github_output = os.environ.get("GITHUB_OUTPUT")
    if github_output:
        with open(github_output, "a") as f:
            f.write(f"{name}={value}\n")
    else:
        # Fallback for local runs
        print(f"OUTPUT: {name}={value}")


def main() -> None:
    queue = load_queue()
    pending = queue.get("pending", [])

    if not pending:
        print("No pending topics in queue. Nothing to do.")
        set_output("skill_topic", "")
        set_output("skill_file", "")
        sys.exit(0)

    item = pending[0]
    topic = item["topic"]
    category = item["category"]
    tags = item.get("tags", [])
    today = date.today().isoformat()

    print(f"Generating skill: {topic!r} → {category}")
    content = generate_skill(topic, category, tags, today)

    filepath = save_skill(content, category, topic)
    rel_path = str(filepath.relative_to(REPO_ROOT))
    print(f"Saved: {rel_path}")

    # Update queue
    queue["pending"] = pending[1:]
    completed = queue.setdefault("completed", [])
    completed.append({"topic": topic, "file": rel_path, "date": today})
    save_queue(queue)
    print(f"{len(queue['pending'])} topics remaining in queue.")

    set_output("skill_topic", topic)
    set_output("skill_file", rel_path)


if __name__ == "__main__":
    main()
