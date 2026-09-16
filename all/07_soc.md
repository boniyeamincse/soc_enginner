# SIEM Engineer #07 — Threat Intelligence

## 🟢 Introduction

A SIEM can tell us:

```text
Which IP connected?
Which user logged in?
Which host generated the event?
What process executed?
When did it happen?
```

But sometimes we need additional context.

For example:

```text
203.x.x.x
```

A SIEM may know that an internal system communicated with this IP.

But Threat Intelligence may provide additional information such as:

```text
Is this IP associated with known malicious activity?
Has it been reported before?
What type of threat has it been associated with?
When was it last observed?
```

This additional context can make SIEM investigations more useful.

The core concept is:

**Security Telemetry + Threat Intelligence → Better Detection & Investigation**

---

# 🧠 1. What is Threat Intelligence?

**Cyber Threat Intelligence (CTI)** is information about threats that helps an organization understand, detect, investigate, and respond to security risks.

Threat Intelligence can provide information about:

==> Malicious IP addresses

==> Malicious domains

==> URLs

==> File hashes

==> Malware families

==> Threat actors

==> Attack techniques

==> Vulnerabilities

==> Campaigns

==> Indicators of compromise

But raw information is not automatically useful intelligence.

The information needs:

```text
Context
+
Validation
+
Relevance
+
Timeliness
```

---

# 🎯 2. Why Threat Intelligence Matters in SIEM

Suppose the SIEM detects:

```text
Internal Host
       ↓
Connection
       ↓
External IP
```

Without intelligence:

```text
Unknown external IP
```

With enrichment:

```text
External IP
       ↓
Threat Intelligence Lookup
       ↓
Known suspicious indicator
       ↓
Additional context
```

This can help the analyst prioritize and investigate the event.

---

# 🔍 3. What is an IOC?

**IOC = Indicator of Compromise**

Common IOCs include:

```text
IP Address
Domain
URL
File Hash
Email Address
Hostname
```

Examples:

```text
IP:
203.x.x.x

Domain:
example-suspicious-domain

Hash:
SHA256 value
```

An IOC is an indicator—not necessarily proof of compromise by itself.

---

# ⚠️ 4. IOC ≠ Incident

This is a very important SOC concept.

Suppose your threat feed contains:

```text
203.x.x.x
```

Your firewall logs show:

```text
Internal Host → 203.x.x.x
```

This is useful evidence.

But you still need to investigate:

==> Which host communicated?

==> Which process initiated the connection?

==> Which user was logged in?

==> When did it happen?

==> Was the indicator still relevant?

==> Was the connection blocked?

==> Was there any additional suspicious activity?

Therefore:

**IOC Match ≠ Automatically Confirmed Compromise**

---

# 🧩 5. Types of Threat Intelligence

Threat Intelligence is commonly discussed in several categories.

## Strategic Intelligence

Focuses on high-level risks and trends.

Audience:

==> Management

==> Security leadership

==> Risk teams

Example:

```text
Increasing ransomware activity
against a particular industry.
```

---

## Tactical Intelligence

Focuses on adversary techniques and behaviors.

Useful for:

==> Detection Engineering

==> Threat Hunting

==> SOC teams

Example:

```text
Adversaries commonly use
specific techniques for credential access.
```

---

## Operational Intelligence

Focuses on campaigns and ongoing threat activity.

Example:

```text
Current campaign
Target
Infrastructure
Attack behavior
Timeline
```

---

## Technical Intelligence

Focuses heavily on technical indicators.

Examples:

```text
IP
Domain
URL
Hash
Email
```

This is especially useful for SIEM enrichment and automated correlation.

---

# 📊 6. Threat Intelligence Lifecycle

Threat Intelligence should follow a lifecycle.

```text
Direction
   ↓
Collection
   ↓
Processing
   ↓
Analysis
   ↓
Dissemination
   ↓
Feedback
   ↓
Improvement
```

Let's understand it.

---

# 🎯 7. Step 1 — Intelligence Requirements

First ask:

> **What information does the organization actually need?**

Examples:

==> Which threats target our industry?

==> Which malicious IPs are contacting our infrastructure?

==> Which vulnerabilities are actively being exploited?

==> Which threat behaviors should our SOC detect?

Without clear requirements, teams may collect large amounts of irrelevant information.

---

# 📥 8. Step 2 — Collection

Threat information can come from multiple sources.

Examples:

==> Threat intelligence platforms

==> Commercial feeds

==> Open-source intelligence

==> Security vendors

==> CERT/CSIRT organizations

==> Internal incident data

==> Malware analysis

==> Security research

The source should be evaluated for reliability and relevance.

---

# 🧹 9. Step 3 — Processing

Raw intelligence often needs processing.

Example:

```text
Raw Feed
   ↓
Remove duplicates
   ↓
Normalize fields
   ↓
Validate format
   ↓
Add timestamps
   ↓
Assign confidence
   ↓
Store
```

For an IP feed:

```text
IP
First Seen
Last Seen
Source
Confidence
Threat Type
Expiration
```

---

# 🔬 10. Step 4 — Analysis

Analysis converts collected information into useful intelligence.

Suppose a feed contains:

```text
IP A
IP B
IP C
```

The analyst asks:

```text
Are these relevant to us?
Have our systems communicated with them?
What activity is associated with them?
How recent is the intelligence?
How reliable is the source?
```

This is where context becomes important.

---

# 📤 11. Step 5 — Dissemination

Useful intelligence should reach the right people and systems.

For example:

```text
Threat Intelligence
      ↓
SIEM
      ↓
SOC Analyst
```

or:

```text
Threat Intelligence
      ↓
Firewall
```

or:

```text
Threat Intelligence
      ↓
EDR
```

The format and level of detail should match the consumer.

---

# 🔄 12. Step 6 — Feedback

SOC analysts should provide feedback.

Example:

```text
Feed Indicator
      ↓
Matched 500 alerts
      ↓
Most were irrelevant
      ↓
Analyst Feedback
      ↓
Feed Filtering / Tuning
```

This improves intelligence quality.

---

# 🧠 13. Threat Intelligence in SIEM

The basic architecture is:

```text
Threat Feed
     ↓
Processing
     ↓
Threat Intelligence Store
     ↓
SIEM
     ↓
Correlation
     ↓
Alert
     ↓
SOC Investigation
```

The SIEM can compare observed events against known indicators.

---

# 🔗 14. IOC Enrichment

Suppose an alert contains:

```text
Destination IP:
203.x.x.x
```

The SIEM can enrich the event:

```text
Destination IP:
203.x.x.x

Threat Intelligence:
Known suspicious indicator

Source:
Threat Feed A

Last Seen:
Recent

Confidence:
High
```

Now the analyst has more context.

---

# 🔥 15. IOC Correlation

Imagine your firewall produces:

```text
Internal Host → External IP
```

Threat Intelligence contains:

```text
External IP = Known Indicator
```

Correlation:

```text
Firewall Event
      +
Threat Intelligence Match
      ↓
Security Alert
```

This is one of the most common uses of Threat Intelligence in SIEM.

---

# 🌐 16. IP Reputation

IP reputation attempts to provide context about an IP address.

Possible classifications include:

```text
Known malicious
Suspicious
Unknown
Benign
```

But reputation information must be treated carefully.

An IP can be:

==> Shared

==> Dynamic

==> Reassigned

==> Compromised temporarily

==> Used by legitimate services

Therefore, reputation should be one part of the investigation.

---

# 🌍 17. Domain Intelligence

Similar analysis can be performed for domains.

Example:

```text
Internal Host
     ↓
DNS Request
     ↓
Suspicious Domain
```

Investigate:

==> Which host requested it?

==> Which user?

==> When?

==> Was there an HTTP/HTTPS connection afterward?

==> Was the domain recently registered?

==> Is it present in trusted intelligence sources?

---

# 🔗 18. URL Intelligence

URLs can be useful in:

==> Phishing investigation

==> Web security monitoring

==> Email security

==> Proxy analysis

Example:

```text
Email
 ↓
URL
 ↓
User Click
 ↓
Proxy Event
 ↓
Endpoint Event
```

Correlating these events can provide much more context than looking at the URL alone.

---

# #️⃣ 19. Hash Intelligence

File hashes can be used to identify known files.

Common hash types include:

```text
MD5
SHA-1
SHA-256
```

For security investigations, SHA-256 is commonly preferred for identifying files.

Example:

```text
Endpoint
 ↓
File Hash
 ↓
Threat Intelligence Lookup
 ↓
Known / Unknown
```

Again:

**Unknown does not mean safe.**

And:

**Known malicious does not replace investigation of the surrounding activity.**

---

# 📧 20. Email Threat Intelligence

Email investigations can involve:

```text
Sender
Recipient
Domain
URL
Attachment Hash
Source IP
Message ID
```

A SIEM can correlate:

```text
Email
 ↓
URL
 ↓
DNS
 ↓
Proxy
 ↓
Endpoint
```

This can help analysts understand the complete activity chain.

---

# 🏷️ 21. Threat Intelligence Confidence

Not all intelligence sources are equally reliable.

A useful intelligence record can contain:

```text
Indicator
Source
First Seen
Last Seen
Confidence
Threat Type
Expiration
```

For example:

```text
Indicator:
203.x.x.x

Source:
Feed-A

Confidence:
High

Last Seen:
Recent
```

Confidence should come from the source methodology or your organization's intelligence process.

Do not invent confidence values simply to make an alert look stronger.

---

# ⏰ 22. Freshness Matters

Threat intelligence changes over time.

An indicator that was malicious months ago may not have the same relevance today.

Therefore consider:

```text
First Seen
Last Seen
Expiration
Current Status
```

Example:

```text
Indicator
 ↓
Old intelligence
 ↓
Current investigation
 ↓
Validate freshness
```

This is especially important for IP and domain reputation.

---

# 🧹 23. Threat Feed Quality

A feed should not be judged only by its size.

For example:

```text
Feed A:
1,000,000 indicators
```

does not automatically mean it is better than:

```text
Feed B:
20,000 high-quality indicators
```

Important factors include:

==> Accuracy

==> Relevance

==> Freshness

==> Confidence

==> Coverage

==> Update frequency

==> False-positive rate

==> Data format

==> Integration capability

---

# 🚨 24. Threat Intelligence False Positives

Suppose an intelligence feed identifies:

```text
IP = Suspicious
```

Your SIEM generates:

```text
500 alerts
```

But investigation shows:

```text
Most traffic belongs to a legitimate cloud service.
```

Possible reasons:

==> Shared infrastructure

==> Stale intelligence

==> Poor feed quality

==> Incorrect classification

==> Legitimate infrastructure reuse

The solution is investigation and controlled tuning—not blindly trusting or ignoring the feed.

---

# 🧩 25. Internal Intelligence

Not all Threat Intelligence comes from external feeds.

Your organization generates valuable intelligence from its own incidents.

Examples:

```text
Previously compromised IP
Compromised account
Malicious hash
Suspicious domain
Observed attack behavior
Internal attacker infrastructure
```

This can become:

```text
Internal Threat Intelligence
```

---

# 🔄 26. Internal IOC Lifecycle

Example:

```text
Incident
 ↓
IOC Discovered
 ↓
Validate
 ↓
Document
 ↓
Add to Intelligence Store
 ↓
Correlate Future Events
 ↓
Detect Reuse
```

This creates organizational memory.

---

# 🧠 27. Threat Intelligence Platform

A **TIP** can help manage threat intelligence.

Common functions include:

==> IOC storage

==> Enrichment

==> Relationships

==> Feeds

==> Confidence

==> Expiration

==> Sharing

==> Investigation

==> Automation

A TIP can integrate with the SIEM.

Architecture:

```text
Threat Sources
       ↓
TIP
       ↓
Enrichment
       ↓
SIEM
       ↓
Detection
       ↓
SOC
```

---

# 🔌 28. SIEM Threat Intelligence Integration

A SIEM integration may use:

```text
API
STIX/TAXII
CSV
JSON
Syslog
Custom Connector
```

The integration process is:

```text
Threat Source
 ↓
Connector
 ↓
Authentication
 ↓
Data Retrieval
 ↓
Parsing
 ↓
Normalization
 ↓
Validation
 ↓
Storage
 ↓
Correlation
```

---

# 📦 29. STIX and TAXII

Two important standards in Threat Intelligence are:

### STIX

**Structured Threat Information Expression**

STIX provides a structured way to represent threat intelligence.

### TAXII

**Trusted Automated Exchange of Intelligence Information**

TAXII provides mechanisms for exchanging threat intelligence.

Conceptually:

```text
Threat Intelligence
       ↓
STIX
       ↓
TAXII
       ↓
Threat Intelligence Platform
       ↓
SIEM
```

---

# 🧠 30. Threat Intelligence + Detection Engineering

Threat Intelligence can directly support Detection Engineering.

Example:

```text
Threat Research
      ↓
Known Behavior
      ↓
Detection Hypothesis
      ↓
Detection Rule
      ↓
SIEM Alert
```

Another example:

```text
Known IOC
      ↓
IOC Detection
      ↓
SIEM Correlation
      ↓
Alert
```

Threat Intelligence therefore provides input into the detection lifecycle.

---

# 🎯 31. Threat Intelligence + Threat Hunting

Threat Intelligence can also create hunting hypotheses.

Example:

```text
Threat Intelligence:
Specific malicious infrastructure observed
```

Hunt:

```text
Search historical DNS
Search proxy logs
Search firewall logs
Search endpoint logs
```

Then:

```text
Indicator Found?
   ↓
Yes → Investigate
No  → Continue / Document
```

---

# 🔍 32. Historical Search

When you discover a new IOC, do not only search current events.

If retention allows, search historical telemetry.

Example:

```text
New IOC
 ↓
Search last 30 days
 ↓
Search last 90 days
 ↓
Identify previous observations
```

This may reveal earlier activity.

The appropriate lookback period depends on the environment and investigation requirements.

---

# 🧬 33. Threat Intelligence Correlation Across Data Sources

One indicator can appear in many places.

Example:

```text
IP
 ↓
Firewall
 ↓
DNS
 ↓
Proxy
 ↓
EDR
 ↓
SIEM
```

Another:

```text
Hash
 ↓
Email
 ↓
Endpoint
 ↓
File Monitoring
 ↓
EDR
```

Correlation across multiple sources can provide stronger context.

---

# 🧠 34. Threat Intelligence and MITRE ATT&CK

Threat Intelligence may describe:

```text
Adversary
Campaign
Technique
Sub-technique
Infrastructure
Malware
```

Detection Engineers can use this information to identify detection opportunities.

For example:

```text
Threat Research
 ↓
Observed Technique
 ↓
Telemetry Requirement
 ↓
Detection
 ↓
MITRE ATT&CK Mapping
```

This connects intelligence with detection coverage.

---

# ⚙️ 35. Automated Enrichment

Automation can enrich alerts automatically.

Example:

```text
SIEM Alert
     ↓
Extract IP
     ↓
Threat Intelligence API
     ↓
Reputation / Context
     ↓
Update Alert
     ↓
SOC Analyst
```

This saves analyst time.

But API integrations must handle:

==> Authentication

==> Rate limits

==> Timeouts

==> API failures

==> Invalid responses

==> Data freshness

==> Duplicate data

---

# 🔐 36. Security of Threat Intelligence Integrations

Protect your integrations.

Use:

==> Secure API credentials

==> Secret management

==> TLS

==> Least privilege

==> API access controls

==> Monitoring

==> Rate limiting

Do not hard-code sensitive API keys inside detection rules or scripts.

---

# 💰 37. Threat Intelligence Cost Management

Large feeds can create significant data volume.

Consider:

```text
1 Million Indicators
        ↓
Continuous Correlation
        ↓
High Storage / Compute
```

Before integrating everything, determine:

==> Which indicators are relevant?

==> Which data types are needed?

==> How long should indicators be retained?

==> How often should feeds update?

==> What should expire?

Quality and relevance are more important than blindly collecting huge amounts of data.

---

# 📊 38. Threat Intelligence Dashboard

A SIEM/TIP dashboard may show:

```text
Active Indicators
New Indicators
Expired Indicators
IOC Matches
Top Sources
Top Threat Types
High-Confidence Matches
Recent Matches
```

SOC analysts may also need:

```text
Top Matched IPs
Top Matched Domains
Affected Hosts
Affected Users
First Seen
Last Seen
```

---

# 🧪 39. Practical SIEM Lab

Build a small lab:

```text
Wazuh / SIEM
+
Firewall Logs
+
DNS Logs
+
Threat Intelligence Feed
```

### Lab 1 — IP Enrichment

Take a test indicator.

```text
IP
 ↓
Threat Intelligence
 ↓
Enrichment
```

### Lab 2 — SIEM Correlation

Generate a controlled network event in your lab.

```text
Network Event
+
Threat Intelligence Match
↓
Alert
```

### Lab 3 — Historical Search

Search whether the indicator appeared previously.

```text
IOC
 ↓
Historical SIEM Search
 ↓
Previous Events
```

### Lab 4 — Detection

Create a detection for a known test indicator.

```text
IOC Match
 ↓
Detection
 ↓
Alert
```

---

# 📋 40. Threat Intelligence Checklist

```text
[ ] Define intelligence requirements

[ ] Identify relevant sources

[ ] Validate source reliability

[ ] Collect intelligence

[ ] Normalize indicators

[ ] Remove duplicates

[ ] Assign source information

[ ] Track first seen / last seen

[ ] Track expiration

[ ] Track confidence

[ ] Integrate with SIEM

[ ] Test correlation

[ ] Monitor false positives

[ ] Monitor feed freshness

[ ] Search historical events

[ ] Provide analyst enrichment

[ ] Feed intelligence into detection engineering

[ ] Protect API credentials

[ ] Monitor integration health

[ ] Review intelligence quality
```

---

# 🔄 41. Complete Threat Intelligence Flow

Remember:

```text
Requirement
     ↓
Collection
     ↓
Processing
     ↓
Validation
     ↓
Analysis
     ↓
Intelligence
     ↓
Integration
     ↓
SIEM Correlation
     ↓
Detection
     ↓
Alert
     ↓
SOC Investigation
     ↓
Feedback
     ↓
Improvement
```

This is the complete relationship between Threat Intelligence and SOC operations.

---

# 🎤 42. SIEM Engineer Interview Questions

### Q1. What is Threat Intelligence?

**Answer:**

Threat Intelligence is analyzed information about threats, adversaries, indicators, vulnerabilities, and attack behavior that helps an organization improve detection, investigation, and response.

---

### Q2. What is an IOC?

**Answer:**

IOC means Indicator of Compromise. Common examples include IP addresses, domains, URLs, file hashes, and email addresses associated with suspicious or malicious activity.

---

### Q3. Does an IOC match mean the system is compromised?

**Answer:**

No. An IOC match is an important investigation signal, but analysts should validate the context, timing, source reliability, related activity, and affected assets before concluding that a compromise occurred.

---

### Q4. What is IOC enrichment?

**Answer:**

IOC enrichment means adding additional context to an indicator, such as threat source, confidence, first-seen/last-seen information, threat type, or reputation.

---

### Q5. What is the difference between Threat Intelligence and an IOC?

**Answer:**

An IOC is a specific indicator. Threat Intelligence is broader information that can include indicators, adversary behavior, campaigns, techniques, vulnerabilities, context, and analysis.

---

### Q6. What is STIX?

**Answer:**

STIX is a structured language and framework for representing cyber threat intelligence.

---

### Q7. What is TAXII?

**Answer:**

TAXII is a protocol and set of services designed to exchange cyber threat intelligence.

---

### Q8. How can Threat Intelligence be integrated with SIEM?

**Answer:**

It can be integrated through APIs, STIX/TAXII, files, feeds, or custom connectors. The data is then normalized, stored, enriched, and correlated with SIEM events.

---

### Q9. How do you handle a high number of IOC false positives?

**Answer:**

I would investigate the source and quality of the intelligence, check indicator freshness, understand why the matches occur, validate the affected infrastructure, and then apply controlled filtering or tuning where appropriate.

---

### Q10. How does Threat Intelligence support Threat Hunting?

**Answer:**

Threat Intelligence can provide hypotheses and indicators that analysts can search across historical and current telemetry to identify related activity.

---

### Q11. What makes a good Threat Intelligence feed?

**Answer:**

Important characteristics include accuracy, relevance, freshness, transparency of sourcing, useful context, appropriate confidence, manageable false positives, and reliable integration.

---

### Q12. How can Threat Intelligence improve Detection Engineering?

**Answer:**

Threat Intelligence can identify new indicators, adversary behaviors, and techniques that can be converted into detection hypotheses, telemetry requirements, and SIEM detection rules.

---

# 🧠 43. Important Lessons

### 1️⃣ Intelligence needs context

```text
IOC
≠
Complete Investigation
```

### 2️⃣ Freshness matters

Old intelligence may have reduced relevance.

### 3️⃣ Quality matters more than quantity

A huge feed is not automatically a useful feed.

### 4️⃣ Internal intelligence is valuable

Your own incidents can generate valuable future detection data.

### 5️⃣ Intelligence should support action

The objective is not simply collecting indicators.

The objective is:

```text
Understand
   ↓
Detect
   ↓
Investigate
   ↓
Respond
   ↓
Improve
```

---

# 🚀 44. Final Takeaway

A SIEM Engineer should understand how Threat Intelligence becomes operational security data.

The important flow is:

**Threat Intelligence → Enrichment → Correlation → Detection → Investigation**

The SIEM Engineer should be able to work with:

==> IP Intelligence

==> Domain Intelligence

==> URL Intelligence

==> Hash Intelligence

==> IOC Feeds

==> STIX/TAXII

==> Threat Intelligence Platforms

==> SIEM Correlation

==> Threat Hunting

==> Detection Engineering

==> Automated Enrichment

The most important mindset is:

> **Don't blindly trust an indicator. Validate the indicator, understand the context, and investigate the evidence.**

---

## 📚 SIEM Engineer Learning Series

**#01 — Log Management**

**#02 — SIEM Platforms**

**#03 — Log Integration**

**#04 — Detection Engineering**

**#05 — Query & Investigation**

**#06 — SOC Operations**

**#07 — Threat Intelligence ← You are here**

**#08 — Automation & SOAR → Next**

**#09 — Dashboard & Reporting**

**#10 — SIEM Infrastructure**

---

### Navigation

**← Previous Article: #06 — SOC Operations**

**SIEM Engineer Index**

**Next Article: #08 — Automation & SOAR →**

---
