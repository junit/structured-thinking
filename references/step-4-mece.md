# Step 4: Organize Horizontally (MECE & Ordering)

## MECE Principle

At every level of the pyramid, categories must be:

- **Mutually Exclusive**: No item fits in two categories
- **Collectively Exhaustive**: Together, the categories cover all possibilities

**Test for MECE:** For any item, ask "which single category does this belong to?" If the answer is "two" or "none," the taxonomy is broken.

## Four Standard MECE Dimensions

When classification is hard, pick one of these proven axes:

| Dimension    | Axis         | Examples                                                       |
| ------------ | ------------ | -------------------------------------------------------------- |
| **Temporal** | Time         | Steps in a workflow, phases in a project, historical timeline  |
| **Structural**| Space       | Regions, departments, layers of a software stack, components   |
| **Qualitative**| Attribute  | Pros vs. cons, internal vs. external, cost vs. benefit         |
| **Quantitative**| Rank      | High/medium/low priority, market segments by size, age brackets|

## When Pure MECE Fails

For very complex cases, extract overlapping elements into a **separate category** that sits outside the main taxonomy. Do not force-fit; an "Other / Cross-cutting" bucket is acceptable if small and clearly labeled.

## Classic Exercise

Practice classifying by brainstorming all options, then grouping:

> **Problem:** Move a 3.05-meter truck through a 3-meter tunnel.

| Category          | Solutions                                   |
| ----------------- | ------------------------------------------- |
| Lower the truck   | Deflate tires, remove cargo, lower suspension |
| Modify the path   | Dig a dip in the road, reroute              |
| Alter the tunnel  | Raise the roof, widen                       |

The three categories are MECE: every solution touches the truck, the path, or the tunnel.

## Ordering Principles

After classifying, sequence items consistently. Within a **single branch**, pick one ordering and apply it uniformly:

- **By structure** — physical or logical composition (front-to-back, top-to-bottom)
- **By time** — sequence of occurrence (first-to-last)
- **By importance** — rank by impact, urgency, or audience priority

**Anti-pattern:** Mixing orderings in the same branch creates confusion. If a list starts by importance, do not switch to chronological halfway through. Split into separate lists if you need both views.

## Advanced MECE Taxonomy Patterns

When classifying software architectures, scopes, or features horizontally, leverage these specialized MECE patterns:

### 1. MoSCoW Classification (For Scopes & Roadmaps)

When detailing a plan, project roadmap, or set of feature requirements, classify items horizontally using the **MoSCoW** framework. This guarantees that every feature falls into exactly one distinct priority bucket (Mutually Exclusive) and covers all scope details (Collectively Exhaustive):

* **Must have (M)** — Non-negotiable requirements. Without these, the release or fix is considered a failure (e.g., security patching, core checkout pipeline).
* **Should have (S)** — Important but not vital. If time is short, can be deferred to a later point (e.g., bulk exports, secondary user roles).
* **Could have (C)** — Nice-to-have features that improve experience but have low impact (e.g., dark mode toggle, minor UI alignments).
* **Won't have (W)** — Explicitly excluded from the current scope. Solves scope creep by aligning expectations upfront (e.g., multi-region clustering in v1).

### 2. DDD Bounded Contexts (For Structural Decomposition)

When describing or proposing a system architecture, avoid grouping purely by technical tiers (e.g., frontend, backend, database), as this leads to high coupling and cross-cutting concerns. Instead, decompose the system horizontally using **Domain-Driven Design (DDD) Bounded Contexts**:

* Group code, endpoints, and databases by **business domain boundaries** (e.g., *User Authentication*, *Order Processing*, *Inventory Management*, *Payment Gateway*).
* Ensure each context owns its model and datastore, creating clean logical boundaries.
* This achieves **structural MECE** in systems representation, as each business capability belongs to exactly one domain context.

### 3. Pareto 80/20 Rule (For Prioritization & Horizontal Ordering)

When presenting causes of a bug or multiple proposed solutions horizontally, avoid displaying a flat list of 10+ items of equal weight. Apply the **Pareto Principle** to sort by importance and focus the audience on the vital few:

* Identify the **critical 20%** of factors that generate **80%** of the impact or risk.
* Structure your horizontal layout by splitting items into two groups:
  1. **Core Drivers** (Top 2-3 items of high impact/severity).
  2. **Secondary/Long-Tail Factors** (Grouped together or relegated to a "Future Considerations" category).
* This preserves MECE structure (items are partitioned cleanly by impact tier) while preventing cognitive overload.


