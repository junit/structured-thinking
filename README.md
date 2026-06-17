# Structured Thinking Skill for AI Agents & Developers

<p align="center">
  <b>English</b> | <a href="README.zh-CN.md">简体中文</a>
</p>

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)](https://github.com/your-username/structured-thinking/pulls)
[![LLM/AI Skill](https://img.shields.io/badge/AI%20Agent-Skill-orange.svg)](SKILL.md)

A systematic framework designed to help AI agents, coding assistants, and software developers transform raw data, scattered logs, and chronological events into high-impact, audience-focused, and decision-ready communication.

---

## 📖 Table of Contents
- [Why Structured Thinking?](#-why-structured-thinking)
- [Before vs. After Comparison](#-before-vs-after-comparison)
- [Project Directory Structure](#-project-directory-structure)
- [The 5-Step Framework](#-the-5-step-framework)
  - [Step 1: Describe the Problem (5W2H & 5-Why)](#step-1-describe-the-problem-5w2h--5-why)
  - [Step 2: Define Goal & Audience (A→B Rule & SCQA)](#step-2-define-goal--audience-ab-rule--scqa)
  - [Step 3: Structure Vertically (Pyramid Principle)](#step-3-structure-vertically-pyramid-principle)
  - [Step 4: Organize Horizontally (MECE & Ordering)](#step-4-organize-horizontally-mece--ordering)
  - [Step 5: Visualize Relationships](#step-5-visualize-relationships)
- [How to Integrate with AI Agents](#-how-to-integrate-with-ai-agents)
  - [Integrating with Claude Code / Gemini CLI](#integrating-with-claude-code--gemini-cli)
  - [Integrating with Cursor / Windsurf / VS Code](#integrating-with-cursor--windsurf--vs-code)
  - [Integrating with LangChain / Custom Agents](#integrating-with-langchain--custom-agents)
- [License](#-license)

---

## 💡 Why Structured Thinking?

AI agents and developers often suffer from "stream of consciousness" reporting. When asked to debug an incident or summarize a plan, they default to dumping raw chronological logs or a narrative timeline of what happened.

This forces human decision-makers, team leads, or executives to sift through paragraphs of noise to find the actual conclusion, impact, and next steps. 

**Structured Thinking** solves this by establishing a rigorous communication system. It ensures that recommendations are presented upfront, supporting data is logically partitioned, and every piece of information directly serves the intended audience's decision-making process.

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
    ├── agent-workflow.md    # Pre-computation steps and output layout templates
    ├── step-1-5w2h.md       # Root-cause analysis via 5W2H & 5-Why
    ├── step-2-scqa.md       # SCQA storytelling structures & A→B rules
    ├── step-3-pyramid.md    # The Pyramid Principle (Vertical Structuring)
    ├── step-4-mece.md       # MECE taxonomy & Horizontal ordering rules
    └── step-5-visualize.md  # Relationship visualization selection guide
```

---

## 🛠️ The 5-Step Framework

### Step 1: Describe the Problem (5W2H & 5-Why)
Before communicating a problem, analyze it objectively:
- **5W2H** (*What, When, Where, Why, Who, How, How much*) captures the full scope of the incident.
- **5-Why** drills down past superficial symptoms to uncover systemic process-level root causes rather than blaming individuals.
- *Refer to [references/step-1-5w2h.md](references/step-1-5w2h.md) for examples.*

### Step 2: Define Goal & Audience (A→B Rule & SCQA)
Tailor communication to drive action:
- **A→B Rule**: Define the **Actor** and the expected **Behavior**. Omit details that do not prompt the Actor to perform the Behavior.
- **SCQA Hook**: Introduce the context using **S**cenario, **C**omplication, **Q**uestion, and **A**nswer. Depending on the audience's patience and goals, choose the optimal layout order:
  - **ASCQ** (Answer first): Best for impatient executives.
  - **QSCA** (Problem first): Best for complacent stakeholders who need to feel the pain.
- *Refer to [references/step-2-scqa.md](references/step-2-scqa.md) for details.*

### Step 3: Structure Vertically (Pyramid Principle)
Organize your argument hierarchically:
- Place the **Main Conclusion/Recommendation** at the top.
- Cluster supporting arguments underneath.
- Ground the bottom layer with factual evidence.
- Ensure every node in the pyramid has a clear purpose (a single-sentence takeaway).
- *Refer to [references/step-3-pyramid.md](references/step-3-pyramid.md) for visual structures.*

### Step 4: Organize Horizontally (MECE & Ordering)
Ensure logical categorization at every horizontal level:
- **MECE** (*Mutually Exclusive, Collectively Exhaustive*): Ensure no items overlap, and no gaps are left.
- Classify ideas using standard dimensions: **Temporal** (time), **Structural** (space/components), **Qualitative** (attributes/pros-cons), or **Quantitative** (rank/impact).
- Sequence ideas consistently within a group (e.g., do not mix chronological ordering with ranking by importance).
- *Refer to [references/step-4-mece.md](references/step-4-mece.md) for exercises.*

### Step 5: Visualize Relationships
When plain text is slow to comprehend, use structural visuals:
- Map processes with **flowcharts** or **swimlanes**.
- Compare options using **tables** or **matrices**.
- Map system models using **node-link graphs** or **block diagrams**.
- Prefer lightweight syntax like **Mermaid** inline in markdown.
- *Refer to [references/step-5-visualize.md](references/step-5-visualize.md) for diagram matching.*

---

## 🤖 How to Integrate with AI Agents

This repository is designed to be directly readable by AI agents (e.g., Claude Code, Cursor, Windsurf, or custom LLM setups) to guide their behavior.

### Integrating with Claude Code / Gemini CLI
Copy the contents of `SKILL.md` to your system prompt or custom instructions configuration. When the agent acts as your coding assistant, it will automatically apply structured thinking when writing postmortems, task lists, or design explanations.

### Integrating with Cursor / Windsurf / VS Code
Create or append to your `.cursorrules` or `.windsurfrules` file at the root of your workspace:

```json
{
  "rules": [
    "When explaining complex bug fixes, architectural proposals, or design patterns, follow the structured thinking principles defined in SKILL.md. Always present conclusions and recommendations at the very beginning."
  ]
}
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
