# Step 4: MECE Bucketing (Pareto + Rule of 3)

Open this file when the response needs to **partition many items into clean categories** — action items, hypotheses, requirements, recommendations.

## MECE Test

At every level of grouping, categories must be:

- **Mutually Exclusive**: no item fits in two buckets.
- **Collectively Exhaustive**: every relevant item fits in some bucket.

**Test**: For any item, ask "which single category?" If the answer is "two" or "none", the taxonomy is broken — merge, split, or add an "Other" bucket.

### Four proven axes (when classification is hard)

Pick the axis that best serves the audience's decision. If unsure, use this heuristic:

| Axis | Example | Best when... |
| :--- | :--- | :--- |
| **Temporal** | Steps in a workflow, project phases, historical timeline | The audience needs to follow a sequence or plan |
| **Structural** | Regions, layers of a stack, components | The audience needs to understand *where* things live |
| **Qualitative** | Pros vs. cons, internal vs. external, cost vs. benefit | The audience needs to compare trade-offs |
| **Quantitative** | High/medium/low priority, market segments, age brackets | The audience needs to rank or triage items |

When two axes seem equally valid, prefer the one that makes the **first bucket header** a conclusion the audience can act on. "Critical: fix before release" beats "Phase 1" because it tells the reader what to do, not just when.

## Pareto 80/20: Vital Few Over Long Tails

Default LLM behavior is to list 10 items of equal weight. Force rank them:

1. Identify the **vital 20%** — the 2-3 items driving 80% of impact/risk.
2. Put them in their own bucket at the top ("Core Drivers" / "Must Fix").
3. Relegate the rest to "Secondary Factors" / "Future Considerations".

This preserves MECE (every item is in exactly one tier) while preventing cognitive overload.

## Rule of 3 (±1): Cognitive Chunking

The brain retains information best in triads. Apply ruthlessly:

- **Top-level takeaways**: at most 3.
- **Plan phases**: at most 3 (e.g., Setup / Migration / Decommission).
- **Recommendations**: at most 3 core, with secondaries collapsed into a bucket.

If you have 7-10 items, **do not** present them as a flat list. Group into 3 buckets, each with a one-sentence summary that itself is a conclusion.

**Test**: Read each bucket header alone. Does it communicate a complete idea? If it's just a category label ("Details", "Other"), it's a failed bucket.

## Eisenhower Matrix (for task prioritization)

When organizing a list of tasks / fixes / refactor suggestions, MECE them by urgency × importance:

| | Urgent | Not Urgent |
| :--- | :--- | :--- |
| **Important** | **Q1 Do First**: critical bugs, security, deliverables | **Q2 Schedule**: tech debt, tests, docs |
| **Not Important** | **Q3 Automate/Delegate**: formatting, admin | **Q4 Eliminate**: speculative work |

Rule: spend 80% on Q1. Propose Q2 as optional. Aggressively cut Q3/Q4.

## MoSCoW (for requirement / scope classification)

Alternative axis for product / feature lists:

- **Must** — non-negotiable; release fails without it.
- **Should** — important but not vital.
- **Could** — nice-to-have, propose only after Must is met.
- **Won't** — explicitly excluded from current scope.

Use MoSCoW when the audience is a product owner; use Eisenhower when the audience is an engineer sorting their queue.

## See also
- Diagnosing root causes before bucketing them: `step-1-problem-diagnosis.md` (5-Why + Fishbone).
- Conclusion-style bucket headers: `SKILL.md` Pattern 2.
