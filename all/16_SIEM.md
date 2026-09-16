# SIEM Engineer #16 — SIEM Data Quality & Troubleshooting

## 🛡️ Introduction

A SIEM is only as useful as the data it receives.

Imagine your SIEM has thousands of detection rules, dashboards, and correlation logic—but:

```text
Firewall logs are missing
Windows logs are delayed
Timestamps are incorrect
Events are duplicated
Fields are not parsed
```

Then even a well-designed SIEM may produce incorrect results.

This is why **SIEM Data Quality** is a critical responsibility for a SIEM Engineer.

A SIEM Engineer should be able to answer:

==> Are the logs arriving?
==> Are they complete?
==> Are they parsed correctly?
==> Are timestamps correct?
==> Are events duplicated?
==> Are important fields available?
==> Is there ingestion delay?
==> Are events being dropped?
==> Is the data trustworthy enough for detection?

---

# 1️⃣ What is SIEM Data Quality?

**SIEM Data Quality** means ensuring that security data entering and stored inside the SIEM is:

==> Available
==> Complete
==> Accurate
==> Timely
==> Correctly parsed
==> Properly normalized
==> Consistent
==> Searchable
==> Reliable

Think of the SIEM pipeline:

```text
Log Source
    ↓
Collection
    ↓
Transport
    ↓
Ingestion
    ↓
Parsing
    ↓
Normalization
    ↓
Enrichment
    ↓
Indexing
    ↓
Storage
    ↓
Search
    ↓
Detection
```

A problem at any stage can affect security operations.

---

# 2️⃣ 💡 Why does this matter?

Suppose a firewall stops sending logs.

The SIEM may show:

```text
No Firewall Alerts
```

A SOC Analyst might think:

```text
"No attack detected."
```

But the real situation could be:

```text
Firewall
   X
   ↓
No Logs
   ↓
No Detection
   ↓
No Alert
```

This is a **visibility problem**, not necessarily a security improvement.

Therefore:

> **No security event can sometimes mean no telemetry.**

---

# 3️⃣ Data Quality Dimensions

Important dimensions include:

### 1. Availability

Are the expected logs arriving?

### 2. Completeness

Are important fields and events present?

### 3. Accuracy

Does the data represent the real event correctly?

### 4. Timeliness

Are logs arriving without excessive delay?

### 5. Consistency

Are the same fields formatted consistently?

### 6. Uniqueness

Are events being duplicated?

### 7. Validity

Do values follow the expected format?

---

# 4️⃣ Common SIEM Data Problems

Common problems include:

```text
Missing Logs
Duplicate Logs
Parsing Failure
Timestamp Problems
Log Delay
Field Mapping Problems
Wrong Source Identification
Malformed Events
Encoding Problems
Dropped Events
Network Connectivity Problems
Certificate Problems
Authentication Problems
Storage Problems
```

A SIEM Engineer needs a structured troubleshooting approach.

---

# 5️⃣ The Data Troubleshooting Flow

Use this process:

```text
Problem Detected
      ↓
Identify Source
      ↓
Check Source Health
      ↓
Check Network
      ↓
Check Collector
      ↓
Check Ingestion
      ↓
Check Parsing
      ↓
Check Normalization
      ↓
Check Indexing
      ↓
Check Search
      ↓
Validate Detection
      ↓
Document Root Cause
```

Do not immediately change configuration.

First identify **where the data pipeline is failing**.

---

# 6️⃣ Missing Logs

One of the most common SIEM problems is:

```text
"Why are logs not coming?"
```

Possible causes:

==> Source service stopped
==> Agent stopped
==> Network problem
==> Firewall blocking traffic
==> Wrong destination
==> Authentication failure
==> Certificate problem
==> Collector failure
==> Parser problem
==> Storage problem
==> Queue overflow
==> Configuration error

---

# 7️⃣ Missing Log Troubleshooting

Suppose:

```text
Firewall logs stopped arriving.
```

Check:

### Step 1 — Source

Is the firewall generating logs?

```text
Firewall
 ↓
Logging Enabled?
```

### Step 2 — Destination

Is the firewall configured with the correct SIEM/collector destination?

### Step 3 — Network

Can the source communicate with the collector?

### Step 4 — Collector

Is the collector listening?

### Step 5 — Ingestion

Are events entering the SIEM?

### Step 6 — Parsing

Are the events being recognized?

### Step 7 — Search

Can you find the events?

This prevents random troubleshooting.

---

# 8️⃣ Source Health Monitoring

Every important log source should have health monitoring.

Example:

```text
Firewall-01
Expected:
Continuous logs

Observed:
No events for 30 minutes
```

This should create a health signal.

A SIEM should ideally monitor:

==> Last event time
==> Event count
==> EPS
==> Connection status
==> Agent status
==> Queue status
==> Error rate

---

# 9️⃣ Log Silence Detection

A useful operational detection is:

```text
Expected Log Source
        ↓
No Events
        ↓
Defined Time Period
        ↓
Health Alert
```

For example:

```text
Firewall-01
No events for 15 minutes
```

The exact threshold depends on the source.

This is sometimes called a **log source health** or **log silence** detection.

---

# 🔟 Duplicate Logs

Duplicate logs happen when the same event reaches the SIEM more than once.

Example:

```text
Original Event
      ↓
Collector A
      ↓
SIEM

Original Event
      ↓
Collector B
      ↓
SIEM
```

Now the same event may appear twice.

Possible causes:

==> Multiple forwarding paths
==> Misconfigured agents
==> Retry behavior
==> Collector duplication
==> Load-balancing issues
==> Replayed events

---

# 1️⃣1️⃣ Why Duplicate Logs Matter

Duplicates can affect:

==> Alert volume
==> EPS calculations
==> Storage
==> Dashboards
==> Correlation rules
==> Threshold detections
==> Incident investigation

Example:

Actual:

```text
5 failed logins
```

SIEM sees:

```text
10 events
```

A threshold rule might incorrectly trigger.

Therefore, duplicate detection is important.

---

# 1️⃣2️⃣ Detecting Duplicates

Useful fields may include:

```text
event_id
timestamp
source
host
message
hash
sequence_number
```

Conceptually:

```text
Same Event
+
Same Source
+
Same Timestamp
+
Same Identifier
```

may indicate duplication.

However, not every identical-looking event is necessarily a duplicate. Validate the source behavior first.

---

# 1️⃣3️⃣ Parsing Failure

Suppose the raw log is:

```text
<134>Sep 16 15:20:10 firewall01
src=10.10.10.20 dst=10.10.20.10 action=deny
```

But the SIEM cannot extract:

```text
src_ip
dst_ip
action
```

Then detection rules may fail.

This is a **parsing problem**.

---

# 1️⃣4️⃣ Why Parsing Matters

Raw:

```text
src=10.10.10.20
dst=10.10.20.10
action=deny
```

Normalized:

```text
source.ip = 10.10.10.20
destination.ip = 10.10.20.10
event.action = deny
```

Detection logic becomes easier when fields are normalized.

For example:

```text
source.ip
destination.ip
user.name
process.name
event.action
```

---

# 1️⃣5️⃣ Parsing Troubleshooting

When parsing fails:

```text
Raw Event
   ↓
Inspect Format
   ↓
Identify Pattern
   ↓
Check Parser
   ↓
Check Field Extraction
   ↓
Test Sample Logs
   ↓
Validate Fields
   ↓
Test Detection
```

Do not modify a parser without first examining real raw events.

---

# 1️⃣6️⃣ Field Mapping Problems

Different vendors may use different names.

Example:

```text
Vendor A:
src_ip

Vendor B:
sourceAddress

Vendor C:
source.ip
```

If your detection expects:

```text
source.ip
```

but the field is never mapped, the detection may not work.

Therefore, normalization is important.

---

# 1️⃣7️⃣ Timestamp Problems

Time is one of the most important parts of SIEM data.

A log may contain:

```text
Source Time:
15:00
```

But the SIEM may display:

```text
09:00
```

Possible causes:

==> Time zone mismatch
==> NTP problem
==> Incorrect parser
==> Timestamp format issue
==> Collector clock problem
==> Daylight-saving handling where applicable

---

# 1️⃣8️⃣ Why Timestamp Accuracy Matters

Consider:

```text
10:00 Login
10:02 PowerShell
10:05 Privilege Change
```

If timestamps are wrong:

```text
10:05 Login
09:50 PowerShell
10:20 Privilege Change
```

The investigation timeline becomes misleading.

This can affect:

==> Correlation
==> Sequence detection
==> Incident investigation
==> Threat hunting
==> Root-cause analysis

---

# 1️⃣9️⃣ Time Synchronization

Important systems should use reliable time synchronization.

Conceptually:

```text
NTP
 ↓
Firewall
Server
Windows
Linux
Collector
SIEM
```

All systems should maintain consistent time.

A SIEM Engineer should monitor:

==> Clock drift
==> Time zone configuration
==> NTP synchronization
==> Timestamp parsing

---

# 2️⃣0️⃣ Log Latency

**Log latency** means the delay between when an event occurs and when it becomes available for analysis.

Example:

```text
Event occurs:
10:00:00

SIEM receives:
10:00:03
```

Latency:

```text
3 seconds
```

But imagine:

```text
Event occurs:
10:00

SIEM receives:
10:20
```

A 20-minute delay can seriously affect SOC response.

---

# 2️⃣1️⃣ Sources of Log Latency

Latency may occur in:

```text
Source
 ↓
Network
 ↓
Collector
 ↓
Queue
 ↓
Parser
 ↓
Indexer
 ↓
Storage
```

Possible causes:

==> Network congestion
==> Collector overload
==> Queue backlog
==> CPU saturation
==> Disk I/O
==> Indexing delay
==> Rate limiting
==> Backpressure

---

# 2️⃣2️⃣ Queue and Backpressure

Suppose:

```text
Incoming:
10,000 EPS

Processing capacity:
7,000 EPS
```

Then:

```text
10,000
   ↓
Queue
   ↓
7,000 processed
```

The remaining events may accumulate.

If the queue becomes full:

```text
Queue Full
   ↓
Event Drop
```

This creates a data-loss risk.

Monitor:

==> Queue depth
==> Queue growth
==> Processing rate
==> Event drops
==> Retry rate

---

# 2️⃣3️⃣ Event Drops

Event drops are particularly important.

Possible causes:

==> Queue overflow
==> Network failure
==> Collector overload
==> Parser errors
==> Storage failure
==> Rate limiting
==> Resource exhaustion

If events are dropped, detection coverage may be affected.

The SIEM Engineer should identify:

```text
How many?
When?
Which source?
Which component?
Why?
```

---

# 2️⃣4️⃣ Log Completeness

Completeness means checking whether the expected data is present.

Suppose a firewall should send:

```text
Allow
Deny
VPN
Authentication
Admin
System
```

But only:

```text
Deny
```

events appear.

The source may technically be connected, but the dataset is incomplete.

Therefore:

**Connected does not always mean complete.**

---

# 2️⃣5️⃣ Data Quality Validation

A practical validation framework:

```text
Availability
      ↓
Completeness
      ↓
Parsing
      ↓
Normalization
      ↓
Timestamp
      ↓
Timeliness
      ↓
Uniqueness
      ↓
Searchability
      ↓
Detection Validation
```

---

# 2️⃣6️⃣ Log Source Onboarding Validation

When onboarding a new source:

### Step 1

Confirm source configuration.

### Step 2

Generate test events.

### Step 3

Verify transport.

### Step 4

Confirm ingestion.

### Step 5

Inspect raw event.

### Step 6

Validate parsing.

### Step 7

Validate normalized fields.

### Step 8

Check timestamp.

### Step 9

Test detection.

### Step 10

Document the source.

---

# 2️⃣7️⃣ Raw vs Parsed Data

Always understand both.

### Raw Data

```text
Original event exactly as received.
```

### Parsed Data

```text
Structured fields extracted from the event.
```

Example:

```text
Raw:
user=admin src=10.0.0.10 action=login
```

Parsed:

```text
user.name = admin
source.ip = 10.0.0.10
event.action = login
```

When troubleshooting detection failures, checking raw data is often essential.

---

# 2️⃣8️⃣ Detection Failure Because of Data Quality

Suppose you have this detection:

```text
source.ip = suspicious_ip
```

But the firewall logs contain:

```text
clientAddress
```

and no mapping exists.

The detection may return:

```text
0 results
```

The problem may not be the detection rule.

It may be the **data model**.

This is why SIEM Engineers should always verify the data before blaming the rule.

---

# 2️⃣9️⃣ Data Quality and Threat Hunting

Threat hunting depends heavily on reliable telemetry.

Suppose you hunt:

```text
PowerShell activity
```

But PowerShell logs are missing.

Your hunt may incorrectly conclude:

```text
No suspicious PowerShell activity found.
```

The correct conclusion may be:

```text
PowerShell telemetry is incomplete.
Hunt confidence is limited.
```

This distinction is extremely important.

---

# 3️⃣0️⃣ Data Quality Monitoring Dashboard

A useful SIEM health dashboard can include:

```text
Log Sources
EPS
Last Event Time
Event Drops
Parsing Errors
Queue Size
Latency
Storage
Collector Health
Agent Health
```

Example:

```text
Source             EPS       Last Event
Firewall-01        450       10 sec ago
Windows-DC01       800       5 sec ago
Linux-Server-01    120       8 sec ago
VPN-01              0        25 min ago  ⚠
```

This immediately highlights a potential problem.

---

# 3️⃣1️⃣ Data Quality Alerts

Automate health monitoring.

Examples:

### No Logs

```text
No events for defined period
→ Health Alert
```

### EPS Drop

```text
Normal: 500 EPS
Current: 20 EPS
→ Investigate
```

### Parsing Error

```text
Parsing failure rate > threshold
→ Alert
```

### Queue Growth

```text
Queue continuously increasing
→ Investigate
```

### Latency

```text
Normal: <10 sec
Observed: 5 min
→ Investigate
```

---

# 3️⃣2️⃣ Troubleshooting Example — Firewall Logs Missing

Problem:

```text
Firewall logs disappeared.
```

### Investigation

```text
Firewall
 ↓
Is logging enabled?
 ↓
Is destination correct?
 ↓
Network connectivity?
 ↓
Collector listening?
 ↓
Events arriving?
 ↓
Parser working?
 ↓
Indexing working?
 ↓
Search working?
```

Suppose you discover:

```text
Firewall
   ↓
Network
   ↓
Collector
   X
```

Root cause:

```text
Collector service stopped.
```

After restarting:

```text
Firewall
 ↓
Collector
 ↓
SIEM
 ↓
Search
 ↓
Detection
```

Validate before closing the incident.

---

# 3️⃣3️⃣ Troubleshooting Example — Duplicate Events

Problem:

```text
Alert volume suddenly doubled.
```

Investigation:

```text
Alert Volume
 ↓
Event Count
 ↓
Source
 ↓
Raw Events
 ↓
Compare Event IDs
 ↓
Check Forwarders
```

Suppose:

```text
Collector A → SIEM
Collector B → SIEM
```

Both are forwarding the same events.

Root cause:

```text
Duplicate forwarding path
```

Fix:

==> Correct forwarding configuration
==> Validate event count
==> Confirm alert volume
==> Check storage impact

---

# 3️⃣4️⃣ Troubleshooting Example — Wrong Timestamp

Problem:

```text
Events appear several hours in the past.
```

Check:

```text
Source timezone
 ↓
Server timezone
 ↓
NTP
 ↓
Collector
 ↓
Parser
 ↓
SIEM timestamp field
```

Identify where the time changed.

Never simply modify the SIEM display without understanding the source of the problem.

---

# 3️⃣5️⃣ Troubleshooting Example — Parsing Failure

Problem:

```text
Firewall events arrive,
but detection cannot find source IP.
```

Check:

```text
Raw Event
 ↓
Parser
 ↓
Field Extraction
 ↓
Field Mapping
```

If raw data contains:

```text
src=10.10.10.10
```

but the parser does not extract it into:

```text
source.ip
```

the detection may fail.

Fix the parsing or normalization layer, then retest.

---

# 3️⃣6️⃣ Data Quality SLA

Organizations can define operational expectations.

For example:

```text
Log Availability:
≥ 99.5% per critical source (example - adapt to org)

Log Latency:
≤ 5 min for critical sources, ≤ 15 min standard (example)

Parsing Success:
≥ 99% parsed, < 1% unparsed (example)

Critical Source Silence:
Alert if no events for > 15 min (example)
```

The exact targets should be based on business and security requirements.

Not every source requires identical thresholds.

---

# 3️⃣7️⃣ Critical vs Non-Critical Sources

Prioritize monitoring based on importance.

### Critical

==> Domain Controllers
==> Firewalls
==> Identity Systems
==> EDR
==> VPN
==> Critical Servers

### Important

==> Application Servers
==> Web Servers
==> Databases

### Lower Priority

==> Development Systems
==> Test Systems

The classification depends on the organization's architecture.

---

# 3️⃣8️⃣ Data Quality and Compliance

Reliable logging can also support:

==> Auditability
==> Investigation
==> Incident response
==> Security monitoring
==> Compliance requirements

But compliance requirements vary by organization, industry, and jurisdiction.

Therefore, SIEM retention and logging requirements should be mapped to the organization's actual policies and applicable regulations.

---

# 3️⃣9️⃣ Practical Lab

Build a lab using:

```text
Wazuh
Linux VM
Windows VM
Firewall
Syslog
```

### Lab 01 — Missing Logs

Stop a log source or agent in your isolated lab.

Observe:

```text
Last Event Time
EPS
Health Status
```

Create a health alert.

---

### Lab 02 — Parsing

Send a sample Syslog event.

Verify:

```text
Raw Event
Source IP
Destination IP
Action
Timestamp
```

---

### Lab 03 — Timestamp

Generate logs from systems with different timezone configurations in a controlled lab.

Observe the effect on:

```text
Timeline
Search
Correlation
```

Then correct the configuration.

---

### Lab 04 — Duplicate Logs

Configure two forwarding paths in the lab.

Observe:

```text
Event Count
EPS
Alert Count
```

Then remove the duplicate path.

---

### Lab 05 — Log Latency

Generate controlled events and measure:

```text
Event Time
 ↓
Collection Time
 ↓
SIEM Search Time
```

Calculate approximate ingestion delay.

---

# 4️⃣0️⃣ SIEM Data Quality Checklist

```text
☑ Log source identified
☑ Source is generating logs
☑ Network path verified
☑ Collector healthy
☑ Authentication verified
☑ Events arriving
☑ Raw logs inspected
☑ Parser validated
☑ Fields mapped
☑ Timestamp verified
☑ Time synchronization checked
☑ Duplicate events checked
☑ Event latency measured
☑ Event drops checked
☑ Queue health checked
☑ Storage health checked
☑ Search validated
☑ Detection tested
☑ Root cause documented
```

---

# 4️⃣1️⃣ SIEM Engineer Interview Questions

### Q1. What is SIEM Data Quality?

**Answer:**

SIEM Data Quality is the process of ensuring that security data is available, complete, accurate, timely, correctly parsed, normalized, and reliable for detection and investigation.

---

### Q2. What would you check if logs suddenly stopped?

**Answer:**

I would check the source, logging configuration, network connectivity, collector status, authentication or certificates, ingestion pipeline, queues, parsing, indexing, and finally search availability.

---

### Q3. What is log latency?

**Answer:**

Log latency is the time difference between when an event occurs and when it becomes available in the SIEM for analysis.

---

### Q4. What causes duplicate logs?

**Answer:**

Common causes include duplicate forwarding paths, multiple agents, retry mechanisms, collector configuration problems, replayed events, or misconfigured load-balancing paths.

---

### Q5. Why is parsing important?

**Answer:**

Parsing converts raw events into structured fields. Detection rules, correlation, dashboards, and investigations often depend on those structured fields.

---

### Q6. How do you troubleshoot a parsing problem?

**Answer:**

I first inspect the raw event, understand its format, verify the parser, check field extraction and mapping, test representative events, and then validate the resulting fields in the SIEM.

---

### Q7. Why is timestamp accuracy important?

**Answer:**

Accurate timestamps are essential for event correlation, attack timelines, threat hunting, incident investigation, and determining the sequence of activities.

---

### Q8. What is backpressure?

**Answer:**

Backpressure occurs when incoming data arrives faster than downstream components can process it, causing queues to grow and potentially resulting in increased latency or event loss.

---

### Q9. How can you detect a silent log source?

**Answer:**

Monitor the source's expected event rate or last-event timestamp and generate a health alert when activity falls below an appropriate threshold or stops for a defined period.

---

### Q10. What is the relationship between data quality and detection engineering?

**Answer:**

Detection logic depends on reliable telemetry. Missing, incorrectly parsed, delayed, or incorrectly mapped data can cause false negatives or misleading detections.

---

# 4️⃣2️⃣ Complete SIEM Data Quality Flow

Remember this:

```text
Log Source
    ↓
Generate Event
    ↓
Transport
    ↓
Collector
    ↓
Ingestion
    ↓
Queue
    ↓
Parsing
    ↓
Normalization
    ↓
Timestamp
    ↓
Enrichment
    ↓
Indexing
    ↓
Storage
    ↓
Search
    ↓
Detection
    ↓
Investigation
```

At every stage ask:

```text
Is the data:
Available?
Complete?
Accurate?
Timely?
Unique?
Valid?
Searchable?
```

---

# 🎯 Final Takeaway

A SIEM Engineer should never think:

```text
"Logs are visible, so everything is fine."
```

Instead, think:

```text
Are all expected logs arriving?
Are important fields present?
Are timestamps correct?
Are events delayed?
Are events duplicated?
Are events being dropped?
Can detection rules trust this data?
```

Because:

> **Bad data can create bad detection.**

A strong SIEM Engineer therefore works on both sides:

```text
Data Quality
      +
Detection Engineering
      +
Performance
      +
Troubleshooting
```

Together, these create a reliable SIEM environment.

---

## 📚 SIEM Engineer Learning Series

**Previous:** #15 — Threat Hunting with SIEM

**Current:** #16 — SIEM Data Quality & Troubleshooting

**Next:** #17 — SIEM Use Case Development

---

## 🔐 Practical Security Takeaway

Before creating a complex detection rule, first ask:

```text
"Can I trust the data?"
```

If the answer is no, fix the **data pipeline** first.

**Good SIEM engineering starts with good data.**

---

**Follow the SIEM Engineer learning series — Boni Yeamin**

