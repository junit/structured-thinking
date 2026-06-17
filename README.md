# Structured Thinking Skill for AI Agents & Developers

<p align="center">
  <b>English</b> | <a href="README.zh-CN.md">简体中文</a>
</p>

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)](https://github.com/junit/structured-thinking/pulls)
[![LLM/AI Skill](https://img.shields.io/badge/AI%20Agent-Skill-orange.svg)](SKILL.md)

A systematic framework designed to help AI agents, coding assistants, and software developers transform raw data, scattered logs, and chronological events into high-impact, audience-focused, and decision-ready communication.

---

## 📖 Table of Contents
- [Why Structured Thinking?](#-why-structured-thinking)
- [Target Industries & Scenarios](#-target-industries--scenarios)
- [Before vs. After Comparison](#-before-vs-after-comparison)
- [Project Directory Structure](#-project-directory-structure)
- [The 5-Step Framework](#-the-5-step-framework)
  - [Step 1: Diagnose the Problem (Cynefin, 5-Why, Fishbone, System Dynamics)](#step-1-diagnose-the-problem-cynefin-5-why-fishbone-system-dynamics)
  - [Step 2: Audience Targeting (A→B, SCQA, Fogg)](#step-2-audience-targeting-ab-scqa-fogg)
  - [Step 3: Decision Architecture (First Principles, Occam, KT Matrix, Pre-Mortem)](#step-3-decision-architecture-first-principles-occam-kt-matrix-pre-mortem)
  - [Step 4: MECE Bucketing (Pareto, Rule of 3, Eisenhower, MoSCoW)](#step-4-mece-bucketing-pareto-rule-of-3-eisenhower-moscow)
  - [Step 5: Visualize Relationships (Diagram Matching, KT Matrix)](#step-5-visualize-relationships-diagram-matching-kt-matrix)
- [How to Integrate with AI Agents](#-how-to-integrate-with-ai-agents)
- [License](#-license)

---

## 💡 Why Structured Thinking?

AI agents and developers often suffer from "stream of consciousness" reporting. When asked to debug an incident or summarize a plan, they default to dumping raw chronological logs or a narrative timeline of what happened.

This forces human decision-makers, team leads, or executives to sift through paragraphs of noise to find the actual conclusion, impact, and next steps. 

**Structured Thinking** solves this by establishing a rigorous communication system. It ensures that recommendations are presented upfront, supporting data is logically partitioned, and every piece of information directly serves the intended audience's decision-making process.

---

## 🎯 Target Industries & Scenarios

While this toolkit was originally designed for the **software engineering and IT industries**, its core principles apply to any **high-knowledge-density, collaborative, and decision-driven professional domain**.

### 1. Applicable Industries
- **Software Engineering & IT Ops (Core)**: AI coding assistants (e.g., Claude Code, Cursor), software engineers, system architects, SREs, and DBAs.
- **Hardware & High-Tech R&D**: Engineering teams diagnosing complex hardware-software integration issues or evaluating multiple design options.
- **Product Management & Analytics**: Product managers (PMs), data analysts, and Scrum masters writing specifications (PRDs) or business reports.
- **Technical Consulting**: Consulting teams delivering technical assessments, Cloud migration paths, or system architecture proposals to executives.

### 2. Common Scenarios
- **Incident Postmortems & RCAs**: When a production outage occurs, use the **5-Why**, **Fishbone**, and **System Dynamics** frameworks in [references/step-1-problem-diagnosis.md](references/step-1-problem-diagnosis.md) to perform MECE root-cause analysis.
- **Technology & Architecture Decisions**: When debating build-vs-buy or database selection, use the **First Principles** and **Kepner-Tregoe (KT) Matrix** in [references/step-3-vertical-structure.md](references/step-3-vertical-structure.md) to drive quantitative alignment.
- **Prioritization & Scoping**: When facing roadmapping or refactoring backlogs, use the **MoSCoW** and **Eisenhower Matrix** in [references/step-4-horizontal-structure.md](references/step-4-horizontal-structure.md) to classify tasks and prevent scope creep.
- **Local Debugging & Refactoring**: When resolving compiler or test errors, follow the **OODA Loop** and **Save Point / Revert Rule** in [references/agent-workflow.md](references/agent-workflow.md) to keep debugging cycles deterministic.

### 3. Core Problems Solved
- **Eliminating Chronological Dumps**: Replaces messy "what-I-did" logs with a "conclusion-first + 3 buckets + explicit ask" structure, accelerating stakeholder decision-making.
- **Stopping Guesswork & Hype-Driven Architecture**: Forces a "probe-first" mindset for complex issues, and roots option comparisons in physical constraints and weighted scores rather than gut feeling or industry trends.
- **Mitigating Silent Launch Failures**: Uses **Pre-Mortem** analysis to pre-emptively discover failure paths and inject preventive tasks before deploying.

---

## 🔄 Before vs. After Comparison

### Chronological Storytelling (Before)
> We deployed a change at 13:55. At 14:00, checkouts started failing. The database connection pool was exhausted. The DBA restarted the DB at 14:15 but it didn't help. At 14:30 we correlated the deploy. At 14:45 we found the connection leak bug. At 15:00 we rolled back. At 15:30 it recovered.

### Structured & Audience-Focused (After)
> **Summary**: The checkout service was restored at 15:30 by reverting a connection leak bug introduced in a rollback deploy at 13:55 (total downtime: 2 hours, impact: $200k loss). We are implementing ESLint rules to prevent future leaks.
>
> **Timeline**:
> 1. **Rollback Deploy** (13:55) — Bug introduced (missing `finally` block).
> 2. **DB Restart** (14:15) — Temporary fix attempted; connections immediately re-exhausted.
> 3. **Code Reverted** (15:00–15:30) — Full service recovery.

---

## 📂 Project Directory Structure

This repository is organized as a plug-and-play instruction set for LLMs and developers:

```
.
├── SKILL.md                 # Main agent skill definition & rules
└── references/              # In-depth framework guides
    ├── agent-workflow.md    # Thought model & Response template (w/ OODA Loop & Save Point)
    ├── step-1-problem-diagnosis.md     # Problem diagnosis (Cynefin, 5-Why, Fishbone, System Dynamics)
    ├── step-2-goal-audience.md         # Goal & Audience (A→B, SCQA, Fogg B=MAP)
    ├── step-3-vertical-structure.md    # Decision Architecture (First Principles, Occam, Pre-Mortem, KT Matrix)
    ├── step-4-horizontal-structure.md  # MECE Bucketing (Pareto, Rule of 3, Eisenhower, MoSCoW)
    └── step-5-visualize.md  # Visualize (Diagram Matching + KT Matrix)
```

---

## 🛠️ The 5-Step Framework

### Step 1: Diagnose the Problem (Cynefin, 5-Why, Fishbone, System Dynamics)
Before communicating a problem, analyze it objectively:
- **Cynefin Complexity**: Categorize the problem domain (Clear, Complicated, Complex, Chaotic) to select the correct approach. For *Complex* domains (e.g., race conditions), **probe first** (logs/tests) instead of guessing.
- **5-Why**: Drill down to systemic process-level root causes instead of placing blame.
- **Fishbone Diagram**: MECE-classify hypotheses into 3-4 categories using a horizontal tree.
- **System Dynamics**: Analyze non-linear feedback loops (e.g., retry storms) to break vicious cycles rather than applying naive linear fixes.
- *Refer to [references/step-1-problem-diagnosis.md](references/step-1-problem-diagnosis.md) for details.*

### Step 2: Audience Targeting (A→B, SCQA, Fogg)
Tailor communication to drive action:
- **A→B Rule**: Define the **Actor** and target **Behavior**. Remove noise that doesn't trigger the behavior.
- **SCQA Hook**: Contextualize with Scenario, Complication, Question, and Answer. Choose the optimal order (e.g., *ASCQ* for conclusion-first to executives).
- **Fogg Behavior Model (B=MAP)**: Align Motivation, Ability (simplify CLI/code), and Prompt (clear CTA) to enable execution.
- *Refer to [references/step-2-goal-audience.md](references/step-2-goal-audience.md) for details.*

### Step 3: Decision Architecture (First Principles, Occam, KT Matrix, Pre-Mortem)
Organize your arguments hierarchically:
- **First Principles**: Root technical arguments in fundamental truths (e.g., CPU cycles, network latency) instead of lazy analogies (e.g., "industry standard").
- **Occam's Razor**: Choose the technical design or logical structure with the fewest moving parts and assumptions. Avoid over-engineering.
- **Kepner-Tregoe (KT) Decision Matrix**: Weighted scoring decision-making to quantitatively compare alternatives.
- **Pre-Mortem**: Assume the release has failed catastrophically in production and implement safeguards pre-emptively.
- *Refer to [references/step-3-vertical-structure.md](references/step-3-vertical-structure.md) for details.*

### Step 4: MECE Bucketing (Pareto, Rule of 3, Eisenhower, MoSCoW)
Ensure logical categorization at every level:
- **MECE**: Categorize horizontally without overlap (Mutually Exclusive) and without gaps (Collectively Exhaustive).
- **Pareto 80/20 Rule**: Prioritize and highlight the 20% core drivers that cause 80% of the impact.
- **The Rule of Three**: Limit lists of recommendations, risks, or phases to 3 (±1) items to avoid cognitive fatigue.
- **Eisenhower Matrix**: Categorize tasks by urgency and importance, focusing energy on Quadrant 1 and ignoring Quadrant 4.
- **MoSCoW**: Priority classification for product/feature scopes.
- *Refer to [references/step-4-horizontal-structure.md](references/step-4-horizontal-structure.md) for details.*

### Step 5: Visualize Relationships (Diagram Matching, KT Matrix)
Enhance comprehension with structural layouts:
- **Diagram Matching**: Map relationships to correct visuals (flows to *flowcharts*, models to *dependency graphs*, loops to *cycles*) using Mermaid syntax.
- **Kepner-Tregoe (KT) Matrix**: Create weighted comparison tables evaluating alternatives.
- *Refer to [references/step-5-visualize.md](references/step-5-visualize.md) for templates.*

---

## 🤖 How to Integrate with AI Agents

This repository is designed to be directly readable by AI agents (e.g., Claude Code, Cursor, Windsurf, or custom LLM setups) to guide their behavior.

### Integrating with Claude Code / Gemini CLI
Copy the contents of `SKILL.md` to your system prompt or custom instructions configuration. The agent will automatically apply structured thinking and use the **OODA Loop** (Observe, Orient, Decide, Act) to govern terminal debugging and task execution.

### Integrating with Cursor / Windsurf / VS Code
Create or append to your `.cursorrules` (Cursor), `.windsurfrules` (Windsurf), or `.github/copilot-instructions.md` (GitHub Copilot) file at the root of your workspace. These files are plain-text instruction files, not JSON:

```text
Follow the structured-thinking principles from SKILL.md when writing bug reports,
postmortems, refactoring proposals, design docs, or any response where the user
needs to make a decision. Specifically:
- Open with a 1-2 sentence conclusion (decision/impact/recommendation).
- Group evidence into 3 (+/-1) buckets with conclusion-style headers.
- End with an explicit ask (Decisions Requested / Next Action / Open Questions).
- For active debugging, use the OODA loop with one hypothesis per cycle.
```

### Integrating with LangChain / Custom Agents
Load `SKILL.md` and pass it as system instructions to your agent executors:

```python
with open("path/to/SKILL.md", "r") as f:
    system_prompt = f.read()

# Pass system_prompt to your agent initialization
```

---

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
