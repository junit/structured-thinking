# Step 5: Visualize Relationships

## When to Visualize

After structuring information vertically (pyramid) and horizontally (MECE), translate the relationships into diagrams **when prose alone would be slower to grasp**. Skip visualization for trivial relationships.

## Match Diagram to Message

Pick the diagram type that matches the relationship you are communicating:

| Relationship            | Diagram type              | Example                                  |
| ----------------------- | ------------------------- | ---------------------------------------- |
| Parts of a whole        | Pie chart, treemap        | Budget allocation, market share          |
| Process / flow          | Flowchart, swimlane       | CI/CD pipeline, approval workflow        |
| Repeated loop           | Cycle diagram             | PDCA, monthly close, dev loop            |
| Causal chain            | Causal loop, fishbone     | Incident root cause, feedback system     |
| Hierarchy               | Tree, org chart, mind map | Org structure, taxonomy, file system     |
| Comparison              | Bar chart, table          | Feature matrix, before/after             |
| Relationship / network  | Node-link, graph          | Service dependencies, social graph       |

## Tools

- **Mermaid** (inline in markdown) — preferred for flowcharts, sequence diagrams, Gantt
- **Tables** — preferred for structured comparisons
- **External tools** — draw.io, Excalidraw for hand-drawn feel; native chart libraries for data

## Anti-patterns

- Using a pie chart for >7 slices (unreadable)
- Using a flowchart for a 2-step process (overkill)
- Decorating instead of informing (3D pie charts, gradient fills)
- Repeating in prose what the diagram already shows (redundancy)

## Kepner-Tregoe (KT) Decision Matrix (For Option Comparison)

When presenting technical proposals or trade-off decisions between multiple options (e.g., electing to build a custom solution vs. buying a SaaS tool, or choosing between MongoDB and Postgres), use a **Kepner-Tregoe (KT) Decision Matrix** structure. This translates a complex, subjective choice into a clear, logical comparison:

1. **Classify Criteria**: Split your requirements into **MUSTs** (mandatory, binary yes/no) and **WANTS** (desirable features with varying importance).
2. **Assign Weights**: Rate each **WANT** on a scale of 1–10 (10 being critical, 1 being nice-to-have).
3. **Score Alternatives**: Score each alternative against the criteria (1–10). Calculate the weighted score (`Weight x Score`).
4. **Identify Risks**: List potential risks for the top-scoring options, assigning Probability (P) and Severity (S) from 1–10.

### Markdown Table Template for KT Analysis:

**Decision: Database Selection for High-Throughput Analytics**

#### 1. Mandatory Criteria (MUSTs)

| Option | MUST: Real-time ingest (>50k RPS) | MUST: SQL compatibility | Status |
| :--- | :--- | :--- | :--- |
| **A: Postgres replica** | YES | YES | **GO** |
| **B: Elasticsearch** | YES | NO (custom DSL) | **NO-GO** |
| **C: ClickHouse** | YES | YES (ANSI SQL) | **GO** |

#### 2. Desirable Criteria (WANTs)

| Criteria | Weight | ClickHouse Score | ClickHouse Weighted | Postgres Score | Postgres Weighted |
| :--- | :--- | :--- | :--- | :--- | :--- |
| Low storage cost (compression) | 8 | 9 | **72** | 4 | **32** |
| Low maintenance overhead | 7 | 5 (new cluster) | **35** | 10 (existing infra)| **70** |
| Query speed for multi-dim group | 9 | 10 | **90** | 3 | **27** |
| **Total Score** | - | - | **197** | - | **129** |

#### 3. Risk Assessment (For ClickHouse - High Score Option)

| Threat / Risk | Probability (1-10) | Severity (1-10) | Total Threat (P x S) | Mitigation Plan |
| :--- | :--- | :--- | :--- | :--- |
| Team lacks ClickHouse operational knowledge | 7 | 6 | **42** | Purchase Managed ClickHouse (Altinity/ClickHouse Cloud) |

