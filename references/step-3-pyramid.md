# Step 3: Structure the Information (Pyramid Principle)

## Core Idea

Start with your **main conclusion**, then **supporting conclusions**, then **evidence**. Each layer elaborates on the layer above. Audiences grasp the central idea first, then decide how deep to drill.

```
        [Main Conclusion]
           /     |     \
    [Support] [Support] [Support]
      /  \      |        /  \
   [E]  [E]   [E]     [E]  [E]
```

## Four Rules

### 1. Conclusion First
State your main conclusion or recommendation at the very top. Do not bury it in background.

**Anti-pattern:** "First, let me explain the history..." → audience loses the thread.

### 2. Supporting Layers
Under the main conclusion, group supporting conclusions that justify it. Beneath each supporting conclusion, provide further sub-conclusions or evidence as needed.

### 3. Audience Perspective
Organize layers based on what your audience cares about. Audiences often think chronologically, but a hierarchical structure helps them quickly grasp your central idea. Reorder chronological content into thematic layers when it serves comprehension.

### 4. Purpose in Every Conclusion
Each layer should carry its own **center of gravity** — a purpose or expected result. Without this, points lack "soul" and confuse the audience.

**Test:** Read any box in the pyramid. Can you state its purpose in one sentence? If not, it is a list item, not a conclusion — merge or split it.

## Practical Build Order

1. Write the top-level conclusion first (forced clarity)
2. Brainstorm all supporting points (divergent)
3. Group supporting points into 3 (±1) buckets (convergent)
4. For each bucket, write a one-sentence conclusion that summarizes it
5. Repeat recursively until evidence level
6. Read top-down: each parent should follow logically from its children
7. Read bottom-up: each child should support its parent

## First Principles Reasoning: Strengthening Vertical Justification

When justifying a supporting conclusion or presenting evidence in your pyramid structure, avoid relying on **analogical reasoning** (e.g., "Industry leaders do X" or "We have always done Y"). Instead, use **First Principles Reasoning** to deconstruct the problem to fundamental technical, architectural, or physical facts and build your argument up from there:

| Reasoning Method | Form | Example (Caching Strategy) | Quality |
| :--- | :--- | :--- | :--- |
| **By Analogy** | "We should do X because others do X or it's standard convention." | "We should deploy Redis because it's the standard industry caching tier for web applications." | **Low** (Fails to justify specific context/limits) |
| **By First Principles** | "We should do X because fundamental limits (CPU, memory, networking) dictate it." | "Database disk read latency is 10ms. RAM lookup latency is <1ms. At 15k RPS, DB disk IOPS will be exhausted. Storing queries in-memory avoids disk bottleneck." | **High** (Rigorous, self-evident technical justification) |

### How to Apply in the Pyramid:
1. **At the Support Layer**: State the conclusion based on functional requirements.
2. **At the Evidence Layer**: Do not just quote tool names. Root the argument in fundamental computer science principles: network round-trip times (RTT), Big-O time complexity, database locks, thread blocking, memory allocation, or physical system constraints.

## Occam's Razor: Pruning the Design Pyramid

When evaluating multiple architectures, logic patterns, or solutions to a problem, apply **Occam's Razor**: *"Plurality should not be posited without necessity"* (or in software terms: the simplest solution with the fewest moving parts is usually the best).

Apply this to prune complexity from your design pyramid:

* **Reduce Layers**: Do not add abstraction layers (e.g., intermediate interfaces, factories, generic wrappers) unless you have an immediate requirement for polymorphism.
* **Minimize Entities**: Prefer single-responsibility functions and cohesive modules over introducing new services, microservices, databases, or third-party dependencies.
* **Keep Explanations Direct**: If 2 facts fully justify a conclusion, do not add 3 speculative justifications to the pyramid. Keep arguments tight.

### Over-Engineered vs. Pruned Design Comparison:

| Over-Engineered Pyramid (Anti-pattern) | Pruned Pyramid (Occam's Razor) |
| :--- | :--- |
| **Conclusion**: Add user billing support.<br>**Support**: Set up a payment microservice, deploy Kafka for event streaming, spin up DynamoDB for ledger records. | **Conclusion**: Add user billing support.<br>**Support**: Integrate Stripe SDK into the existing API, save transactions to the primary database using transactional checks. |


