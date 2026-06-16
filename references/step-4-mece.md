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
