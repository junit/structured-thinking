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
