# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## What This Repo Is

An open, community-curated collection of Claude Code finance skills — prompt files (`.md`) organized into a taxonomy of finance categories. Skills can be installed as Claude Code slash commands, copy-pasted into any Claude interface, or used as system prompts via the API.

The README skill index is **auto-generated** from skill frontmatter by `scripts/update_readme.py`. Never hand-edit the tables between `<!-- SKILLS:{category}:START -->` and `<!-- SKILLS:{category}:END -->`.

## Scripts

### Setup

```bash
pip install -r requirements.txt
# API key goes in .env.local:
echo "ANTHROPIC_API_KEY=sk-..." > .env.local
```

### Generate the next skill from the queue

```bash
python scripts/generate_skill.py
```

Reads `scripts/skill_queue.yaml`, calls `claude-sonnet-4-6` to produce the skill file, saves it to the correct `skills/` path, and moves the topic from `pending` to `completed` in the queue.

### Rebuild the README index

```bash
python scripts/update_readme.py
```

Scans all `skills/**/*.md` frontmatter and regenerates the category tables and skill-count badge in `README.md`.

### GitHub Actions (automated)

The workflow `.github/workflows/daily-skill-update.yml` runs both scripts daily at 9 AM UTC and commits the result. It can also be triggered manually via `workflow_dispatch`.

## Skill File Format

Every skill lives at `skills/<category>/<subcategory>/<skill-name>.md` (lowercase, hyphenated). For agent-style skills with supporting files, use a directory: `skills/<category>/<subcategory>/<skill-name>/SKILL.md`.

### Required frontmatter

```yaml
---
name: Human-readable skill name
description: One sentence describing what this skill does
category: category/subcategory   # must match the taxonomy exactly
tags: [tag1, tag2, tag3]
author: your-github-username
source: https://original-url     # omit if you wrote it yourself
license: MIT
claude_version: ">=claude-sonnet-4-6"
date_added: YYYY-MM-DD
---
```

`update_readme.py` parses this frontmatter to build the README tables — if frontmatter is missing or malformed, the skill will not appear in the index.

### Required body sections

```
## Description
## Usage
## Example
## Skill Prompt   ← the actual prompt Claude follows when the skill is invoked
## Notes          ← optional
```

The financial disclaimer must appear in the `## Description` section (see any existing skill for the exact wording).

## Category Taxonomy

Nine top-level categories under `skills/`:

```
personal-finance/       budgeting, debt-management, savings-goals, fire-planning, tax-personal
investing/              stock-analysis, etf-funds, options-derivatives, crypto, real-estate, portfolio-analysis, portfolio-management
real-estate-investment/ market-analysis, property-analysis, roi-calculation, rental-analysis, financing
financial-modeling/     dcf-valuation, lbo-analysis, comparable-analysis, scenario-modeling, forecasting
accounting/             bookkeeping, financial-statements, ratio-analysis, tax-business
trading/                technical-analysis, quantitative, risk-management, backtesting
data-and-research/      market-data, earnings-analysis, economic-indicators, sec-filings
news-and-reporting/     daily-digest, market-analysis, macro-events, sector-news
tools-and-utilities/    calculators, converters, report-generators, api-integrations
```

The authoritative taxonomy is in `PRD.md §4`.

## Skill Queue

`scripts/skill_queue.yaml` has two keys:
- `pending` — ordered list of topics to generate; processed one per day
- `completed` — log of generated skills with file path and date

To add a topic:
```yaml
- topic: Topic Name
  category: category/subcategory
  tags: [tag1, tag2]
```

## Contributing a New Skill

1. Branch: `add/<skill-name>`
2. Place the `.md` file in the correct `skills/` folder
3. Fill all required frontmatter fields and body sections
4. Run `python scripts/update_readme.py` to update the index
5. Verify against `QUALITY_CHECKLIST.md` before opening a PR

The PR template is at `.github/PULL_REQUEST_TEMPLATE.md`.
