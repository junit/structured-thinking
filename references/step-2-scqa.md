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
