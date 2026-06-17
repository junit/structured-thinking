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

## MoSCoW & Kano Model (For Scopes & Requirement Classification)

When detailing a plan, project roadmap, or set of feature requirements, classify items horizontally using the **MoSCoW** and **Kano** frameworks to guarantee that every feature falls into exactly one distinct priority bucket (Mutually Exclusive) and covers all scope details (Collectively Exhaustive):

* **Must have (M) [Kano: Basic / 基本型]** — Non-negotiable requirements. Without these, the release or fix is considered a failure. (e.g., login works, data is saved). Ensure all Basic needs are completed first. These represent the core behaviors expected from the Actor (see [A→B Rule in Step 2](step-2-goal-audience.md#actor-behavior-a-b-rule)).
* **Should have (S) [Kano: Performance / 期望型]** — Important but not vital. Satisfaction increases linearly with these features. (e.g., page loads in 100ms instead of 1s, bulk exports).
* **Could have (C) [Kano: Excitement / 兴奋型]** — Nice-to-have features that delight the user but have low impact. (e.g., dark mode toggle, auto-complete AI diagnostics). Propose these *only* after Basic needs are met.
* **Won't have (W) [Kano: Indifferent / 无差异型]** — Explicitly excluded from the current scope to prevent scope creep.

## DDD Bounded Contexts & Ubiquitous Language (For Structural Decomposition)

When describing or proposing a system architecture, avoid grouping purely by technical tiers (e.g., frontend, backend, database), as this leads to high coupling and cross-cutting concerns. Instead, decompose the system horizontally using **Domain-Driven Design (DDD) Bounded Contexts**:

* Group code, endpoints, and databases by **business domain boundaries** (e.g., *User Authentication*, *Order Processing*, *Inventory Management*, *Payment Gateway*).
* Ensure each context owns its model and datastore, creating clean logical boundaries.
* This achieves **structural MECE** in systems representation, as each business capability belongs to exactly one domain context.
* **DDD Ubiquitous Language (通用语言)**: Maintain strict term alignment between business concepts, documentation, database schemas, and code naming. Choose one term for a domain entity (e.g., select `Booking` or `Reservation`, but never mix both) to ensure semantic MECE and eliminate concept overlap.
* **Conway's Law Constraint (康威定律约束)**: Ensure domain boundaries align with the organization's team structure and communication paths. Avoid proposing complex multi-module or microservice boundaries if the team size is too small to handle the integration and communication overhead. Keep architecture matched to team bandwidth.

## Pareto 80/20 Rule (For Prioritization & Horizontal Ordering)

When presenting causes of a bug or multiple proposed solutions horizontally, avoid displaying a flat list of 10+ items of equal weight. Apply the **Pareto Principle** to sort by importance and focus the audience on the vital few:

* Identify the **critical 20%** of factors that generate **80%** of the impact or risk.
* Structure your horizontal layout by splitting items into two groups:
  1. **Core Drivers** (Top 2-3 items of high impact/severity).
  2. **Secondary/Long-Tail Factors** (Grouped together or relegated to a "Future Considerations" category).
* This preserves MECE structure (items are partitioned cleanly by impact tier) while preventing cognitive overload.

## The Rule of Three (For Cognitive Synthesis & Formatting)

To avoid cognitive fatigue and ensure high-impact communication, apply the **Rule of Three**. The human brain retains information best when grouped in triads:

* **Limit Core Items**: Whenever presenting recommendations, risks, plan steps, or diagnostic findings, restrict the list to exactly **3 (±1) items**.
* **Synthesize Long Lists**: If you have 7-10 distinct points, do not present them as a flat list. Group them logically into 3 main buckets, and place the details inside those buckets.
* **Application Areas**:
  * **Summary**: Limit top-level takeaways to 3 points.
  * **Plan**: Divide execution into 3 clear phases (e.g., Setup, Migration, Decommission).
  * **Evidence**: Use 3 core supporting arguments to defend your main conclusion.

## Eisenhower Matrix (For Task Prioritization & Scoping)

When organizing a list of tasks, refactoring suggestions, or bug fixes, categorize them horizontally into MECE priority quadrants using the **Eisenhower Matrix** to prevent scope drift and optimize developer focus:

| Importance / Urgency | Urgent | Not Urgent |
| :--- | :--- | :--- |
| **Important** | **Quadrant 1: Do First**<br>• Critical bug fixes<br>• Security vulnerabilities<br>• Main task deliverables | **Quadrant 2: Schedule**<br>• Technical debt refactoring<br>• Writing unit/integration tests<br>• Context documentation |
| **Not Important** | **Quadrant 3: Automate/Delegate**<br>• Code formatting changes<br>• Minor style adjustments<br>• Administrative tasks | **Quadrant 4: Eliminate**<br>• Speculative optimization<br>• Unused feature updates<br>• Premature scaling config |

* **Execution Rule**: Focus 80% of active development energy on **Quadrant 1**. Propose **Quadrant 2** items as optional future work. Aggressively ignore or automate **Quadrant 3 & 4** items.

> [!TIP]
> Quadrant 1 and Quadrant 2 tasks should be formulated as **SMART Goals** (Specific, Measurable, Achievable, Relevant, Time-bound) to ensure they are actionable. See [SMART Goals in Step 2](step-2-goal-audience.md#smart-goals-setting-actionable-targets).

## Related
- **A→B Rule & expected behavior**: See [step-2-goal-audience.md](step-2-goal-audience.md#actor-behavior-a-b-rule) to align MoSCoW priority with expected Actor behavior.
- **SMART Goals**: See [step-2-goal-audience.md](step-2-goal-audience.md#smart-goals-setting-actionable-targets) to translate Eisenhower Quadrant 1 and 2 tasks into concrete, measurable goals.
- **Vertical Structure**: See [step-3-vertical-structure.md](step-3-vertical-structure.md) to ensure each horizontally organized layer is properly supported by vertical logic.




