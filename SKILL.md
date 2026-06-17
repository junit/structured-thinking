---
name: structured-thinking
description: "Use when organizing complex information for an audience: writing incident reports, postmortems, executive summaries, design documents, proposals, or presentation outlines. Triggered when there is a risk of presenting unstructured, raw, or chronological logs and details to executives, stakeholders, or teams."
---

# Structured Thinking

## Overview
Structured thinking is a communication method that organizes scattered information into a high-impact, audience-focused structure. It ensures recommendations are delivered first, supporting details are logically grouped, and actions are clear.

## When to Use

### Symptoms / Triggers
- You are about to present raw chronological lists of events or raw server logs to a stakeholder.
- You are drafting a postmortem, report, design document, proposal, or presentation outline.
- The audience needs to make a decision, approve a plan, or understand a root cause quickly.
- You feel tempted to write a "wall of text" or tell a narrative story instead of showing structure.

### When NOT to Use
- Live debugging sessions where you are actively running terminal commands to fix errors (use debugging skills instead).
- Writing raw source code files or configuration changes.

## Core Pattern

### Before (Chronological Storytelling)
> We deployed a change at 13:55. At 14:00, checkouts started failing. The database connection pool was exhausted. The DBA restarted the DB at 14:15 but it didn't help. At 14:30 we correlated the deploy. At 14:45 we found the connection leak bug. At 15:00 we rolled back. At 15:30 it recovered.

### After (Structured & Audience-Focused)
> **Summary**: The checkout service was restored at 15:30 by reverting a connection leak bug introduced in a rollback deploy at 13:55 (total downtime: 2 hours, impact: $200k loss). We are implementing ESLint rules to prevent future leaks.
>
> **Timeline**:
> 1. **Rollback Deploy** (13:55) - Bug introduced (missing `finally` block).
> 2. **DB Restart** (14:15) - Temporary fix attempted; connections immediately re-exhausted.
> 3. **Code Reverted** (15:00-15:30) - Full service recovery.

## Quick Reference

| Step | Objective | Key Framework | Reference File |
| :--- | :--- | :--- | :--- |
| **1. Describe Problem** | Find root cause, not blame | 5W2H + 5-Why + Cynefin | [step-1-5w2h.md](file:///Users/wifibaby4u/LLM/structured-thinking/references/step-1-5w2h.md) |
| **2. Goal & Audience** | Define target behavior | A→B + SCQA + STAR + SMART + Pre-Mortem + Golden Circle | [step-2-scqa.md](file:///Users/wifibaby4u/LLM/structured-thinking/references/step-2-scqa.md) |
| **3. Vertical Structure** | State conclusion first | Pyramid Principle + First Principles + Occam's Razor | [step-3-pyramid.md](file:///Users/wifibaby4u/LLM/structured-thinking/references/step-3-pyramid.md) |
| **4. Horizontal Structure**| Logical categorization | MECE + MoSCoW + DDD + Pareto + Rule of 3 | [step-4-mece.md](file:///Users/wifibaby4u/LLM/structured-thinking/references/step-4-mece.md) |
| **5. Visualization** | Speed up comprehension | Diagrams/Tables + KT Matrix | [step-5-visualize.md](file:///Users/wifibaby4u/LLM/structured-thinking/references/step-5-visualize.md) |
| **Agent Workflow** | Pre-compute and layout | Response Template | [agent-workflow.md](file:///Users/wifibaby4u/LLM/structured-thinking/references/agent-workflow.md) |

## Red Flags — STOP and Rethink
- Emitting raw timelines or raw server logs without a top-level summary.
- Saying: "First, let's look at the history of the issue..."
- Mixing chronological order and priority order in a single list.
- Writing paragraphs that do not directly help the Actor take the target Behavior.

## Rationalization Table

| Excuse | Reality |
| :--- | :--- |
| "The user requested a raw list / timeline, so I should just give them that." | Give them the timeline, but always prefix it with a 1-2 sentence core conclusion/impact summary first. |
| "I'm in a rush / exhausted, I don't have time to pre-compute SCQA or Pyramid." | Pre-computing takes 30 seconds in thoughts and saves paragraphs of writing and correction. |
| "The problem is too simple for structured thinking." | Simple problems benefit the most from a single, clear recommendation upfront. |
