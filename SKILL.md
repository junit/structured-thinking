---
name: structured-thinking
description: "Use whenever you are about to present complex information to a user — incident reports, postmortems, design reviews, refactoring proposals, debugging summaries, PR descriptions, status updates, technical recommendations, architecture decisions, trade-off analyses, or any response where you might dump raw logs, timelines, or unstructured narrative. Trigger proactively on phrases like 'write a report', 'summarize', 'propose', 'review this design', 'what should we do about', 'help me decide', 'compare these options', 'what went wrong', 'explain the situation', or whenever a response could otherwise become a wall of text. Also use when the user provides raw data (logs, metrics, error traces) and expects a synthesized conclusion rather than a reformatted dump. Even short answers benefit when the user needs to make a decision — if you're about to write more than 3 paragraphs, this skill almost certainly applies."
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

| Tier | Signals | Action | Target length |
| :--- | :--- | :--- | :--- |
| **Trivial** (1-2 sentence answer) | User asks a single yes/no or lookup question. | Stop. Answer directly. Do not read references. | 1-3 sentences |
| **Moderate** (one short structured response) | Summary, status update, simple recommendation. | Use the **Three Core Patterns** below. Skip references unless you realize mid-draft that the problem is deeper than expected. | 100-300 words |
| **Complex** (full report, design doc, postmortem, multi-option decision) | Multiple findings, options, or stakeholders; raw logs/timeline involved. | Use Core Patterns + open the relevant `references/` file. | 300-800 words |

The triage exists because reading every reference costs ~30 seconds of latency. Spend it only when the response genuinely needs depth.

**Escalation rule**: If you start drafting a Moderate response and discover hidden depth (multiple root causes, competing options, multi-stakeholder impact), upgrade to Complex mid-stream. Don't force a shallow structure onto a deep problem.

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

## Output Template (all 3 patterns in action)

Use this shape for every Moderate and Complex response. Adapt section names to the actual content — these are structural slots, not fixed headings.

```
[1-2 sentence conclusion: decision / impact / recommendation]

## [Bucket 1: conclusion-style header]
[Supporting evidence, data, or reasoning — 2-5 bullets or short paragraphs]

## [Bucket 2: conclusion-style header]
[Supporting evidence, data, or reasoning]

## [Bucket 3: conclusion-style header] (optional for Moderate)
[Supporting evidence, data, or reasoning]

## Next Action / Decisions Requested / Open Questions
- [Specific ask #1]
- [Specific ask #2]
```

For **Moderate** responses, 2 buckets and a shorter ask section is often enough. For **Complex** responses, use 3 buckets and a more detailed ask.

### Data presentation rule

When evidence includes numbers (metrics, costs, benchmarks, SLA targets), present them in a table or inline comparison — not buried in prose. Quantitative evidence that the reader has to hunt for is evidence they won't use.

### Multi-audience responses

When the same output serves different audiences (e.g., VP + engineering team), use a **layered structure**: lead with the executive summary (2-3 sentences for the VP), then expand into technical detail (for the engineers). The VP stops reading after the summary; the engineer reads on. Both get what they need without a separate document.

## When to Go Deeper (Complex tier only)

Open these reference files when the situation matches:

| If the task involves... | Read this | High-value method you'll find |
| :--- | :--- | :--- |
| **Root cause / incident** with unclear causation | `references/step-1-problem-diagnosis.md` | **Cynefin** (probe before guessing for Complex), **5-Why** (push to process failure), **Fishbone** (MECE cause tree) |
| **A decision between 2+ options** | `references/step-3-vertical-structure.md` | **First Principles** (root in fundamentals, not analogy), **Occam's Razor** (prune over-engineering), **Kepner-Tregoe Matrix** (MUSTs + weighted WANTs + P×S risk) |
| **Multiple causes / hypotheses to rank** | `references/step-4-horizontal-structure.md` | **MECE** (no overlap, no gaps), **Pareto** (vital few), **Rule of 3** (cognitive chunking) |
| **Active debugging loop** | `references/agent-workflow.md` | **OODA Loop**, **Save Point + Revert Rule** (one hypothesis per cycle, never stack unverified changes) |
| **Audience-tailored structure** (ASCQ vs QSCA) | `references/step-2-goal-audience.md` | **A→B** (define Actor + expected Behavior), **SCQA** ordering, **Fogg B=MAP** (for actionable guides) |
| **Visualizing relations & comparing options** | `references/step-5-visualize.md` | **Diagram Matching** (flows/loops/causal chains to Mermaid), **KT Matrix** (scannable comparison tables) |

You do not need to read all six. Pick the one matching the task. The references contain the discipline the model does not have by default.

## Red Flags — STOP and Rethink

- The response opens with "First, let me explain the history..." or a raw timestamp.
- A list mixes chronological order and priority order.
- The response has no explicit ask or next action.
- Paragraphs of narrative that don't help the audience make a decision.
- Multiple options presented without a scoring matrix or recommendation.
- Numbers or metrics buried in prose instead of a table or inline comparison.
- A "Moderate" response growing past 300 words — it's probably Complex, escalate.

## Self-Verification Checklist

Before sending:

1. [ ] **Conclusion at top**: First sentence is a self-contained decision/impact/recommendation.
2. [ ] **3 (±1) buckets**: Evidence grouped under conclusion-style headers.
3. [ ] **Explicit ask**: Last section tells the audience what to do.
4. [ ] **No raw dumps**: Raw logs/timelines are synthesized, not copy-pasted.
5. [ ] **No over-engineering**: Simplest solution presented first (Occam).
6. [ ] **Debugging discipline**: One hypothesis per cycle; revert path stated if it fails.
