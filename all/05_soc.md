# SIEM Engineer #05 — Query & Investigation

## 🟢 Introduction

A SIEM collects and stores huge amounts of security data.

But collecting logs is only the beginning.

A SIEM Engineer and SOC Analyst must be able to **search, filter, correlate, analyze, and investigate** that data.

This is where **Query & Investigation** becomes important.

A simple security investigation looks like:

**Alert → Search → Filter → Correlate → Timeline → Evidence → Verdict**

If you know how to write good SIEM queries, you can investigate incidents much faster.

---

# 🧠 1. What is Query & Investigation?

**Query** means asking the SIEM for specific information from collected data.

For example:

```text
Show me all failed logins from 10.10.10.50
during the last 30 minutes.
```

The SIEM searches the available data and returns matching events.

**Investigation** goes further.

You ask:

```text
Who?
What?
When?
Where?
How?
Why?
What happened before?
What happened after?
```

The goal is to understand the complete activity.

---

# 🎯 2. Why Query Skills Matter

Imagine your SIEM contains:

```text
10,000,000 events
```

An alert says:

```text
Multiple failed login attempts
```

You cannot manually read 10 million events.

Instead, you query:

```text
source_ip = suspicious IP
username = affected user
time = incident window
event_type = authentication failure
```

Then you gradually expand the investigation.

### 💡 Why does this matter?

Good query skills help you:

- Investigate alerts faster

- Find related events

- Build incident timelines

- Perform threat hunting

- Validate detections

- Identify false positives

- Find suspicious behavior

- Collect evidence

---

# 🔎 3. The Basic Investigation Questions

During an investigation, start with:

### WHO?

```text
Which user?
Which account?
Which process?
Which administrator?
```

### WHAT?

```text
What happened?
What event occurred?
What command was executed?
```

### WHEN?

```text
Exact timestamp?
First event?
Last event?
Duration?
```

### WHERE?

```text
Source IP?
Destination IP?
Hostname?
Geographic location?
```

### HOW?

```text
How did the activity happen?
Which protocol?
Which process?
Which authentication method?
```

### WHY?

This is usually the most difficult question.

You should not assume the reason.

Use available evidence to determine whether the activity was:

```text
Expected
Benign
Suspicious
Malicious
Unknown
```

---

# 🧩 4. Query Building Fundamentals

Most SIEM queries use some combination of:

```text
Search
Filter
Fields
Aggregation
Grouping
Sorting
Time Range
Correlation
```

Conceptually:

```text
Raw Events
    ↓
Filter
    ↓
Select Fields
    ↓
Group
    ↓
Count
    ↓
Sort
    ↓
Investigate
```

---

# ⏰ 5. Time Range

Time is one of the most important investigation fields.

For example:

```text
14:00 → Alert
```

Don't only investigate the exact alert timestamp.

Check:

```text
13:00 → 15:00
```

You may discover:

```text
13:20  Initial login
13:35  Failed authentication
13:42  Successful login
13:47  Privilege change
13:52  Process execution
14:00  SIEM alert
14:10  Network connection
```

Now you have a timeline.

---

# 📅 6. Investigation Timeline

A timeline helps explain an incident.

Example:

```text
10:00
   ↓
Failed Login

10:02
   ↓
Failed Login

10:04
   ↓
Successful Login

10:06
   ↓
New Process

10:08
   ↓
Privilege Change

10:10
   ↓
Outbound Connection
```

The individual events become more meaningful when placed together.

---

# 🔥 7. Splunk SPL

Splunk uses **Search Processing Language (SPL)**.

A simple search:

```spl
index=security
```

Filter:

```spl
index=security source_ip="10.10.10.50"
```

Filter by event:

```spl
index=security event_type="authentication_failure"
```

Count events:

```spl
index=security event_type="authentication_failure"
| stats count
```

Group by source IP:

```spl
index=security event_type="authentication_failure"
| stats count by source_ip
```

Sort:

```spl
index=security event_type="authentication_failure"
| stats count by source_ip
| sort - count
```

The basic idea is:

```text
Search
  ↓
Filter
  ↓
Aggregate
  ↓
Sort
```

---

# ☁️ 8. Microsoft Sentinel and KQL

Microsoft Sentinel commonly uses **Kusto Query Language (KQL)**.

Example:

```kql
SigninLogs
| where ResultType != 0
```

Group authentication failures:

```kql
SigninLogs
| where ResultType != 0
| summarize count() by IPAddress
```

Sort:

```kql
SigninLogs
| where ResultType != 0
| summarize FailedAttempts=count() by IPAddress
| order by FailedAttempts desc
```

The concept is similar:

```text
Table
 ↓
Filter
 ↓
Aggregate
 ↓
Sort
```

---

# 🔍 9. Elasticsearch / OpenSearch Query

Elastic and OpenSearch investigations commonly use field-based searches and query DSL.

Conceptually:

```text
event.action = authentication_failure
```

Then filter by:

```text
source.ip
user.name
host.name
@timestamp
```

You may also use aggregations to identify:

```text
Top source IPs
Top users
Top destinations
Event counts
```

The exact syntax depends on the interface and query language being used.

---

# 🛡️ 10. Wazuh Investigation

In Wazuh, an analyst may investigate:

```text
Rule ID
Agent
Timestamp
Source IP
Username
Location
Event
MITRE ATT&CK information
```

A useful investigation process is:

```text
Wazuh Alert
    ↓
Open Alert Details
    ↓
Identify Source
    ↓
Check Related Events
    ↓
Check Host
    ↓
Check User
    ↓
Check Timeline
    ↓
Determine Verdict
```

---

# 🧱 11. Filtering

Filtering is one of the most important query skills.

Suppose you have:

```text
1,000,000 events
```

You can reduce the dataset by filtering.

Example:

```text
event_type = authentication_failure
```

Then:

```text
source_ip = specific IP
```

Then:

```text
username = specific account
```

Then:

```text
hostname = specific server
```

Now the investigation becomes manageable.

---

# 🎯 12. Field Selection

Do not always return every field.

For authentication investigation, useful fields may be:

```text
timestamp
username
source_ip
destination_ip
hostname
event_type
status
logon_type
```

For process investigation:

```text
timestamp
username
hostname
process_name
parent_process
command_line
process_id
```

For network investigation:

```text
timestamp
source_ip
destination_ip
source_port
destination_port
protocol
action
bytes
```

Selecting useful fields makes investigations easier to understand.

---

# 📊 13. Aggregation

Aggregation converts many events into useful statistics.

Example:

```text
Authentication Failures:

10.10.10.10 → 5
10.10.10.20 → 12
10.10.10.30 → 97
```

This immediately tells you which source deserves further investigation.

Common aggregation concepts include:

- Count

- Sum

- Average

- Minimum

- Maximum

- Distinct count

- Group by

---

# 👤 14. Group By

Suppose you have:

```text
User A → 10 failures
User B → 2 failures
User C → 75 failures
```

Grouping by username can highlight unusual accounts.

Similarly, group by:

```text
source_ip
destination_ip
username
hostname
process_name
parent_process
```

The correct grouping depends on the investigation question.

---

# 🔗 15. Correlation

One event rarely tells the complete story.

Suppose:

```text
Authentication Failure
```

Then:

```text
Successful Login
```

Then:

```text
Privilege Change
```

Then:

```text
Suspicious Process
```

Correlation connects these events.

Conceptually:

```text
Event A
 +
Event B
 +
Event C
 +
Event D
 ↓
Investigation Story
```

---

# 🧠 16. Pivoting

**Pivoting** means using information from one event to search for related activity.

Example:

You receive:

```text
Source IP:
10.10.10.50
```

Pivot:

```text
Search all activity from 10.10.10.50
```

You discover:

```text
User:
admin
```

Pivot again:

```text
Search all activity by admin
```

You discover:

```text
Hostname:
SERVER-01
```

Pivot again:

```text
Search SERVER-01 activity
```

This creates an investigation chain.

---

# 🔄 17. Investigation Pivot Example

Start:

```text
Alert
 ↓
Source IP
 ↓
Username
 ↓
Hostname
 ↓
Process
 ↓
Destination IP
 ↓
Threat Intelligence
 ↓
Related Alerts
```

This is a fundamental SOC investigation technique.

---

# 🌐 18. IP Investigation

Suppose an alert contains:

```text
source_ip = 203.x.x.x
```

You may investigate:

- How many connections?

- Which internal systems contacted it?

- Which ports?

- When did communication begin?

- Which users were involved?

- Was it seen before?

- Is it associated with known threat intelligence?

Do not conclude that an IP is malicious based only on one indicator.

Context matters.

---

# 👤 19. User Investigation

For a suspicious account:

```text
username = admin
```

Search:

```text
All authentication events
All failed logins
All successful logins
Privilege changes
Process activity
Endpoint activity
Network activity
```

Then construct:

```text
User Timeline
```

Example:

```text
09:00 Login
09:05 Failed authentication
09:07 Successful authentication
09:10 Privilege change
09:12 Process execution
09:15 Network connection
```

---

# 💻 20. Host Investigation

For a suspicious host:

```text
hostname = SERVER-01
```

Investigate:

- Authentication

- Processes

- Network connections

- File activity

- Privilege changes

- Security alerts

- Endpoint detections

- Configuration changes

This helps determine whether the host is affected or simply generated an alert.

---

# ⚙️ 21. Process Investigation

For endpoint activity, look at:

```text
Process Name
Parent Process
User
Command Line
Path
Timestamp
Host
Network Activity
```

The **parent-child relationship** can be particularly useful.

Example:

```text
Process A
   ↓
Process B
   ↓
Process C
```

Unexpected process relationships may deserve investigation.

But again:

**Unusual does not automatically mean malicious.**

---

# 🔐 22. Authentication Investigation

Authentication investigations often involve:

```text
User
Source IP
Destination Host
Authentication Result
Logon Type
Timestamp
Location
Device
```

Questions:

- Was the login successful?

- Was the account expected?

- Was the source known?

- Was the destination expected?

- Were there repeated failures?

- Was there a privilege change afterward?

---

# 🚨 23. Alert Investigation

When receiving a SIEM alert, do not immediately close it.

Use a structured process:

```text
Alert
 ↓
Understand Detection
 ↓
Validate Event
 ↓
Identify Assets
 ↓
Identify Users
 ↓
Search Related Events
 ↓
Build Timeline
 ↓
Check Threat Intelligence
 ↓
Determine Scope
 ↓
Determine Verdict
 ↓
Document
```

---

# 🧪 24. True Positive vs False Positive

After investigation, classify the alert according to your SOC process.

### True Positive

The detection identified the intended suspicious/malicious behavior.

### False Positive

The detection fired, but the activity was not the behavior it was intended to identify.

### Benign / Expected

The activity is legitimate and expected.

### Unknown

There is insufficient evidence to confidently determine the nature of the activity.

The exact verdict categories depend on the organization's SOC process.

---

# 🔎 25. Threat Hunting

Threat hunting is proactive.

Traditional workflow:

```text
Alert
 ↓
Investigation
```

Threat hunting:

```text
Hypothesis
 ↓
Query
 ↓
Search Environment
 ↓
Find Evidence
 ↓
Investigate
```

Example hypothesis:

> “There may be unusual authentication activity against privileged accounts.”

Then search:

```text
Privileged accounts
+
Authentication failures
+
Authentication successes
+
Source IPs
+
Time patterns
```

---

# 🎯 26. Threat Hunting Questions

Good hunters ask questions such as:

- Which accounts have unusual login behavior?

- Which systems have unexpected outbound connections?

- Which hosts are communicating with suspicious destinations?

- Which users suddenly have privilege changes?

- Which processes are rarely observed?

- Which authentication failures are increasing?

- Which systems have missing security telemetry?

---

# 🧭 27. Query → Hypothesis → Evidence

Do not search randomly.

Use:

```text
Hypothesis
    ↓
Required Evidence
    ↓
Query
    ↓
Results
    ↓
Analysis
```

Example:

```text
Hypothesis:
An account may have unusual login activity.

Required Evidence:
Login time
Source IP
Destination host
Login result
Historical behavior

Query:
Search authentication events.

Result:
Multiple unusual login events.

Next:
Pivot into source IP and host.
```

---

# ⏱️ 28. Time-Based Investigation

Always think about:

```text
Before
During
After
```

If an alert occurred at:

```text
15:00
```

Investigate:

```text
Before:
What happened before the alert?

During:
What happened when the alert triggered?

After:
What happened after the alert?
```

This can reveal the attack chain or explain why the detection fired.

---

# 🧩 29. Baseline Analysis

You need to understand normal behavior.

Example:

```text
User normally:
Login 09:00–18:00

Observed:
Login at 03:30
```

This is unusual.

But you should investigate context:

```text
Was the user on-call?
Was it a scheduled task?
Was VPN involved?
Was the device known?
Was there an approved activity?
```

Baseline is useful, but unusual behavior is not automatically malicious.

---

# 📈 30. Statistical Investigation

Queries can help identify unusual volumes.

Example:

```text
Normal:
20 events/hour

Current:
800 events/hour
```

This may indicate:

- Misconfiguration

- System issue

- Scanning

- Attack activity

- Logging problem

The query identifies the anomaly.

Investigation determines the cause.

---

# 🔥 31. Example — Investigating SSH Brute Force

Alert:

```text
Multiple SSH Authentication Failures
```

### Step 1

Identify:

```text
Source IP
Destination Host
Username
Time
```

### Step 2

Search all events from the source IP.

```text
Source IP
     ↓
All related authentication events
```

### Step 3

Check whether a successful login occurred.

```text
Failed
Failed
Failed
Successful
```

This changes the investigation priority.

### Step 4

Search activity after successful login.

```text
Login
 ↓
Process
 ↓
Privilege
 ↓
Network
```

### Step 5

Determine scope.

```text
One host?
Multiple hosts?
One account?
Multiple accounts?
```

### Step 6

Document findings.

---

# 🪟 32. Example — Windows Account Investigation

Alert:

```text
Multiple Authentication Failures
```

Search:

```text
username
source_ip
hostname
event_id
logon_type
timestamp
```

Then ask:

```text
Was there a successful login?
Was the account privileged?
Was the source device known?
Were other systems targeted?
Did privilege changes occur?
```

---

# 🛡️ 33. Example — Suspicious Process Investigation

Alert:

```text
Suspicious Process Activity
```

Collect:

```text
Process
Parent Process
User
Host
Command Line
Timestamp
Network Activity
```

Then search:

```text
What happened before process creation?
What happened after?
Were similar processes observed elsewhere?
Did the same user perform related activity?
```

---

# 🔗 34. IOC Investigation

Indicators can include:

```text
IP
Domain
URL
Hash
Email
Username
Hostname
```

Suppose you receive a suspicious hash.

Search:

```text
hash = X
```

Then:

```text
Which hosts?
Which users?
When observed?
How many times?
What process?
What network connections?
```

This determines the scope of the IOC.

---

# 📊 35. Search Broad → Narrow

A useful investigation strategy is:

```text
Broad Search
    ↓
Identify Pattern
    ↓
Narrow Search
    ↓
Pivot
    ↓
Correlate
    ↓
Confirm
```

Do not begin with an extremely narrow query if you don't yet understand the event.

You may accidentally exclude important evidence.

---

# 🚫 36. Common Query Mistakes

### Mistake 1 — Wrong Time Range

You may miss the initial activity.

### Mistake 2 — Wrong Field

For example:

```text
src_ip
```

when your normalized field is:

```text
source.ip
```

### Mistake 3 — Case Sensitivity

Some systems or fields may behave differently depending on query syntax.

### Mistake 4 — Searching Only One Event

The surrounding events may contain the real story.

### Mistake 5 — Ignoring Normal Activity

You may incorrectly classify legitimate administrative activity.

### Mistake 6 — Overly Broad Queries

Searching everything can create:

```text
Slow Query
Huge Result
Analyst Confusion
```

---

# ⚡ 37. Query Performance

A SIEM Engineer must care about query performance.

Poor queries can create:

```text
High CPU
High Memory
Slow Search
High Storage/Compute Cost
Delayed Investigation
```

Good practices:

- Use appropriate time ranges

- Filter early

- Search relevant indexes/data sources

- Select necessary fields

- Avoid unnecessary expensive operations

- Use indexed/search-optimized fields where applicable

- Test queries before production use

---

# 📚 38. Query Language Skills

A SIEM Engineer should become comfortable with the query language of their platform.

### Splunk

**SPL**

### Microsoft Sentinel

**KQL**

### QRadar

**AQL**

### Elastic

**KQL / ES|QL / Query DSL**, depending on the workflow

### OpenSearch

**DQL / Query DSL**, depending on the interface and configuration

The syntax differs.

The investigation mindset remains similar.

---

# 🧠 39. Query Skill Progression

Learn in this order:

```text
1. Basic Search
      ↓
2. Filtering
      ↓
3. Fields
      ↓
4. Sorting
      ↓
5. Aggregation
      ↓
6. Grouping
      ↓
7. Time Windows
      ↓
8. Correlation
      ↓
9. Sub-search / Advanced Logic
      ↓
10. Threat Hunting
```

Do not try to memorize everything at once.

Understand the logic first.

---

# 🧪 40. Practical SIEM Lab

Build a lab with:

```text
Windows VM
Linux VM
Wazuh / SIEM
Firewall Logs
Authentication Logs
Process Logs
```

Create alerts and investigate them.

### Lab 1

Search failed SSH authentication.

### Lab 2

Find top source IPs.

### Lab 3

Find top targeted usernames.

### Lab 4

Find successful login after multiple failures.

### Lab 5

Build a timeline around the login.

### Lab 6

Pivot from IP → User → Host.

### Lab 7

Search related alerts.

### Lab 8

Document the final verdict.

---

# 📋 41. Investigation Checklist

Use this checklist during an alert investigation:

```text
[ ] Read the alert carefully

[ ] Understand why the detection triggered

[ ] Record timestamp

[ ] Identify source IP

[ ] Identify destination

[ ] Identify username

[ ] Identify hostname

[ ] Check related events

[ ] Search before the alert

[ ] Search after the alert

[ ] Check authentication activity

[ ] Check process activity

[ ] Check network activity

[ ] Check privilege changes

[ ] Check threat intelligence

[ ] Determine affected assets

[ ] Determine affected accounts

[ ] Determine scope

[ ] Decide verdict according to SOC process

[ ] Document evidence

[ ] Escalate if required

[ ] Provide detection feedback
```

---

# 🔄 42. Complete Investigation Flow

Remember this:

```text
Alert
 ↓
Validate
 ↓
Identify
 ↓
Search
 ↓
Filter
 ↓
Pivot
 ↓
Correlate
 ↓
Build Timeline
 ↓
Enrich
 ↓
Determine Scope
 ↓
Analyze Evidence
 ↓
Verdict
 ↓
Document
 ↓
Escalate / Close
```

This is one of the most important workflows for a SOC environment.

---

# 🎤 43. SIEM Engineer Interview Questions

### Q1. What is a SIEM query?

**Answer:**

A SIEM query is a structured search used to retrieve, filter, aggregate, correlate, or analyze security data stored in a SIEM platform.

---

### Q2. What is SPL?

**Answer:**

SPL stands for Search Processing Language and is used in Splunk to search and analyze machine-generated data.

---

### Q3. What is KQL?

**Answer:**

KQL stands for Kusto Query Language and is used across Microsoft security and Azure data-analysis workflows, including Microsoft Sentinel.

---

### Q4. What is pivoting?

**Answer:**

Pivoting means using information discovered from one event to search for related activity.

For example:

```text
IP → User → Host → Process → Network
```

---

### Q5. Why is time range important during investigation?

**Answer:**

Time range helps identify what happened before, during, and after an alert. A narrow time range may miss important related events.

---

### Q6. What is threat hunting?

**Answer:**

Threat hunting is a proactive process where analysts develop hypotheses and search security telemetry for evidence of suspicious activity that may not have generated an alert.

---

### Q7. How do you investigate a suspicious IP?

**Answer:**

I would identify where the IP appeared, which hosts communicated with it, which users were involved, when the activity occurred, what services or protocols were used, whether related events exist, and whether threat intelligence provides additional context.

---

### Q8. What is correlation?

**Answer:**

Correlation means connecting multiple related events or data sources to identify a larger security pattern.

---

### Q9. How do you investigate a suspicious login?

**Answer:**

I would examine the username, source IP, destination host, authentication result, timestamp, login type, historical activity, related authentication events, privilege changes, endpoint activity, and network activity.

---

### Q10. What is the difference between searching and investigating?

**Answer:**

Searching retrieves relevant data. Investigation analyzes that data, correlates related events, builds context, determines scope, and supports a security verdict.

---

# 🚀 44. Final Takeaway

A SIEM Engineer should not only know how to write queries.

They should know **how to think during an investigation**.

The key mindset is:

```text
Don't just search for events.

Understand the story behind the events.
```

A strong investigation follows:

**Question → Query → Evidence → Context → Correlation → Timeline → Verdict**

The most important skills are:

- SPL

- KQL

- Elasticsearch/OpenSearch Query

- Filtering

- Aggregation

- Correlation

- Pivoting

- Timeline Analysis

- Threat Hunting

- IOC Investigation

- Evidence-based Investigation

---

## 📚 SIEM Engineer Learning Series

**#01 — Log Management**

**#02 — SIEM Platforms**

**#03 — Log Integration**

**#04 — Detection Engineering**

**#05 — Query & Investigation ← You are here**

**#06 — SOC Operations → Next**

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

**← Previous Article: #04 — Detection Engineering**

**SIEM Engineer Index**

**Next Article: #06 — SOC Operations →**

---

