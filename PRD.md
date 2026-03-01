# PRD: Awesome Finance Skills Collection

**Version:** 1.1
**Date:** 2026-02-28
**Status:** Active

---

## Changelog

| Version | Date | Summary |
|---|---|---|
| 1.0 | 2026-02-25 | Initial draft — taxonomy, file standard, milestone plan |
| 1.1 | 2026-02-28 | Added `real-estate-investment` category; daily auto-generation live; Phase 1 complete; Phase 2 in progress |

---

## 1. Overview

### 1.1 Product Vision

An open, community-curated repository of Claude Code skills focused on finance — a single place where anyone can discover, download, and contribute finance-related skills covering personal finance, investing, real estate, accounting, financial modeling, trading, and more.

Think of it as the **"awesome-lists" meets Claude Code skills** for the finance domain.

### 1.2 Problem Statement

Finance-related tasks (budgeting, DCF modeling, portfolio analysis, tax prep, options pricing, etc.) are among the most common use cases people want AI assistance for. However:

- Finance skills are scattered across the web with no central discovery point.
- Quality varies widely; users waste time evaluating broken or outdated skills.
- No consistent categorization makes browsing and finding relevant skills hard.
- Contributors have nowhere to submit high-quality, domain-specific finance skills.

### 1.3 Goals

1. Aggregate and organize the best openly available finance skills for Claude Code.
2. Provide a clear taxonomy so users can quickly find what they need.
3. Establish contribution guidelines and quality standards.
4. Make the collection self-serve — no sign-up, no paywalls.
5. Automate daily skill generation to grow the collection continuously.

---

## 2. Target Users

| User Type | Description | Primary Need |
|---|---|---|
| **Individual Investors** | Retail investors managing personal portfolios | Portfolio tracking, stock analysis, options tools |
| **Personal Finance Users** | People managing budgets, debt, savings | Budget templates, debt payoff calculators, FIRE tools |
| **Real Estate Investors** | Landlords, house hackers, BRRRR investors | Cash flow analysis, deal scoring, cap rate/ROI calculators |
| **Finance Professionals** | Analysts, bankers, accountants, advisors | DCF models, financial statement analysis, reporting |
| **Developers / Builders** | Building fintech apps or automations | API integrations, data pipelines, calculation utilities |
| **Students / Learners** | Finance students, self-learners | Educational skills, concept explainers, practice tools |

---

## 3. Scope

### 3.1 In Scope

- Curating and hosting finance-related Claude Code skills (`.md` prompt files).
- Organizing skills into a clear category hierarchy.
- Providing a browsable `README.md` as the primary discovery interface.
- Contributor guidelines (`CONTRIBUTING.md`) and skill submission process.
- A quality review checklist for all submitted skills.
- Metadata standard (frontmatter) for each skill file.
- Automated daily skill generation via GitHub Actions + Claude API.

### 3.2 Out of Scope (v1)

- A web UI or dedicated website (README-based discovery is sufficient for v1).
- Automated frontmatter validation CI pipeline (planned for Phase 3).
- Monetization or premium tiers.
- Skills for non-finance domains.

---

## 4. Category Taxonomy

Skills are organized into 9 top-level categories, each with sub-categories.

```
skills/
├── personal-finance/
│   ├── budgeting/
│   ├── debt-management/
│   ├── savings-goals/
│   ├── fire-planning/          # Financial Independence / Retire Early
│   └── tax-personal/
│
├── investing/
│   ├── stock-analysis/
│   ├── etf-funds/
│   ├── options-derivatives/
│   ├── crypto/
│   ├── real-estate/            # kept for legacy; primary RE skills in real-estate-investment/
│   ├── portfolio-analysis/
│   └── portfolio-management/
│
├── real-estate-investment/     # NEW in v1.1 — dedicated top-level category
│   ├── market-analysis/        # news digests, price trends, market conditions
│   ├── property-analysis/      # deal analyzers, investment opportunity screeners
│   ├── roi-calculation/        # cap rate, cash-on-cash, GRM, total ROI
│   ├── rental-analysis/        # cash flow, NOI, break-even, 5-year projections
│   └── financing/              # mortgage calculators, amortization, DSCR
│
├── financial-modeling/
│   ├── dcf-valuation/
│   ├── lbo-analysis/
│   ├── comparable-analysis/
│   ├── scenario-modeling/
│   └── forecasting/
│
├── accounting/
│   ├── bookkeeping/
│   ├── financial-statements/
│   ├── ratio-analysis/
│   └── tax-business/
│
├── trading/
│   ├── technical-analysis/
│   ├── quantitative/
│   ├── risk-management/
│   └── backtesting/
│
├── data-and-research/
│   ├── market-data/
│   ├── earnings-analysis/
│   ├── economic-indicators/
│   └── sec-filings/
│
├── news-and-reporting/
│   ├── daily-digest/
│   ├── market-analysis/
│   ├── macro-events/
│   └── sector-news/
│
└── tools-and-utilities/
    ├── calculators/
    ├── converters/
    ├── report-generators/
    └── api-integrations/
```

---

## 5. Skill File Standard

Each skill must follow this structure:

### 5.1 File Naming

```
skills/<category>/<subcategory>/<skill-name>.md
```

Example: `skills/investing/stock-analysis/buffett-checklist.md`

For agent-style skills with supporting files, a directory layout is also supported:

```
skills/<category>/<subcategory>/<skill-name>/SKILL.md
skills/<category>/<subcategory>/<skill-name>/references/
```

### 5.2 Required Frontmatter

```yaml
---
name: Buffett-Style Stock Checklist
description: Evaluate a stock using Warren Buffett's fundamental investing criteria
category: investing/stock-analysis
tags: [fundamental-analysis, value-investing, checklist]
author: community
source: https://example.com/original-skill   # URL if sourced from the web
license: MIT                                  # or CC0, Apache-2.0, etc.
claude_version: ">=claude-sonnet-4-6"
date_added: 2026-02-25
---
```

All fields except `source` are required. The `update_readme.py` script parses this frontmatter to auto-generate the README skill index.

### 5.3 Skill Body Sections

```markdown
## Description
[What this skill does — 1–3 sentences]

## Usage
[How to invoke the skill and what input it expects]

## Example
[A sample prompt and expected output]

## Skill Prompt
[The actual Claude Code skill content]

## Notes
[Optional caveats, limitations, data sources required]
```

---

## 6. Repository Structure

```
awesome-finance-skills/
├── README.md                  # Main index — auto-generated skill tables by category
├── PRD.md                     # This document
├── CONTRIBUTING.md            # How to add or improve skills
├── QUALITY_CHECKLIST.md       # Standards every skill must meet before merging
├── LICENSE                    # Repository license (MIT)
│
├── skills/                    # All skill files (organized by taxonomy above)
│   ├── personal-finance/
│   ├── investing/
│   ├── real-estate-investment/
│   ├── financial-modeling/
│   ├── accounting/
│   ├── trading/
│   ├── data-and-research/
│   ├── news-and-reporting/
│   └── tools-and-utilities/
│
├── scripts/
│   ├── generate_skill.py      # Calls Claude API to generate the next skill from the queue
│   ├── update_readme.py       # Scans all skill frontmatter and regenerates README tables
│   └── skill_queue.yaml       # Ordered queue of pending skill topics + completed log
│
└── .github/
    └── workflows/
        └── daily-skill-update.yml   # Runs generate_skill.py + update_readme.py daily at 9 AM UTC
```

---

## 7. README Design (Discovery Interface)

The `README.md` is the primary UX. It includes:

1. **Hero section** — project name, one-line description, badges (skills count, PRs welcome, license).
2. **Quick-start** — how to use any skill in 3 steps.
3. **How to Use Skills** — three methods: install as Claude Code skill, copy-paste, use via API.
4. **Category index** — one section per category with auto-generated skills table.
5. **Contributing CTA** — how to add a skill.
6. **Acknowledgements** — credits for sourced skills (e.g., AlphaEar suite from RKiding).
7. **License and credits**.

Skill tables are auto-generated by `scripts/update_readme.py` between HTML comment markers:
```html
<!-- SKILLS:{category}:START -->
...auto-generated table...
<!-- SKILLS:{category}:END -->
```

The skill count badge is also auto-updated on each run.

---

## 8. Automated Skill Generation

### 8.1 Daily GitHub Actions Workflow

A scheduled workflow (`.github/workflows/daily-skill-update.yml`) runs every day at 9:00 AM UTC:

1. Reads the first pending entry from `scripts/skill_queue.yaml`
2. Calls `claude-sonnet-4-6` via the Anthropic API with a structured system prompt
3. Saves the generated `.md` file to the correct `skills/` directory
4. Moves the topic from `pending` to `completed` in the queue
5. Runs `update_readme.py` to refresh the README index and badge
6. Commits and pushes as `github-actions[bot]`

The workflow can also be triggered manually via `workflow_dispatch` from the GitHub UI.

### 8.2 Skill Queue

`scripts/skill_queue.yaml` maintains two lists:
- `pending` — ordered list of topics to generate next (50+ topics queued)
- `completed` — log of generated skills with file path and date

To add topics to the queue, append entries to the `pending` list in this format:
```yaml
- topic: Topic Name
  category: category/subcategory
  tags: [tag1, tag2, tag3]
```

---

## 9. Contribution Workflow

### 9.1 Sourcing Skills from the Web

1. Find a finance skill, prompt, or template published on the open web.
2. Verify the source license permits redistribution (MIT, CC0, CC-BY, public domain).
3. Fork the repo and create a branch: `add/<skill-name>`.
4. Place the `.md` file in the correct category folder with proper frontmatter.
5. Submit a PR — fill in the PR template confirming license and quality checklist.

The README index is auto-regenerated by the daily workflow; contributors do not need to edit README manually.

### 9.2 Quality Checklist (gate for merging)

- [ ] Frontmatter is complete and valid (all required fields present).
- [ ] Skill produces correct, useful output when tested.
- [ ] Source URL and license are documented.
- [ ] Placed in the correct category.
- [ ] No PII, hardcoded secrets, or offensive content.
- [ ] Description is clear to a non-expert.

---

## 10. Milestones

### Phase 1 — Foundation ✅ Complete
- [x] Finalize taxonomy and file standard.
- [x] Create repo scaffolding (folders, README shell, CONTRIBUTING.md, LICENSE).
- [x] Source and add seed skills across all major categories (27 skills at launch).
- [x] Publish initial README index with auto-generated tables.
- [x] Integrate AlphaEar agent skill suite (9 skills from RKiding/Awesome-finance-skills).

### Phase 2 — Content Growth 🔄 In Progress
- [x] Implement daily automated skill generation (GitHub Actions + Claude API).
- [x] Add `real-estate-investment` as a dedicated top-level category (5 skills).
- [x] Queue 50+ skill topics across all categories.
- [ ] Reach 50 skills in the repository.
- [ ] Invite early contributors; process first external PRs.

### Phase 3 — Community & Discovery
- [ ] Promote on finance and AI communities (Reddit, HN, Twitter/X, Discord).
- [ ] Reach 100+ skills and 500+ GitHub stars.
- [ ] Add `scripts/validate.py` to enforce frontmatter schema on PRs via CI.
- [ ] Evaluate need for a static site (GitHub Pages) for richer browsing.
- [ ] Add a "featured skills" section to README highlighting the best picks.

---

## 11. Success Metrics

| Metric | Phase 1 Target | Current (v1.1) | Phase 3 Target |
|---|---|---|---|
| Total skills in repo | 10 | **30** | 100+ |
| Top-level categories covered | 5/7 | **9/9** | 9/9 |
| GitHub stars | — | — | 500+ |
| External contributors | 0 | 1 (RKiding) | 20+ |
| README index completeness | 100% | **100%** | 100% |
| Daily auto-generation | — | **Live** | Live |

---

## 12. Open Questions

| # | Question | Status |
|---|---|---|
| 1 | **License strategy** — MIT for repo; require OSI/CC license for contributions? | ✅ Resolved — MIT repo, MIT per-skill default |
| 2 | **Skill format** — `.md` with YAML frontmatter only, or also standalone `.yaml`? | ✅ Resolved — `.md` with frontmatter; directory layout (`SKILL.md`) also supported |
| 3 | **Automated validation** — GitHub Actions to enforce frontmatter schema on PRs? | 🔄 Planned for Phase 3 (`scripts/validate.py`) |
| 4 | **Language scope** — English-only for v1, or welcome multilingual skill files? | 🔄 Open — English default; Chinese-market skills (AlphaEar) are in English with Chinese data sources |
| 5 | **Skill versioning** — changelog section in the file when a skill is updated? | 🔄 Open |

---

## 13. Non-Goals and Anti-Patterns

- **Not financial advice.** All skills must include a disclaimer that outputs are for informational/educational purposes only.
- **No proprietary data.** Skills must not require access to paid data sources without clearly documenting it.
- **No hallucination-prone skills without grounding.** Skills asking Claude to recall specific live prices or current news should always instruct the user to supply the data.

---

*End of PRD v1.1*
