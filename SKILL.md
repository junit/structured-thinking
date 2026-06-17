---
name: structured-thinking
description: "Use whenever you are about to present complex information to a user — incident reports, postmortems, design reviews, refactoring proposals, debugging summaries, PR descriptions, status updates, technical recommendations, or any response where you might dump raw logs, timelines, or unstructured narrative. Trigger proactively on phrases like 'write a report', 'summarize', 'propose', 'review this design', 'what should we do about', 'help me decide', or whenever a response could otherwise become a wall of text. Even short answers benefit when the user needs to make a decision."
---

# Structured Thinking

A communication discipline that forces conclusions to the top, supports them with logically grouped evidence, and ends with an explicit ask. The goal is not "more structured" — it is to make the audience's next decision obvious.

## When NOT to Use

- Live debugging where you are actively running shell commands (use debugging skills).
- Writing source code, config, or commit messages.
- One-line factual answers ("yes", "use `npm ci`").
- Casual conversation.

## Step 0: Complexity Triage (read this first)

Before opening any reference file, classify the task:

| Tier | Signals | Action |
| :--- | :--- | :--- |
| **Trivial** (1-2 sentence answer) | User asks a single yes/no or lookup question. | Stop. Answer directly. Do not read references. |
| **Moderate** (one short structured response) | Summary, status update, simple recommendation. | Use only the **Three Core Patterns** below. Skip references. |
| **Complex** (full report, design doc, postmortem, multi-option decision) | Multiple findings, options, or stakeholders; raw logs/timeline involved. | Use Core Patterns + open the relevant `references/` file. |

The triage exists because reading every reference costs ~30 seconds of latency. Spend it only when the response genuinely needs depth.

## The Three Core Patterns (apply to every Moderate and Complex response)

These are the patterns that separate a structured response from a default LLM response. Use all three on every non-trivial answer.

### Pattern 1: Conclusion at the Top

Open with 1-2 sentences that contain the **decision, impact, or recommendation** — not background.

**Bad**: "At 13:00, an alert fired. At 13:05, we checked CPU. At 13:10, we hypothesized..."

**Good**: "Service was restored at 13:35 by blocking a scraper IP range in Cloudflare after a 35-minute latency spike. The durable fix is per-IP rate limiting; need your sign-off for ~1 engineer-week."

If you cannot write the first sentence as a self-contained conclusion, you do not yet understand the problem — go back and figure it out.

### Pattern 2: Group Evidence into 3 (±1) Buckets

After the conclusion, partition supporting detail into at most 3 buckets. Use headers. The bucket names should be **conclusions in miniature**, not categories.

**Bad headers**: "Details", "Background", "Misc"
**Good headers**: "Root cause: scraper flood", "Why detection was slow", "Remediation plan"

If a bucket has more than 3 items, ask whether those items are actually 2 buckets mashed together.

### Pattern 3: End with an Explicit Ask

The last section of any Moderate or Complex response tells the audience **what to do next**. Use one of:

- **Decisions Requested** (for reports/proposals): bullet list of approvals/choices needed.
- **Next Action** (for debugging): the one command to run next.
- **Open Questions** (for design docs): what's still unknown.

A response without an explicit ask is informational noise. The audience has to invent the action — which is exactly what structured communication is meant to prevent.

## When to Go Deeper (Complex tier only)

Open these reference files when the situation matches:

| If the task involves... | Read this | High-value method you'll find |
| :--- | :--- | :--- |
| **Root cause / incident** with unclear causation | `references/step-1-problem-diagnosis.md` | **Cynefin** (probe before guessing for Complex), **5-Why** (push to process failure), **Fishbone** (MECE cause tree) |
| **A decision between 2+ options** | `references/step-3-vertical-structure.md` | **First Principles** (root in fundamentals, not analogy), **Occam's Razor** (prune over-engineering), **Kepner-Tregoe Matrix** (MUSTs + weighted WANTs + P×S risk) |
| **Multiple causes / hypotheses to rank** | `references/step-4-horizontal-structure.md` | **MECE** (no overlap, no gaps), **Pareto** (vital few), **Rule of 3** (cognitive chunking) |
| **Active debugging loop** | `references/agent-workflow.md` | **OODA Loop**, **Save Point + Revert Rule** (one hypothesis per cycle, never stack unverified changes) |
| **Audience-tailored structure** (ASCQ vs QSCA) | `references/step-2-goal-audience.md` | **A→B** (define Actor + expected Behavior), **SCQA** ordering, **Fogg B=MAP** (for actionable guides) |

You do not need to read all five. Pick the one matching the task. The references contain the discipline the model does not have by default.

## Red Flags — STOP and Rethink

- The response opens with "First, let me explain the history..." or a raw timestamp.
- A list mixes chronological order and priority order.
- The response has no explicit ask or next action.
- Paragraphs of narrative that don't help the audience make a decision.
- Multiple options presented without a scoring matrix or recommendation.

## Self-Verification Checklist

Before sending:

1. [ ] **Conclusion at top**: First sentence is a self-contained decision/impact/recommendation.
2. [ ] **3 (±1) buckets**: Evidence grouped under conclusion-style headers.
3. [ ] **Explicit ask**: Last section tells the audience what to do.
4. [ ] **No raw dumps**: Raw logs/timelines are synthesized, not copy-pasted.
5. [ ] **No over-engineering**: Simplest solution presented first (Occam).
6. [ ] **Debugging discipline**: One hypothesis per cycle; revert path stated if it fails.
