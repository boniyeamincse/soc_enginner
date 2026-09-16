# SIEM Engineer #06 — SOC Operations

## 🟢 Introduction

A SIEM can generate thousands of alerts.

But an alert by itself is not an incident.

A SOC team needs a structured process to understand:

==> What happened?

==> Is the alert valid?

==> Which user or system is affected?

==> What is the scope?

==> What action should be taken?

==> Does the incident need escalation?

This is where **SOC Operations** becomes important.

The core SOC workflow is:

**Detect → Validate → Investigate → Contain → Eradicate → Recover → Document**

A SIEM Engineer works closely with SOC Analysts to make this workflow effective.

---

# 🧠 1. What is SOC Operations?

**SOC Operations** means the day-to-day process of monitoring, detecting, investigating, responding to, and documenting cybersecurity events and incidents.

A typical SOC contains:

```text id="soc01"
Security Logs
      ↓
SIEM
      ↓
Detection Rules
      ↓
Alerts
      ↓
SOC Analyst
      ↓
Investigation
      ↓
Incident Response
      ↓
Resolution
      ↓
Documentation
```

The SOC continuously monitors the organization's security environment.

---

# 🎯 2. Main Responsibilities of a SOC

A SOC generally performs activities such as:

==> Security monitoring

==> Alert triage

==> Incident investigation

==> Threat detection

==> Threat hunting

==> Incident response

==> Threat intelligence enrichment

==> Vulnerability awareness

==> Security reporting

==> Detection tuning

==> Incident documentation

==> Continuous improvement

---

# 🏢 3. SOC Team Structure

A traditional SOC may have several levels.

```text id="soc02"
L1 Analyst
   ↓
L2 Analyst
   ↓
L3 Analyst
   ↓
SOC Engineer / Detection Engineer
   ↓
Incident Response / Threat Hunting
```

The exact structure varies between organizations.

---

# 👨‍💻 4. SOC L1 Analyst

L1 usually focuses on initial alert handling.

Responsibilities can include:

==> Monitor alerts

==> Validate alerts

==> Perform initial investigation

==> Identify false positives

==> Collect basic evidence

==> Follow runbooks

==> Escalate complex incidents

Example:

```text id="soc03"
SIEM Alert
    ↓
L1 Analyst
    ↓
Validate
    ↓
Initial Investigation
    ↓
Close / Escalate
```

---

# 🧑‍💻 5. SOC L2 Analyst

L2 generally performs deeper investigation.

Responsibilities may include:

==> Advanced log analysis

==> Correlation

==> Threat hunting

==> Incident scoping

==> Root-cause investigation

==> Detection tuning

==> Supporting containment

==> L1 guidance

Example:

```text id="soc04"
L1 Escalation
      ↓
L2 Investigation
      ↓
Deep Analysis
      ↓
Scope
      ↓
Containment Recommendation
```

---

# 🧑‍🔬 6. SOC L3 / Senior Security Roles

L3-level work may involve:

==> Advanced threat hunting

==> Malware analysis

==> Detection engineering

==> Incident response

==> Advanced forensic analysis

==> Complex attack-chain investigation

==> Security architecture

==> Engineering improvements

Not every organization uses the same L1/L2/L3 structure.

---

# ⚙️ 7. SIEM Engineer in SOC Operations

A SIEM Engineer is not simply a person who manages a SIEM server.

They may be responsible for:

==> Log onboarding

==> Parser management

==> Detection rules

==> Correlation rules

==> Alert quality

==> SIEM health

==> Query performance

==> Dashboards

==> Integrations

==> Automation

==> Data retention

==> Troubleshooting

==> Detection coverage

The SIEM Engineer enables analysts to work effectively.

---

# 🚨 8. Event vs Alert vs Incident

These terms are often confused.

## Event

An event is a recorded activity.

Example:

```text id="soc05"
User login failed
```

## Alert

An alert is generated when a detection identifies activity that meets defined conditions.

```text id="soc06"
Multiple failed logins
        ↓
Detection Rule
        ↓
Alert
```

## Incident

An incident is a security case requiring investigation and potentially response.

```text id="soc07"
Multiple alerts
      +
Evidence
      +
Impact / Risk
      ↓
Security Incident
```

An alert does not automatically mean an incident.

---

# 🔄 9. SOC Alert Lifecycle

A practical alert lifecycle is:

```text id="soc08"
Alert Created
      ↓
Assigned
      ↓
Triaged
      ↓
Validated
      ↓
Investigated
      ↓
Verdict
      ↓
Escalated / Contained / Closed
      ↓
Documented
```

This workflow should be clearly defined inside a SOC.

---

# 🔎 10. Step 1 — Detect

The SIEM identifies suspicious activity.

Example:

```text id="soc09"
20 failed logins
from same source IP
within 5 minutes
```

Detection rule:

```text id="soc10"
Authentication Failure
+
Threshold
+
Time Window
```

Result:

```text id="soc11"
Security Alert
```

---

# ✅ 11. Step 2 — Validate

The analyst checks whether the alert is valid.

Questions:

==> Did the event actually occur?

==> Are the logs correct?

==> Is the source known?

==> Is the user legitimate?

==> Is this expected administrative activity?

==> Is the detection working correctly?

Validation prevents analysts from spending unnecessary time on bad data or broken detections.

---

# 🔍 12. Step 3 — Investigate

After validation, investigate the activity.

Look at:

```text id="soc12"
User
Source IP
Destination
Host
Process
Timestamp
Authentication
Network Activity
Related Alerts
Threat Intelligence
```

Then build the timeline.

```text id="soc13"
Before
  ↓
During
  ↓
After
```

---

# 🧭 13. Step 4 — Determine Scope

One of the most important SOC questions is:

> **“How much of the environment is affected?”**

Check:

==> One user?

==> Multiple users?

==> One host?

==> Multiple hosts?

==> One IP?

==> Multiple IPs?

==> One application?

==> Multiple applications?

Example:

```text id="soc14"
Alert
 ↓
Host A
 ↓
User A
 ↓
Host B
 ↓
User B
```

The scope may be larger than the original alert.

---

# 🛑 14. Step 5 — Contain

Containment attempts to limit further impact.

Depending on the incident and organizational procedures, actions may include:

==> Isolating an affected endpoint

==> Blocking a malicious network indicator

==> Disabling a compromised account

==> Revoking sessions

==> Restricting network access

==> Applying emergency firewall controls

Containment should be authorized and carefully documented.

---

# 🧹 15. Step 6 — Eradicate

Eradication means removing the cause or malicious artifacts from the environment.

Examples can include:

==> Removing malicious persistence

==> Removing unauthorized accounts

==> Removing malicious files

==> Patching exploited vulnerabilities

==> Rotating compromised credentials

==> Removing unauthorized configurations

The exact action depends on the incident.

---

# 🔄 16. Step 7 — Recover

Recovery returns affected systems to normal operation.

Activities may include:

==> Restoring systems

==> Rebuilding compromised hosts

==> Restoring clean backups

==> Validating security controls

==> Monitoring affected systems

==> Confirming normal operation

Recovery should not simply mean:

```text id="soc15"
System is working
```

You should also confirm:

```text id="soc16"
System is secure
+
Monitoring is active
+
Root cause is addressed
```

---

# 📝 17. Step 8 — Document

Documentation is a critical SOC responsibility.

Record:

```text id="soc17"
What happened?
When?
Which system?
Which user?
Which IP?
What evidence?
What actions?
Who performed them?
What was the verdict?
What was the impact?
What was the root cause?
What recommendations?
```

A well-documented incident helps future investigations.

---

# 🔥 18. Complete Incident Response Flow

Remember:

```text id="soc18"
Detect
  ↓
Validate
  ↓
Investigate
  ↓
Scope
  ↓
Contain
  ↓
Eradicate
  ↓
Recover
  ↓
Document
  ↓
Lessons Learned
  ↓
Improve Detection
```

This is one of the most important workflows for a SOC Engineer.

---

# 🎯 19. Alert Triage

**Triage** means quickly determining what an alert represents and what should happen next.

During triage, ask:

```text id="soc19"
What triggered the alert?
Who is involved?
Which asset?
When?
Where?
Is it expected?
What is the potential impact?
Is there related activity?
Does it require escalation?
```

The goal is to prioritize investigation appropriately.

---

# 🚦 20. Alert Priority

Organizations may classify alerts using:

```text id="soc20"
Low
Medium
High
Critical
```

But priority should be based on organizational criteria.

Consider:

==> Asset importance

==> User privilege

==> Detection confidence

==> Potential impact

==> Scope

==> Business context

==> Evidence

For example, an alert involving a critical production server may require different handling from an identical alert on a test machine.

---

# 🧠 21. Severity vs Priority vs Confidence

These concepts should not be confused.

### Severity

Potential seriousness of the security activity.

### Confidence

How strongly the evidence supports the detection.

### Priority

How urgently the SOC should handle the case.

Example:

```text id="soc21"
High Severity
+
High Confidence
+
Critical Asset
=
High Investigation Priority
```

The exact prioritization model should be defined by the organization.

---

# 📋 22. Ticket Management

A SOC should track incidents using a case or ticketing system.

A case may contain:

```text id="soc22"
Case ID
Title
Severity
Priority
Status
Assigned Analyst
Affected Asset
Affected User
Detection
Evidence
Timeline
Comments
Actions
Verdict
Resolution
```

Common statuses include:

```text id="soc23"
New
Assigned
In Progress
Waiting
Escalated
Contained
Resolved
Closed
```

---

# 👥 23. Alert Assignment

When an alert is generated:

```text id="soc24"
Alert
 ↓
Queue
 ↓
Analyst Assignment
 ↓
Investigation
```

Assignment can be based on:

==> Shift

==> Analyst skill

==> Severity

==> Workload

==> Incident type

Good assignment prevents important alerts from being ignored.

---

# 🔺 24. Escalation

Escalation is necessary when the current analyst or team needs additional expertise or authority.

Examples:

```text id="soc25"
L1
 ↓
L2
```

or:

```text id="soc26"
SOC
 ↓
Incident Response
```

or:

```text id="soc27"
Security Team
 ↓
Network Team
```

or:

```text id="soc28"
Security Team
 ↓
System Owner
```

Escalation should include useful evidence instead of simply saying:

> “Please investigate.”

---

# 📦 25. Good Escalation Information

A useful escalation should include:

```text id="soc29"
Incident Summary

Detection Name

Timestamp

Affected Host

Affected User

Source IP

Destination IP

Relevant Events

Timeline

Investigation Performed

Evidence

Current Impact

Actions Already Taken

Recommended Next Step
```

This makes the next analyst's job much easier.

---

# 🔬 26. Root Cause Analysis

After an incident, ask:

> **“Why did this happen?”**

Possible causes:

==> Stolen credentials

==> Misconfiguration

==> Vulnerability

==> Weak access control

==> Malicious email

==> Exposed service

==> Insider activity

==> Compromised endpoint

Do not assume the root cause before collecting evidence.

---

# 🧩 27. Attack Chain Analysis

A security incident may contain multiple stages.

For example:

```text id="soc30"
Initial Access
      ↓
Execution
      ↓
Persistence
      ↓
Privilege Escalation
      ↓
Discovery
      ↓
Lateral Movement
      ↓
Collection
      ↓
Command & Control
```

MITRE ATT&CK can help analysts describe observed behaviors using common terminology.

---

# 🛡️ 28. SOC Runbooks

A **runbook** provides predefined instructions for handling common events.

Example:

### Suspicious Login Runbook

```text id="soc31"
1. Validate login event
2. Identify user
3. Identify source IP
4. Check authentication history
5. Check device
6. Check geographic context
7. Check related events
8. Determine whether activity is expected
9. Escalate if required
10. Document findings
```

Runbooks help maintain consistency across analysts and shifts.

---

# ⚙️ 29. Playbook vs Runbook

These terms are sometimes used differently by organizations.

Generally:

### Runbook

Step-by-step operational instructions.

### Playbook

A broader response workflow that can include decisions, automation, people, tools, and actions.

Example:

```text id="soc32"
Alert
 ↓
Playbook
 ↓
Enrichment
 ↓
Decision
 ↓
Containment
 ↓
Ticket Update
```

---

# 🤖 30. Automation in SOC

Automation can reduce repetitive work.

Example:

```text id="soc33"
SIEM Alert
 ↓
Automation
 ↓
Extract IP
 ↓
Threat Intelligence Lookup
 ↓
Enrich Alert
 ↓
Update Ticket
```

Automation should be carefully controlled.

Not every alert should automatically trigger destructive or disruptive actions.

---

# 🧠 31. Analyst Feedback

SOC analysts interact with detections every day.

Their feedback is extremely valuable.

Example:

```text id="soc34"
Detection
 ↓
100 Alerts
 ↓
80 Benign
 ↓
15 Suspicious
 ↓
5 Confirmed
```

The analyst can report:

> “Most alerts are generated by an approved scanner.”

The Detection Engineer can then investigate and tune the rule.

---

# 🔄 32. SOC Feedback Loop

A mature SOC operates as a continuous loop:

```text id="soc35"
Detection
 ↓
Alert
 ↓
Investigation
 ↓
Analyst Feedback
 ↓
Detection Tuning
 ↓
Better Alert
 ↓
Better Investigation
```

This is how SOC operations improve over time.

---

# 📊 33. SOC Metrics

SOC teams may track metrics such as:

==> Alert volume

==> Mean Time to Detect (MTTD)

==> Mean Time to Respond (MTTR)

==> False-positive rate

==> Escalation rate

==> Incident volume

==> Detection coverage

==> Response time

==> Case closure time

Metrics should be interpreted in context rather than used in isolation.

---

# ⏱️ 34. MTTD

**MTTD = Mean Time to Detect**

It measures how long it takes to identify a security event or incident.

Conceptually:

```text id="soc36"
Security Activity
      ↓
Time passes
      ↓
Detection
```

The smaller the detection delay, the sooner the SOC can begin investigation.

---

# ⚡ 35. MTTR

**MTTR = Mean Time to Respond/Resolve**, depending on the organization's definition.

Always check how your organization defines the metric.

Conceptually:

```text id="soc37"
Detection
 ↓
Investigation
 ↓
Response
 ↓
Resolution
```

MTTR helps organizations understand response efficiency.

---

# 🧮 36. SOC Shift Handover

SOC operations often run across multiple shifts.

A good handover should include:

```text id="soc38"
Open Incidents
Pending Investigations
High-Priority Alerts
Affected Assets
Actions Taken
Expected Follow-up
Escalations
Important Changes
```

Example:

```text id="soc39"
Case #1024

Status:
Investigation

Affected Host:
SERVER-01

Current Finding:
Suspicious authentication activity

Action:
Network team notified

Pending:
Review endpoint telemetry
```

This prevents important information from being lost between shifts.

---

# 🔐 37. Evidence Handling

During investigations, preserve relevant evidence.

Examples:

==> Log events

==> Alert details

==> Screenshots

==> Hashes

==> Network information

==> Timeline

==> Analyst notes

==> Ticket history

Maintain accurate timestamps and document actions.

For incidents requiring formal forensic handling, follow the organization's evidence-preservation procedures.

---

# 🧑‍⚖️ 38. Least Privilege in SOC

SOC analysts should have only the permissions needed for their role.

Example:

```text id="soc40"
L1 Analyst
 ↓
Read / Investigate
```

More sensitive actions may require:

```text id="soc41"
L2 / Incident Response
 ↓
Containment
```

and administrative changes may require additional authorization.

This reduces operational risk.

---

# 🔒 39. SOC Access Control

A SOC platform should ideally support:

==> RBAC

==> MFA

==> Audit logs

==> Session management

==> Access reviews

==> Separation of duties

For example:

```text id="soc42"
Analyst
 ↓
Investigate

Engineer
 ↓
Modify Detection

Administrator
 ↓
Manage Platform
```

---

# 📈 40. SOC Dashboard

A SOC dashboard may show:

```text id="soc43"
Open Alerts
Open Incidents
Critical Alerts
Alert Trends
Top Source IPs
Top Affected Hosts
Top Users
Detection Health
Incident Status
MTTD
MTTR
```

The dashboard should help analysts make decisions rather than simply display large numbers.

---

# 🧪 41. Practical SOC Lab

You can build a basic SOC lab using:

```text id="soc44"
Windows VM
Linux VM
Wazuh
Firewall
SIEM Dashboard
Threat Intelligence
Ticket / Case Management
```

### Scenario

Generate several authentication failures in your authorized lab.

Then follow:

```text id="soc45"
Event
 ↓
SIEM Detection
 ↓
Alert
 ↓
L1 Triage
 ↓
Investigation
 ↓
Scope
 ↓
Verdict
 ↓
Containment Decision
 ↓
Documentation
```

---

# 🔥 42. Realistic SOC Investigation Example

Suppose the SIEM generates:

```text id="soc46"
Alert:
Multiple Failed SSH Logins
```

### Step 1 — Validate

Check:

```text id="soc47"
Timestamp
Source IP
Destination Host
Username
```

### Step 2 — Investigate

Search:

```text id="soc48"
All activity from source IP
```

### Step 3 — Check Successful Login

```text id="soc49"
Failed
Failed
Failed
Successful
```

Now investigate the successful login.

### Step 4 — Check Host Activity

Search:

```text id="soc50"
Processes
Authentication
Privilege changes
Network connections
```

### Step 5 — Determine Scope

```text id="soc51"
One host?
Multiple hosts?
One account?
Multiple accounts?
```

### Step 6 — Decide Response

Based on evidence and organizational procedures:

```text id="soc52"
Close
or
Escalate
or
Contain
```

### Step 7 — Document

Record:

```text id="soc53"
Finding
Evidence
Timeline
Actions
Verdict
```

---

# 🧠 43. SOC and SIEM Relationship

Think of it this way:

```text id="soc54"
SIEM
=
Security Data + Detection + Investigation Platform
```

SOC:

```text id="soc55"
People
+
Process
+
Technology
```

The SIEM is one important component of the SOC.

A strong SOC needs all three.

---

# 🔗 44. SIEM Engineer + SOC Analyst

The relationship is very important.

### SOC Analyst says:

> “This detection generates too many false positives.”

### SIEM Engineer:

```text id="soc56"
Investigates Rule
      ↓
Checks Data
      ↓
Tunes Logic
      ↓
Tests
      ↓
Deploys
```

Another example:

### SIEM Engineer says:

> “We are missing endpoint telemetry.”

SOC:

```text id="soc57"
Reports Detection Gap
      ↓
Security / IT Team
      ↓
Endpoint Logging Enabled
      ↓
SIEM Integration
      ↓
New Detection
```

This creates a continuous security improvement cycle.

---

# 📋 45. SOC Operations Checklist

```text id="soc58"
[ ] Monitor SIEM

[ ] Review new alerts

[ ] Validate alert

[ ] Assign alert

[ ] Investigate

[ ] Identify affected assets

[ ] Identify affected users

[ ] Search related events

[ ] Build timeline

[ ] Check threat intelligence

[ ] Determine scope

[ ] Determine verdict

[ ] Escalate if required

[ ] Contain when authorized

[ ] Eradicate root cause

[ ] Recover affected systems

[ ] Document evidence

[ ] Close incident

[ ] Perform lessons learned

[ ] Improve detection
```

---

# 🎤 46. SIEM Engineer / SOC Interview Questions

### Q1. What is SOC Operations?

**Answer:**

SOC Operations is the continuous process of monitoring security telemetry, detecting suspicious activity, investigating alerts, responding to incidents, and documenting the results.

---

### Q2. What is the difference between an event, alert, and incident?

**Answer:**

An event is recorded activity. An alert is generated when a detection identifies activity matching defined conditions. An incident is a security case requiring investigation and potentially response.

---

### Q3. Explain the incident response lifecycle.

**Answer:**

A practical SOC workflow is:

**Detect → Validate → Investigate → Scope → Contain → Eradicate → Recover → Document → Lessons Learned**

---

### Q4. What do you do when a SIEM alert is triggered?

**Answer:**

First, I validate the alert and understand why it triggered. Then I identify the affected user, host, IP, and timestamp, search related events, build a timeline, determine the scope and verdict, and escalate or respond according to the SOC procedure.

---

### Q5. How do you handle false positives?

**Answer:**

I investigate why the detection triggered, determine whether the activity is expected, and provide feedback to the Detection Engineer. The rule can then be tuned using better conditions, thresholds, context, or controlled exceptions.

---

### Q6. When should an alert be escalated?

**Answer:**

An alert should be escalated when it requires deeper technical expertise, additional authority, incident-response support, broader investigation, or involvement from another team.

---

### Q7. What information should be included in an escalation?

**Answer:**

The escalation should contain the alert summary, timestamps, affected users and assets, source and destination information, relevant events, timeline, investigation findings, evidence, actions already taken, and recommended next steps.

---

### Q8. What is MTTD?

**Answer:**

MTTD means Mean Time to Detect. It measures the average time between a security event or incident occurring and its detection, according to the organization's measurement definition.

---

### Q9. What is MTTR?

**Answer:**

MTTR is a time-based response metric. Organizations may define it as Mean Time to Respond or Mean Time to Resolve/Recover, so the exact definition should be confirmed before comparing metrics.

---

### Q10. What is a SOC runbook?

**Answer:**

A runbook is a documented set of operational steps that helps analysts consistently handle a particular alert or incident type.

---

### Q11. Why is documentation important in SOC operations?

**Answer:**

Documentation preserves evidence, explains decisions and actions, supports handovers and escalations, provides an audit trail, and helps improve future detection and response.

---

### Q12. What is the role of a SIEM Engineer in a SOC?

**Answer:**

A SIEM Engineer manages and improves the SIEM ecosystem, including log collection, integrations, parsing, detection rules, alert quality, dashboards, performance, data retention, troubleshooting, and support for SOC investigations.

---

# 🧠 47. Important SOC Principles

### Principle 1 — Alert ≠ Incident

Never treat every alert as a confirmed incident.

### Principle 2 — Evidence Before Conclusion

Do not make conclusions without supporting evidence.

### Principle 3 — Context Matters

An event must be understood in its environment.

### Principle 4 — Document Everything Important

If an important action or finding is not documented, it becomes difficult to verify later.

### Principle 5 — Learn From Every Incident

Every investigation can improve:

```text id="soc59"
Detection
Process
Runbook
Automation
Training
```

---

# 🚀 48. Final Takeaway

A SOC is not just a room full of analysts watching dashboards.

A mature SOC combines:

```text id="soc60"
People
+
Process
+
Technology
+
Data
+
Detection
+
Investigation
+
Response
```

For a SIEM Engineer, understanding SOC Operations is essential because the SIEM exists to support the security operation.

Remember the core flow:

**Detect → Validate → Investigate → Scope → Contain → Eradicate → Recover → Document → Improve**

If you understand this workflow and can explain it with real examples during an interview, you demonstrate practical SOC knowledge—not just SIEM tool knowledge.

---

## 📚 SIEM Engineer Learning Series

**#01 — Log Management**

**#02 — SIEM Platforms**

**#03 — Log Integration**

**#04 — Detection Engineering**

**#05 — Query & Investigation**

**#06 — SOC Operations ← You are here**

**#07 — Threat Intelligence → Next**

**#08 — Automation & SOAR**

**#09 — Dashboard & Reporting**

**#10 — SIEM Infrastructure**

---

### Navigation

**← Previous Article: #05 — Query & Investigation**

**SIEM Engineer Index**

**Next Article: #07 — Threat Intelligence →**

---


