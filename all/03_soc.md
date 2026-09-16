# SIEM Engineer #03 — Log Integration

## Introduction

A SIEM platform is only as useful as the data it receives.

In the previous articles, we discussed:

**#01 — Log Management**
**#02 — SIEM Platforms**

Now we will focus on one of the most practical responsibilities of a SIEM Engineer:

# Log Integration

Log Integration means connecting different **servers, network devices, security products, applications, cloud platforms, and other data sources** to the SIEM so their security events can be collected, processed, and analyzed.

A simple way to think about it is:

**Log Source → Connector/Agent → Transport → SIEM → Parsing → Normalization → Detection**

---

# 1. What is Log Integration?

Suppose an organization has:

==> FortiGate Firewall
==> Windows Servers
==> Linux Servers
==> Active Directory
==> VPN
==> EDR
==> Web Application
==> AWS
==> Wazuh

The SIEM Engineer needs to connect these systems to the SIEM.

For example:

```text
FortiGate
    │
    │ Syslog
    ▼
Log Collector
    │
    ▼
SIEM
```

Another system might use an API:

```text
Cloud Platform
      │
      │ API
      ▼
SIEM Connector
      │
      ▼
SIEM
```

The integration method depends on the source and the SIEM platform.

---

# 2. Why is Log Integration Important?

Imagine a SOC has a detection rule for:

**Multiple Failed VPN Logins**

But the VPN logs are not connected to the SIEM.

The detection rule cannot work properly.

This gives us a simple principle:

**No Data → No Visibility → No Detection**

Therefore, a SIEM Engineer must ensure that critical data sources are properly onboarded.

---

# 3. Common Log Integration Methods

The most common methods include:

==> Syslog
==> CEF
==> API Integration
==> Agents
==> Forwarders
==> Windows Event Forwarding
==> File-based collection
==> Cloud Connectors
==> Message Queues
==> Custom Connectors
==> Custom Parsers

Let's understand them one by one.

---

# 4. Syslog Integration

**Syslog** is one of the most common methods for collecting logs from network and security devices.

Common sources include:

==> Firewalls
==> Routers
==> Switches
==> VPN Gateways
==> IDS/IPS
==> Proxy Servers
==> Network Appliances

A basic architecture:

```text
Firewall
   │
   │ Syslog
   ▼
Syslog Collector
   │
   ▼
SIEM
```

Common Syslog ports include:

==> UDP 514
==> TCP 514
==> TCP 6514 for Syslog over TLS

The exact configuration depends on the vendor and environment.

---

# 5. Syslog Facility and Severity

A SIEM Engineer should understand the basic Syslog structure.

Syslog messages commonly contain information such as:

==> Timestamp
==> Host
==> Facility
==> Severity
==> Message

Severity levels commonly range from:

**0 — Emergency**

to

**7 — Debug**

This helps systems classify the importance of messages.

However, severity values should not automatically be treated as the actual business/security risk of an event. Detection context matters.

---

# 6. Syslog over UDP vs TCP

### UDP

Advantages:

==> Simple
==> Low overhead
==> Commonly supported

Limitations:

==> No delivery guarantee
==> Packets may be lost

### TCP

Advantages:

==> Reliable transport
==> Better delivery behavior

Limitations:

==> More connection overhead
==> Requires appropriate configuration

For security-sensitive environments, encrypted transport such as **Syslog over TLS** may be appropriate.

---

# 7. CEF Integration

**CEF** means:

**Common Event Format**

CEF is a standardized event format commonly used to send security events to SIEM systems.

A simplified example:

```text
CEF:0|Vendor|Firewall|1.0|100|Blocked Connection|8|
src=192.168.1.10 dst=10.10.10.20
```

The event contains structured information such as:

==> Vendor
==> Product
==> Event ID
==> Event Name
==> Severity
==> Source IP
==> Destination IP

Using standardized formats can make integration and parsing easier.

---

# 8. API Integration

Not every platform sends logs through Syslog.

Cloud services and SaaS platforms often expose APIs.

A typical architecture:

```text
Cloud / SaaS
     │
     ▼
REST API
     │
     ▼
SIEM Connector
     │
     ▼
SIEM
```

API-based integration may require:

==> API Endpoint
==> Authentication
==> API Key/Token
==> OAuth
==> Pagination
==> Rate-limit handling
==> Error handling
==> Data transformation

A SIEM Engineer should understand basic REST API concepts.

---

# 9. API Authentication

Security data should not be collected using insecure authentication methods.

Common authentication mechanisms include:

==> API Keys
==> Bearer Tokens
==> OAuth 2.0
==> Certificates
==> Service Accounts

Credentials should be stored securely and should not be hardcoded into scripts or configuration files unnecessarily.

---

# 10. API Pagination

Some APIs do not return all events in one response.

Instead:

```text
Request
  ↓
Page 1
  ↓
Page 2
  ↓
Page 3
  ↓
Page 4
```

The connector must handle pagination correctly.

Otherwise, the SIEM may receive only part of the available data.

---

# 11. API Rate Limits

Cloud APIs may limit the number of requests that can be made within a specific period.

Example:

```text
100 requests/minute
```

If the SIEM connector sends too many requests, the API may return:

**HTTP 429 — Too Many Requests**

A properly designed integration should handle rate limits using appropriate retry/backoff mechanisms.

---

# 12. Agent-Based Integration

An **agent** is software installed on a system that collects and forwards data.

Architecture:

```text
Windows/Linux
      │
      ▼
   Agent
      │
      ▼
Collector / SIEM
```

Agents can provide capabilities such as:

==> Log collection
==> File monitoring
==> Process monitoring
==> Security event collection
==> Secure transport
==> Buffering
==> Filtering

Wazuh Agent is one example of agent-based security data collection.

---

# 13. Forwarders

Some SIEM platforms use **forwarders** to collect and send data.

For example, a forwarder can collect local logs and forward them to a central SIEM component.

Conceptually:

```text
Server
  │
  ▼
Forwarder
  │
  ▼
SIEM
```

Forwarders can help distribute collection responsibilities and reduce the need for direct connections from every data source to the central platform.

---

# 14. Windows Event Forwarding

Windows environments can use **Windows Event Forwarding (WEF)** to centralize Windows event data.

A simplified architecture:

```text
Windows Server 1 ──┐
Windows Server 2 ──┤
Windows Server 3 ──┤
                   ▼
              WEF Collector
                   │
                   ▼
                  SIEM
```

This can be useful when an organization wants centralized Windows event collection.

---

# 15. File-Based Integration

Some applications write logs to local files.

Example:

```text
/var/log/application.log
```

A collector or agent can monitor the file and forward new entries to the SIEM.

Important considerations include:

==> File rotation
==> Encoding
==> Permissions
==> Multiline events
==> Log format
==> File path changes

---

# 16. Multiline Logs

Some applications generate events across multiple lines.

Example:

```text
ERROR: Application failed
Exception:
    Connection refused
    Database unavailable
```

If the SIEM treats every line as a separate event, the original event may become fragmented.

Therefore, the collector/parser may need **multiline handling**.

---

# 17. Custom Parsers

Sometimes a SIEM does not understand a vendor's log format automatically.

Then a custom parser may be required.

Example raw log:

```text
AUTHFAIL|admin|192.168.10.20|VPN01|2026-09-16 14:20:10
```

We may want:

```text
event.action = authentication_failure
user.name = admin
source.ip = 192.168.10.20
device.name = VPN01
event.time = 2026-09-16 14:20:10
```

Custom parsing converts vendor-specific data into usable security fields.

---

# 18. Parsing vs Normalization

These two concepts are related but different.

### Parsing

Extract information from raw data.

```text
Raw Log
   ↓
source.ip
username
event.action
timestamp
```

### Normalization

Map different field names/formats into a common structure.

```text
src_ip
sourceIP
source_address
      ↓
source.ip
```

A SIEM Engineer should understand both.

---

# 19. Data Onboarding

**Data Onboarding** means bringing a new log source into the SIEM and making sure it is usable.

A practical onboarding process:

### Step 1 — Identify the Source

Example:

**FortiGate Firewall**

### Step 2 — Identify Available Logs

==> Traffic
==> VPN
==> Authentication
==> IPS
==> Malware

### Step 3 — Select Integration Method

Example:

**Syslog**

### Step 4 — Configure Source

Configure the firewall to send logs to the collector/SIEM.

### Step 5 — Verify Transport

Check whether the events are reaching the collector.

### Step 6 — Parse

Make sure fields are extracted correctly.

### Step 7 — Normalize

Map fields into the expected schema.

### Step 8 — Test Search

Search for newly received events.

### Step 9 — Create Detection

Build relevant detection rules.

### Step 10 — Monitor

Monitor ingestion and data quality continuously.

---

# 20. Log Integration Testing

Never assume that an integration is working simply because the configuration was saved.

Test:

==> Are logs being generated?
==> Are packets/events reaching the collector?
==> Is authentication working?
==> Are events being parsed?
==> Are fields populated?
==> Are timestamps correct?
==> Are events searchable?
==> Are alerts working?

---

# 21. End-to-End Validation

A good validation process follows:

```text
Source
  ↓
Transport
  ↓
Collector
  ↓
Parser
  ↓
Normalizer
  ↓
Indexer
  ↓
SIEM Search
  ↓
Detection
  ↓
Alert
```

If something fails, troubleshoot from the source toward the SIEM.

---

# 22. Troubleshooting: Logs Not Arriving

Suppose:

**"The firewall is configured, but no logs are appearing in the SIEM."**

Do not immediately change the SIEM rule.

Start from the source.

### Check 1 — Firewall

Is the firewall generating logs?

### Check 2 — Configuration

Is the destination IP correct?

### Check 3 — Port

Is the correct port configured?

### Check 4 — Network

Can the firewall reach the collector?

### Check 5 — Collector

Is the Syslog/collection service running?

### Check 6 — Packet Capture

Are packets actually arriving?

Tools such as `tcpdump` can help verify network traffic.

Example:

```bash
tcpdump -ni any port 514
```

### Check 7 — Parser

Are events arriving but failing to parse?

### Check 8 — Index/Data Stream

Are events being stored correctly?

### Check 9 — Search

Can you find the latest event?

This approach is much better than guessing.

---

# 23. Troubleshooting: Logs Arrive but Fields Are Empty

Suppose the SIEM receives:

```text
Firewall login failed admin 192.168.10.20
```

But the fields show:

```text
username = null
source.ip = null
event.action = null
```

Possible causes:

==> Parser mismatch
==> Vendor format changed
==> Wrong parser selected
==> Incorrect regular expression
==> Unexpected delimiter
==> New log format

The SIEM Engineer should inspect the raw event and update the parsing logic.

---

# 24. Troubleshooting: Duplicate Logs

Suppose the same firewall is sending logs through:

==> Syslog
==> API

Both may contain the same events.

The result could be duplicate events.

Possible solutions:

==> Disable unnecessary ingestion path
==> Configure deduplication
==> Adjust source configuration
==> Add unique event identifiers
==> Review ingestion architecture

---

# 25. Troubleshooting: Log Delay

Sometimes logs arrive several minutes late.

Possible causes:

==> Network latency
==> Collector queue
==> High ingestion volume
==> API polling interval
==> SIEM processing delay
==> Storage/indexing load

Monitor:

**Event Time vs Ingestion Time**

This helps identify where the delay is occurring.

---

# 26. Secure Log Integration

Log integration itself must be secured.

Important practices:

==> Use encrypted transport where appropriate
==> Protect API credentials
==> Use least privilege
==> Restrict network access
==> Validate certificates
==> Monitor collector access
==> Protect log integrity
==> Avoid exposing collectors unnecessarily

Security infrastructure should not create a new attack surface.

---

# 27. Network Requirements

Before integrating a source, identify:

==> Source IP
==> Destination IP
==> Protocol
==> Port
==> DNS requirement
==> Firewall rules
==> Routing
==> NAT requirements
==> TLS requirements

Example:

```text
Firewall
10.10.10.10
     │
     │ TCP/6514
     ▼
Collector
10.10.20.10
```

Both network and security teams may need to coordinate the implementation.

---

# 28. Certificates and TLS

When TLS is used, certificate problems can stop ingestion.

Check:

==> Certificate validity
==> Certificate chain
==> Hostname/SAN
==> Trusted CA
==> Expiration
==> TLS version
==> Client/server configuration

A certificate may be valid but still fail if the trust chain or hostname validation is incorrect.

---

# 29. Log Filtering

Not every event must always be sent to the SIEM.

Filtering may be used to reduce unnecessary data.

For example:

```text
All Events
    │
    ├── Security Events → SIEM
    ├── Authentication → SIEM
    ├── Critical Errors → SIEM
    └── Low-value Debug → Filter/Archive
```

However, filtering must be carefully designed.

If you filter too aggressively, you may remove data required for future detection or investigation.

---

# 30. Cost and Data Volume

Log integration also affects cost.

More logs mean:

==> More network traffic
==> More storage
==> More indexing
==> More processing
==> More search workload
==> Potentially higher licensing/cloud costs

Therefore, SIEM Engineers need to balance:

**Security Visibility + Data Quality + Cost + Performance**

---

# 31. Critical vs Non-Critical Logs

Not every data source has the same security value.

An organization may prioritize:

### High Priority

==> Authentication
==> Firewall
==> Active Directory
==> EDR
==> VPN
==> IDS/IPS
==> Privileged activity

### Medium Priority

==> Application
==> Proxy
==> DNS
==> Network devices

### Contextual

==> General operational logs
==> Debug logs
==> Low-value informational events

The exact priority depends on the organization's architecture and monitoring requirements.

---

# 32. Log Integration Documentation

Every onboarded data source should ideally have documentation.

Record:

==> Source name
==> Vendor/product
==> IP/hostname
==> Integration method
==> Protocol
==> Port
==> Authentication
==> Parser
==> Normalized fields
==> Expected EPS
==> Retention
==> Owner
==> Detection rules
==> Troubleshooting steps

This becomes extremely useful when the environment grows.

---

# 33. Real-World Example: Firewall Integration

Imagine an organization wants to connect a firewall to Wazuh.

Basic flow:

```text
Firewall
   │
   │ Syslog
   ▼
Wazuh Server
   │
   ▼
Decoder / Rules
   │
   ▼
Wazuh Indexer
   │
   ▼
Wazuh Dashboard
```

The SIEM Engineer should verify:

==> Firewall logging enabled
==> Correct destination configured
==> Correct protocol/port
==> Network connectivity
==> Wazuh receiving logs
==> Decoder extracting fields
==> Rules generating alerts
==> Dashboard showing events

This is a complete integration—not simply "send Syslog."

---

# 34. Real-World Example: Windows Integration

A Windows environment might look like:

```text
Windows Server
      │
      ▼
Agent / WEF
      │
      ▼
SIEM
      │
      ▼
Windows Security Events
      │
      ▼
Detection
      │
      ▼
Alert
```

Potential detections:

==> Brute Force
==> Suspicious Account Creation
==> Privilege Changes
==> Suspicious PowerShell
==> Abnormal Authentication

Again, detection quality depends on the underlying log collection.

---

# 35. Integration Monitoring

After onboarding, the job is not finished.

You need continuous monitoring.

Ask:

**Is the source still sending logs?**

**Has the volume suddenly dropped?**

**Did the vendor change the log format?**

**Are parsers still working?**

**Are events delayed?**

**Are fields still populated?**

**Is the collector healthy?**

This is why production SIEM environments need **data-source health monitoring**.

---

# 36. Common Log Integration Mistakes

Avoid these common mistakes:

==> Connecting a source without defining the use case
==> Sending logs without validating them
==> Ignoring timestamps
==> Ignoring time synchronization
==> Not monitoring log volume
==> Creating parsers without testing raw events
==> Filtering too much data
==> Hardcoding API credentials
==> Not documenting the integration
==> Assuming "configured" means "working"

---

# 37. SIEM Engineer Log Integration Checklist

### Before Integration

==> Identify log source
==> Identify security use cases
==> Determine required events
==> Select integration method
==> Identify network requirements

### During Integration

==> Configure source
==> Configure collector/connector
==> Configure authentication
==> Verify network
==> Verify transport
==> Configure parser

### After Integration

==> Verify events
==> Verify fields
==> Verify timestamps
==> Verify normalization
==> Test searches
==> Test detection
==> Monitor ingestion
==> Document configuration

---

# 38. The Complete Integration Flow

Remember this:

```text
Identify
   ↓
Design
   ↓
Configure
   ↓
Connect
   ↓
Transport
   ↓
Collect
   ↓
Parse
   ↓
Normalize
   ↓
Validate
   ↓
Detect
   ↓
Monitor
   ↓
Document
```

This is the practical lifecycle of SIEM Log Integration.

---

# 💡 Why Does Log Integration Matter?

A SIEM platform cannot protect an environment if it cannot see what is happening inside that environment.

Good integration provides:

**Better Visibility → Better Detection → Better Investigation → Better Response**

But remember:

> **Successful SIEM integration is not just about making logs arrive. It is about making sure the right security data arrives correctly, consistently, securely, and in a form that the SIEM can actually use.**

---

# Interview Questions

### Q1. What is Log Integration?

Log Integration is the process of connecting systems, applications, network devices, and security tools to a SIEM so their events can be collected, processed, searched, and used for security monitoring.

### Q2. What are common log integration methods?

==> Syslog
==> CEF
==> API
==> Agents
==> Forwarders
==> Windows Event Forwarding
==> Cloud connectors
==> File-based collection

### Q3. What would you check if Syslog logs are not arriving?

**Source → Configuration → Network → Port → Collector → Transport → Parser → Index → Search**

### Q4. What is the difference between parsing and normalization?

**Parsing** extracts fields from raw logs.

**Normalization** maps different formats and field names into a common structure.

### Q5. Why is API integration important?

Because many cloud and SaaS platforms expose security data through APIs instead of traditional Syslog.

### Q6. What is CEF?

CEF stands for **Common Event Format**, a standardized format commonly used to represent security events for SIEM ingestion.

### Q7. What is log onboarding?

Log onboarding is the process of connecting a new data source to the SIEM, validating the data, parsing/normalizing it, testing searches and detections, and monitoring the integration.

### Q8. What is EPS?

**EPS = Events Per Second.**

It measures event ingestion/generation rate and is important for capacity planning and monitoring.

---

# Final Takeaway

A SIEM Engineer should be able to take an unknown data source and ask:

**What data does it generate?**

↓

**How can I collect it?**

↓

**How will I transport it securely?**

↓

**How will I parse it?**

↓

**How will I normalize it?**

↓

**How will I validate it?**

↓

**What detection can I build from it?**

↓

**How will I monitor its health?**

That is the real skill behind **SIEM Log Integration**.

---

# Next Article

## SIEM Engineer #04 — Detection Engineering

In the next article, we will move from **collecting security data** to **detecting threats from that data**.

We will cover:

==> Detection Rules
==> Correlation Rules
==> Sigma
==> MITRE ATT&CK
==> Detection Logic
==> Threshold Detection
==> Behavioral Detection
==> False Positive Reduction
==> Alert Tuning
==> Detection Testing
==> Detection Lifecycle
==> Real-world Brute Force Detection

**Logs give us visibility. Detection Engineering turns that visibility into security alerts.**
