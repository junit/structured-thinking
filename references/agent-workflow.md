# Applying the Skill as an Agent

When executing a task that requires structured thinking or presenting complex information to the user, follow this two-phase process.

## Phase 1: Pre-computation (Mental Draft)

Before generating the final response, outline your thoughts in your `thought` block:

- **A→B Target**: Who is the user (developer, manager, designer)? What decision or action should they make?
- **SCQA Hook**: What is the context (S), what went wrong (C), what is the core question (Q), and what is my answer (A)?
- **Pyramid Outline**: Map out the top-level conclusion and the supporting arguments.
- **MECE Check**: Are the categories distinct and complete? Are they ordered logically (chronologically, structurally, or by importance)?

## Phase 2: Response Template

Adopt this structured output layout:

1. **Core Summary (Pyramid Top)** — A 1-2 sentence executive summary or recommendation at the very beginning.
2. **Context Hook (SCQA)** — A brief intro setting the stage.
3. **Detailed Structure (Pyramid Body)** — Grouped and ordered sections with clear headings and bullet points. Use **bolding** to emphasize key actions.
4. **Visual Aid (Optional)** — Include a Mermaid diagram or table to illustrate workflows, architectures, or comparisons.

## Example Output Shape

```markdown
## Recommendation

Migrate to PostgreSQL 16 by Q3 to avoid EOL compliance failure.

## Context

We run PostgreSQL 11 (EOL Nov 2025). Compliance audit on Oct 15 will flag
unpatched CVEs. Migration takes ~6 weeks; we have ~14 weeks of runway.

## Plan

1. **Snapshot + replica** (week 1-2) — stand up PG16 replica of PG11 primary
2. **Shadow traffic** (week 3-4) — dual-write from app, compare row counts
3. **Cutover** (week 5) — promote replica, keep PG11 read-only for rollback
4. **Decommission** (week 6) — drop PG11 after 1 week clean operation

## Risks

| Risk                  | Mitigation                              |
| --------------------- | --------------------------------------- |
| Extension incompatibility | Audit `pg_stat_user_functions` first  |
| Replication lag spike  | Alert if lag > 1s during shadow traffic |
```

Notice the order: conclusion → context → plan → risks. This is **ASCQ** ordering — answer first, because the audience (likely an engineering lead) wants the decision before the justification.

## Example 2: Incident Repair Plan (QSCA — Problem First)

```markdown
## The Question

Why are we losing order items in production, and how do we stop it permanently?

## What We Assumed

Our cart-to-order pipeline was atomic — one INSERT, one order.

## What's Actually Happening

Under concurrent checkout, `INSERT ... SELECT` runs without a transaction.
Two sessions read the same cart snapshot and both insert — one silently wins,
the other's items vanish. 4 occurrences this quarter; 1 lost order worth ¥18k.

## The Fix

1. **Wrap in transaction** (week 1) — `BEGIN ... SELECT FOR UPDATE ... INSERT ... COMMIT`
2. **Add idempotency key** (week 2) — client sends UUID; reject duplicates
3. **Reconcile missing orders** (week 3) — backfill from payment records
```

Notice the order: **question → assumed state → reality → fix**. This is **QSCA** — the audience (a product manager who dismissed earlier incidents as "one-off bugs") needs the question framed and the gap exposed before approving a 3-week repair. Contrast with Example 1 (ASCQ), where the engineering lead wanted the answer up front. The A→B rule drives the ordering: same frameworks, different Actor, different sequence.
