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
