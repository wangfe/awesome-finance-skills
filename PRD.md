# PRD: Awesome Finance Skills Collection

**Version:** 1.0
**Date:** 2026-02-25
**Status:** Draft

---

## 1. Overview

### 1.1 Product Vision

An open, community-curated repository of Claude Code skills focused on finance — a single place where anyone can discover, download, and contribute finance-related skills covering personal finance, investing, accounting, financial modeling, trading, and more.

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

---

## 2. Target Users

| User Type | Description | Primary Need |
|---|---|---|
| **Individual Investors** | Retail investors managing personal portfolios | Portfolio tracking, stock analysis, options tools |
| **Personal Finance Users** | People managing budgets, debt, savings | Budget templates, debt payoff calculators, FIRE tools |
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

### 3.2 Out of Scope (v1)

- A web UI or dedicated website (README-based discovery is sufficient for v1).
- Automated skill testing or CI validation pipeline (future).
- Monetization or premium tiers.
- Skills for non-finance domains.

---

## 4. Category Taxonomy

Skills are organized into top-level categories, each with sub-categories.

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
│   ├── real-estate/
│   └── portfolio-management/
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
SkillsFinance/
├── README.md                  # Main index — browsable list of all skills by category
├── PRD.md                     # This document
├── CONTRIBUTING.md            # How to add or improve skills
├── QUALITY_CHECKLIST.md       # Standards every skill must meet before merging
├── LICENSE                    # Repository license (MIT)
│
├── skills/                    # All skill files (organized by taxonomy above)
│   ├── personal-finance/
│   ├── investing/
│   ├── financial-modeling/
│   ├── accounting/
│   ├── trading/
│   ├── data-and-research/
│   └── tools-and-utilities/
│
└── scripts/                   # (Future) tooling to validate metadata, generate index
```

---

## 7. README Design (Discovery Interface)

The `README.md` is the primary UX. It should include:

1. **Hero section** — project name, one-line description, badges (stars, PRs welcome, license).
2. **Quick-start** — how to use any skill in 3 steps.
3. **Category index** — linked table of contents to each category.
4. **Skills table per category** — name, description, tags, source link.
5. **Contributing CTA** — how to add a skill.
6. **License and credits**.

---

## 8. Contribution Workflow

### 8.1 Sourcing Skills from the Web

1. Find a finance skill, prompt, or template published on the open web.
2. Verify the source license permits redistribution (MIT, CC0, CC-BY, public domain).
3. Fork the repo and create a branch: `add/<skill-name>`.
4. Place the `.md` file in the correct category folder with proper frontmatter.
5. Add it to the README index table.
6. Submit a PR — fill in the PR template confirming license and quality checklist.

### 8.2 Quality Checklist (gate for merging)

- [ ] Frontmatter is complete and valid.
- [ ] Skill produces correct, useful output when tested.
- [ ] Source URL and license are documented.
- [ ] Placed in the correct category.
- [ ] README index entry is added.
- [ ] No PII, hardcoded secrets, or offensive content.
- [ ] Description is clear to a non-expert.

---

## 9. Milestones

### Phase 1 — Foundation (Week 1–2)
- [ ] Finalize taxonomy and file standard.
- [ ] Create repo scaffolding (folders, README shell, CONTRIBUTING.md, LICENSE).
- [ ] Source and add 5–10 seed skills across major categories.
- [ ] Publish initial README index.

### Phase 2 — Content Growth (Week 3–6)
- [ ] Source and add 30+ skills covering all top-level categories.
- [ ] Invite early contributors; process first external PRs.
- [ ] Add QUALITY_CHECKLIST.md and PR template.

### Phase 3 — Community & Discovery (Week 7+)
- [ ] Promote on finance and AI communities (Reddit, HN, Twitter/X, Discord).
- [ ] Add skill count badges and "featured" skills section to README.
- [ ] Evaluate need for a static site (GitHub Pages) for richer browsing.
- [ ] Implement a `scripts/validate.py` to check frontmatter on all PRs.

---

## 10. Success Metrics

| Metric | Phase 1 Target | Phase 3 Target |
|---|---|---|
| Total skills in repo | 10 | 100+ |
| GitHub stars | — | 500+ |
| External contributors | 0 | 20+ |
| Categories covered | 5/7 | 7/7 |
| README index completeness | 100% | 100% |

---

## 11. Open Questions

1. **License strategy** — should the repo itself use MIT, and require all contributed skills to carry an OSI-approved or Creative Commons license?
2. **Skill format** — should we support `.yaml` frontmatter in `.md` only, or also allow standalone `.yaml` skill definition files?
3. **Automated validation** — do we want a GitHub Actions workflow from day one to enforce frontmatter schema on PRs?
4. **Language scope** — English-only for v1, or welcome multilingual skill files?
5. **Skill versioning** — when a skill is updated, should we keep a changelog section in the file itself?

---

## 12. Non-Goals and Anti-Patterns

- **Not financial advice.** All skills must include a disclaimer that outputs are for informational/educational purposes only.
- **No proprietary data.** Skills must not require access to paid data sources without clearly documenting it.
- **No hallucination-prone skills without grounding.** Skills asking Claude to recall specific live prices or current news should always instruct the user to supply the data.

---

*End of PRD v1.0*
