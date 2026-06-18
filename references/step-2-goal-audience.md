# Step 2: Audience Targeting (A→B + SCQA + Fogg)

Open this file when the response must drive a **specific audience to take a specific action** — proposals, integration guides, executive asks, behavioral change requests.

## A→B: Actor and Behavior

Before drafting, name them:

- **Actor** — who reads this? (VP, team lead, peer dev, customer, future self)
- **Behavior** — what should they do after? (approve, assign, fix, buy, reproduce)

Every paragraph either advances the Behavior or it gets deleted. Test by re-reading each paragraph: "If the Actor reads this, will they do the Behavior?" If not, rewrite or cut.

| Actor | Typical expected Behavior |
| :--- | :--- |
| VP / Executive | Approve budget, escalate, sponsor |
| Team lead | Assign tasks, remove blockers, prioritize |
| Engineering peer | Review code, fix bug, adopt pattern |
| Customer | Buy, renew, upgrade, refer |
| Future self | Reproduce decision, re-derive context |

## SCQA: Order the Opening for the Audience

Pick the order that matches the audience's state of mind:

| Order | Sequence | Use when |
| :--- | :--- | :--- |
| **SCQA** | Situation → Complication → Question → Answer | Default; gradual reveal. |
| **ASCQ** | Answer → Situation → Complication → Question | Impatient audience (most executives). |
| **QSCA** | Question → Situation → Complication → Answer | Audience dismissed earlier incidents; needs the question framed. |
| **CSQA** | Complication → Situation → Question → Answer | Complacent audience; needs provocation. |

Most technical reports should use **ASCQ** — the conclusion-first ordering also required by Pattern 1 of the core skill. Reserve SCQA for situations where the audience needs the context before they'll accept the answer.

### Worked example: same incident, two orderings

**ASCQ (for VP — conclusion-first):**
> The checkout outage cost $200k and was caused by a connection leak in the v1.2.4 rollback deploy. *[Answer]* We deployed v1.2.4 at 13:55 to fix a cart bug. *[Situation]* The deploy introduced a missing `finally` block that leaked DB connections, exhausting the pool within 5 minutes. *[Complication]* Should we mandate ESLint connection-safety rules and add pool-exhaustion alerts? *[Question]*

**SCQA (for post-mortem audience — needs context first):**
> At 13:55 we deployed v1.2.4 to fix a cart calculation bug — a routine hotfix. *[Situation]* Within 5 minutes, the DB connection pool was exhausted because the hotfix introduced a missing `finally` block in the checkout middleware. The DBA restarted the DB, but connections re-exhausted immediately. *[Complication]* How do we prevent connection leaks from reaching production? *[Question]* Mandate ESLint `no-floating-connection` rule in CI, and add a pool-utilization alert at 80% threshold. *[Answer]*

The VP version leads with impact and cost; the post-mortem version builds the causal chain so attendees can follow the reasoning.

## Fogg Behavior Model (B=MAP) — for Actionable Guides

When you want the Actor to actually do something (run a command, adopt a pattern, follow a guide), make sure all three elements converge:

$$\text{Behavior} = \text{Motivation} \times \text{Ability} \times \text{Prompt}$$

| Element | What to provide | Anti-pattern |
| :--- | :--- | :--- |
| **Motivation** | Why it matters (resolves CVE, 5x speedup, prevents data loss) | "Best practice" with no stakes |
| **Ability** | Copy-pasteable code/commands; complete blocks (no `// TODO`); minimal cognitive load | Reference docs that require synthesis |
| **Prompt** | Explicit CTA ("Run `npm run verify` now") | Implicit next step the user has to infer |

If the audience isn't acting on your docs, one of these three is missing.

## See also
- Conclusion-first ordering: `SKILL.md` Pattern 1.
- Risk brainstorming before deployment: `step-3-vertical-structure.md` (Occam + Pre-Mortem).
