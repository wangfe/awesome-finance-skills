---
name: AlphaEar Reporter
description: Plan, write, and assemble professional financial reports by clustering signals into themes, writing analysis sections, and compiling a final structured report
category: tools-and-utilities/report-generators
tags: [report-generation, financial-reports, signal-clustering]
---

# AlphaEar Reporter Skill

## Overview

This skill provides a structured workflow for generating professional financial reports. It includes planning, writing, editing, and creating visual aids (charts).

## Capabilities

### 1. Generate Structured Reports (Agentic Workflow)

**YOU (the Agent)** are the Report Generator. Use the prompts in `references/PROMPTS.md` to progressively build the report.

**Workflow:**
1.  **Cluster Signals**: Read input signals and use the **Cluster Signals Prompt** to group them.
2.  **Write Sections**: For each cluster, use the **Write Section Prompt** to generate analysis.
3.  **Assemble**: Use the **Final Assembly Prompt** to compile the report.

### 2. Visualization Tools

Use `scripts/visualizer.py` to generate chart configurations if needed manually, though the Writer Prompt usually handles this via `json-chart` blocks.

## Dependencies

-   `sqlite3` (built-in)
