# SIEM Engineer #04 — Detection Engineering

## 🟢 Introduction

A SIEM is only useful when it can help the security team identify suspicious activity.

Collecting thousands or millions of logs is not enough.

The SIEM Engineer needs to answer an important question:

> **“What activity should generate a security alert, and why?”**

This is where **Detection Engineering** comes in.

Detection Engineering is the process of designing, developing, testing, tuning, deploying, and maintaining security detections that identify suspicious or malicious activity from security telemetry.

A simple detection flow is:

**Log Source → Telemetry → Detection Logic → Rule → Alert → Investigation → Tuning**

---

# 🧠 1. What is Detection Engineering?

Detection Engineering means creating security logic that can identify suspicious behavior from available data.

For example:

Suppose a Linux server receives:

```text
Failed SSH login
Failed SSH login
Failed SSH login
Failed SSH login
Failed SSH login
```

One failed login may be normal.

But:

```text
50 failed SSH logins
from the same IP
against the same server
within 5 minutes
```

could indicate a brute-force attempt.

A detection could therefore be:

```text
IF
failed SSH login >= 20
FROM same source IP
WITHIN 5 minutes

THEN
generate alert
```

This is a simple example of detection logic.

---

# 🎯 2. Why Detection Engineering Matters

A SOC may receive millions of events every day.

Analysts cannot manually inspect every event.

Detection Engineering converts raw telemetry into meaningful security signals.

### Example

Without detection:

```text
10,000 Windows events
        ↓
Analyst manually searches
        ↓
High workload
```

With detection:

```text
10,000 Windows events
        ↓
Detection Rules
        ↓
Suspicious activity
        ↓
Security Alert
        ↓
SOC Analyst
```

### 💡 Why does this matter?

Good detections help SOC teams:

- Reduce manual investigation

- Detect suspicious behavior faster

- Improve incident response

- Reduce unnecessary alerts

- Improve MITRE ATT&CK visibility

- Support threat hunting

- Standardize security monitoring

---

# 🔄 3. Detection Engineering Lifecycle

Detection Engineering is not simply:

**Write Rule → Deploy**

A mature process looks like:

```text
Detection Idea
      ↓
Security Hypothesis
      ↓
Identify Data Sources
      ↓
Check Required Fields
      ↓
Develop Detection Logic
      ↓
Create Rule
      ↓
Test
      ↓
Validate
      ↓
Deploy
      ↓
Monitor
      ↓
Tune
      ↓
Review
      ↓
Retire / Update
```

Let's understand each step.

---

# 🔍 4. Step 1 — Detection Idea

Everything starts with a security question.

Examples:

- Can we detect SSH brute-force activity?

- Can we detect suspicious PowerShell execution?

- Can we detect unexpected administrator creation?

- Can we detect privilege group changes?

- Can we detect suspicious login behavior?

- Can we detect communication with known malicious IPs?

This is the starting point.

---

# 💡 5. Step 2 — Create a Security Hypothesis

A detection should have a clear reason.

For example:

> “An attacker attempting to gain access to a Linux server may generate multiple failed SSH authentication events from the same source IP.”

This becomes the detection hypothesis.

Then we determine:

```text
What behavior?
Which system?
Which log?
Which fields?
What threshold?
What time window?
What response?
```

---

# 📊 6. Step 3 — Identify Required Telemetry

A detection cannot work without the required data.

For SSH brute-force detection, we may need:

```text
timestamp
source_ip
destination_ip
username
event_type
authentication_result
hostname
```

For Windows authentication detection:

```text
timestamp
user
source_ip
hostname
event_id
logon_type
authentication_result
```

For process detection:

```text
timestamp
hostname
user
parent_process
process_name
command_line
process_id
```

### Important

Before writing a rule, ask:

> **“Do I actually have the data required for this detection?”**

A great detection idea is useless if the SIEM does not receive the necessary telemetry.

---

# 🧩 7. Detection Data Quality

Detection quality depends heavily on log quality.

For example:

```text
source_ip = NULL
username = NULL
event_type = NULL
```

makes many detections difficult.

Therefore:

**Good Detection = Good Telemetry + Good Logic**

You should verify:

- Logs are arriving

- Parsing is correct

- Fields are normalized

- Timestamps are correct

- Required fields exist

- Events are not duplicated

- Events are not heavily delayed

---

# ⚙️ 8. Detection Logic

Detection logic defines what behavior should trigger an alert.

Example:

```text
failed_login >= 10
AND
same_source_ip
AND
within 5 minutes
```

Another example:

```text
new_admin_account = TRUE
AND
account_created_outside_change_window = TRUE
```

Another:

```text
known_malicious_ip = TRUE
AND
internal_host_connection = TRUE
```

Detection logic can be simple or complex.

---

# 🧱 9. Types of Detection

There are several common detection approaches.

## 9.1 Threshold Detection

A threshold detection looks for an event count above a certain value.

Example:

```text
More than 20 failed logins
from one IP
within 5 minutes
```

Useful for:

- Brute force

- Repeated authentication failures

- Excessive connection attempts

- Repeated security events

---

# 🔗 9.2 Sequence Detection

Sequence detection looks for multiple events occurring in a specific order.

Example:

```text
Login
   ↓
Privilege escalation
   ↓
Sensitive command
   ↓
Outbound connection
```

Individually, each event may not be highly suspicious.

Together, the sequence may be more meaningful.

---

# 👤 9.3 Behavioral Detection

Behavioral detection looks for activity that differs from expected behavior.

Example:

A user normally logs in from:

```text
Dhaka
```

Suddenly the same account authenticates from:

```text
Another geographic location
```

The detection may investigate the unusual behavior.

Behavioral detections often require additional context.

---

# 📈 9.4 Anomaly Detection

Anomaly detection attempts to identify activity that differs significantly from an established baseline.

Example:

```text
Normal:
20–50 login events/day

Observed:
2,000 login events/day
```

This could trigger investigation.

However, anomaly does not automatically mean malicious.

It means:

> **“This behavior is unusual and should be investigated.”**

---

# 🔀 9.5 Correlation Detection

Correlation combines multiple events or data sources.

Example:

```text
Firewall connection
       +
Endpoint process
       +
Threat Intelligence IOC
       ↓
Security Alert
```

Correlation is one of the most important SIEM capabilities.

---

# 🛡️ 10. Detection Rules vs Correlation Rules

### Detection Rule

Usually focuses on a specific event or behavior.

Example:

```text
PowerShell process created
```

### Correlation Rule

Combines multiple events or conditions.

Example:

```text
Suspicious PowerShell
+
Network connection
+
Known malicious destination
```

Both are useful.

---

# 🧪 11. Sigma

**Sigma** is a generic, open detection-rule format designed to describe suspicious activity in a SIEM-independent way.

A simplified Sigma-style rule can look like:

```yaml
title: Multiple Failed SSH Logins
status: experimental

logsource:
  product: linux
  service: ssh

detection:
  selection:
    event_type: "authentication_failure"

  condition: selection

level: medium
```

The exact fields depend on the telemetry and backend.

The important idea is:

```text
Detection Logic
      ↓
Sigma Rule
      ↓
Backend-specific query/rule
```

Sigma helps security teams maintain detection logic in a portable format.

---

# 🧠 12. Sigma Rule Structure

Common Sigma components include:

```text
title
id
status
description
references
author
date
tags
logsource
detection
falsepositives
level
```

Example concept:

```yaml
title: Suspicious Authentication Activity

description: Detects repeated authentication failures.

logsource:
  product: linux
  service: ssh

detection:
  selection:
    event_type: authentication_failure

  condition: selection

falsepositives:
  - Administrative activity

level: medium
```

The quality of the rule depends on the quality of the underlying data.

---

# 🎯 13. MITRE ATT&CK Mapping

Detection Engineers often map detections to **MITRE ATT&CK** techniques.

MITRE ATT&CK provides a common knowledge base for describing adversary tactics and techniques.

A detection can contain tags such as:

```text
Tactic
Technique
Sub-technique
```

For example, a PowerShell-related detection can be associated with:

```text
Tactic: Execution (TA0002)
Technique: T1059 Command and Scripting Interpreter
Sub-technique: T1059.001 PowerShell
```

Other common mappings: T1110 Brute Force, T1078 Valid Accounts, T1003 Credential Dumping, T1021 Remote Services. See #14 Advanced Detection and #17 hands-on for full examples.

The exact mapping should be based on what the detection actually identifies.

### Important

Do not map a detection to a technique simply because the technique sounds related.

The mapping should reflect the behavior the rule is actually detecting.

---

# 🗺️ 14. Detection Coverage

A mature SOC should understand:

```text
What can we detect?
What cannot we detect?
What telemetry do we have?
What telemetry is missing?
```

Example:

| Area             | Telemetry | Detection |
| ---------------- | --------- | --------- |
| Windows Login    | Available | Yes       |
| Linux SSH        | Available | Yes       |
| Firewall         | Available | Yes       |
| Cloud Identity   | Missing   | No        |
| Endpoint Process | Partial   | Limited   |

This helps identify detection gaps.

---

# 🚨 15. Example — SSH Brute Force Detection

Suppose the SIEM receives:

```text
timestamp
source_ip
username
hostname
event_type
```

Example events:

```text
10:01:01  10.10.10.50  admin  server01  failed
10:01:10  10.10.10.50  admin  server01  failed
10:01:18  10.10.10.50  root   server01  failed
...
```

Detection:

```text
IF

authentication_failure >= 10

FROM same source_ip

WITHIN 5 minutes

THEN

generate alert
```

Possible alert:

```text
Alert:
Possible SSH Brute Force

Source IP:
10.10.10.50

Target:
server01

Failed Attempts:
24

Time Window:
5 minutes
```

The analyst then investigates whether it is:

```text
True Positive
False Positive
Benign Activity
```

---

# 🪟 16. Windows Failed Login Detection

A detection may monitor repeated authentication failures.

Concept:

```text
Event:
Authentication Failure

Group By:
user + source_ip + destination_host

Threshold:
multiple failures

Time Window:
5 minutes
```

Potential alert:

```text
Multiple Windows Authentication Failures
```

The analyst can then investigate:

- Source IP

- Username

- Target host

- Login type

- Historical activity

- Related events

- Endpoint activity

---

# ⚡ 17. PowerShell Detection

PowerShell is legitimate administrative software.

Therefore:

> **PowerShell execution does not automatically mean malicious activity.**

A useful detection may look for suspicious combinations of:

```text
PowerShell execution
+
unusual parent process
+
encoded/suspicious command characteristics
+
unexpected user
+
unusual host
```

This is an important Detection Engineering principle:

**Context matters.**

---

# 🔐 18. Privileged Account Change Detection

Another useful detection:

```text
User added to privileged group
```

For example:

```text
User
   ↓
Added to Administrator Group
   ↓
Outside approved change window
   ↓
Alert
```

The detection becomes stronger when additional context is available:

- Who performed the change?

- Which account was modified?

- Which host?

- Was there an approved ticket?

- Was the change expected?

---

# 🌐 19. Threat Intelligence Correlation

Suppose the organization has a threat intelligence feed.

The SIEM receives:

```text
Source IP:
203.x.x.x
```

Threat Intelligence says:

```text
IP = Known Malicious
```

The SIEM can correlate:

```text
Internal Host
      ↓
Connection
      ↓
External IP
      ↓
Threat Intelligence Match
      ↓
Alert
```

This can increase investigation priority.

But remember:

**IOC match ≠ automatic confirmation of compromise.**

Analysts still need context and validation.

---

# 🎚️ 20. Severity and Confidence

A common mistake is treating severity and confidence as the same thing.

They are different concepts.

### Severity

How serious could the activity be?

### Confidence

How strongly does the detection indicate the suspected behavior?

Example:

```text
High Severity
Low Confidence
```

could mean:

> The potential impact is serious, but the detection has a significant chance of being benign.

Another example:

```text
Medium Severity
High Confidence
```

could mean:

> The detection is very likely to represent the behavior it was designed to identify, but the impact may be limited.

This distinction helps SOC analysts prioritize investigation.

---

# 🚫 21. False Positives

False positives are one of the biggest problems in SOC environments.

Example:

A rule detects:

```text
20 failed logins
```

But the source IP belongs to:

```text
Internal vulnerability scanner
```

The alert may be legitimate activity.

This does not necessarily mean the detection is useless.

It may need tuning.

---

# 🔧 22. Detection Tuning

Detection tuning can include:

- Adjusting thresholds

- Changing time windows

- Adding conditions

- Adding context

- Creating exceptions

- Adding trusted sources

- Excluding approved service accounts

- Improving field normalization

- Correlating additional events

Example:

Before:

```text
failed_login > 10
```

After:

```text
failed_login > 10
AND
source_ip NOT IN approved_scanner_list
```

The goal is not simply to reduce alert numbers.

The goal is to improve **signal quality**.

---

# 🔁 23. Alert Deduplication

Sometimes the same activity generates many alerts.

Example:

```text
100 events
     ↓
100 alerts
```

This can overwhelm analysts.

A better design may group related events:

```text
100 events
     ↓
Correlation
     ↓
1 security alert
```

This is called **alert aggregation/deduplication**, depending on the implementation.

---

# 📋 24. Exceptions and Allowlisting

Some activities are known and approved.

Examples:

```text
Security Scanner
Backup Server
Monitoring Server
Patch Management Server
Approved Administrator
```

Instead of disabling the detection completely, create controlled exceptions where appropriate.

Bad approach:

```text
Too many alerts
      ↓
Disable rule
```

Better approach:

```text
Too many alerts
      ↓
Investigate reason
      ↓
Tune rule
      ↓
Add controlled exception
      ↓
Monitor
```

---

# 🧪 25. Detection Testing

Never deploy an important detection without testing it.

Testing can include:

### Unit Testing

Test individual detection conditions.

### Replay Testing

Use historical or representative events.

### Synthetic Events

Generate controlled test events.

### Attack Simulation

Use authorized security testing to produce expected telemetry.

### Regression Testing

Make sure a rule change does not break previously working behavior.

---

# 🔬 26. Example Detection Test

Detection:

```text
Multiple SSH authentication failures
```

Test cases:

```text
Test 1:
1 failed login
Expected:
No alert

Test 2:
5 failed logins
Expected:
No alert

Test 3:
20 failed logins from same IP
Expected:
Alert

Test 4:
20 failed logins from approved scanner
Expected:
Exception / controlled handling
```

This is much better than simply writing the rule and assuming it works.

---

# 💻 27. Splunk Detection Example

A simplified Splunk SPL concept:

```spl
index=linux authentication_failure
| stats count by source_ip
| where count >= 10
```

This demonstrates the basic idea:

```text
Search
  ↓
Group
  ↓
Count
  ↓
Threshold
  ↓
Detection
```

A production rule should normally include appropriate time windows, fields, exclusions, and context.

---

# ☁️ 28. Microsoft Sentinel / KQL Concept

A simplified KQL example:

```kql
SigninLogs
| where ResultType != 0
| summarize FailedAttempts=count() by IPAddress
| where FailedAttempts >= 10
```

Again, this is a simplified learning example.

A production detection should account for:

- Time window

- Identity context

- Trusted sources

- User risk

- Related events

- Appropriate exclusions

---

# 🛡️ 29. Wazuh Detection Concept

Wazuh can use rules to identify specific security events.

Conceptually:

```text
Log
 ↓
Decoder
 ↓
Rule
 ↓
Alert
 ↓
Active Response / SOC Investigation
```

For example:

```text
SSH authentication failure
        ↓
Wazuh decoder
        ↓
Rule matching
        ↓
Alert
        ↓
SOC investigation
```

The important lesson is that Detection Engineering is not limited to one SIEM platform.

The concepts apply across:

- Wazuh

- Splunk

- Microsoft Sentinel

- QRadar

- Elastic Security

- OpenSearch

and other security monitoring platforms.

---

# 🧑‍💻 30. Detection-as-Code

Modern security teams increasingly manage detections similarly to software.

Instead of keeping rules only inside a SIEM:

```text
Detection Rules
      ↓
Git Repository
      ↓
Version Control
      ↓
Testing
      ↓
Review
      ↓
Deployment
```

Benefits include:

- Version history

- Peer review

- Change tracking

- Testing

- Rollback

- Collaboration

A detection rule should be treated as production security logic.

---

# 📁 31. Detection Rule Documentation

Every important detection should have documentation.

A useful detection document can contain:

```text
Detection Name
Description
Purpose
Data Sources
Required Fields
Detection Logic
MITRE ATT&CK Mapping
Severity
Confidence
False Positives
Exceptions
Response Guidance
Owner
Version
Last Reviewed
```

Example:

```text
Detection:
SSH Brute Force

Purpose:
Detect repeated SSH authentication failures.

Data Source:
Linux / SSH

Threshold:
10 failures

Time Window:
5 minutes

MITRE Mapping:
Relevant authentication technique mapping

False Positives:
Approved security scanners

Response:
Investigate source IP and target host
```

---

# 📈 32. Detection Health Monitoring

Creating a rule is not the end.

You should monitor whether the rule is healthy.

Useful metrics include:

- Alert volume

- False-positive rate

- Detection firing frequency

- Data freshness

- Rule execution errors

- Query performance

- Missing telemetry

- Detection coverage

- Analyst feedback

A rule that worked six months ago may become ineffective after an infrastructure or logging change.

---

# 💰 33. Detection Performance and Cost

Detection rules consume resources.

Poorly designed queries can cause:

```text
High CPU
High memory
Slow searches
High SIEM cost
Delayed alerts
```

Therefore:

**Detection Engineering = Security + Performance**

Optimize:

- Search scope

- Time range

- Indexed fields

- Query structure

- Event volume

- Correlation frequency

- Data retention

---

# 🧠 34. Detection Coverage vs Detection Count

A SOC should not measure maturity only by:

```text
We have 1,000 detection rules.
```

More rules do not automatically mean better security monitoring.

Instead ask:

```text
What threats can we detect?
What telemetry supports them?
How reliable are the detections?
What are the detection gaps?
```

A small number of well-tested detections can be more useful than a huge collection of poorly maintained rules.

---

# 🔄 35. Detection Improvement Cycle

A mature detection process looks like:

```text
Create
  ↓
Test
  ↓
Deploy
  ↓
Monitor
  ↓
Investigate Alerts
  ↓
Collect Analyst Feedback
  ↓
Tune
  ↓
Retest
  ↓
Improve
```

Detection Engineering is a continuous process.

---

# 🧪 36. Practical SIEM Lab

You can build a small detection engineering lab using:

```text
Linux VM
Windows VM
Wazuh / SIEM
Syslog
Windows Event Logs
```

### Lab 1 — SSH Detection

Generate several failed SSH authentication events in your authorized lab.

Then:

```text
Collect logs
   ↓
Parse logs
   ↓
Identify source IP
   ↓
Create threshold detection
   ↓
Generate alert
   ↓
Investigate
   ↓
Tune
```

### Lab 2 — Windows Authentication

Collect Windows security events.

Create a detection for repeated authentication failures.

Test:

```text
Normal login
Failed login
Repeated failures
Approved administrative activity
```

### Lab 3 — Privilege Change

Monitor administrative group membership changes.

Create a detection:

```text
Privilege Group Change
        ↓
Alert
        ↓
Validate
        ↓
Investigate
```

---

# 📋 37. Detection Engineering Checklist

Before deploying a detection, ask:

```text
[ ] What behavior am I detecting?

[ ] What is the security hypothesis?

[ ] Which data source provides the evidence?

[ ] Are the required logs available?

[ ] Are required fields parsed?

[ ] Is the timestamp correct?

[ ] Is the detection logic clear?

[ ] Is a threshold required?

[ ] Is a time window required?

[ ] Is correlation required?

[ ] What are the expected false positives?

[ ] Are exceptions required?

[ ] What severity should it have?

[ ] What confidence should it have?

[ ] Is MITRE ATT&CK mapping appropriate?

[ ] Has the rule been tested?

[ ] Has it been reviewed?

[ ] Is it documented?

[ ] Is it version controlled?

[ ] How will it be monitored?

[ ] When will it be reviewed again?
```

---

# 🎯 38. Complete Detection Engineering Flow

Remember this flow:

```text
Security Requirement
        ↓
Detection Hypothesis
        ↓
Data Source
        ↓
Telemetry Validation
        ↓
Field Identification
        ↓
Detection Logic
        ↓
Rule Development
        ↓
MITRE Mapping
        ↓
Testing
        ↓
False Positive Analysis
        ↓
Tuning
        ↓
Peer Review
        ↓
Deployment
        ↓
Alert Monitoring
        ↓
Investigation Feedback
        ↓
Continuous Improvement
```

This is the core workflow of a SIEM Detection Engineer.

---

# 🎤 39. SIEM Engineer Interview Questions

### Q1. What is Detection Engineering?

**Answer:**

Detection Engineering is the process of designing, developing, testing, deploying, tuning, and maintaining security detections that identify suspicious or malicious activity from security telemetry.

---

### Q2. What is a detection rule?

**Answer:**

A detection rule contains logic that identifies a specific suspicious event or behavior and generates an alert when the defined conditions are met.

---

### Q3. What is a correlation rule?

**Answer:**

A correlation rule combines multiple events, conditions, or data sources to identify a more meaningful security pattern.

---

### Q4. What is Sigma?

**Answer:**

Sigma is a generic and SIEM-independent format for describing detection rules. It allows detection logic to be shared and converted for different SIEM backends.

---

### Q5. Why is MITRE ATT&CK important for Detection Engineering?

**Answer:**

MITRE ATT&CK provides a common framework for describing adversary tactics and techniques. Mapping detections to ATT&CK helps security teams understand detection coverage and identify gaps.

---

### Q6. What is a false positive?

**Answer:**

A false positive occurs when a detection generates an alert for activity that is not actually malicious according to the detection's intended purpose.

---

### Q7. How do you reduce false positives?

**Answer:**

I first investigate why the alert is firing. Then I can improve the detection using better conditions, thresholds, time windows, contextual fields, correlation, or carefully controlled exceptions.

---

### Q8. What is detection tuning?

**Answer:**

Detection tuning is the process of improving a detection's accuracy, relevance, and performance based on real-world alert results and analyst feedback.

---

### Q9. What is Detection-as-Code?

**Answer:**

Detection-as-Code means managing detection rules using software-engineering practices such as Git, version control, testing, peer review, documentation, and controlled deployment.

---

### Q10. What makes a good detection?

**Answer:**

A good detection should have a clear purpose, reliable telemetry, understandable logic, acceptable false-positive behavior, appropriate context, testing, documentation, and continuous monitoring.

---

# 🧠 40. Important Lessons

Remember these principles:

### 1️⃣ Logs are not detections

```text
Log ≠ Alert
```

Logs provide evidence.

Detections turn evidence into security signals.

### 2️⃣ More alerts do not mean better security

```text
High Alert Volume
≠
High Security
```

Signal quality matters.

### 3️⃣ Context is extremely important

A single event may be normal.

Multiple related events may tell a different story.

### 4️⃣ Detection Engineering is continuous

A detection should be:

```text
Built → Tested → Monitored → Tuned → Improved
```

### 5️⃣ Detection depends on telemetry

If you do not collect the required data, you cannot reliably detect the behavior.

---

# 🚀 Final Takeaway

A SIEM Engineer should not only know how to collect logs.

A strong SIEM Engineer should understand:

```text
What should we detect?
Why should we detect it?
Which logs provide the evidence?
How should the events be correlated?
How do we test the detection?
How do we reduce false positives?
How do we measure detection quality?
How do we maintain the rule?
```

The complete Detection Engineering mindset is:

**Hypothesis → Data → Logic → Rule → Test → Tune → Deploy → Monitor → Improve**

If you master this process, you move beyond simply operating a SIEM and start thinking like a **Detection Engineer**.

---

## 📚 SIEM Engineer Learning Series

**#01 — Log Management**

**#02 — SIEM Platforms**

**#03 — Log Integration**

**#04 — Detection Engineering ← You are here**

**#05 — Query & Investigation → Next**

**#06 — SOC Operations**

**#07 — Threat Intelligence**

**#08 — Automation & SOAR**

**#09 — Dashboard & Reporting**

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

**← Previous Article: #03 — Log Integration**

**SIEM Engineer Index**

**Next Article: #05 — Query & Investigation →**

---

