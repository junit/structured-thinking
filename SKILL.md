---
name: structured-thinking
description: "Use when the user must organize information for an audience — writing reports, preparing presentations, designing docs, drafting executive summaries, or planning meetings. Applies 5W2H, 5-Why, MECE, pyramid principle, and SCQA. Also use when analyzing root causes for a written report or postmortem (not for live debugging — use debugging skills instead), or comparing options in a decision document."
---

# Structured Thinking

## When to use this skill

Use whenever the user must organize information for an audience or analyze a problem: writing reports, preparing presentations, designing docs, drafting executive summaries, planning meetings, or comparing options.

## Overview

Structured thinking transforms scattered thoughts into audience-focused structure via five steps:

1. **Describe the problem** (5W2H + 5-Why) — gather context and root cause
2. **Define goal and audience** (A→B rule + SCQA) — tailor to elicit behavior
3. **Structure vertically** (Pyramid principle) — conclusion first, then support
4. **Organize horizontally** (MECE + ordering) — non-overlapping, exhaustive
5. **Visualize relationships** — diagrams where prose is slower

## Workflow

For each step, **Read the matching reference file** before executing — detailed tables, examples, and anti-patterns live there, not here.

### Step 1 — Describe the problem
Use 5W2H (What/When/Where/Why/Who/How/How much) to gather context, then 5-Why to drill to the root cause.
→ **Reference**: `references/step-1-5w2h.md`

### Step 2 — Define goal and audience
Identify the Actor and the Behavior you want from them (A→B). Open with SCQA (Scenario, Complication, Question, Answer) — reorder as ASCQ/QSCA/CSQA to emphasize solution/problem/conflict.
→ **Reference**: `references/step-2-scqa.md`

### Step 3 — Structure vertically (Pyramid)
State the main conclusion first. Under it, group supporting conclusions, each with its own center of gravity. Below those, evidence.
→ **Reference**: `references/step-3-pyramid.md`

### Step 4 — Organize horizontally (MECE)
At every level, categories must be Mutually Exclusive and Collectively Exhaustive. Pick one ordering principle per branch (structure, time, or importance) — never mix.
→ **Reference**: `references/step-4-mece.md`

### Step 5 — Visualize relationships
Match diagram type to relationship: pie for parts-of-whole, flowchart for process, cycle for loops, tree for hierarchy, table for comparison. Use Mermaid inline where possible.
→ **Reference**: `references/step-5-visualize.md`

## How to apply as an Agent

Two-phase process: (1) pre-compute in your `thought` block (A→B target, SCQA hook, pyramid outline, MECE check), then (2) emit the response template (core summary → context → detailed structure → optional visual).
→ **Reference**: `references/agent-workflow.md`

## Rules

- **Conclusion first**: never bury the recommendation in background
- **One ordering per branch**: do not mix chronological and importance ordering
- **Tailor to the Behavior**: omit details that don't elicit the Actor's target behavior
- **Read references on demand**: this SKILL.md is an index; depth lives in `references/`

## Limitations

This skill provides structured thinking guidance but does not replace subject-matter expertise. It does not auto-generate diagrams — use Mermaid blocks or external tools when needed.
