# SIEM Engineer #08 — Automation & SOAR

## 🟢 Introduction

A modern SOC may receive hundreds or thousands of alerts every day.

Analysts cannot manually perform every repetitive task.

For example:

```text
SIEM Alert
   ↓
Extract IP
   ↓
Check Threat Intelligence
   ↓
Enrich Alert
   ↓
Create Ticket
   ↓
Notify Analyst
```

Doing this manually for every alert takes time.

This is where **Automation** and **SOAR** become important.

**SOAR = Security Orchestration, Automation and Response**

The main idea is:

> **Automate repetitive tasks so analysts can spend more time on complex investigations.**

---

# 🧠 1. What is SOAR?

SOAR is a security technology and operational approach that connects security tools, automates workflows, and supports incident response.

A simple architecture:

```text
SIEM
 ↓
SOAR
 ↓
Threat Intelligence
 ↓
EDR
 ↓
Firewall
 ↓
Ticketing
 ↓
Notification
```

Instead of analysts manually switching between many tools, SOAR can coordinate the workflow.

---

# 🎯 2. Why Automation Matters in SOC

Imagine:

```text
100 Alerts
```

For every alert, an analyst manually:

```text
Copy IP
 ↓
Threat Intelligence Lookup
 ↓
Copy Result
 ↓
Update Ticket
 ↓
Send Message
```

This creates:

==> Repetitive work

==> Human error

==> Slow response

==> Analyst fatigue

Automation can reduce these repetitive activities.

---

# ⚙️ 3. Automation vs SOAR

These concepts are related but not exactly identical.

### Automation

A system performs a predefined task automatically.

Example:

```text
Extract IP
 ↓
Threat Intelligence Lookup
```

### SOAR

Coordinates multiple tools and actions into a broader security workflow.

Example:

```text
SIEM Alert
 ↓
Enrich IOC
 ↓
Create Case
 ↓
Notify Analyst
 ↓
Request Approval
 ↓
Contain
 ↓
Update Case
```

---

# 🔗 4. What is Orchestration?

**Orchestration** means coordinating multiple systems and actions.

Example:

```text
SIEM
  ↕
SOAR
  ↕
Threat Intelligence
  ↕
Firewall
  ↕
EDR
  ↕
Ticketing
```

The SOAR platform acts as the workflow coordinator.

---

# 🔄 5. Basic SOAR Architecture

A typical workflow:

```text
Security Event
      ↓
SIEM
      ↓
Detection
      ↓
Alert
      ↓
SOAR
      ↓
Playbook
      ↓
Enrichment
      ↓
Decision
      ↓
Response
      ↓
Case Update
```

---

# 📋 6. What is a Playbook?

A **Playbook** is an automated or semi-automated workflow for handling a specific security scenario.

Example:

### Suspicious IP Playbook

```text
Alert Received
      ↓
Extract IP
      ↓
Threat Intelligence Lookup
      ↓
Check Reputation
      ↓
Check Internal History
      ↓
Update Alert
      ↓
Notify Analyst
```

Another example:

### Phishing Playbook

```text
Phishing Alert
      ↓
Extract URL
      ↓
Extract Domain
      ↓
Extract Attachment Hash
      ↓
Threat Intelligence Lookup
      ↓
Enrich Case
      ↓
Notify SOC
```

---

# 🧩 7. Runbook vs Playbook

These terms can vary by organization.

Generally:

### Runbook

Human-readable operational instructions.

```text
Step 1
Step 2
Step 3
```

### Playbook

A broader workflow that can include:

```text
Automation
Decision
Tools
Analyst Approval
Response
Documentation
```

Example:

```text
Runbook:
How to investigate suspicious IP

Playbook:
Automatically enrich suspicious IP
and create an investigation case.
```

---

# 🚨 8. Alert Automation

Suppose a SIEM generates:

```text
Suspicious IP Alert
```

SOAR can automatically:

```text
1. Extract IP
2. Lookup intelligence
3. Find previous SIEM activity
4. Identify affected hosts
5. Create case
6. Add enrichment
7. Notify analyst
```

The analyst receives a more complete alert.

---

# 🧠 9. Enrichment Automation

Enrichment means adding additional information.

Example:

```text
IOC:
203.x.x.x
```

Automation can query an approved intelligence source and add:

```text
Reputation
Source
Confidence
First Seen
Last Seen
Related Information
```

Then:

```text
Raw Alert
+
Enrichment
=
Context-Rich Alert
```

---

# 🔍 10. Automated Investigation

Automation can perform repetitive investigation tasks.

Example:

```text
Alert
 ↓
Extract User
 ↓
Search Authentication History
 ↓
Search Endpoint Activity
 ↓
Search Network Activity
 ↓
Collect Results
 ↓
Update Case
```

This does not necessarily replace the analyst.

Instead, it gives the analyst useful context faster.

---

# 🎫 11. Automatic Ticket Creation

A SOAR workflow can create a ticket automatically.

Example:

```text
SIEM Alert
 ↓
SOAR
 ↓
Case Creation
```

Ticket fields:

```text
Title
Severity
Priority
User
Host
Source IP
Detection
Timestamp
Evidence
Status
```

This reduces manual data entry.

---

# 📢 12. Notification Automation

SOAR can notify the appropriate team.

Examples:

```text
SIEM
 ↓
SOAR
 ↓
Email
```

or:

```text
SIEM
 ↓
SOAR
 ↓
Chat / Collaboration Platform
```

or:

```text
SIEM
 ↓
SOAR
 ↓
Incident Management System
```

Notifications should contain enough context to be useful.

---

# 🛑 13. Automated Response

Some actions can be automated.

Examples may include:

==> Disable a compromised account

==> Isolate an endpoint

==> Block an indicator

==> Revoke a session

==> Create a firewall block

==> Add an IOC to a security control

But automated response requires careful design.

---

# ⚠️ 14. Why Automated Response Is Risky

Suppose the SIEM incorrectly identifies an IP as malicious.

Automation:

```text
Alert
 ↓
Automatic Firewall Block
```

could accidentally block a legitimate service.

Therefore:

```text
Detection
 ↓
Validation
 ↓
Confidence
 ↓
Approval / Policy
 ↓
Response
```

may be more appropriate for higher-impact actions.

---

# 👤 15. Human-in-the-Loop

A **Human-in-the-Loop** workflow requires analyst approval before a potentially disruptive action.

Example:

```text
Alert
 ↓
Enrichment
 ↓
High Confidence
 ↓
Request Approval
 ↓
Analyst Approves
 ↓
Containment
```

This is useful when an automated action could affect business operations.

---

# 🟢 16. Fully Automated vs Semi-Automated

### Fully Automated

```text
Alert
 ↓
Decision
 ↓
Action
```

Useful for low-risk, well-understood tasks.

### Semi-Automated

```text
Alert
 ↓
Enrichment
 ↓
Recommendation
 ↓
Analyst Approval
 ↓
Action
```

Useful for actions with higher operational impact.

---

# 🧠 17. Automation Decision Matrix

A SOC can classify actions by risk.

| Action                     | Automation Approach     |
| -------------------------- | ----------------------- |
| Extract IOC                | Automatic               |
| Threat Intelligence Lookup | Automatic               |
| Case Creation              | Automatic               |
| Alert Enrichment           | Automatic               |
| Analyst Notification       | Automatic               |
| Endpoint Isolation         | Approval / Policy-based |
| Account Disable            | Approval / Policy-based |
| Firewall Block             | Approval / Policy-based |
| Production System Shutdown | Strong authorization    |

The exact policy depends on the organization.

---

# 🔌 18. APIs in SOAR

APIs are extremely important.

A SOAR platform may communicate with:

```text
SIEM API
EDR API
Firewall API
Threat Intelligence API
Ticketing API
Identity API
Email API
Cloud API
```

Example:

```text
SOAR
 ↓
GET /indicator/203.x.x.x
 ↓
Threat Intelligence
 ↓
Result
 ↓
SOAR
```

Then:

```text
SOAR
 ↓
POST /cases
 ↓
Ticketing System
```

---

# 🔐 19. API Authentication

Automation requires secure authentication.

Common methods include:

==> API Keys

==> OAuth

==> Service Accounts

==> Bearer Tokens

==> Client Certificates

Secrets should be stored securely.

Never put sensitive credentials directly inside source code or public repositories.

---

# 🚦 20. API Rate Limits

External APIs may have rate limits.

Example:

```text
100 requests/minute
```

If the SOAR platform suddenly sends:

```text
1,000 requests/minute
```

the API may reject requests.

Automation should handle:

==> Rate limits

==> Retries

==> Backoff

==> Timeouts

==> API errors

==> Duplicate requests

---

# 🔄 21. Retry Logic

Suppose:

```text
Threat Intelligence API
      ↓
Temporary Failure
```

The automation should not immediately fail the entire incident workflow.

A controlled retry strategy can be:

```text
Request
 ↓
Failure
 ↓
Wait
 ↓
Retry
 ↓
Success / Failure Handling
```

Avoid infinite retries.

---

# 🧹 22. Idempotency

Automation should avoid performing the same action repeatedly.

Example:

```text
Block IP
```

If the same alert triggers five times, the system should not create five duplicate actions unnecessarily.

A good workflow checks:

```text
Already Blocked?
Already Ticketed?
Already Enriched?
Already Isolated?
```

This concept is called **idempotency**.

---

# 🔁 23. Duplicate Alert Handling

Suppose:

```text
100 identical alerts
```

Without aggregation:

```text
100 tickets
```

With proper logic:

```text
100 alerts
      ↓
Correlation / Deduplication
      ↓
1 Case
```

This reduces unnecessary workload.

---

# 📊 24. Automation Metrics

A SOC should measure automation.

Useful metrics include:

==> Number of automated workflows

==> Automation success rate

==> Automation failure rate

==> Average execution time

==> Manual effort reduced

==> Number of enriched alerts

==> Number of duplicate cases prevented

==> Analyst approval rate

==> Rollback/failure incidents

Metrics should help identify whether automation is actually improving operations.

---

# 🧪 25. Testing Automation

Never deploy automation directly into production without testing.

Test:

```text
Success
Failure
Timeout
Invalid Input
Duplicate Event
API Rate Limit
Missing Field
Permission Error
```

Example:

```text
Input:
IP = 203.x.x.x

Expected:
Threat Intelligence lookup

API Failure:
Retry

Repeated Alert:
No duplicate case

Invalid IP:
Graceful error
```

---

# 🧰 26. Automation Development Lifecycle

Use:

```text
Requirement
 ↓
Design
 ↓
Build
 ↓
Unit Test
 ↓
Integration Test
 ↓
Security Review
 ↓
Pilot
 ↓
Production
 ↓
Monitor
 ↓
Improve
```

This is similar to software engineering.

---

# 🧑‍💻 27. Detection + SOAR

Detection Engineering and SOAR work together.

Example:

```text
Detection
 ↓
Alert
 ↓
SOAR Playbook
 ↓
Enrichment
 ↓
Response
```

A detection answers:

> **“What happened?”**

SOAR helps answer:

> **“What should happen next?”**

---

# 🛡️ 28. Example — Suspicious IP Workflow

Suppose the SIEM detects:

```text
Internal Host
      ↓
Suspicious External IP
```

SOAR workflow:

```text
1. Receive Alert
2. Extract IP
3. Validate IP Format
4. Threat Intelligence Lookup
5. Search Historical Activity
6. Identify Affected Host
7. Enrich Case
8. Assign Priority
9. Notify Analyst
10. Request Approval if Containment Is Required
11. Record Action
```

This can significantly reduce repetitive analyst work.

---

# 📧 29. Example — Phishing Workflow

A phishing alert arrives.

SOAR can:

```text
Email Alert
 ↓
Extract Sender
 ↓
Extract URLs
 ↓
Extract Domains
 ↓
Extract Hashes
 ↓
Threat Intelligence
 ↓
Search Similar Emails
 ↓
Identify Recipients
 ↓
Create Case
 ↓
Notify SOC
```

If organizational policy allows, further response actions can be performed after validation and authorization.

---

# 🔑 30. Example — Compromised Account Workflow

Suppose there is strong evidence that an account may be compromised.

Workflow:

```text
SIEM Alert
 ↓
Identify User
 ↓
Search Login History
 ↓
Check Endpoint Activity
 ↓
Check Risk Context
 ↓
Create Case
 ↓
Notify Analyst
 ↓
Approval
 ↓
Session Revocation / Account Action
 ↓
Document
```

High-impact identity actions should have strong authorization controls.

---

# 🌐 31. Example — Malware Alert Workflow

Endpoint generates:

```text
Suspicious File Detection
```

SOAR can:

```text
Extract Hash
 ↓
Threat Intelligence Lookup
 ↓
Search Other Endpoints
 ↓
Check Related Network Events
 ↓
Create Case
 ↓
Notify Analyst
 ↓
Recommend Containment
```

This helps determine whether the event is isolated or widespread.

---

# 🧠 32. SOAR and Threat Intelligence

Threat Intelligence is one of the easiest areas to automate.

```text
Alert
 ↓
Extract IOC
 ↓
Threat Intelligence API
 ↓
Reputation
 ↓
Confidence
 ↓
Context
 ↓
Update Case
```

This can happen in seconds instead of requiring manual lookups.

---

# 📈 33. SOAR and Threat Hunting

SOAR can also automate predefined searches.

Example:

```text
IOC Discovered
 ↓
Search SIEM
 ↓
Search DNS
 ↓
Search Proxy
 ↓
Search EDR
 ↓
Aggregate Results
 ↓
Create Investigation Case
```

This is especially useful when the same investigation steps are repeated frequently.

---

# 🧩 34. SOAR Error Handling

Every automation workflow should expect failures.

Possible failures:

```text
SIEM unavailable
API unavailable
Invalid token
Timeout
Rate limit
Missing data
Permission denied
Unexpected response
```

Good automation should:

==> Detect the failure

==> Record the error

==> Retry when appropriate

==> Avoid destructive assumptions

==> Notify the responsible team

==> Continue safely when possible

---

# 🔐 35. SOAR Security

SOAR has powerful permissions.

Therefore protect it carefully.

Use:

==> RBAC

==> MFA

==> Least privilege

==> Secure secret storage

==> API access controls

==> Audit logging

==> Approval workflows

==> Change management

==> Network restrictions

A compromised SOAR platform could potentially affect multiple security systems.

---

# 📝 36. Audit Logging

Every important automated action should be traceable.

Record:

```text
Who triggered it?
What automation ran?
When?
Which API?
What action?
What result?
What error?
Who approved it?
```

Example:

```text
Action:
Firewall Block

Trigger:
SIEM Alert #1024

Automation:
Suspicious-IP Playbook

Approval:
SOC Analyst

Time:
14:32

Result:
Success
```

---

# 🔄 37. Rollback

Some automated actions should have rollback capability.

Example:

```text
Firewall Block
 ↓
False Positive Identified
 ↓
Rollback
 ↓
Remove Block
 ↓
Document
```

Rollback capability is especially important for actions that can disrupt business operations.

---

# 🧠 38. Human Approval Workflow

A mature workflow may look like:

```text
Detection
 ↓
SOAR
 ↓
Enrichment
 ↓
Risk Evaluation
 ↓
Analyst Approval
 ↓
Response
 ↓
Verification
 ↓
Documentation
```

This balances:

**Automation + Human Judgment**

---

# 📋 39. Playbook Documentation

Every important playbook should document:

```text
Playbook Name
Purpose
Trigger
Required Data
Actions
APIs
Permissions
Conditions
Approval Requirements
Failure Handling
Rollback
Logging
Owner
Version
Last Review
```

This makes automation maintainable.

---

# 🧪 40. Practical SOAR Lab

You can create a small lab with:

```text
Wazuh / SIEM
+
Threat Intelligence
+
Python
+
Webhook / REST API
+
Ticketing System
```

### Lab 1 — IOC Enrichment

```text
SIEM Alert
 ↓
Extract IP
 ↓
API Lookup
 ↓
Add Result
```

### Lab 2 — Automatic Case Creation

```text
SIEM Alert
 ↓
Webhook
 ↓
Create Ticket
```

### Lab 3 — Notification

```text
High-Priority Alert
 ↓
Automation
 ↓
SOC Notification
```

### Lab 4 — Approval-Based Response

```text
Alert
 ↓
Enrichment
 ↓
Analyst Approval
 ↓
Authorized Response
```

---

# 📊 41. SOC Automation Architecture

A practical architecture:

```text
             ┌──────────────┐
             │     SIEM     │
             └──────┬───────┘
                    ↓
             ┌──────────────┐
             │     SOAR     │
             └──────┬───────┘
                    ↓
       ┌────────────┼────────────┐
       ↓            ↓            ↓
 Threat Intel     EDR        Ticketing
       ↓            ↓            ↓
       └────────────┼────────────┘
                    ↓
             SOC Analyst
                    ↓
             Response Action
```

The SOAR layer coordinates the workflow.

---

# ⚡ 42. Automation Maturity

Automation can mature gradually.

### Level 1

Manual investigation.

```text
Analyst does everything.
```

### Level 2

Automated enrichment.

```text
Alert → IOC Lookup
```

### Level 3

Automated case management.

```text
Alert → Enrichment → Ticket
```

### Level 4

Semi-automated response.

```text
Alert → Enrichment → Analyst Approval → Action
```

### Level 5

Controlled automated response.

```text
Alert → Validation → Policy → Automated Action
```

The organization should decide which level is appropriate for each use case.

---

# 🚫 43. Common SOAR Mistakes

### Mistake 1 — Automating Everything

Not every task should be automated.

### Mistake 2 — No Error Handling

APIs will fail.

### Mistake 3 — Excessive Permissions

SOAR should follow least privilege.

### Mistake 4 — No Approval

High-impact actions may require human approval.

### Mistake 5 — No Logging

Every important action should be auditable.

### Mistake 6 — No Rollback

Some actions need recovery mechanisms.

### Mistake 7 — No Testing

Untested automation can create operational problems.

### Mistake 8 — Duplicate Actions

Automation must handle repeated alerts safely.

---

# 📋 44. SOAR Checklist

```text
[ ] Define automation objective

[ ] Identify repetitive task

[ ] Define trigger

[ ] Identify required data

[ ] Identify APIs

[ ] Configure authentication

[ ] Apply least privilege

[ ] Build workflow

[ ] Add validation

[ ] Add error handling

[ ] Add retry logic

[ ] Handle duplicates

[ ] Add approval where required

[ ] Add audit logging

[ ] Add rollback where appropriate

[ ] Test success path

[ ] Test failure path

[ ] Test API timeout

[ ] Test invalid input

[ ] Test duplicate alert

[ ] Deploy gradually

[ ] Monitor performance

[ ] Review regularly
```

---

# 🔄 45. Complete SOAR Flow

Remember:

```text
Security Event
      ↓
SIEM Detection
      ↓
Alert
      ↓
SOAR Trigger
      ↓
Data Extraction
      ↓
Enrichment
      ↓
Correlation
      ↓
Decision
      ↓
Human Approval if Required
      ↓
Response
      ↓
Verification
      ↓
Case Update
      ↓
Audit Log
      ↓
Lessons Learned
```

---

# 🎤 46. SIEM Engineer Interview Questions

### Q1. What is SOAR?

**Answer:**

SOAR stands for Security Orchestration, Automation and Response. It connects security tools and automates or coordinates repetitive security workflows and response processes.

---

### Q2. What is a SOAR playbook?

**Answer:**

A playbook is a predefined workflow that describes the steps, decisions, integrations, and actions used to handle a specific security scenario.

---

### Q3. What is orchestration?

**Answer:**

Orchestration means coordinating multiple security tools and systems so they can work together as part of a single workflow.

---

### Q4. Why is automation important in a SOC?

**Answer:**

Automation reduces repetitive manual work, improves response speed, standardizes workflows, and allows analysts to focus on more complex investigations.

---

### Q5. Should every response action be automated?

**Answer:**

No. Low-risk and repetitive actions can often be automated, while high-impact actions may require validation, policy controls, or analyst approval.

---

### Q6. What is human-in-the-loop automation?

**Answer:**

It is a workflow where automation performs investigation or enrichment but waits for human approval before executing a potentially high-impact action.

---

### Q7. How do you secure a SOAR platform?

**Answer:**

Use least privilege, RBAC, MFA, secure secret storage, API access controls, audit logging, network restrictions, approval workflows, and strong change management.

---

### Q8. How do you handle API failures in automation?

**Answer:**

I would implement timeout handling, controlled retries, backoff, error logging, rate-limit handling, validation of responses, and safe failure behavior.

---

### Q9. What is idempotency in automation?

**Answer:**

Idempotency means repeating the same operation does not create unwanted duplicate effects. For example, repeated alerts should not unnecessarily create multiple identical firewall blocks or tickets.

---

### Q10. How would you automate suspicious IP investigation?

**Answer:**

I would trigger the workflow from the SIEM, extract and validate the IP, perform approved Threat Intelligence enrichment, search historical SIEM activity, identify affected hosts, update the case, and notify the analyst. Any containment action would follow organizational authorization requirements.

---

### Q11. What should be included in a SOAR playbook?

**Answer:**

The playbook should define the trigger, required data, actions, integrations, permissions, conditions, approval requirements, error handling, logging, rollback where appropriate, owner, and version.

---

### Q12. How do you test a SOAR workflow?

**Answer:**

I test normal execution as well as API failures, timeouts, invalid inputs, missing fields, duplicate alerts, permission errors, rate limits, and rollback or recovery scenarios where applicable.

---

# 🧠 47. Important Lessons

### 1️⃣ Automation should solve a problem

Don't automate simply because you can.

### 2️⃣ Automate repetitive work first

Start with:

```text
Enrichment
Ticket Creation
Notification
Data Collection
```

### 3️⃣ High-impact actions need control

Use:

```text
Validation
+
Policy
+
Approval
```

when appropriate.

### 4️⃣ Automation must be observable

You should always know:

```text
What happened?
When?
Why?
Who approved it?
Did it succeed?
```

### 5️⃣ SOAR is not a replacement for analysts

SOAR handles repetitive workflows.

Analysts provide:

```text
Context
Judgment
Investigation
Decision-making
```

---

# 🚀 48. Final Takeaway

A modern SIEM Engineer should understand how SIEM connects with automation.

The complete concept is:

**SIEM → Detection → SOAR → Enrichment → Decision → Response → Documentation**

Important skills include:

==> REST API

==> Webhooks

==> Python automation

==> Playbooks

==> Threat Intelligence integration

==> Ticketing integration

==> Error handling

==> Authentication

==> RBAC

==> Approval workflows

==> Audit logging

==> Rollback

==> Automation testing

The goal is not:

> **“Automate everything.”**

The goal is:

> **“Automate the right things safely.”**

---


---

## 📚 SIEM Engineer Learning Series

**#01 — Log Management**

**#02 — SIEM Platforms**

**#03 — Log Integration**

**#04 — Detection Engineering**

**#05 — Query & Investigation**

**#06 — SOC Operations**

**#07 — Threat Intelligence**

**#08 — Automation & SOAR ← You are here**

**#09 — Dashboard & Reporting → Next**

**#10 — SIEM Infrastructure**

**#11 — SIEM Architecture Design**

**#12 — SIEM Capacity Planning**

**#13 — SIEM Performance Tuning**

**#14 — Advanced Detection Engineering**

**#15 — Threat Hunting with SIEM**

**#16 — SIEM Data Quality & Troubleshooting**

**#17 — Hands-On SIEM: Multi-Platform Practical Guide**

---

### Navigation

**← Previous Article: #07 — Threat Intelligence**

**SIEM Engineer Index**

**Next Article: #09 — Dashboard & Reporting →**

---

