# Contributing to Awesome Finance Skills

Thank you for helping grow this collection. Every skill you add helps someone manage money, make better investment decisions, or understand their finances more clearly.

---

## Ways to Contribute

- **Add a new skill** — source a skill from the open web or write one yourself.
- **Improve an existing skill** — fix bugs, clarify prompts, update outdated content.
- **Fix metadata** — correct frontmatter, add missing tags, update source URLs.
- **Report issues** — open a GitHub Issue for broken, misleading, or low-quality skills.

---

## Before You Start

1. **Search first.** Make sure the skill doesn't already exist in the repo.
2. **Check the license.** If sourcing from the web, confirm the original license permits redistribution (MIT, CC0, CC-BY, Apache-2.0, or explicit public domain). Document the source URL in the frontmatter.
3. **Check the quality checklist.** Your PR will not be merged unless all items in `QUALITY_CHECKLIST.md` are satisfied.

---

## Adding a New Skill

### Step 1 — Fork and branch

```bash
git checkout -b add/<skill-name>
# e.g. add/buffett-stock-checklist
```

### Step 2 — Create the skill file

Place your `.md` file in the correct category folder:

```
skills/<category>/<subcategory>/<skill-name>.md
```

Use hyphens, lowercase, no spaces in filenames.

**Example path:**
```
skills/investing/stock-analysis/buffett-checklist.md
```

### Step 3 — Follow the skill file format

Every skill file must have this structure:

```markdown
---
name: Human-readable skill name
description: One sentence describing what this skill does
category: investing/stock-analysis
tags: [tag1, tag2, tag3]
author: your-github-username (or "community")
source: https://original-url.com   # omit if you wrote it yourself
license: MIT
claude_version: ">=claude-sonnet-4-6"
date_added: YYYY-MM-DD
---

## Description

[2–4 sentences explaining what the skill does, who it's for, and what it produces.]

> **Disclaimer:** This skill is for informational and educational purposes only.
> It does not constitute financial advice. Always consult a qualified financial
> professional before making investment or financial decisions.

## Usage

[Explain how to invoke the skill. What inputs does the user provide? What format?]

## Example

**Input:**
[Sample user prompt]

**Output:**
[Representative output — can be abbreviated]

## Skill Prompt

[The actual Claude Code skill prompt content goes here.]

## Notes

[Optional: data requirements, known limitations, caveats, related skills.]
```

### Step 4 — Add to the README index

Find the right category table in `README.md` and add a row:

```markdown
| [Skill Name](skills/category/subcategory/skill-name.md) | Short description | `tag1` `tag2` |
```

### Step 5 — Submit a Pull Request

Use the PR template. Fill every section. Link to the source URL if applicable.

---

## Updating an Existing Skill

- Keep the original `source` URL in frontmatter.
- Update `date_added` to today's date only if you are making substantive changes.
- Add a `## Changelog` section at the bottom of the file if making breaking changes.

---

## Skill Categories

See `PRD.md` for the full taxonomy. If your skill doesn't fit an existing category, propose a new subcategory in your PR and explain why.

---

## Code of Conduct

- Be respectful in PR reviews and issues.
- No financial advice presented as fact.
- No skills that exploit, deceive, or harm users financially.
- No skills requiring proprietary paid data without clear documentation.

---

## Questions?

Open a GitHub Issue with the `question` label.
