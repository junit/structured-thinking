# Step 2: Define Goal and Audience (A→B Rule & SCQA)

## Actor → Behavior (A→B) Rule

Determine **who** will receive the message (the Actor) and **what behavior** you expect from them (the Behavior). Tailor every sentence to elicit that behavior; omit details that do not serve it.

**Examples of A→B pairs:**

| Actor            | Expected Behavior                              |
| ---------------- | ---------------------------------------------- |
| Team lead        | Assign tasks, remove blockers, set priorities  |
| Engineering peer | Review code, fix bugs, adopt a pattern         |
| Executive        | Approve budget, escalate, sponsor initiative   |
| Customer         | Buy, renew, refer, upgrade                     |
| Future you       | Reconstruct context, reproduce decision        |

**Test:** After drafting, re-read each paragraph and ask: "If the Actor reads this, will they do the Behavior?" If not, rewrite or delete.

## SCQA Principle

Structure your opening to capture attention in four moves:

1. **Scenario (S)** — Establish the current state the audience already accepts
2. **Complication (C)** — Introduce what disrupts or threatens that state
3. **Question (Q)** — Articulate the question the complication raises
4. **Answer (A)** — Deliver your recommendation or conclusion

**Reorder for emphasis:**

| Order  | Emphasizes | When to use                                    |
| ------ | ---------- | ---------------------------------------------- |
| SCQA   | Story arc  | Default; gradual reveal                        |
| ASCQ   | Solution   | Audience is impatient for the answer           |
| QSCA   | Problem    | Audience needs to feel the pain first          |
| CSQA   | Conflict   | Audience is complacent; need to provoke        |

**Example (ASCQ):**
- **A**: Migrate to PostgreSQL 16 by Q3.
- **S**: We currently run PostgreSQL 11, which is end-of-life this November.
- **C**: EOL means no security patches; our compliance review will fail.
- **Q**: How do we stay compliant without downtime?

## STAR Framework: Detailing the Action Steps

While **SCQA** is the ideal storytelling hook to capture attention and frame a situation, the **STAR** framework is the best methodology for detailing the **Actions** and **Results** of a plan or incident resolution (especially in postmortems, task execution logs, and contributions):

1. **Situation (S)** — Describe the specific state of the system or business when the event happened.
2. **Task (T)** — Clarify what was required to resolve the situation, including metrics, constraints, and targets.
3. **Action (A)** — Outline the exact steps taken. Highlight technical decisions, debugging tasks, or code modifications.
4. **Result (R)** — Share the quantifiable outcome (e.g., performance impact, cost saved, time restored).

### Combining SCQA and STAR

Use **SCQA** to write the executive-level introduction (conclusion-first), then use **STAR** to structure the body sections explaining what was actually executed.

**Example (STAR structure for an Incident Remediation section):**
* **Situation**: CPU utilization on API gateways spiked to 98% at 14:00, causing 502 Bad Gateway errors for 15% of checkout traffic.
* **Task**: Reduce CPU utilization below 50% and restore 100% checkout success rate within 15 minutes.
* **Action**: Identified a rogue loop in the logging middleware, deployed a hotfix to bypass it, and scaled gateway pods from 3 to 10 replicas.
* **Result**: CPU utilization dropped to 22%, 502 errors ceased, and the checkout success rate returned to 100% within 12 minutes.

## SMART Goals: Setting Actionable Targets

When formulating the **Expected Behavior (A→B)** or defining tasks in the **STAR** framework, avoid vague, non-committal goals. Apply the **SMART** principle to ensure that any goal proposed by the agent is actionable, measurable, and clear:

* **Specific (S)** — Target a precise area for improvement. Avoid vague statements like "optimize query speed." Use "add index and rewrite SQL join."
* **Measurable (M)** — Define a quantitative metric of success. (e.g., "reduce query execution time from 500ms to <20ms," "decrease memory footprint by 30%").
* **Achievable (A)** — Ensure the goal is realistic given constraints (e.g., locking tables during production hours makes immediate schema changes unachievable; schedule a migration instead).
* **Relevant (R)** — Align the goal with the parent problem. (e.g., if the user's constraint is network egress cost, optimizing CPU usage is secondary).
* **Time-bound (T)** — State a clear deadline, estimation, or window. (e.g., "restore connection pool limits in 5 minutes," "deliver the refactoring proposal by end-of-day").

### Anti-pattern vs. SMART Goal Comparison:

| Vague Goal (Anti-pattern) | SMART Goal |
| :--- | :--- |
| "We need to fix the database performance soon." | "Add a composite index on `orders(user_id, created_at)` to bring the slow query list under 50ms by tomorrow morning." |
| "Let's clean up the code to make it more readable." | "Refactor `large-auth-service.ts` by splitting its 6 methods into separate helper classes, reducing file size from 600 lines to under 200 lines by Friday." |

## Pre-Mortem: Mitigating Risks Before Code Execution

When defining expected behavior or formulating deployment plans (especially for high-risk changes like data migrations, system refactoring, or dependency updates), perform a **Pre-Mortem** to force defensive planning:

1. **Assume Catastrophic Failure** — Fast-forward to the future and imagine that the change has failed spectacularly in production (e.g., database corrupted, API crashed under traffic).
2. **Brainstorm the "Causes of Death"** — List 2-3 most probable reasons for this specific failure.
3. **Pre-emptively Mitigate** — Add safeguard tasks to your active plan to prevent these causes from happening.

### Pre-Mortem Plan Example:

* **Goal**: Upgrade dependencies and refactor validation logic in the user login pipeline.
* **Assumed Failure (Pre-Mortem)**: The login service is failing in production. Users cannot authenticate.
* **Brainstormed Causes**:
  * New validator library is throwing runtime exceptions for existing null values in legacy database records.
  * Dependency mismatch caused a loading collision with the passport-jwt library.
* **Safeguard Actions Deployed**:
  * Run static test checks against 10,000 legacy DB snapshots locally.
  * Audit exact peer dependency requirements in package.json before running install.

## The Golden Circle: Structuring Intent (Why → How → What)

When communicating a goal, architectural change, or proposal to an audience, structure your explanation from the inside out using Simon Sinek's **Golden Circle** to establish immediate alignment and context:

```
      /-------------\
     /   [ WHAT ]    \
    /  /-----------\  \
   /  /  [ HOW ]    \  \
  /  /  /---------\  \  \
  |  |  | [ WHY ] |  |  |
  \  \  \---------/  /  /
   \  \             /  /
    \  \-----------/  /
     \---------------/
```

1. **Why (Core Purpose)** — Why does this change matter? What is the systemic value? (Always start here).
   * *Anti-pattern*: Starting with the file diff. (e.g., "I modified lines 45-60 in database.ts").
   * *Correct*: "We need to eliminate SQL injection vulnerabilities to protect customer PII."
2. **How (Process/Methodology)** — How does the change achieve the 'Why'? Which mechanisms or architectural patterns are used?
   * *Correct*: "By replacing raw SQL strings with parameterized queries using the Prisma ORM layer."
3. **What (The Output)** — What specific code, endpoints, or scripts were created or modified? (Mention this last).
   * *Correct*: "Updated `getUserById` in `user-service.ts` to use Prisma's `findUnique` query."

Always sequence your technical summaries and design headers as: **Why $\rightarrow$ How $\rightarrow$ What**.

## The Feynman Technique: Simplifying Explanations for Your Audience

When communicating complex technical designs, system errors, or code logic, apply the **Feynman Technique** to ensure your audience (regardless of their technical background) can comprehend the issue instantly:

1. **Target the Simplest Language** — Explain the topic as if explaining it to a non-technical peer or a 10-year-old. Remove abstract jargon.
2. **Use Real-World Analogies** — Map abstract computer science concepts to physical world scenarios.
3. **Identify and Fill Gaps** — If you struggle to explain a mechanism simply, it means your understanding of the codebase is incomplete. Go back and research.

### Jargon Translation Guide:

| Technical Jargon (Anti-pattern) | Simplified Analogy (Feynman Technique) |
| :--- | :--- |
| "We are experiencing race conditions in our idempotent webhook handler due to unindexed unique keys." | "Two notification messages from Stripe arrived at the same millisecond. Because the database was slow, both were processed simultaneously, resulting in duplicate charges. We added a lock to ensure we only process one message at a time." |
| "Implement a polymorphic decorator pattern to abstract repository access." | "Create a shared wrapper that lets us swap between saving data to local files or a cloud database without modifying the main application code." |

## Fogg Behavior Model: Driving Developer Action (B=MAP)

When formulating your **Expected Behavior (A→B)**, especially when writing integration guides, setup READMEs, or pull request instructions, apply the **Fogg Behavior Model** to ensure the Actor actually executes the target Behavior:

$$\text{Behavior (B)} = \text{Motivation (M)} \times \text{Ability (A)} \times \text{Prompt (P)}$$

To drive action, ensure all three elements converge:

1. **Motivation (M) [动力]** — Address *Why* the developer should act (e.g., "resolves critical CVE," "improves query speed by 5x"). Link back to the **Golden Circle**.
2. **Ability (A) [能力/易用性]** — Make the action as simple as possible. Minimize cognitive friction. Provide copy-pasteable shell commands, complete code blocks (no `// TODO: implement later` placeholders), and clear verification checks.
3. **Prompt (P) [触发点]** — Give a clear, unambiguous call-to-action (e.g., "Run `npm run verify` to test the changes now," "Copy and paste this config block into your `.env`").

### Guide Design Comparison:

| High Friction (Anti-pattern) | Actionable Guide (B=MAP) |
| :--- | :--- |
| "Set up the database connection pool in your local config, import the pool client, and test if it works." | "**Step 1**: To prevent connection starvation under load (**Motivation**), copy and paste this block into `config.ts` (**Ability**):<br>`export const pool = new Pool({...});`<br>**Step 2**: Run `npm run test:db` now to verify the connection (**Prompt**)." |






