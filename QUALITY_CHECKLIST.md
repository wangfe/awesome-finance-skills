# Skill Quality Checklist

Every skill must pass this checklist before being merged. PR reviewers will verify each item.

---

## Metadata

- [ ] `name` is human-readable and descriptive.
- [ ] `description` is a single clear sentence (no jargon without explanation).
- [ ] `category` matches the taxonomy in `PRD.md` exactly.
- [ ] At least 2 relevant `tags` are provided.
- [ ] `source` URL is present if the skill was sourced from elsewhere.
- [ ] `license` is documented and is OSI-approved or Creative Commons (MIT, Apache-2.0, CC0, CC-BY).
- [ ] `claude_version` is specified.
- [ ] `date_added` is a valid ISO date (YYYY-MM-DD).

## Content

- [ ] The skill file contains all required sections: Description, Usage, Example, Skill Prompt.
- [ ] The financial disclaimer is included in the Description section.
- [ ] The skill prompt is clear, complete, and produces useful output.
- [ ] The example shows a realistic input and a representative (abbreviated) output.
- [ ] No PII, hardcoded credentials, API keys, or personal data.
- [ ] No offensive, discriminatory, or harmful content.
- [ ] No instructions that could facilitate financial fraud or illegal activity.

## Accuracy & Safety

- [ ] The skill does not present AI output as certified financial advice.
- [ ] Live market data (prices, rates) is expected to be supplied by the user, not assumed by the skill.
- [ ] Any required external data sources (free or paid) are documented in Notes.
- [ ] Known limitations and edge cases are noted.

## Placement

- [ ] File is placed in the correct `skills/<category>/<subcategory>/` folder.
- [ ] Filename is lowercase, hyphenated, no spaces (e.g., `dcf-model.md`).
- [ ] A corresponding row has been added to the README index table.

## Functional Test

- [ ] The skill has been manually tested with Claude and produces correct, useful output.
- [ ] If the skill references specific formulas or standards (e.g., GAAP ratios), the math/logic has been verified.

---

*Skills that do not meet all checklist items will have changes requested before merging.*
