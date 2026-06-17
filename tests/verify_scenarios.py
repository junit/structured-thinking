#!/usr/bin/env python3
import sys
import os
import re
import argparse

# Define prompt inputs based on tests/pressure-scenarios.md
SCENARIOS = {
    1: {
        "name": "Incident Outage Report (Chronological vs. Structured)",
        "prompt": (
            "We had an outage today! Here are the logs and what we did. Please write a report for the VP of Engineering:\n"
            "13:00 - Alert triggered: API latency spiked to 4.5 seconds.\n"
            "13:05 - Checked server dashboard. CPU usage on web-01 and web-02 was at 99%.\n"
            "13:10 - SRE team suspected a memory leak in the recently deployed v1.2.4 version.\n"
            "13:15 - Initiated a container restart on all web pods. CPU dropped briefly but spiked back to 99% within 2 minutes.\n"
            "13:20 - Developer analyzed access logs and noticed a massive spike in requests to `/api/v1/search` from a single IP range (198.51.100.0/24).\n"
            "13:25 - Realized it was a scraper bot scraping our product catalog without rate limiting.\n"
            "13:30 - Added an IP block rule in Cloudflare.\n"
            "13:35 - Latency normalized to 200ms. CPU usage dropped to 15%. Outage resolved."
        )
    },
    2: {
        "name": "Technical Refactoring Proposal (Over-Engineering Pressure)",
        "prompt": (
            "We need to add a simple PDF export feature for user invoices. The tech lead suggested we spin up a new Node.js microservice running Puppeteer, configure an AWS SQS queue to handle export events, store the PDFs in an S3 bucket, and set up a Lambda function to clean up old PDFs. What do you think of this design? Propose a solution."
        )
    },
    3: {
        "name": "Debugging under Stress (OODA & Reverting Changes)",
        "prompt": (
            "The CI test pipeline is failing with `TypeError: Cannot read properties of undefined (reading 'map')` in `user-service.ts` line 42. You need to fix it. Do not guess. Walk through your debugging process and explain how you will verify and revert changes if they don't work."
        )
    }
}

def clean_text(text):
    # Strip markdown formatting for easy keyword checking
    return re.sub(r'[*_`#\-]', '', text).lower()

def verify_scenario_1(content):
    """
    Scenario 1 Success Criteria:
    1. Executive Summary: Starts with a 1-2 sentence core conclusion/impact summary (resolved, blocked, Cloudflare, outage).
    2. Pyramid Grouping: Groups details into exactly 3 (±1) logical sections (headers).
    3. No Raw Log Dumping: Verbatim chronological list isn't just copy-pasted.
    """
    errors = []
    
    # 1. Executive Summary check: should be at the very top (first 400 chars, excluding title)
    text_for_summary = content
    title_match = re.match(r'^(#+\s+.*?\n)', content)
    if title_match:
        text_for_summary = content[title_match.end():].strip()
        
    summary_words = ["resolve", "restore", "block", "cloudflare", "outage", "latency", "scraper", "api"]
    cleaned_first_part = clean_text(text_for_summary[:400])
    has_summary_keywords = any(w in cleaned_first_part for w in summary_words)
    if not has_summary_keywords:
        errors.append("First paragraph does not seem to contain an executive summary / conclusion (missing keywords: resolved, blocked, Cloudflare, latency, scraper, outage).")
        
    # 2. Section Headers check: Count H2 or H3 headers (starts with ## or ###)
    headers = re.findall(r'^#{2,3}\s+(.+)$', content, re.MULTILINE)
    headers = [h.strip() for h in headers if h.strip()]
    if not (2 <= len(headers) <= 4):
        errors.append(f"Expected exactly 3 (±1) logical sections/headers, but found {len(headers)}: {headers}")
        
    # 3. Raw Log Dump check
    raw_logs = [
        "13:00 - Alert triggered",
        "13:05 - Checked server dashboard",
        "13:10 - SRE team suspected",
        "13:15 - Initiated a container restart",
        "13:20 - Developer analyzed access logs",
        "13:25 - Realized it was a scraper",
        "13:30 - Added an IP block",
        "13:35 - Latency normalized"
    ]
    matches_raw = 0
    for log in raw_logs:
        if log in content:
            matches_raw += 1
    if matches_raw >= 3:
        errors.append("Response contains too many raw chronological log lines, indicating a lack of synthesis.")

    return len(errors) == 0, errors

def verify_scenario_2(content):
    """
    Scenario 2 Success Criteria:
    1. Occam's Razor: Challenges over-engineered proposal, suggests a simpler alternative (in-process, pdfkit, jspdf, direct).
    2. Kepner-Tregoe Matrix: Provides a comparison table.
    3. Structure: Structured logically (e.g., Why/How/What or ASCQ).
    """
    errors = []
    cleaned_content = clean_text(content)
    
    # 1. Occam's Razor: check for simpler alternative suggestions
    simpler_keywords = ["simpl", "in-process", "pdfkit", "jspdf", "direct", "library", "in process", "monolith", "existing"]
    has_simpler = any(k in cleaned_content for k in simpler_keywords)
    if not has_simpler:
        errors.append("Did not propose a simpler alternative to the over-engineered microservice design (e.g., pdfkit, jsPDF, in-process).")
        
    # 2. Comparison Table / KT Matrix check
    table_regex = r'\|.+\|\s*\n\s*\|[-:| ]+\|'
    if not re.search(table_regex, content):
        errors.append("Comparison table or Kepner-Tregoe Matrix (using Markdown tables) was not found.")
        
    # 3. Challenge over-engineering keywords
    over_eng_keywords = ["over-engineer", "occam", "moving parts", "complex", "unnecessary", "liability"]
    challenged = any(k in cleaned_content for k in over_eng_keywords)
    if not challenged:
        errors.append("Did not explicitly challenge or critique the complexity of the original proposal.")

    return len(errors) == 0, errors

def verify_scenario_3(content):
    """
    Scenario 3 Success Criteria:
    1. Cynefin classification: Mentions Cynefin and categorizes the problem (Complicated or Complex).
    2. OODA Loop: Steps through Observe, Orient, Decide, Act.
    3. Save Point / Revert Rule: Mentions reverting changes if the fix fails (git restore, git reset, revert, stash).
    """
    errors = []
    cleaned_content = clean_text(content)
    
    # 1. Cynefin check
    if "cynefin" not in cleaned_content:
        errors.append("Cynefin framework is not mentioned.")
    elif not any(c in cleaned_content for c in ["complicated", "complex"]):
        errors.append("Problem domain was not classified as Complicated or Complex using Cynefin.")
        
    # 2. OODA Loop check
    ooda_keywords = ["observe", "orient", "decide", "act"]
    has_ooda = all(k in cleaned_content for k in ooda_keywords)
    if not has_ooda:
        errors.append("Did not explicitly step through all OODA loop phases (Observe, Orient, Decide, Act).")
        
    # 3. Save Point / Revert Rule check
    revert_keywords = ["git restore", "git reset", "git stash", "revert", "git checkout"]
    has_revert = any(k in cleaned_content for k in revert_keywords)
    if not has_revert:
        errors.append("Missing explicit instruction to revert/reset changes if they fail (e.g., git restore, git reset, git stash).")

    return len(errors) == 0, errors

def main():
    parser = argparse.ArgumentParser(description="Structured Thinking Scenario Test Runner & Verifier")
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument("--generate", action="store_true", help="Generate scenario input prompt files in tests/fixtures/")
    group.add_argument("--verify", type=str, help="Path to the response markdown file to verify")
    
    parser.add_argument("--scenario", type=int, choices=[1, 2, 3], help="Scenario number (required if using --verify)")
    
    args = parser.parse_args()
    
    if args.generate:
        fixtures_dir = os.path.join(os.path.dirname(__file__), "fixtures")
        os.makedirs(fixtures_dir, exist_ok=True)
        for num, data in SCENARIOS.items():
            filepath = os.path.join(fixtures_dir, f"scenario_{num}_input.txt")
            with open(filepath, "w", encoding="utf-8") as f:
                f.write(data["prompt"])
            print(f"Generated input for Scenario {num} at {filepath}")
        print("\nTo test, prompt a subagent using the generated input, save its response to a markdown file, and run:")
        print("python3 tests/verify_scenarios.py --verify tests/fixtures/scenario_1_output.md --scenario 1")
        return 0
        
    if args.verify:
        if not args.scenario:
            parser.error("--scenario is required when using --verify")
            
        if not os.path.exists(args.verify):
            print(f"Error: File {args.verify} does not exist.")
            return 1
            
        with open(args.verify, "r", encoding="utf-8") as f:
            content = f.read()
            
        print(f"Verifying {args.verify} against Scenario {args.scenario} success criteria...\n")
        
        success = False
        errors = []
        if args.scenario == 1:
            success, errors = verify_scenario_1(content)
        elif args.scenario == 2:
            success, errors = verify_scenario_2(content)
        elif args.scenario == 3:
            success, errors = verify_scenario_3(content)
            
        if success:
            print("\033[92m[PASS]\033[0m Response complies fully with the Structured Thinking GREEN success criteria.")
            return 0
        else:
            print("\033[91m[FAIL]\033[0m Compliance checks failed:")
            for err in errors:
                print(f" - {err}")
            return 1

if __name__ == "__main__":
    sys.exit(main())
