# Step 3: Decision Architecture (First Principles + Occam + KT Matrix)

Open this file when the task involves a **decision between 2+ technical options** — design proposals, refactoring plans, build-vs-buy, technology selection.

## First Principles: Argue from Fundamentals, Not Analogy

Default LLM behavior is to justify decisions by analogy ("industry standard", "X company does this", "best practice"). This produces weak, context-free arguments. Force arguments to bottom out in **fundamental limits**:

| Weak (by analogy) | Strong (by first principles) |
| :--- | :--- |
| "We should use Redis because it's the standard caching tier." | "DB disk read latency is 10ms; RAM lookup is <1ms. At 15k RPS, DB disk IOPS saturate. In-memory cache removes the disk bottleneck." |
| "Microservices are the industry standard for scale." | "A single Node process handles ~10k concurrent connections before event-loop saturation. Our peak is 50k. We need either cluster mode or horizontal services." |

If you catch yourself writing "industry standard" or "common practice", stop. Find the underlying constraint (RTT, IOPS, memory bandwidth, Big-O complexity, lock contention) and argue from there.

## Occam's Razor: Prune Before You Build

When evaluating a proposed design, count the moving parts. Each new component (microservice, queue, database, third-party dependency, abstraction layer) must justify itself against a concrete non-functional requirement. Otherwise it's liability.

**Test**: For each component, ask "What requirement fails if I remove this?"
- If the answer is "none" → **delete it**.
- If the answer is speculative ("might need it for scale") → **defer it** with a measured trigger.
- If the answer is concrete ("needed for durability per compliance") → **keep it**.

**Anti-pattern — speculative generality**:
> Bad: "Add Kafka for event streaming, in case we need event-sourcing later."
> Better: "Use the existing Postgres LISTEN/NOTIFY. Add Kafka only when measured event throughput exceeds 5k/sec."

## Kepner-Tregoe Decision Matrix: Quantify the Choice

For any 2+ option decision, replace prose argument with a structured table:

**Decision**: [the question, e.g., "Choose the database for analytics workload"]

### 1. MUSTs (binary gate)

| Option | MUST: ingest >50k RPS | MUST: SQL | Status |
| :--- | :--- | :--- | :--- |
| A: Postgres replica | YES | YES | **GO** |
| B: Elasticsearch | YES | NO | **NO-GO** |
| C: ClickHouse | YES | YES | **GO** |

Any option failing a MUST is eliminated. Do not score it.

### 2. WANTs (weighted score)

| Criterion | Weight | C: ClickHouse | A: Postgres |
| :--- | :--- | :--- | :--- |
| Storage cost (compression) | 8 | 9 / **72** | 4 / 32 |
| Maintenance overhead | 7 | 5 / **35** | 10 / **70** |
| Multi-dim query speed | 9 | 10 / **90** | 3 / 27 |
| **Total** | — | **197** | **129** |

### 3. Risk assessment (P × S) for the top scorer

| Threat | P (1-10) | S (1-10) | P×S | Mitigation |
| :--- | :--- | :--- | :--- | :--- |
| Team lacks operational experience | 7 | 6 | **42** | Buy managed service |

The matrix prevents "gut feel" decisions and exposes where the team is actually uncertain.

## Pre-Mortem: Assume Failure, Plan Backwards

Before recommending a plan, assume it has failed in production 6 months from now. Brainstorm 2-3 **specific** causes of failure, then add preventive tasks to the plan.

**Anti-pattern**: "What could go wrong?" (too vague, produces nothing).
**Better**: "It is 6 months later. The migration corrupted user data. What *specifically* caused it?"

Common pre-mortem findings for software changes:
- New validator throws on legacy data shape → add fixture test against 10k legacy records before deploy.
- Dependency peer mismatch → audit `peerDependencies` in `package.json` before install.
- Migration locks table → run during low-traffic window with explicit timeout.

## See also
- Audience tailoring: `step-2-goal-audience.md` (A→B + SCQA).
- Bucketing supporting points: `step-4-horizontal-structure.md` (MECE + Rule of 3).
