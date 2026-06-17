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


