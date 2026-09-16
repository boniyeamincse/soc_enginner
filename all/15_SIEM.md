# SIEM Engineer #15 — Threat Hunting with SIEM

## 🛡️ Introduction

A traditional SOC often works like this:

```text
Alert
 ↓
Investigation
 ↓
Response
```

But attackers do not always generate an obvious alert.

Sometimes suspicious activity exists inside normal-looking logs.

This is where **Threat Hunting** becomes important.

Threat Hunting means proactively searching security data to discover:

==> Unknown threats
==> Hidden attacker activity
==> Suspicious behavior
==> Compromised accounts
==> Persistence
==> Lateral movement
==> Data exfiltration
==> Detection gaps

A SIEM Engineer should understand how SIEM data can support continuous threat hunting.

---

# 1️⃣ What is Threat Hunting?

**Threat Hunting** is a proactive security activity where analysts search available data for evidence of malicious or suspicious activity.

Traditional detection:

```text
Attacker
 ↓
Detection Rule
 ↓
Alert
 ↓
SOC Analyst
```

Threat hunting:

```text
Threat Hypothesis
 ↓
Search SIEM Data
 ↓
Find Suspicious Pattern
 ↓
Investigate
 ↓
Validate
 ↓
Improve Detection
```

The key difference is that hunting does not always wait for an alert.

---

# 2️⃣ 💡 Why does this matter?

Attackers may:

==> Use legitimate tools
==> Compromise valid accounts
==> Modify existing processes
==> Blend into normal traffic
==> Avoid known malware signatures
==> Operate slowly
==> Exploit detection gaps

Therefore:

**No alert does not always mean no threat.**

Threat hunting helps search for activity that existing detections may have missed.

---

# 3️⃣ Threat Hunting vs Alert Investigation

These two activities are related but different.

### Alert Investigation

You already have a signal:

```text
SIEM Alert
 ↓
Validate
 ↓
Investigate
 ↓
Verdict
```

### Threat Hunting

You start with a question or hypothesis:

```text
Hypothesis
 ↓
Search
 ↓
Investigate
 ↓
Evidence
 ↓
Verdict
```

Example:

### Alert Investigation

```text
"Multiple failed SSH logins detected."
```

### Threat Hunting

```text
"Are there any unusual SSH login patterns
that our current detections are not identifying?"
```

---

# 4️⃣ Threat Hunting Lifecycle

A practical hunting lifecycle is:

```text
Define Objective
      ↓
Create Hypothesis
      ↓
Identify Data Sources
      ↓
Build Search
      ↓
Analyze Results
      ↓
Pivot
      ↓
Correlate
      ↓
Enrich
      ↓
Validate
      ↓
Scope
      ↓
Document
      ↓
Improve Detection
```

The final step is extremely important.

A successful hunt can produce a **new detection rule**.

---

# 5️⃣ Start with a Hypothesis

Don't begin with:

```text
"Let me search everything."
```

That creates enormous amounts of data.

Start with a focused hypothesis.

Example:

```text
I suspect that a compromised account may
be performing unusual authentication activity.
```

Then ask:

==> Which users?
==> Which hosts?
==> Which source IPs?
==> What time period?
==> What authentication methods?
==> What behavior is unusual?

---

# 6️⃣ Types of Threat Hunting

Common hunting approaches include:

### 🔎 IOC Hunting

Search for known indicators.

```text
IP
Domain
URL
Hash
Email
```

---

### 🧠 TTP Hunting

Search for attacker behavior associated with techniques.

```text
PowerShell
Credential Access
Persistence
Lateral Movement
Command Execution
```

---

### 👤 User Hunting

Investigate unusual user behavior.

```text
Login time
Source location
Device
Privilege
Authentication failures
```

---

### 🖥️ Host Hunting

Look for suspicious host behavior.

```text
New process
New service
Unexpected connection
Privilege change
Unusual login
```

---

### 🌐 Network Hunting

Analyze:

```text
DNS
Firewall
Proxy
VPN
NetFlow
IDS/IPS
```

---

# 7️⃣ IOC Hunting

IOC means **Indicator of Compromise**.

Examples:

==> Malicious IP
==> Malicious domain
==> URL
==> File hash
==> Email address

Suppose you have:

```text
Suspicious IP:
203.0.113.50
```

A hunter may search:

```text
src_ip = "203.0.113.50"
OR
dst_ip = "203.0.113.50"
```

Then investigate:

==> Which systems communicated with it?
==> When?
==> How frequently?
==> Which user was involved?
==> Which process generated the traffic?
==> Was there related DNS activity?

---

# 8️⃣ Historical IOC Hunting

One powerful feature of a SIEM is historical search.

Suppose an IP is identified as malicious today.

Don't only search:

```text
Today
```

Search historical data according to your retention period.

Example:

```text
Last 30 days
```

Then determine:

```text
First Seen
Last Seen
Total Connections
Affected Hosts
Affected Users
```

This helps determine potential scope.

---

# 9️⃣ TTP Hunting

IOC hunting depends on known indicators.

TTP hunting focuses on attacker behavior.

For example:

```text
Suspicious PowerShell
```

Instead of searching only for one known hash or IP, search for behaviors such as:

==> Encoded commands
==> Unusual PowerShell execution
==> Suspicious parent-child processes
==> Unexpected network connections
==> Unusual users executing PowerShell

This can help identify previously unknown infrastructure.

---

# 🔟 MITRE ATT&CK and Threat Hunting

MITRE ATT&CK provides a useful framework for describing adversary behavior.

A hunter can start with:

```text
Tactic
 ↓
Technique
 ↓
Expected Behavior
 ↓
Required Data
 ↓
SIEM Search
```

For example:

```text
Execution
 ↓
PowerShell
 ↓
PowerShell execution
 ↓
Windows process logs
 ↓
SIEM query
```

The exact data required depends on the environment.

---

# 1️⃣1️⃣ Data Sources for Threat Hunting

A SIEM hunter may use:

### Endpoint

==> Windows Security Logs
==> Sysmon
==> Linux audit logs
==> EDR

### Network

==> Firewall
==> IDS/IPS
==> DNS
==> Proxy
==> NetFlow

### Identity

==> Active Directory
==> VPN
==> SSO
==> MFA
==> Cloud Identity

### Application

==> Web Server
==> Database
==> API Gateway
==> Application logs

The more useful telemetry available, the more hunting possibilities exist.

---

# 1️⃣2️⃣ Search Strategy

A good hunt usually moves:

```text
Broad
 ↓
Narrow
 ↓
Pivot
 ↓
Correlate
 ↓
Deep Investigation
```

Example:

```text
All authentication events
        ↓
Unusual login hours
        ↓
Specific user
        ↓
Specific source IP
        ↓
Related host activity
        ↓
Process activity
        ↓
Network activity
```

Don't immediately search millions of events with complicated logic.

Start small and expand based on evidence.

---

# 1️⃣3️⃣ Time-Based Hunting

Time is one of the most important dimensions in SIEM investigations.

Example:

```text
12:00
Login

12:03
PowerShell

12:05
Privilege Change

12:08
Network Connection
```

A timeline can reveal relationships that individual events do not show.

Always ask:

```text
What happened before?
What happened during?
What happened after?
```

---

# 1️⃣4️⃣ Baseline Hunting

Threat hunters should understand normal behavior.

Example:

```text
User A
Normally:
08:30–18:00
Corporate Network
Laptop-01
```

Suddenly:

```text
02:15
New Device
External IP
Administrative Login
```

This is an anomaly worth investigating.

But remember:

**Anomaly ≠ confirmed attack.**

The analyst must validate the context.

---

# 1️⃣5️⃣ User Behavior Hunting

Consider:

```text
Username
Source IP
Host
Login Time
Authentication Method
Privilege
Application
```

Example:

```text
User: admin01

Normal:
10 logins/day

Observed:
150 login attempts/day
```

Questions:

==> Is this legitimate?
==> Was the password recently changed?
==> Is an application generating the activity?
==> Is the account under attack?
==> Was there a successful login afterward?

---

# 1️⃣6️⃣ Host-Based Hunting

A hunter can investigate unusual hosts.

Example:

```text
SERVER-01
```

Search:

```text
Process Activity
Authentication
Network Connections
File Changes
Service Changes
Privilege Changes
```

Then build a timeline.

```text
Login
 ↓
Process
 ↓
Privilege Change
 ↓
Network Connection
```

This provides stronger context.

---

# 1️⃣7️⃣ Process Hunting

Process telemetry can provide valuable information.

Useful fields:

```text
process_name
parent_process
command_line
user
hostname
timestamp
```

Example:

```text
Parent:
winword.exe

Child:
powershell.exe
```

This relationship may deserve investigation depending on the environment and context.

The key is not simply:

```text
PowerShell = malicious
```

Instead:

```text
Who?
What?
When?
Where?
Parent process?
Command line?
Network activity?
```

---

# 1️⃣8️⃣ Network Threat Hunting

Network hunting can investigate:

==> Rare destinations
==> High-volume connections
==> Unusual ports
==> Multiple destination hosts
==> DNS anomalies
==> Repeated failed connections
==> Unexpected outbound traffic

Example:

```text
Host-01
 ↓
100 different external IPs
 ↓
within 10 minutes
```

Investigate:

==> What process created the connections?
==> Is the destination legitimate?
==> Is this normal for the host?
==> What DNS requests occurred?

---

# 1️⃣9️⃣ DNS Hunting

DNS is extremely useful for threat hunting.

Search for:

==> Rare domains
==> Newly observed domains
==> High-frequency queries
==> Suspicious query patterns
==> Unexpected external domains

Example:

```text
Host-01
 ↓
Rare Domain
 ↓
DNS Query
 ↓
Connection
```

Correlating DNS with firewall and endpoint data can provide additional context.

---

# 2️⃣0️⃣ Authentication Hunting

Authentication hunting is especially useful for detecting account compromise.

Look for:

```text
Failed Login
Successful Login
New Source
New Device
Unusual Time
Privilege Change
```

Example:

```text
20 Failed Logins
      ↓
Successful Login
      ↓
New Device
      ↓
Administrative Activity
```

This creates a useful investigation hypothesis.

---

# 2️⃣1️⃣ Impossible Travel / Abnormal Location

A user's authentication activity may show:

```text
Login A
Location A
10:00

Login B
Location B
10:20
```

If the locations or network paths are inconsistent with realistic travel, this may require investigation.

However, VPNs, proxies, cloud services, mobile networks, and corporate gateways can create misleading locations.

Therefore:

**Impossible travel should be treated as an investigation signal, not automatic proof of compromise.**

---

# 2️⃣2️⃣ Threat Hunting with Multiple Data Sources

A strong hunt often combines multiple sources.

Example:

```text
Authentication
      +
Endpoint
      +
DNS
      +
Firewall
```

Suppose:

```text
Authentication:
Unusual login

Endpoint:
Suspicious process

DNS:
Rare domain

Firewall:
Outbound connection
```

Together, these events provide stronger context than any single source.

---

# 2️⃣3️⃣ Pivoting

Pivoting means moving from one finding to another related piece of evidence.

Example:

```text
Suspicious IP
     ↓
Affected Host
     ↓
Affected User
     ↓
Process
     ↓
DNS
     ↓
Other Hosts
```

Another example:

```text
Suspicious User
     ↓
Login Events
     ↓
Hosts
     ↓
Processes
     ↓
Network Connections
```

Pivoting is one of the most important SIEM investigation skills.

---

# 2️⃣4️⃣ Entity Relationship Hunting

Think about relationships:

```text
User
 ↓
Host
 ↓
Process
 ↓
IP
 ↓
Domain
 ↓
External Service
```

This can be represented as:

```text
admin01
   |
   +---- SERVER-01
             |
             +---- powershell.exe
                       |
                       +---- 203.0.113.50
```

This relationship-based thinking makes complex investigations easier.

---

# 2️⃣5️⃣ Threat Intelligence Enrichment

Threat Intelligence can add context to hunting.

Example:

```text
Observed IP
     ↓
Threat Intelligence Lookup
     ↓
Reputation / Context
     ↓
Historical Activity
     ↓
Investigation
```

But threat intelligence should not be treated as absolute truth.

Consider:

==> Source reputation
==> Confidence
==> Age
==> Expiration
==> Context
==> Multiple sources

---

# 2️⃣6️⃣ Hunt Results

A hunt can produce several outcomes.

### Outcome 1 — No Suspicious Activity

```text
No relevant evidence found.
```

This is still useful because it documents the hypothesis and search scope.

### Outcome 2 — Suspicious Activity

```text
Suspicious activity found.
```

Continue investigation.

### Outcome 3 — Confirmed Incident

```text
Evidence supports malicious activity.
```

Follow incident response procedures.

### Outcome 4 — Detection Gap

You discover behavior that existing rules did not detect.

This should lead to:

```text
New Detection
 ↓
Testing
 ↓
Deployment
```

---

# 2️⃣7️⃣ Threat Hunting → Detection Engineering

One of the strongest outcomes of hunting is creating new detections.

Example:

```text
Threat Hunt
     ↓
Suspicious PowerShell Pattern
     ↓
Repeated Observation
     ↓
Detection Logic
     ↓
Rule
     ↓
Testing
     ↓
Production Detection
```

This creates a continuous improvement cycle:

```text
Hunt
 ↓
Discover
 ↓
Detect
 ↓
Monitor
 ↓
Hunt Again
```

---

# 2️⃣8️⃣ Practical Hunt — SSH Activity

Suppose you want to investigate SSH activity.

Start with:

```text
Authentication logs
```

Search:

```text
SSH login
```

Then identify:

```text
Source IP
Username
Destination Host
Success/Failure
Timestamp
```

Next:

```text
Top source IPs
```

Then:

```text
Failed login count
```

Then:

```text
Successful login after failures
```

Then:

```text
Post-login activity
```

Finally:

```text
sudo
process
network
file
```

This is a real hunting workflow.

---

# 2️⃣9️⃣ Practical Hunt — Suspicious PowerShell

Start with:

```text
PowerShell events
```

Then analyze:

```text
User
Host
Parent Process
Command Line
Timestamp
Destination
```

Pivot into:

```text
Network Connections
```

Then:

```text
DNS
```

Then:

```text
Authentication
```

Finally determine:

```text
Normal
Suspicious
Malicious
Unknown
```

---

# 3️⃣0️⃣ Practical Hunt — Lateral Movement

Start with remote authentication:

```text
RDP
SSH
SMB
WinRM
VPN
```

Then ask:

```text
Which user?
Which source host?
Which destination?
How many destinations?
Was the behavior normal?
What happened after login?
```

Example:

```text
User A
 ↓
Host 01
 ↓
Host 02
 ↓
Host 03
 ↓
Host 04
```

Multiple remote connections in a short period may warrant investigation depending on the user's role and normal behavior.

---

# 3️⃣1️⃣ Threat Hunting Query Design

A good query should be:

==> Focused
==> Understandable
==> Reusable
==> Efficient
==> Documented

Start with a simple query.

Then add:

```text
Time
 ↓
User
 ↓
Host
 ↓
IP
 ↓
Process
 ↓
Network
```

Avoid writing one huge query before understanding the data.

---

# 3️⃣2️⃣ Hunting Notebook

Maintain a hunting record.

Example:

```text
Hunt ID:
TH-2026-001

Hypothesis:
Possible compromised privileged account

Data Sources:
Authentication
Endpoint
Firewall

Time Range:
30 Days

Queries:
...

Findings:
...

Affected Entities:
...

Evidence:
...

Verdict:
...

Detection Gap:
...

New Detection:
...

Analyst:
...

Date:
...
```

This improves repeatability and knowledge sharing.

---

# 3️⃣3️⃣ Threat Hunting Metrics

Threat hunting should not be measured only by the number of hunts.

Useful metrics include:

==> Hunts completed
==> Suspicious findings
==> Confirmed incidents
==> Detection gaps discovered
==> New detections created
==> Existing detections improved
==> Time spent per hunt
==> Data sources used
==> Coverage improvements

A hunt that finds a detection gap can be valuable even when no incident is discovered.

---

# 3️⃣4️⃣ Common Threat Hunting Mistakes

Avoid:

==> Searching without a hypothesis
==> Searching too much data at once
==> Ignoring normal behavior
==> Trusting one IOC blindly
==> Ignoring historical data
==> Not correlating data sources
==> Not documenting findings
==> Treating anomalies as confirmed attacks
==> Never converting findings into detections
==> Ignoring query performance

---

# 3️⃣5️⃣ Threat Hunting Lab

You can create a practical lab with:

```text
Wazuh
Linux VM
Windows VM
Firewall
Syslog
Network Traffic
```

### Hunt 01

Investigate:

```text
SSH Failed Login
```

### Hunt 02

Investigate:

```text
Successful Login After Multiple Failures
```

### Hunt 03

Investigate:

```text
Unusual PowerShell Activity
```

### Hunt 04

Investigate:

```text
New Privileged Account Activity
```

### Hunt 05

Investigate:

```text
One Host Connecting to Many Destinations
```

### Hunt 06

Investigate:

```text
Rare DNS Domains
```

For each hunt:

```text
Hypothesis
 ↓
Query
 ↓
Evidence
 ↓
Pivot
 ↓
Correlation
 ↓
Verdict
 ↓
Detection Improvement
```

---

# 3️⃣6️⃣ SIEM Engineer Interview Questions

### Q1. What is Threat Hunting?

**Answer:**

Threat Hunting is a proactive process of searching security data for suspicious or malicious activity that may not have generated an existing SIEM alert.

---

### Q2. What is the difference between Threat Hunting and Alert Investigation?

**Answer:**

Alert investigation starts with an existing security alert, while threat hunting starts with a hypothesis or security question and searches available data proactively.

---

### Q3. What is IOC hunting?

**Answer:**

IOC hunting searches SIEM and security telemetry for known indicators such as malicious IPs, domains, URLs, hashes, or other indicators.

---

### Q4. What is TTP hunting?

**Answer:**

TTP hunting focuses on attacker behaviors and techniques rather than depending only on known indicators.

---

### Q5. How do you start a threat hunt?

**Answer:**

I start by defining a clear objective and hypothesis, identify the required data sources, validate the available fields, create focused queries, analyze results, pivot into related evidence, correlate events, and document the findings.

---

### Q6. Why is historical data important?

**Answer:**

Historical data can reveal previous activity associated with a newly discovered IOC, account, host, or behavior and helps determine the potential scope and timeline.

---

### Q7. What do you do when a hunt discovers suspicious activity?

**Answer:**

I preserve the relevant evidence, investigate the scope and context, determine whether the activity is benign, suspicious, or malicious, and follow the organization's incident response process when appropriate.

---

### Q8. How can Threat Hunting improve SIEM?

**Answer:**

Threat hunting can identify detection gaps, improve existing rules, create new detections, identify missing telemetry, and improve overall detection coverage.

---

### Q9. Why is baseline important in threat hunting?

**Answer:**

A baseline helps distinguish unusual behavior from normal operational activity. It provides context for determining whether an observed deviation deserves further investigation.

---

### Q10. What is pivoting?

**Answer:**

Pivoting means moving from one investigation artifact to related evidence, such as moving from an IP to a host, then to a user, process, DNS activity, and network connections.

---

# 3️⃣7️⃣ Threat Hunting Checklist

Before completing a hunt:

```text
☑ Objective defined
☑ Hypothesis created
☑ Data sources identified
☑ Fields validated
☑ Time range defined
☑ Initial query created
☑ Baseline considered
☑ Historical data checked
☑ Pivot points identified
☑ Multiple data sources correlated
☑ Threat Intelligence considered
☑ Evidence documented
☑ Scope evaluated
☑ Verdict recorded
☑ Detection gap considered
☑ New detection identified
☑ Final report completed
```

---

# 3️⃣8️⃣ Complete Threat Hunting Flow

Remember this flow:

```text
Threat Hypothesis
       ↓
Data Sources
       ↓
SIEM Search
       ↓
Initial Finding
       ↓
Pivot
       ↓
Correlation
       ↓
Enrichment
       ↓
Timeline
       ↓
Scope
       ↓
Evidence
       ↓
Verdict
       ↓
Detection Improvement
       ↓
Documentation
```

---

# 🎯 Final Takeaway

A SIEM Engineer should not think only in terms of:

```text
"Which alert fired?"
```

A mature security mindset also asks:

```text
"What could be happening that we are not detecting?"
```

Threat Hunting helps answer that question.

Remember:

==> **IOC Hunting** finds known indicators.
==> **TTP Hunting** finds attacker behavior.
==> **Behavioral Hunting** finds abnormal activity.
==> **Historical Hunting** finds previous exposure.
==> **Correlation** connects separate events.
==> **Pivoting** expands the investigation.
==> **Detection Engineering** turns hunting knowledge into repeatable detection.

The strongest SIEM workflow is not:

```text
Alert → Investigation → Close
```

It is:

```text
Alert
 ↓
Investigation
 ↓
Threat Hunt
 ↓
Detection Gap
 ↓
New Detection
 ↓
Continuous Improvement
```

---

## 📚 SIEM Engineer Learning Series

**Previous:** #14 — Advanced Detection Engineering

**Current:** #15 — Threat Hunting with SIEM

**Next:** #16 — SIEM Data Quality & Troubleshooting

---

## 🔐 Practical Security Takeaway

**Don't wait for every threat to generate an alert.**

Build the habit of asking:

```text
What behavior should I expect?
What behavior is unusual?
What evidence do I have?
What else is connected?
What happened before and after?
What detection gap did I discover?
```

That is the mindset of a **Threat Hunter + SIEM Engineer**.

---

**Follow the SIEM Engineer learning series — Boni Yeamin**

