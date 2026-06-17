# Pressure Testing Scenarios: `structured-thinking`

This document outlines the standardized pressure scenarios used to test and verify the `structured-thinking` skill. To comply with the **Iron Law of Writing Skills**, these scenarios must be run with a subagent (using `invoke_subagent`) to observe baseline failure (RED phase) and verify compliance (GREEN phase).

---

## Scenario 1: Incident Outage Report (Chronological vs. Structured)

* **Objective**: Test if the agent defaults to chronological storytelling or properly structures an incident report conclusion-first.
* **Target Actor**: VP of Engineering (wants executive impact and immediate restoration steps).
* **Pressure**: Chronological logs dump + urgency.

### Prompt Input
```text
We had an outage today! Here are the logs and what we did. Please write a report for the VP of Engineering:
13:00 - Alert triggered: API latency spiked to 4.5 seconds.
13:05 - Checked server dashboard. CPU usage on web-01 and web-02 was at 99%.
13:10 - SRE team suspected a memory leak in the recently deployed v1.2.4 version.
13:15 - Initiated a container restart on all web pods. CPU dropped briefly but spiked back to 99% within 2 minutes.
13:20 - Developer analyzed access logs and noticed a massive spike in requests to `/api/v1/search` from a single IP range (198.51.100.0/24).
13:25 - Realized it was a scraper bot scraping our product catalog without rate limiting.
13:30 - Added an IP block rule in Cloudflare.
13:35 - Latency normalized to 200ms. CPU usage dropped to 15%. Outage resolved.
```

### Baseline Failure Mode (RED)
The agent copy-pastes the timeline directly, starts with *"First, at 13:00..."*, does not provide a top-level impact/downtime summary, and writes a long narrative wall of text.

### Success Criteria (GREEN)
1. **Executive Summary**: Starts with a 1-2 sentence core conclusion/impact summary (e.g., *"The API outage was resolved at 13:35 by blocking a malicious scraping IP range in Cloudflare, restoring CPU usage to 15% after 35 minutes of latency spikes"*).
2. **Pyramid Grouping**: Groups details into exactly 3 (±1) logical sections (e.g., Overview/Impact, Timeline, Root Cause & Preventive Actions).
3. **No Raw Log Dumping**: The chronological timeline is synthesized and clean, not just copy-pasted raw logs.

---

## Scenario 2: Technical Refactoring Proposal (Over-Engineering Pressure)

* **Objective**: Test if the agent applies Occam's Razor and First Principles when asked to design a new feature.
* **Target Actor**: Technical Lead (wants low complexity and clear trade-offs).
* **Pressure**: Authority suggestion to over-engineer.

### Prompt Input
```text
We need to add a simple PDF export feature for user invoices. The tech lead suggested we spin up a new Node.js microservice running Puppeteer, configure an AWS SQS queue to handle export events, store the PDFs in an S3 bucket, and set up a Lambda function to clean up old PDFs. What do you think of this design? Propose a solution.
```

### Baseline Failure Mode (RED)
The agent accepts the microservice + SQS + S3 + Lambda design without questioning, starts detailing the infrastructure config, and creates an over-engineered implementation plan.

### Success Criteria (GREEN)
1. **Occam's Razor Application**: Challenges the over-engineered proposal. Recommends a simpler alternative first (e.g., generating PDFs in-process using `pdfkit` or `jsPDF` directly inside the existing API if volume is low).
2. **Kepner-Tregoe Matrix**: Provides a comparison table comparing the two options against MUSTs and WANTs (e.g., low maintenance vs. scalability).
3. **Golden Circle Structure**: Organizes the response using **Why $\rightarrow$ How $\rightarrow$ What** sequence.

---

## Scenario 3: Debugging under Stress (OODA & Reverting Changes)

* **Objective**: Test if the agent applies systematic OODA loops and reverts failed attempts, rather than stacking unverified code changes.
* **Target Actor**: Future self / developer peer.
* **Pressure**: Stacked test failures.

### Prompt Input
```text
The CI test pipeline is failing with `TypeError: Cannot read properties of undefined (reading 'map')` in `user-service.ts` line 42. You need to fix it. Do not guess. Walk through your debugging process and explain how you will verify and revert changes if they don't work.
```

### Baseline Failure Mode (RED)
The agent immediately suggests 3 different code edits at once (e.g., adding a optional chain `?.map`, changing the default initializer, wrapping in try/catch) without locating the root cause first, and does not mention reverting changes if they fail.

### Success Criteria (GREEN)
1. **Cynefin Classification**: Classifies the problem (Complicated or Complex) to define the action pattern.
2. **OODA Loop Execution**: Explicitly steps through **Observe** (inspecting line 42), **Orient** (determining what variable is undefined), **Decide** (formulating a single testable hypothesis), and **Act** (running a targeted verification test).
3. **Save Point / Revert Rule**: Explicitly states that if the fix does not resolve the `TypeError`, the change will be reverted (using `git restore`) before trying another approach.
