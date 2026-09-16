# SIEM Engineer #14 — Advanced Detection Engineering

## 🛡️ Introduction

A SIEM can collect millions of events, but collecting logs alone does not make a SOC effective.

The real value comes from identifying **suspicious behavior** from those events.

This is where **Detection Engineering** becomes important.

Basic detection may look for one event:

```text
Failed login detected
```

Advanced detection asks:

```text
Why did this happen?
Who performed it?
From where?
How many times?
What happened before and after?
Does this behavior match an attack pattern?
```

Advanced Detection Engineering focuses on building detections that are:

==> Accurate
==> Context-aware
==> Scalable
==> Testable
==> Maintainable
==> Low-noise
==> Useful for SOC Analysts

---

# 1️⃣ What is Advanced Detection Engineering?

**Advanced Detection Engineering** is the process of designing SIEM detection logic that identifies suspicious activities by analyzing:

==> Multiple events
==> User behavior
==> Host behavior
==> Network activity
==> Authentication patterns
==> Process activity
==> Threat Intelligence
==> Attack techniques
==> Historical behavior

Instead of depending on a single event, advanced detection can combine multiple signals.

### Basic Detection

```text
Failed Login
```

### Advanced Detection

```text
10 Failed Logins
        ↓
Successful Login
        ↓
Same Source IP
        ↓
Privileged Account
        ↓
Suspicious Activity
        ↓
High-Risk Alert
```

This provides much more context to the SOC Analyst.

---

# 2️⃣ 💡 Why does this matter?

A large organization can generate thousands or millions of events every day.

If every suspicious-looking event becomes an alert, the SOC may experience:

==> Alert Fatigue
==> High False Positives
==> Analyst Overload
==> Missed Threats
==> Slow Investigation

Good detection engineering tries to answer:

> **Which events actually deserve analyst attention?**

The goal is not simply to create more alerts.

The goal is to create **better alerts**.

---

# 3️⃣ Detection Engineering Lifecycle

A mature detection normally follows this lifecycle:

```text
Idea
 ↓
Security Hypothesis
 ↓
Identify Data Sources
 ↓
Understand Fields
 ↓
Create Detection Logic
 ↓
Build Rule
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
```

A SIEM Engineer should understand every stage.

---

# 4️⃣ Security Hypothesis

Before creating a rule, define what behavior you want to detect.

For example:

```text
An attacker may perform password spraying
against multiple user accounts from a single source.
```

Now identify the required evidence.

==> Authentication logs
==> Username
==> Source IP
==> Destination system
==> Authentication result
==> Timestamp
==> Account type

The hypothesis becomes the foundation of the detection.

---

# 5️⃣ Data Source Identification

A detection is only as good as the data available to it.

For example:

### Windows Detection

Possible sources:

==> Windows Security Logs
==> Sysmon
==> PowerShell logs
==> Endpoint Security
==> EDR

### Linux Detection

==> SSH logs
==> Authentication logs
==> Audit logs
==> Process logs
==> Shell history where appropriate

### Network Detection

==> Firewall
==> IDS/IPS
==> Proxy
==> DNS
==> VPN
==> NetFlow

### Identity Detection

==> Active Directory
==> Azure/Cloud Identity
==> VPN
==> SSO
==> MFA

---

# 6️⃣ Understand Your Fields

Before writing detection logic, understand the available fields.

For example:

```text
src_ip
dst_ip
username
hostname
event_type
process_name
command_line
timestamp
action
status
severity
```

Bad field understanding can create bad detections.

Always verify:

==> Field name
==> Data type
==> Example values
==> Normal values
==> Missing values
==> Normalization
==> Timestamp format

---

# 7️⃣ Single-Event Detection

The simplest detection uses one event.

Example:

```text
event_type = "privilege_change"
AND
target_group = "Domain Admins"
```

This may generate an alert.

Single-event detections are useful, but they often lack context.

For example:

```text
User added to privileged group
```

does not tell us:

==> Was this authorized?
==> Who performed it?
==> From which host?
==> Was there suspicious activity before it?
==> Is this normal for the user?

This is why correlation becomes important.

---

# 8️⃣ 🔗 Correlation Detection

**Correlation** means combining multiple events to identify a meaningful security pattern.

Example:

```text
Failed Login
+
Failed Login
+
Failed Login
+
Successful Login
```

Together, these events may indicate a possible brute-force attack.

Another example:

```text
PowerShell Execution
+
Encoded Command
+
External Network Connection
```

Together, these signals may deserve more attention than any single event.

---

# 9️⃣ Threshold Detection

Threshold detection looks for repeated activity.

Example:

```text
More than 20 failed logins
from the same IP
within 5 minutes
```

Conceptually:

```text
count(failed_login)
GROUP BY src_ip
WHERE count > 20
TIME WINDOW = 5 minutes
```

Thresholds should be based on:

==> Environment baseline
==> User behavior
==> Authentication system
==> Business requirements
==> Historical activity

Avoid choosing arbitrary thresholds.

---

# 🔟 Sequence Detection

Sequence detection focuses on the **order of events**.

Example:

```text
Login Failure
      ↓
Successful Login
      ↓
Privilege Escalation
      ↓
Suspicious Process
      ↓
Outbound Connection
```

Each event alone may not be enough.

The sequence creates stronger context.

### Example

```text
1. Multiple failed SSH logins
2. Successful SSH login
3. sudo execution
4. New process starts
5. External connection
```

This could represent a potential attack chain.

The SIEM Engineer should investigate the relationship between these events.

---

# 1️⃣1️⃣ Behavioral Detection

Behavioral detection focuses on **what is unusual**, rather than only looking for known indicators.

For example:

A user normally logs in:

```text
09:00–18:00
Dhaka
Corporate Network
```

Suddenly:

```text
03:15
Unknown Location
New Device
VPN
```

Instead of simply asking:

```text
Is this IP malicious?
```

behavioral detection asks:

```text
Is this behavior unusual for this user?
```

---

# 1️⃣2️⃣ Baseline Analysis

A baseline represents normal activity.

For example:

```text
Normal Login Count:
20–50/day
```

Suddenly:

```text
Login Count:
500/day
```

That deviation may deserve investigation.

Baselines can be created for:

==> Users
==> Hosts
==> Applications
==> IP addresses
==> Network traffic
==> Processes
==> Authentication

But remember:

**Unusual does not automatically mean malicious.**

It should become a signal for investigation.

---

# 1️⃣3️⃣ Entity-Based Detection

Advanced SIEM detections often analyze entities.

Common entities include:

```text
User
Host
IP
Application
Account
Device
```

Example:

```text
User: admin
Host: SERVER-01
Source IP: 10.10.10.50
```

The SIEM can build context around these entities.

For example:

```text
admin
  ↓
Multiple Failed Logins
  ↓
Successful Login
  ↓
Privilege Change
  ↓
Suspicious Process
```

Now the SOC Analyst has a much stronger investigation context.

---

# 1️⃣4️⃣ Risk-Based Detection

Instead of treating every event equally, we can assign risk values.

Conceptually:

```text
Failed Login              +5
Suspicious PowerShell     +20
Privilege Escalation       +30
Known Malicious IP         +40
```

Total:

```text
5 + 20 + 30 + 40 = 95
```

The SIEM may then treat the entity as high risk.

A generic model could be:

```text
Risk =
Event Risk
+
Behavior Risk
+
Threat Intelligence Risk
+
Entity Context
```

The exact implementation depends on the SIEM platform.

Risk scoring should be carefully tested because poor scoring can create excessive alerts.

---

# 1️⃣5️⃣ Severity vs Risk vs Confidence

These concepts should not be confused.

### Severity

How serious the detected activity could be.

```text
Low
Medium
High
Critical
```

### Confidence

How confident we are that the detection represents suspicious activity.

```text
Low Confidence
Medium Confidence
High Confidence
```

### Risk

Potential overall security impact based on multiple signals.

Example:

```text
Severity: High
Confidence: Medium
Risk: 75
```

These values provide different types of context.

---

# 1️⃣6️⃣ False Positive Reduction

A detection can be technically correct but operationally noisy.

Example:

```text
PowerShell detected
```

PowerShell itself is not malicious.

Administrators and applications may legitimately use it.

Therefore, detection logic may consider:

==> User
==> Parent process
==> Command line
==> Destination
==> Host role
==> Time
==> Frequency
==> Known administrative activity

Instead of:

```text
PowerShell = Alert
```

Use contextual logic.

---

# 1️⃣7️⃣ Exceptions and Allowlists

Sometimes legitimate activity should be excluded.

Examples:

```text
Approved vulnerability scanner
Approved administrator
Approved backup server
Approved monitoring system
Approved automation account
```

But exceptions must be controlled carefully.

Bad approach:

```text
Ignore entire IP
```

Better approach:

```text
Ignore specific activity
under specific conditions
for a documented reason.
```

Every exception should have:

==> Owner
==> Reason
==> Scope
==> Expiration/review date
==> Approval

---

# 1️⃣8️⃣ Suppression

If the same event repeatedly creates alerts, suppression can reduce noise.

Example:

```text
Same User
Same Host
Same Detection
Repeated 100 times
```

Instead of creating 100 separate alerts, the SIEM may group or suppress them according to defined logic.

However, suppression should never hide meaningful changes in behavior.

---

# 1️⃣9️⃣ Detection for Brute Force

A simple brute-force detection could be:

```text
Multiple authentication failures
+
Same source
+
Short time window
```

Advanced version:

```text
Multiple failed logins
        ↓
Multiple accounts targeted
        ↓
Same source IP
        ↓
Successful authentication
```

The second detection provides more context.

---

# 2️⃣0️⃣ PowerShell Detection

PowerShell is widely used for legitimate administration.

Therefore, detection should focus on suspicious characteristics.

Potential signals:

==> Encoded commands
==> Suspicious parent process
==> Unusual user
==> Unexpected server
==> Download activity
==> External connection
==> Abnormal execution time
==> Suspicious command-line patterns

A stronger detection may correlate:

```text
Office Application
      ↓
PowerShell
      ↓
Encoded Command
      ↓
Network Connection
```

---

# 2️⃣1️⃣ Privilege Escalation Detection

Possible signals include:

```text
User privilege change
+
New privileged group membership
+
Administrative command execution
```

For Linux:

```text
Normal User
    ↓
sudo
    ↓
Root Command
```

For Windows:

```text
Standard Account
    ↓
Privilege Change
    ↓
Administrative Activity
```

Context is important because legitimate administrators also perform these actions.

---

# 2️⃣2️⃣ Lateral Movement Detection

Lateral movement often involves one system accessing another.

Example:

```text
Host A
  ↓
Host B
  ↓
Host C
```

Possible signals:

==> New remote login
==> RDP
==> SMB
==> WinRM
==> SSH
==> Remote administration tools

A useful detection can correlate:

```text
New Source Host
+
Privileged Account
+
Remote Authentication
+
Multiple Destination Hosts
```

---

# 2️⃣3️⃣ Firewall Scanning Detection

A single connection is usually not enough.

Instead:

```text
One source IP
      ↓
Many destination ports
      ↓
Many destination hosts
      ↓
Short time period
```

This can indicate scanning behavior.

Example logic:

```text
COUNT(unique_destination_ports) > threshold
```

and/or:

```text
COUNT(unique_destination_hosts) > threshold
```

The threshold should be adapted to the environment.

---

# 2️⃣4️⃣ MITRE ATT&CK Mapping

Detection engineers should understand **MITRE ATT&CK**.

A detection can be mapped to:

```text
Tactic
   ↓
Technique
   ↓
Sub-technique
```

For example, a detection involving suspicious PowerShell activity can be mapped to the appropriate ATT&CK technique.

This helps the SOC understand:

==> What behavior are we detecting?
==> Which attack technique does it represent?
==> Which techniques are missing?
==> Where are our detection gaps?

---

# 2️⃣5️⃣ Detection Coverage

A mature SOC should not only count the number of rules.

It should understand coverage.

Example:

```text
ATT&CK Technique
        ↓
Data Source
        ↓
Detection
        ↓
Alert
        ↓
Investigation
        ↓
Response
```

A technique without the required data source cannot be reliably detected.

Therefore:

**Detection coverage = Data + Logic + Validation + Operational Response**

---

# 2️⃣6️⃣ Sigma Rules

**Sigma** is a generic rule format for describing SIEM detections.

Conceptually:

```text
Log Source
Detection Conditions
Fields
Severity
Tags
References
```

The advantage is portability.

A detection idea can be represented independently of one specific SIEM query language and then adapted to platforms such as:

==> Splunk
==> Elastic
==> Microsoft Sentinel
==> Other SIEM platforms

Always validate the converted query against your actual data.

---

# 2️⃣7️⃣ Detection-as-Code

Detection-as-Code treats detection rules like software.

That means using:

```text
Git
Version Control
Code Review
Testing
Documentation
CI/CD
Change History
```

Example workflow:

```text
Developer
   ↓
Create Detection
   ↓
Git Commit
   ↓
Review
   ↓
Test
   ↓
Deploy
   ↓
Monitor
```

This makes detection management more controlled and repeatable.

---

# 2️⃣8️⃣ Detection Testing

Never deploy an important detection without testing it.

Testing should include:

### Positive Test

Generate the behavior that should trigger the rule.

```text
Expected:
Alert = YES
```

### Negative Test

Generate legitimate activity.

```text
Expected:
Alert = NO
```

### Edge Case

Test unusual but legitimate scenarios.

```text
Expected:
Correct handling
```

This helps identify:

==> False positives
==> False negatives
==> Missing fields
==> Logic errors
==> Performance problems

---

# 2️⃣9️⃣ Detection Performance

A detection may be logically correct but computationally expensive.

For example:

```text
Search entire dataset
+
Long time range
+
Complex wildcard
+
Large aggregation
```

This can consume significant SIEM resources.

Detection engineers should consider:

==> Search scope
==> Time window
==> Indexed fields
==> Query complexity
==> Event volume
==> Scheduling frequency
==> Correlation strategy

A good detection should be both **accurate and efficient**.

---

# 3️⃣0️⃣ Detection Monitoring

After deployment, the work is not finished.

Monitor:

```text
Alert Volume
False Positive Rate
True Positive Rate
Execution Time
Rule Errors
Data Availability
Detection Coverage
Analyst Feedback
```

For example:

```text
Before tuning:
1,000 alerts/day

After tuning:
100 alerts/day
```

But reducing alerts is not automatically success.

You must verify that important detections are still firing.

---

# 3️⃣1️⃣ Detection Tuning Process

A practical tuning process:

```text
Review Alert
      ↓
Understand Why It Triggered
      ↓
Determine TP / FP
      ↓
Identify Noise Pattern
      ↓
Modify Detection
      ↓
Test
      ↓
Deploy
      ↓
Monitor
```

Never tune only to reduce alert numbers.

The objective is to improve **signal quality**.

---

# 3️⃣2️⃣ Real-World Example — Suspicious Login

Suppose the SIEM detects:

```text
03:15 — Login from IP A
03:17 — Login from IP B
03:18 — MFA failure
03:20 — Successful login
03:21 — Privileged action
```

A basic detection might only detect:

```text
Successful Login
```

An advanced detection considers the complete context:

```text
Unusual Time
+
New Source
+
MFA Failure
+
Successful Login
+
Privileged Activity
```

This creates a stronger investigation signal.

---

# 3️⃣3️⃣ Practical Detection Engineering Lab

You can build a small lab using:

```text
Wazuh
Linux VM
Windows VM
Firewall
Syslog
```

### Lab 01 — SSH Brute Force

Generate:

```text
Multiple Failed SSH Logins
```

Detect:

```text
Same Source IP
+
Multiple Failures
+
Short Time Window
```

---

### Lab 02 — Successful Login After Failures

Create:

```text
Failed Login
Failed Login
Failed Login
Successful Login
```

Build a correlation rule.

---

### Lab 03 — Privilege Escalation

Generate controlled activity:

```text
User
 ↓
sudo
 ↓
Privileged Command
```

Create a detection.

---

### Lab 04 — Suspicious Process

Monitor:

```text
Process Name
Parent Process
User
Command Line
Network Connection
```

Create a contextual detection.

---

### Lab 05 — Network Scanning

Generate authorized lab traffic:

```text
One Source
 ↓
Many Ports
 ↓
Many Hosts
```

Create a threshold-based detection.

---

# 3️⃣4️⃣ Detection Engineering Documentation

Every important detection should have documentation.

A useful template:

```text
Detection Name:
Description:
Objective:
Data Sources:
Required Fields:
Detection Logic:
MITRE ATT&CK:
Severity:
Confidence:
Risk:
False Positive Scenarios:
Exceptions:
Testing Method:
Owner:
Version:
Last Review:
```

This is extremely useful for SOC operations.

---

# 3️⃣5️⃣ Detection Engineering + SOC

Detection engineering and SOC operations should work together.

```text
Detection Engineer
       ↓
Creates Detection
       ↓
SOC Analyst
       ↓
Investigates Alert
       ↓
Provides Feedback
       ↓
Detection Engineer
       ↓
Tunes Detection
```

Analyst feedback is extremely valuable.

The SOC Analyst sees real-world alert behavior that may not be visible during initial rule development.

---

# 3️⃣6️⃣ Common Mistakes

Avoid these mistakes:

==> Creating alerts for every suspicious event
==> Using arbitrary thresholds
==> Ignoring normal user behavior
==> Not testing negative cases
==> No documentation
==> No MITRE mapping
==> No exception management
==> Excessive allowlisting
==> Ignoring query performance
==> Never reviewing old detections
==> Measuring success only by alert reduction
==> Deploying rules without validating data

---

# 3️⃣7️⃣ SIEM Engineer Interview Questions

### Q1. What is Detection Engineering?

**Answer:**

Detection Engineering is the process of designing, testing, deploying, monitoring, and tuning security detections that identify suspicious activity from security data.

---

### Q2. What is correlation detection?

**Answer:**

Correlation detection combines multiple related events to identify a meaningful security pattern instead of relying on a single event.

---

### Q3. What is behavioral detection?

**Answer:**

Behavioral detection identifies unusual or abnormal activity based on patterns, baselines, or entity behavior.

---

### Q4. What is the difference between severity and confidence?

**Answer:**

Severity describes the potential seriousness of the activity, while confidence describes how strongly the available evidence supports the detection.

---

### Q5. How do you reduce false positives?

**Answer:**

I first analyze why the detection triggered, identify legitimate patterns, and then improve the logic using context such as user, host, process, destination, frequency, baseline, and approved exceptions. I then test the updated rule before deployment.

---

### Q6. What is sequence detection?

**Answer:**

Sequence detection identifies a meaningful order of events, such as multiple login failures followed by a successful login and then privilege escalation.

---

### Q7. Why is baseline important?

**Answer:**

A baseline helps establish normal behavior so that unusual deviations can be identified and investigated.

---

### Q8. What is Detection-as-Code?

**Answer:**

Detection-as-Code applies software engineering practices such as Git, version control, testing, code review, and controlled deployment to security detections.

---

### Q9. What is Sigma?

**Answer:**

Sigma is a generic format for describing SIEM detection rules in a platform-independent way.

---

### Q10. How do you validate a detection?

**Answer:**

I perform positive, negative, and edge-case testing, verify the required data fields, check false positives, validate the generated alert, and monitor the rule after deployment.

---

# 3️⃣8️⃣ Detection Engineering Checklist

Before deploying a detection:

```text
☑ Security hypothesis defined
☑ Data sources identified
☑ Required fields verified
☑ Detection logic created
☑ Threshold reviewed
☑ Correlation considered
☑ Baseline considered
☑ False positives identified
☑ Positive test completed
☑ Negative test completed
☑ MITRE mapping completed
☑ Severity defined
☑ Confidence considered
☑ Documentation completed
☑ Performance checked
☑ Deployment approved
☑ Monitoring enabled
☑ Review date defined
```

---

# 3️⃣9️⃣ Complete Advanced Detection Flow

The complete SIEM detection engineering process can be remembered as:

```text
Security Problem
      ↓
Hypothesis
      ↓
Data Sources
      ↓
Field Validation
      ↓
Detection Logic
      ↓
Correlation / Behavior / Sequence
      ↓
Risk & Context
      ↓
Rule Development
      ↓
Testing
      ↓
Validation
      ↓
MITRE Mapping
      ↓
Deployment
      ↓
Monitoring
      ↓
SOC Feedback
      ↓
Tuning
      ↓
Review
```

---

# 🎯 Final Takeaway

Advanced Detection Engineering is not about writing complicated queries.

It is about creating **reliable security signals from raw data**.

A strong SIEM Engineer should understand:

==> Detection Logic
==> Correlation
==> Behavioral Detection
==> Sequence Detection
==> Risk-Based Detection
==> Baselines
==> False Positive Reduction
==> MITRE ATT&CK
==> Sigma
==> Detection-as-Code
==> Testing
==> Performance
==> Continuous Tuning

Remember:

> **Good detection creates useful signals. Great detection creates useful context.**

---

## 📚 SIEM Engineer Learning Series

**Previous:** #13 — SIEM Performance Tuning

**Current:** #14 — Advanced Detection Engineering

**Next:** #15 — Threat Hunting with SIEM

---

### 🔐 Practical Security Takeaway

Don't ask only:

```text
"Did an event happen?"
```

Ask:

```text
"Is this behavior unusual?"
"How is it connected to other events?"
"Who is involved?"
"What happened before and after?"
"Can I confidently explain why this deserves investigation?"
```

That mindset is the foundation of advanced Detection Engineering.

---

**Follow the SIEM Engineer learning series — Boni Yeamin**

