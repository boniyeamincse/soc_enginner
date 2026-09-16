# SIEM Engineer #02 — SIEM Platforms

## Introduction

In the previous article, we discussed **Log Management**—how logs are collected, transported, parsed, normalized, enriched, stored, and monitored.

But where do all these logs actually go?

This is where **SIEM Platforms** come in.

A SIEM platform provides a centralized place where security data can be:

**Collected → Stored → Searched → Correlated → Detected → Investigated → Reported**

For a SIEM Engineer, knowing only the name of a SIEM product is not enough.

You need to understand **how the platform works, how data enters it, how searches are performed, how detections are created, and how the platform is maintained.**

In this article, we will explore the major SIEM and security monitoring platforms a SIEM Engineer should know.

---

# 1. What is a SIEM Platform?

**SIEM** stands for:

**Security Information and Event Management**

A SIEM platform collects security-related events from different sources and provides capabilities for centralized monitoring, searching, correlation, detection, investigation, alerting, and reporting.

A simplified architecture looks like this:

```text
Firewall
Windows
Linux
AD
VPN
EDR
Cloud
Application
    │
    ▼
Data Collection
    │
    ▼
SIEM Platform
    │
    ├── Search
    ├── Detection
    ├── Correlation
    ├── Alerting
    ├── Investigation
    ├── Dashboard
    └── Reporting
```

---

# 2. What Does a SIEM Engineer Do With a SIEM Platform?

A SIEM Engineer may be responsible for:

==> Deploying the SIEM
==> Configuring data sources
==> Onboarding logs
==> Creating indexes/data streams
==> Building parsers
==> Creating detection rules
==> Writing queries
==> Creating dashboards
==> Managing alerts
==> Tuning false positives
==> Monitoring ingestion
==> Managing storage
==> Troubleshooting performance
==> Integrating threat intelligence
==> Automating security workflows
==> Maintaining and upgrading the platform

So, SIEM engineering is much broader than simply watching a dashboard.

---

# 3. Major SIEM Platforms

Some commonly encountered platforms include:

==> Splunk
==> Microsoft Sentinel
==> IBM QRadar
==> Elastic Security
==> OpenSearch
==> Wazuh

Each platform has its own architecture, terminology, query language, integrations, and operational model.

The concepts are often similar even though the implementation differs.

---

# 4. Splunk

**Splunk** is a widely used platform for collecting, searching, analyzing, and monitoring machine-generated data.

In security environments, **Splunk Enterprise Security** provides security monitoring and analytics capabilities.

For a SIEM Engineer, important Splunk concepts include:

==> Index
==> Sourcetype
==> Source
==> Host
==> Forwarder
==> Indexer
==> Search Head
==> SPL
==> Data Model
==> Correlation Search
==> Risk-based Alerting
==> Dashboard
==> Alert

---

# 5. Splunk Architecture

A simplified Splunk environment can look like:

```text
Servers / Devices
       │
       ▼
Universal Forwarder
       │
       ▼
Indexer
       │
       ▼
Search Head
       │
       ▼
Analyst
```

In larger environments, Splunk architecture can become distributed with multiple indexers and search heads.

### ==> Search Head

The Search Head handles user searches and search-related workloads.

### ==> Indexer

The Indexer stores and indexes incoming data.

### ==> Forwarder

A Forwarder can collect and forward data from systems to Splunk.

---

# 6. SPL — Splunk Search Processing Language

One of the most important skills for a Splunk-focused SIEM Engineer is **SPL**.

Example:

```text
index=windows EventCode=4625
```

This searches for Windows failed authentication events based on the specified fields.

You can then perform operations such as:

==> Filtering
==> Counting
==> Grouping
==> Statistical analysis
==> Time-based analysis
==> Correlation

Example:

```text
index=windows EventCode=4625
| stats count by src_ip
| sort - count
```

This can help identify source IPs generating large numbers of failed authentication events.

---

# 7. Microsoft Sentinel

**Microsoft Sentinel** is Microsoft's cloud-native SIEM and security analytics platform.

It integrates closely with the Microsoft security ecosystem and Azure services.

Important Sentinel concepts include:

==> Data Connectors
==> Log Analytics Workspace
==> KQL
==> Analytics Rules
==> Incidents
==> Workbooks
==> Hunting Queries
==> Automation Rules
==> Playbooks

---

# 8. KQL — Kusto Query Language

For Microsoft Sentinel, **KQL** is an essential skill.

Example:

```text
SecurityEvent
| where EventID == 4625
| summarize FailedLogins=count() by Account
| order by FailedLogins desc
```

This can help identify accounts with a high number of failed authentication events.

A SIEM Engineer working with Sentinel should become comfortable with:

==> `where`
==> `summarize`
==> `project`
==> `extend`
==> `join`
==> `count()`
==> Time filtering
==> Aggregation
==> Correlation

---

# 9. Microsoft Sentinel Data Flow

A simplified architecture:

```text
Data Sources
     │
     ▼
Data Connectors
     │
     ▼
Log Analytics
     │
     ▼
Analytics Rules
     │
     ▼
Incidents
     │
     ▼
SOC Analyst
     │
     ▼
Automation / Response
```

Sentinel supports connectors for bringing data from Microsoft and non-Microsoft sources into the platform.

---

# 10. IBM QRadar

**IBM QRadar** is another enterprise SIEM platform.

QRadar is known for centralized security event monitoring, correlation, offense management, and network/security data analysis.

Important concepts include:

==> Events
==> Flows
==> Log Sources
==> Offenses
==> Rules
==> CRE
==> DSM
==> Ariel
==> Reference Sets

---

# 11. QRadar Events

A QRadar environment can receive events from different sources:

==> Firewall
==> Windows
==> Linux
==> IDS/IPS
==> VPN
==> Proxy
==> Applications

QRadar can correlate events and generate an **Offense** when activity meets configured conditions.

For example:

```text
Multiple Failed Logins
        +
Successful Login
        +
Unusual Source
        ↓
     Offense
```

The SOC analyst can then investigate the offense.

---

# 12. QRadar DSM

**DSM** stands for **Device Support Module**.

It helps QRadar understand and process events from different device types.

A SIEM Engineer working with QRadar should understand:

==> Log Source configuration
==> DSM
==> Event parsing
==> Rules
==> Offenses
==> Reference Sets
==> Event properties

---

# 13. Elastic Security

**Elastic Security** provides security monitoring, detection, investigation, and threat hunting capabilities on top of the Elastic Stack.

Important components include:

==> Elasticsearch
==> Kibana
==> Elastic Agent
==> Beats
==> Data Streams
==> Detection Rules
==> Cases
==> Timeline
==> Threat Intelligence

---

# 14. Elasticsearch

**Elasticsearch** is a distributed search and analytics engine.

In an Elastic Security environment, security events can be stored and searched through Elasticsearch.

A simplified flow:

```text
Endpoint / Network
       │
       ▼
Elastic Agent
       │
       ▼
Elasticsearch
       │
       ▼
Kibana
       │
       ▼
Security Analyst
```

A SIEM Engineer should understand:

==> Indexing
==> Data Streams
==> Mappings
==> Fields
==> Querying
==> Shards
==> Replicas
==> Cluster health

---

# 15. OpenSearch

**OpenSearch** is an open-source search and analytics platform that is also used for security monitoring and log analytics.

An OpenSearch-based security environment can provide:

==> Log collection
==> Search
==> Dashboards
==> Alerting
==> Security analytics
==> Detection capabilities

For an engineer, useful concepts include:

==> OpenSearch
==> OpenSearch Dashboards
==> Index
==> Index Pattern
==> Data Stream
==> Query
==> Alert
==> Security Analytics

---

# 16. Wazuh

**Wazuh** is an open-source security platform commonly used for security monitoring, endpoint protection, threat detection, vulnerability detection, compliance monitoring, and log analysis.

For someone starting SIEM engineering, Wazuh can be a useful hands-on platform because it allows you to build a practical lab environment.

Important Wazuh components include:

==> Wazuh Agent
==> Wazuh Server
==> Wazuh Indexer
==> Wazuh Dashboard

---

# 17. Wazuh Architecture

A simplified Wazuh architecture:

```text
Windows ───┐
Linux ─────┤
            ▼
       Wazuh Agent
            │
            ▼
      Wazuh Server
            │
            ▼
      Wazuh Indexer
            │
            ▼
     Wazuh Dashboard
```

Wazuh can also receive logs from network devices and other systems through supported integration methods.

---

# 18. SIEM Platforms Have Similar Concepts

Although the products are different, many concepts are similar.

| Concept       | Splunk             | Sentinel       | QRadar       | Elastic        | Wazuh                        |
| ------------- | ------------------ | -------------- | ------------ | -------------- | ---------------------------- |
| Log/Data      | Events             | Logs           | Events       | Events         | Alerts/Events                |
| Search        | SPL                | KQL            | AQL          | Query DSL/KQL  | Search                       |
| Detection     | Correlation Search | Analytics Rule | Rule         | Detection Rule | Rules                        |
| Investigation | Search             | Investigation  | Offense      | Timeline       | Alert/Events                 |
| Dashboard     | Dashboard          | Workbook       | Dashboard    | Dashboard      | Dashboard                    |
| Automation    | SOAR/Integrations  | Playbooks      | Integrations | Connectors     | Active Response/Integrations |

The exact terminology and capabilities vary by product and version, but the underlying security workflow is similar.

---

# 19. Query Language Is a Core Skill

A SIEM Engineer should not depend entirely on the graphical interface.

You should know how to query the underlying data.

### Splunk

**SPL**

```text
index=auth
| stats count by user
```

### Microsoft Sentinel

**KQL**

```text
SigninLogs
| summarize count() by UserPrincipalName
```

### QRadar

**AQL**

Used to search and analyze QRadar event/flow data.

### Elastic/OpenSearch

Query languages and query APIs are used to search indexed security data.

The important skill is not memorizing syntax.

The important skill is understanding:

**What data do I need? → Where is it stored? → How do I filter it? → How do I correlate it?**

---

# 20. Detection Rules

SIEM platforms provide different mechanisms for detection.

Example:

**Possible Brute Force**

```text
Failed Login
      ↓
Failed Login
      ↓
Failed Login
      ↓
Failed Login
      ↓
Threshold Reached
      ↓
Alert
```

The implementation differs between platforms, but the security logic remains similar.

---

# 21. Alert vs Incident vs Offense

Different platforms use different terminology.

Generally:

**Event**

A single piece of activity.

↓

**Detection**

A rule identifies suspicious activity.

↓

**Alert**

The platform creates a security notification.

↓

**Incident/Offense**

Related suspicious activity may be grouped for investigation.

↓

**Investigation**

SOC analyst reviews evidence.

Understanding this distinction is important for SIEM Engineer interviews.

---

# 22. Dashboard

SIEM platforms provide dashboards to visualize security data.

Common dashboard components:

==> Alert count
==> Severity
==> Top source IPs
==> Top targeted assets
==> Failed authentication
==> Malware events
==> Network activity
==> Incident trends
==> Detection trends

But remember:

> **A dashboard is not a detection strategy.**

A beautiful dashboard is useful only when the underlying data and detection logic are reliable.

---

# 23. SIEM Platform Health

A SIEM Engineer also needs to monitor the platform itself.

Important metrics include:

==> CPU
==> Memory
==> Disk
==> Network
==> EPS
==> Ingestion latency
==> Queue size
==> Search performance
==> Storage utilization
==> Service health
==> Cluster health

The SIEM should be treated as a production security system.

---

# 24. Choosing a SIEM Platform

There is no single platform that fits every organization.

The choice may depend on:

==> Organization size
==> Existing infrastructure
==> Cloud strategy
==> Budget
==> Compliance requirements
==> Data volume
==> Security requirements
==> Existing Microsoft environment
==> Required integrations
==> Available engineering skills

For example, an organization heavily invested in Microsoft services may evaluate Microsoft Sentinel, while another organization may already have a mature Splunk environment.

The technical requirements and operational context should drive the decision.

---

# 25. What Should a SIEM Engineer Learn?

You do not need to master every platform at the same depth.

A practical approach is:

### Foundation

==> Networking
==> Linux
==> Windows
==> Authentication
==> Logs
==> Security fundamentals

### Choose One Primary SIEM

Go deep into one:

==> Splunk
**or**
==> Microsoft Sentinel
**or**
==> QRadar
**or**
==> Elastic
**or**
==> Wazuh

### Then Learn Others

After understanding one platform deeply, learn how the same concepts are implemented elsewhere.

For example:

**Splunk SPL**

↓

**KQL**

↓

**QRadar AQL**

↓

**Elastic/OpenSearch Query**

This makes it easier to move between SIEM technologies.

---

# 26. Practical Lab

You can create a small SIEM lab using:

```text
Windows VM
    │
Linux VM
    │
Network Device
    │
    ▼
  Wazuh
    │
    ▼
Dashboard
```

Then practice:

==> Generate failed SSH logins
==> Generate Windows authentication events
==> Collect logs
==> Search events
==> Create detection rules
==> Generate alerts
==> Investigate alerts
==> Tune false positives
==> Build dashboard
==> Configure Active Response

After that, repeat similar exercises using another SIEM platform.

This is much more valuable than only watching product demonstrations.

---

# 27. SIEM Engineer Interview Questions

### Q1. What is SIEM?

**Answer:**

SIEM stands for Security Information and Event Management. It provides centralized collection, analysis, correlation, detection, alerting, investigation, and reporting of security-related data.

### Q2. What SIEM platforms have you worked with?

A good answer should be honest.

For example:

> I have hands-on experience with Wazuh and have worked with Splunk-related concepts and security monitoring workflows. I understand log ingestion, parsing, detection rules, alert investigation, and SIEM operations, and I am continuously expanding my knowledge of other enterprise SIEM platforms.

### Q3. What is the difference between an Event and an Alert?

**Event** is an individual activity recorded by a system.

**Alert** is generated when a detection mechanism identifies activity that requires attention.

### Q4. What is a correlation rule?

A correlation rule combines multiple events or conditions to identify a potentially meaningful security event.

### Q5. Why is query language important?

Because SIEM Engineers and SOC analysts need to search large amounts of security data, investigate incidents, create detections, and perform threat hunting efficiently.

---

# 28. The Most Important Mindset

Do not learn SIEM platforms by memorizing menus.

Learn them by understanding the security workflow:

```text
Where does data come from?
          ↓
How is it collected?
          ↓
How is it stored?
          ↓
How do I search it?
          ↓
How do I detect threats?
          ↓
How do I investigate?
          ↓
How do I respond?
          ↓
How do I automate?
          ↓
How do I report?
```

Once you understand this workflow, learning a new SIEM becomes much easier.

---

# Final Takeaway

A SIEM Engineer is not simply a person who operates a SIEM dashboard.

A strong SIEM Engineer understands the relationship between:

**Log Sources → SIEM Platform → Query → Detection → Alert → Investigation → Response → Automation**

The platform may change:

**Splunk → Sentinel → QRadar → Elastic → OpenSearch → Wazuh**

but the fundamental security concepts remain connected.

If you understand those concepts deeply, you can adapt to different SIEM technologies much more effectively.

---

## Next Article

**SIEM Engineer #03 — Log Integration**

In the next article, we will go deeper into:

==> Syslog
==> CEF
==> API Integration
==> Agents
==> Forwarders
==> Cloud Connectors
==> Custom Parsers
==> Data Onboarding
==> Log Pipeline Troubleshooting

**Collecting logs is one thing. Successfully integrating them into a SIEM is another.**
