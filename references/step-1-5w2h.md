# Step 1: Describe the Problem (5W2H & 5-Why)

## 5W2H Framework

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

Collecting these dimensions ensures you can choose what to include when communicating.

## 5-Why Method

When investigating causes, use the 5-Why method to go beyond surface symptoms.

**Procedure:**
1. Ask "why" the problem occurs
2. Treat the answer as a new problem
3. Ask "why" again
4. Repeat until you reach the root cause (typically 5 iterations, but stop when the answer leads to a process/system failure rather than a person)

**Anti-patterns to avoid:**
- Stopping at the first convenient answer
- Blaming individuals instead of processes
- Asking "who" instead of "why"
- Skipping levels (going from symptom directly to "system failure" without intermediate causes)

**Example:**
- Problem: Deploy failed in production
- Why 1: The migration script timed out
- Why 2: The script locked the users table for 4 minutes
- Why 3: The migration added a NOT NULL column without a default
- Why 4: The schema review checklist didn't flag missing defaults
- Why 5: The checklist lives in a wiki that no one updates
- **Root cause**: Schema review process is unenforced and stale

## Cynefin Framework: Classifying Problem Complexity

Before executing root-cause analysis (5-Why), categorize the problem using the **Cynefin Framework**. This dictates the appropriate action pattern and prevents you from "guessing" solutions to complex systems issues:

| Domain | Problem Nature | Action Pattern | Agent Execution Guideline |
| :--- | :--- | :--- | :--- |
| **Clear** | Well-known, obvious bug (e.g., syntax error). | **Sense $\rightarrow$ Categorize $\rightarrow$ Respond** | Apply standard best practices immediately. Do not over-analyze. |
| **Complicated** | Technical issue requiring analysis (e.g., query tuning). | **Sense $\rightarrow$ Analyze $\rightarrow$ Respond** | Perform analysis, compare options (e.g., KT Matrix), and implement the optimal solution. |
| **Complex** | Emergent/unpredictable behavior (e.g., race conditions, memory leaks). | **Probe $\rightarrow$ Sense $\rightarrow$ Respond** | **Do not guess.** You cannot solve by static analysis. Propose a *probe* first (e.g., add telemetry logs, run profilers, write repro script) to gather data before drawing conclusions. |
| **Chaotic** | Emergency outage, data corruption. | **Act $\rightarrow$ Sense $\rightarrow$ Respond** | **Stop the bleeding first.** Take immediate action (rollback, rate-limit, revert config) to stabilize the system, then analyze. |

