---
name: structured-thinking
description: |
  Provide clear workflows and best practices for structured thinking.
  Use this skill when the conversation involves planning, problem solving,
  designing, summarizing complex information, or preparing communication such as
  reports, presentations, or notes. It helps transform unorganized thoughts
  into clear, audience-focused structures using frameworks like 5W2H,
  5-Why, the Actor→Behavior rule, SCQA, the pyramid principle, MECE
  classification, and appropriate ordering and visualization.
---

# Structured Thinking

## When to use this skill

Use this skill whenever the user asks to structure information, analyze a
problem, plan a meeting or event, prepare a report or design document,
organize personal notes, or communicate complex ideas. This skill is
especially relevant when the user needs to clarify requirements, present
options, or summarize work for specific stakeholders.

## Overview

To practice structured thinking, follow five high-level steps:

1. **Describe the problem clearly** using the 5W2H framework. Understand what
   the problem is, when and where it occurs, why it happens, who is affected,
   how it happens, and how severe it is. Applying
   the 5-Why method helps uncover the root cause by repeatedly asking "why"
   until the underlying cause is found.
2. **Define the goal and audience** using the Actor→Behavior (A→B) rule.
   Identify who will receive your information and what behavior you want from
   them. Tailor your message to serve that
   behavior; omit details that do not support your desired outcome.
   Use the SCQA principle to hook your audience: describe the **Scenario**,
   highlight a **Complication**, pose a **Question**, and offer an **Answer**.
   You can reorder SCQA to emphasize solutions (ASCQ), problems (QSCA), or
   conflicts (CSQA).
3. **Structure the information** using the pyramid principle. Start with your
   main conclusion, then provide supporting conclusions and finally the
   detailed evidence or arguments. Think from the
   audience's perspective: organize your points in layers so that each
   successive layer elaborates on the layer above.
4. **Organize horizontally** by categorizing and ordering items at the same
   level. Use the MECE principle (Mutually Exclusive, Collectively Exhaustive)
   to ensure categories do not overlap and together cover all possibilities. If pure
   MECE classification is hard, extract overlapping elements into separate
   categories. After classifying, sequence items
   consistently—by structure, time, or importance—and avoid mixing orderings
   within the same branch. Use practical
   classification exercises to verify your categories; for example, brainstorm
   all ways to get an over-height truck through a low tunnel and group them
   into non-overlapping solutions.
5. **Visualize relationships** to make complex structures easy to grasp. After
   organizing your information vertically and horizontally, translate the
   relationships into diagrams or charts. Common relationship types include
   comparison, action/effect, flow, and association.
   Select the diagram type that matches your message—pie charts for parts of
   a whole, flow charts for processes, cycle diagrams for repeated states, etc.

### Step 1: Describe the problem (5W2H & 5-Why)

Use the 5W2H framework to gather all necessary context:

| Question    | Purpose                                          |
| ----------- | ------------------------------------------------ |
| **What**    | Define the problem itself                        |
| **When**    | Identify when the problem occurs                 |
| **Where**   | Locate where it happens                          |
| **Why**     | Understand why it happens                        |
| **Who**     | Identify stakeholders                            |
| **How**     | Describe the process                             |
| **How much**| Assess the severity/extent                       |

Collecting these dimensions ensures you can choose what to include when
communicating. When investigating causes, use the 5-Why method to go
beyond surface symptoms. Ask "why" repeatedly until you reach the root
cause; avoid prematurely stopping at a convenient answer.

### Step 2: Define the goal and audience (A→B rule & SCQA)

1. **Actor→Behavior (A→B)**: Determine who will receive the message and
   what behavior you expect. For example, when reporting to team leaders
   (the actors), you may expect them to assign new tasks, remove blockers,
   or emphasize best practices. Include only
   information that leads to these behaviors.
2. **SCQA principle**: Structure your opening to capture attention. Present
   the **Scenario** (current state), introduce a **Complication** that
   disrupts it, pose a **Question**, and then deliver your **Answer**.
   Adjust the order (ASCQ, QSCA, CSQA) to emphasize solutions, problems, or conflicts.

### Step 3: Structure the information (Pyramid principle)

1. **Conclusion first**: State your main conclusion or recommendation up
   front.
2. **Supporting layers**: Under the main conclusion, group supporting
   conclusions that justify it. Beneath each supporting conclusion, provide
   further sub-conclusions or evidence as needed.
3. **Audience perspective**: Organize layers based on what your audience
   cares about. Remember that audiences often think chronologically, but a
   hierarchical structure helps them quickly grasp your central idea.
4. **Purpose in every conclusion**: Each layer should carry its own center
   of gravity—a purpose or expected result. Without this, your points may
   lack "soul" and confuse the audience.

### Step 4: Organize horizontally (MECE & ordering)

1. **Classify**: At each level, ensure your categories are mutually exclusive
   and collectively exhaustive (MECE). For very
   complex cases, extract overlapping elements into separate categories.
2. **Standard MECE Dimensions**:
   - **Temporal (Time-based)**: Steps in a workflow, phases in a project, or historical timeline.
   - **Structural (Space-based)**: Regions, departments, layers of a software stack, components of a system.
   - **Qualitative (Attribute-based)**: Pros vs. cons, internal vs. external factors, cost vs. benefit.
   - **Quantitative (Rank-based)**: High/medium/low priority, market segments by size, age brackets.
3. **Exercise**: Practice classifying by brainstorming all options and
   grouping them. For example, when moving a 3.05-meter truck through a
   3-meter tunnel, categories might include lowering the truck (deflate tires),
   modifying the path (digging), or altering the tunnel (raising the roof).
4. **Order**: Arrange items consistently. Within a single branch, choose one
   ordering principle—structure, time, or importance—and apply it uniformly. Mixing orderings in the same branch creates confusion.

### Step 5: Visualize relationships

After structuring information, depict the relationships graphically if
appropriate. Diagrams help audiences grasp comparisons, causal chains,
flows, or associations. Choose a diagram type that
matches your message: use pie charts for parts of a whole, flow charts for
processes, cycle diagrams for repeated loops, or simple node-link diagrams
for relationships (e.g., Mermaid diagrams).

## How to apply this skill as an Agent

When executing a task that requires structured thinking or presenting complex information to the user, follow this process:

### 1. Pre-computation (Mental Draft)
Before generating the final response, outline your thoughts in your `thought` block:
- **A→B Target**: Who is the user (developer, manager, designer)? What decision/action should they make?
- **SCQA Hook**: What is the context (S), what went wrong (C), what is the core question (Q), and what is my answer (A)?
- **Pyramid Outline**: Map out the top-level conclusion and the supporting arguments.
- **MECE Check**: Are the categories distinct and complete? Are they ordered logically (e.g., chronologically, structurally, or by importance)?

### 2. Response Template
Adopt a structured output layout:
- **Core Summary (Pyramid Top)**: A 1-2 sentence executive summary or recommendation at the very beginning.
- **Context Hook (SCQA)**: A brief intro setting the stage.
- **Detailed Structure (Pyramid Body)**: Grouped and ordered sections with clear headings and bullet points. Use bolding to emphasize key actions.
- **Visual Aid (Optional)**: Include a Mermaid diagram or table to illustrate workflows, architectures, or comparisons.

## Additional tips

- **Practice across contexts**: Structured thinking applies to daily reports, problem analyses, design documents, presentations, personal notes, and everyday decisions.
- **Write for future you**: When taking notes, imagine you are writing for a stranger—your future self. Provide sufficient context and structure so they can understand without assumptions.
- **Iterate and refine**: Structured thinking is a skill that improves with practice. Use these frameworks regularly, evaluate what works, and adjust your approach over time.

## Limitations

This skill provides structured thinking guidance but does not replace
subject-matter expertise. It does not automatically generate diagrams. Use
appropriate tools (like Mermaid blocks) to create diagrams when needed.