
# SIEM Engineer #11 — SIEM Architecture Design

A SIEM Engineer শুধু SIEM platform install বা alert monitor করে না।

একজন SIEM Engineer-এর গুরুত্বপূর্ণ দায়িত্ব হলো এমন একটি **SIEM Architecture** design করা, যেখানে হাজার হাজার বা millions of security events reliably collect, process, store, search, detect এবং investigate করা যায়।

এই article-এ আমরা SIEM Architecture-এর foundation থেকে **Enterprise Architecture, Single-node vs Distributed Architecture, Collector, Indexer, Search Layer, High Availability (HA), Scalability, Security, Disaster Recovery এবং Real-World Design** পর্যন্ত শিখব।

---

## 🧠 1. What is SIEM Architecture?

**SIEM Architecture** হলো একটি SIEM environment-এর বিভিন্ন components কীভাবে একে অপরের সাথে connected এবং কাজ করবে তার overall design।

একটি সাধারণ SIEM flow:

```text
Log Sources
    ↓
Collection
    ↓
Ingestion
    ↓
Parsing & Normalization
    ↓
Processing & Enrichment
    ↓
Indexing / Storage
    ↓
Search & Detection
    ↓
Alerts / Incidents
    ↓
Investigation
    ↓
Reporting
```

উদাহরণ:

```text
Firewall
Windows
Linux
Active Directory
Cloud
EDR
Network Devices
Applications
       |
       v
+----------------+
| Log Collectors |
+----------------+
       |
       v
+----------------+
| Ingestion      |
+----------------+
       |
       v
+----------------+
| Processing     |
| Parsing        |
| Normalization  |
| Enrichment     |
+----------------+
       |
       v
+----------------+
| Index / Storage|
+----------------+
       |
       v
+----------------+
| Search / SIEM  |
+----------------+
       |
       v
+----------------+
| Detection      |
+----------------+
       |
       v
+----------------+
| SOC Analyst    |
+----------------+
```

---

# 💡 2. Why does SIEM Architecture matter?

একটি SIEM ছোট environment-এ খুব সহজ হতে পারে।

কিন্তু environment বড় হলে কয়েকটি সমস্যা দেখা দেয়:

==> অনেক বেশি logs

==> High EPS

==> Storage growth

==> Search performance

==> Network latency

==> Single Point of Failure

==> Data loss

==> High availability requirement

==> Multiple SOC analysts

==> Compliance requirements

==> Disaster Recovery requirement

তাই SIEM deploy করার আগে architecture design করা অত্যন্ত গুরুত্বপূর্ণ।

---

# 🏗️ 3. SIEM Architecture Design Principles

একটি ভালো architecture design করার সময় কয়েকটি বিষয় মাথায় রাখতে হয়।

### মূল principles:

==> Scalability

==> Availability

==> Performance

==> Security

==> Reliability

==> Maintainability

==> Observability

==> Disaster Recovery

==> Cost efficiency

একটি ভালো architecture শুধু **আজকের workload** handle করবে না।

এটি future growth-এর জন্যও প্রস্তুত থাকবে।

---

# 🏠 4. Small SIEM Architecture

ছোট organization বা lab environment-এর জন্য single-node architecture যথেষ্ট হতে পারে।

```text
+----------------------+
| Windows / Linux      |
| Firewall / Network   |
| Applications         |
+----------+-----------+
           |
           v
+----------------------+
|      SIEM Node       |
|                      |
| Collection           |
| Processing           |
| Storage              |
| Detection            |
| Search               |
| Dashboard            |
+----------+-----------+
           |
           v
+----------------------+
|     SOC Analyst      |
+----------------------+
```

এখানে একটি server অনেকগুলো কাজ করতে পারে।

==> Log collection

==> Processing

==> Storage

==> Detection

==> Search

==> Dashboard

### সুবিধা

==> Simple deployment

==> Low cost

==> Easy management

==> Lab-এর জন্য ভালো

### সীমাবদ্ধতা

==> Single Point of Failure

==> Limited scalability

==> Resource contention

==> Large workload-এ performance সমস্যা হতে পারে

---

# 🏢 5. Medium SIEM Architecture

Medium environment-এ components আলাদা করা শুরু করা যায়।

```text
              Log Sources
                   |
                   v
          +----------------+
          |   Collectors   |
          +--------+-------+
                   |
                   v
          +----------------+
          |   Processing   |
          +--------+-------+
                   |
                   v
          +----------------+
          | Index / Storage|
          +--------+-------+
                   |
                   v
          +----------------+
          | Search / SIEM  |
          +--------+-------+
                   |
                   v
          +----------------+
          | Dashboard/SOC  |
          +----------------+
```

এতে workload আলাদা করা যায়।

উদাহরণ:

==> Collector শুধু logs collect করবে

==> Processing layer parsing করবে

==> Indexer data store করবে

==> Search layer queries handle করবে

==> Dashboard analyst interface provide করবে

---

# 🌐 6. Enterprise SIEM Architecture

Large enterprise environment-এ distributed architecture বেশি প্রয়োজন হয়।

```text
                  Internet
                     |
              +--------------+
              |   Firewall   |
              +------+-------+
                     |
        +------------+------------+
        |            |            |
        v            v            v
    Windows        Linux       Network
    Servers        Servers      Devices
        |            |            |
        +------------+------------+
                     |
                     v
             +---------------+
             |   Collectors  |
             |  / Forwarders |
             +-------+-------+
                     |
                     v
             +---------------+
             | Ingestion Bus |
             | / Processing   |
             +-------+-------+
                     |
          +----------+----------+
          |          |          |
          v          v          v
      Indexer 1  Indexer 2  Indexer 3
          |          |          |
          +----------+----------+
                     |
                     v
              Search Layer
                     |
          +----------+----------+
          |          |          |
          v          v          v
       SOC L1     SOC L2     SOC L3
```

এখানে system-এর বিভিন্ন অংশ আলাদা করে scale করা যায়।

---

# 🔄 7. Centralized vs Distributed Architecture

## Centralized Architecture

সব logs একটি central SIEM environment-এ পাঠানো হয়।

```text
Sources
  |
  +----> SIEM
  |
  +----> SIEM
  |
  +----> SIEM
```

### সুবিধা

==> Simple management

==> Centralized visibility

==> Easy investigation

==> Easier policy management

### সমস্যা

==> Network dependency

==> Central bottleneck হতে পারে

==> Large scale-এ scalability challenge

---

# 🌍 8. Distributed Architecture

Large environment-এ বিভিন্ন location বা network segment-এ collectors রাখা যায়।

```text
              Central SIEM
                   |
        +----------+----------+
        |          |          |
        v          v          v
     Region A   Region B   Region C
     Collector  Collector  Collector
        |          |          |
        v          v          v
      Logs       Logs       Logs
```

উদাহরণ:

==> Dhaka Data Center

==> Chattogram Data Center

==> Cloud Environment

==> Remote Office

প্রতিটি location local collection করতে পারে এবং central SIEM-এ normalized data পাঠাতে পারে।

---

# 🖥️ 9. Single-node vs Multi-node

## Single-node

একটি node বিভিন্ন services চালায়।

```text
+----------------------+
|       SIEM Node      |
|                      |
| Collector            |
| Processing           |
| Storage              |
| Search               |
| Detection            |
| Dashboard            |
+----------------------+
```

এটি সাধারণত:

==> Lab

==> Small organization

==> POC

==> Training environment

-এর জন্য ব্যবহারযোগ্য।

---

## Multi-node

Different workloads different nodes-এ distribute করা হয়।

```text
              +-------------+
              | Collectors  |
              +------+------+
                     |
                     v
              +-------------+
              | Processing  |
              +------+------+
                     |
          +----------+----------+
          |          |          |
          v          v          v
       Indexer    Indexer    Indexer
          |          |          |
          +----------+----------+
                     |
                     v
                Search Layer
```

### সুবিধা

==> Better scalability

==> Better availability

==> Workload separation

==> Easier capacity planning

==> Better performance isolation

---

# 📥 10. Collector

**Collector** হলো এমন component যা বিভিন্ন source থেকে logs/events collect করে।

Sources হতে পারে:

==> Windows

==> Linux

==> Firewall

==> Router

==> Switch

==> Active Directory

==> Database

==> Web Server

==> Application

==> Cloud service

==> EDR

==> IDS/IPS

Collector-এর কাজ:

```text
Source
  ↓
Collect
  ↓
Buffer
  ↓
Forward
```

---

# 🚚 11. Forwarder

Forwarder একটি source বা intermediate system থেকে logs SIEM-এর দিকে forward করে।

```text
Server
   |
   v
Forwarder
   |
   v
Collector
   |
   v
SIEM
```

Forwarder architecture-এর সুবিধা:

==> Network traffic control

==> Local buffering

==> Reliable forwarding

==> Centralized ingestion

==> Remote site support

---

# 📡 12. Ingestion Layer

**Ingestion Layer** হলো SIEM-এর সেই অংশ যেখানে collected events system-এর ভিতরে প্রবেশ করে।

```text
Logs
 ↓
Network Transport
 ↓
Ingestion
 ↓
Queue / Buffer
 ↓
Processing
```

Ingestion layer-এর গুরুত্বপূর্ণ বিষয়:

==> Throughput

==> Buffering

==> Backpressure

==> Reliability

==> Authentication

==> Encryption

==> Error handling

---

# ⚙️ 13. Processing Layer

Raw logs সরাসরি investigation-এর জন্য সবসময় useful নয়।

Processing layer data-কে usable format-এ convert করে।

```text
Raw Log
   ↓
Parsing
   ↓
Normalization
   ↓
Field Extraction
   ↓
Enrichment
   ↓
Correlation
   ↓
Processed Event
```

উদাহরণ:

```text
Raw:
Failed password for admin from 10.10.10.50

Normalized:

event.category = authentication
event.action   = login_failed
user.name      = admin
source.ip      = 10.10.10.50
```

এতে detection এবং investigation সহজ হয়।

---

# 🗄️ 14. Indexer / Storage Layer

Processed events storage/indexing system-এ যায়।

```text
Processed Events
       |
       v
+----------------+
| Indexer        |
+----------------+
       |
       v
+----------------+
| Storage        |
+----------------+
```

Indexer-এর primary responsibilities:

==> Index events

==> Store searchable data

==> Support queries

==> Manage data lifecycle

==> Support retention policies

Large deployment-এ একাধিক indexer ব্যবহার করা যেতে পারে।

---

# 🔎 15. Search Layer

Search layer analysts এবং detection systems-কে data query করতে সাহায্য করে।

```text
SOC Analyst
     |
     v
Search Query
     |
     v
Search Layer
     |
     v
Indexes
     |
     v
Results
```

উদাহরণ:

```text
Find all failed logins
from source IP 10.10.10.50
during the last 24 hours.
```

Search layer-এর performance SIEM-এর overall user experience-এ বড় ভূমিকা রাখে।

---

# 🖥️ 16. Dashboard Layer

Dashboard হলো analyst এবং management-এর জন্য visualization layer।

এখানে থাকতে পারে:

==> Security Alerts

==> Authentication Events

==> Failed Logins

==> Malware Alerts

==> Firewall Events

==> Top Source IPs

==> Top Destination IPs

==> Detection Trends

==> Incident Metrics

==> System Health

---

# 🧠 17. Detection Layer

Detection engine incoming events analyse করে suspicious activity identify করে।

```text
Event
  ↓
Detection Rule
  ↓
Condition Match?
  ↓
Yes
  ↓
Alert
  ↓
SOC Investigation
```

Detection logic হতে পারে:

==> Signature-based

==> Threshold-based

==> Correlation-based

==> Behavioral

==> Sequence-based

==> Risk-based

Detection Engineering নিয়ে বিস্তারিত আমরা **#14 Advanced Detection Engineering**-এ দেখব।

---

# 🔗 18. SIEM Components — Complete View

একটি enterprise SIEM-কে এভাবে চিন্তা করতে পারেন:

```text
                  LOG SOURCES
                      |
                      v
             +----------------+
             |   Collectors   |
             +----------------+
                      |
                      v
             +----------------+
             |   Forwarders   |
             +----------------+
                      |
                      v
             +----------------+
             |   Ingestion    |
             +----------------+
                      |
                      v
             +----------------+
             |   Processing   |
             | Parse/Normalize|
             +----------------+
                      |
                      v
             +----------------+
             | Index / Storage|
             +----------------+
                      |
                      v
             +----------------+
             | Search Layer   |
             +----------------+
                      |
          +-----------+-----------+
          |                       |
          v                       v
     Detection                 Dashboard
          |                       |
          v                       v
       Alerts                  Analysts
          |
          v
      Incident
```

---

# 🚀 19. High Availability — HA

**High Availability (HA)** মানে system-এর একটি component failure হলেও service যতটা সম্ভব available রাখা।

ধরুন:

```text
Collector
    |
    v
SIEM Node
```

SIEM node down হলে ingestion বন্ধ হয়ে যেতে পারে।

এটি Single Point of Failure।

HA architecture:

```text
             Load Balancer
                  |
          +-------+-------+
          |               |
          v               v
       SIEM Node 1     SIEM Node 2
          |               |
          +-------+-------+
                  |
                  v
              Storage
```

এতে একটি node failure হলেও অন্য node service continue করতে পারে—যদি platform এবং architecture সেই failover support করে।

---

# ⚖️ 20. Load Balancing

একটি node-এর উপর সব workload না দিয়ে traffic distribute করা যায়।

```text
                  Clients
                     |
                     v
              +-------------+
              |Load Balancer|
              +------+------+
                     |
             +-------+-------+
             |       |       |
             v       v       v
          Node 1  Node 2  Node 3
```

Load balancing ব্যবহার করা যায়:

==> Log ingestion

==> API traffic

==> Search requests

==> Web interface

==> Collector traffic

---

# 📈 21. Scalability

Scalability হলো workload বাড়লে system-এর capacity বাড়ানোর ability।

দুই ধরনের scaling গুরুত্বপূর্ণ।

## Vertical Scaling

একটি server-এর resources বাড়ানো।

```text
8 CPU
32 GB RAM
      ↓
16 CPU
64 GB RAM
```

## Horizontal Scaling

আরও nodes যোগ করা।

```text
Node 1
Node 2
Node 3
   ↓
Node 4
Node 5
```

Large SIEM environment-এ workload অনুযায়ী horizontal scaling গুরুত্বপূর্ণ হতে পারে।

---

# 📊 22. Architecture Design-এর আগে কী জানতে হবে?

SIEM architecture design করার আগে requirements collect করতে হবে।

### Questions:

==> কতগুলো log source আছে?

==> কত EPS generate হচ্ছে?

==> Peak EPS কত?

==> প্রতিদিন কত GB logs?

==> Retention কতদিন?

==> কতজন analyst?

==> কতগুলো office/data center?

==> Cloud environment আছে?

==> Compliance requirement কী?

==> HA requirement কী?

==> RPO কী?

==> RTO কী?

==> Future growth কত?

এই প্রশ্নগুলোর উত্তর ছাড়া architecture blindly design করা উচিত নয়।

---

# 📦 23. EPS — Events Per Second

SIEM architecture-এর সবচেয়ে গুরুত্বপূর্ণ sizing inputs-এর একটি হলো **EPS**।

EPS মানে:

**Events Per Second**

উদাহরণ:

```text
Average EPS = 5,000

Peak EPS = 12,000
```

Architecture design করার সময় শুধু average EPS দেখলে হবে না।

**Peak workload** consider করতে হবে।

কারণ attack বা incident-এর সময় event volume অনেক বেড়ে যেতে পারে।

Capacity Planning আমরা **#12**-এ বিস্তারিত করব।

---

# 💾 24. Storage Architecture

SIEM environment-এ storage খুব গুরুত্বপূর্ণ।

একটি conceptual storage model:

```text
            Incoming Logs
                  |
                  v
            Hot Storage
                  |
                  v
            Warm Storage
                  |
                  v
            Cold Storage
                  |
                  v
             Archive
```

### Hot

Frequently searched data।

### Warm

Less frequently accessed data।

### Cold

Long-term retention-এর জন্য।

### Archive

Compliance বা historical requirement-এর জন্য রাখা data।

Actual tiers এবং capabilities platform অনুযায়ী আলাদা হতে পারে।

---

# 🔐 25. SIEM Network Architecture

SIEM environment-কে security zones-এর মধ্যে design করা ভালো।

উদাহরণ:

```text
                Internet
                    |
                Firewall
                    |
          +---------+---------+
          |                   |
       DMZ Zone           Internal Zone
          |                   |
          v                   v
     Web Servers          AD/Servers
          |                   |
          +---------+---------+
                    |
                    v
              SIEM Network
                    |
          +---------+---------+
          |                   |
       Collectors          SIEM Core
                              |
                              v
                          SOC Users
```

Principles:

==> Least privilege

==> Network segmentation

==> Restricted management access

==> TLS where supported

==> Firewall rules

==> Administrative access control

==> Monitoring

---

# 🔒 26. SIEM Security Architecture

SIEM নিজেই একটি highly sensitive system।

কারণ SIEM-এর মধ্যে থাকতে পারে:

==> Authentication logs

==> User information

==> IP addresses

==> Security alerts

==> Investigation data

==> Threat intelligence

==> Incident information

তাই SIEM security গুরুত্বপূর্ণ।

### Security controls:

==> RBAC

==> MFA যেখানে supported

==> TLS encryption

==> Secure API authentication

==> Secrets management

==> Admin network restriction

==> Audit logging

==> Certificate management

==> Regular patching

==> Backup protection

==> Strong authentication

---

# 👥 27. Role-Based Access Control — RBAC

সব analyst-এর একই permission থাকা উচিত নয়।

Example:

```text
SOC L1
  ↓
Read + Triage

SOC L2
  ↓
Investigation + Case Management

SOC L3
  ↓
Advanced Investigation + Detection

SIEM Engineer
  ↓
Configuration + Integration

Administrator
  ↓
Platform Administration
```

Exact roles organization এবং platform অনুযায়ী আলাদা হবে।

---

# 🌍 28. On-Prem SIEM Architecture

On-prem environment:

```text
Servers
   |
Network
   |
Collectors
   |
SIEM Infrastructure
   |
Storage
   |
SOC
```

Advantages:

==> Infrastructure control

==> Data residency control

==> Custom networking

==> Internal integration

Challenges:

==> Hardware cost

==> Maintenance

==> Scaling

==> Backup

==> DR

==> Infrastructure management

---

# ☁️ 29. Cloud SIEM Architecture

Cloud SIEM environment-এ cloud services এবং cloud-native data sources integrate করা হয়।

```text
Cloud Services
      |
      v
Cloud Logs
      |
      v
SIEM / Analytics
      |
      v
Detection
      |
      v
SOC
```

Considerations:

==> API integration

==> Cloud identity

==> Network connectivity

==> Data transfer

==> Storage cost

==> Access control

==> Multi-account architecture

---

# 🔀 30. Hybrid SIEM Architecture

অনেক organization-এর on-prem + cloud দুই environment থাকে।

```text
 On-Prem                       Cloud
    |                             |
    v                             v
Servers                       Cloud Services
    |                             |
    v                             v
Collectors                    Cloud Logs
    |                             |
    +-------------+---------------+
                  |
                  v
             Central SIEM
                  |
                  v
                 SOC
```

Hybrid architecture-এ data integration এবং secure connectivity খুব গুরুত্বপূর্ণ।

---

# 🛡️ 31. Disaster Recovery — DR

SIEM architecture শুধু primary environment নিয়ে design করা উচিত নয়।

ধরুন:

```text
Primary SIEM
     |
     X
  Failure
     |
     v
DR SIEM
```

DR planning-এর গুরুত্বপূর্ণ বিষয়:

==> Backup

==> Replication যেখানে supported

==> Configuration backup

==> Detection rule backup

==> Dashboard backup

==> Integration configuration

==> Certificate/secret recovery process

==> Restore testing

---

# ⏱️ 32. RPO and RTO

### RPO — Recovery Point Objective

Failure-এর পরে সর্বোচ্চ কত data loss acceptable?

Example:

```text
RPO = 15 minutes
```

মানে organization এমন recovery design করতে চায় যাতে data-loss window roughly 15 minutes-এর মধ্যে রাখা যায়।

### RTO — Recovery Time Objective

Service কত সময়ের মধ্যে restore করতে হবে?

Example:

```text
RTO = 1 hour
```

অর্থাৎ recovery process-এর target হলো service প্রায় 1 hour-এর মধ্যে restore করা।

Actual targets organization-এর business requirements অনুযায়ী নির্ধারিত হবে।

---

# 📡 33. Observability & Health Monitoring

SIEM-এর নিজের health monitor করতে হবে।

Monitor করুন:

==> EPS

==> Ingestion rate

==> Event latency

==> Queue size

==> CPU

==> RAM

==> Disk usage

==> Disk I/O

==> Network

==> Search latency

==> Failed ingestion

==> Collector status

==> Index health

==> Certificate expiry

==> Service availability

একজন SIEM Engineer-এর জন্য **SIEM health monitoring** অত্যন্ত গুরুত্বপূর্ণ।

---

# 🔧 34. Common SIEM Architecture Mistakes

### ❌ Mistake 1 — শুধু current workload দেখা

Future growth consider না করলে কয়েক মাস পরে capacity problem হতে পারে।

### ❌ Mistake 2 — Single Point of Failure

একটি server-এর উপর পুরো SIEM depend করা।

### ❌ Mistake 3 — Peak EPS ignore করা

Average EPS দিয়ে architecture design করা।

### ❌ Mistake 4 — Storage underestimate করা

Retention এবং growth ঠিকভাবে calculate না করা।

### ❌ Mistake 5 — Network architecture ignore করা

সব logs direct central system-এ পাঠানো কিন্তু bandwidth এবং latency analysis না করা।

### ❌ Mistake 6 — Security ignore করা

SIEM-কে normal application server হিসেবে treat করা।

### ❌ Mistake 7 — Backup test না করা

Backup আছে কিন্তু restore কখনও test করা হয়নি।

### ❌ Mistake 8 — Monitoring না রাখা

SIEM itself unhealthy হলেও কেউ জানতে পারছে না।

### ❌ Mistake 9 — Documentation না করা

কোন source কোথায় connected—তা documented না থাকা।

---

# 🧪 35. Practical SIEM Architecture Lab

একটি learning lab-এর জন্য আপনি এমন architecture তৈরি করতে পারেন:

```text
                 Internet
                    |
                 Firewall
                    |
          +---------+---------+
          |                   |
          v                   v
     Windows VM            Linux VM
          |                   |
          +---------+---------+
                    |
                    v
              Wazuh Server
                    |
          +---------+---------+
          |                   |
          v                   v
       Dashboard             API
          |
          v
      SOC Analyst
```

তারপর ধীরে ধীরে add করুন:

```text
Firewall
   ↓
Network Device
   ↓
Threat Intelligence
   ↓
Detection Rules
   ↓
Automation
   ↓
Ticketing
```

এভাবে একটি ছোট SOC architecture ধীরে ধীরে enterprise-style architecture-এ evolve করা যায়।

---

# 🏢 36. Real-World Example

ধরুন একটি organization-এর:

==> 2,000 endpoints

==> Windows Servers

==> Linux Servers

==> Active Directory

==> Firewalls

==> Routers/Switches

==> Web Applications

==> Cloud workloads

এবং একটি SOC team আছে।

একটি conceptual architecture হতে পারে:

```text
                  LOG SOURCES
                       |
      +----------------+----------------+
      |                |                |
   Windows           Linux          Network
      |                |             Devices
      +----------------+----------------+
                       |
                       v
              Regional Collectors
                       |
                       v
                Ingestion Layer
                       |
                       v
               Processing Layer
                       |
             +---------+---------+
             |         |         |
             v         v         v
          Indexer   Indexer   Indexer
             |         |         |
             +---------+---------+
                       |
                       v
                  Search Layer
                       |
             +---------+---------+
             |                   |
             v                   v
        Detection             Dashboard
             |
             v
          Alerts
             |
             v
         SOC Analysts
```

এর সাথে:

```text
Threat Intelligence
        |
        v
   Enrichment
        |
        v
    Detection
```

এবং:

```text
SIEM
 |
 v
SOAR / Automation
 |
 +----> Ticketing
 |
 +----> Notification
 |
 +----> Controlled Response
```

---

# 🧩 37. SIEM Architecture Design Process

একজন SIEM Engineer architecture design করার সময় এই process follow করতে পারেন:

```text
Requirements
     ↓
Asset & Log Source Discovery
     ↓
EPS & Data Volume
     ↓
Retention
     ↓
Capacity Planning
     ↓
Component Design
     ↓
Network Design
     ↓
Security Design
     ↓
HA Design
     ↓
DR Design
     ↓
Implementation
     ↓
Testing
     ↓
Monitoring
     ↓
Documentation
     ↓
Continuous Improvement
```

এটাই একটি practical architecture design lifecycle।

---

# 📝 38. Architecture Documentation

Architecture design করার পরে documentation করতে হবে।

Documentation-এ থাকতে পারে:

==> Architecture diagram

==> IP/network zones

==> Data sources

==> Collectors

==> Ingestion paths

==> Storage

==> Retention

==> Detection components

==> Integrations

==> HA configuration

==> DR configuration

==> Backup process

==> Monitoring

==> Ports and protocols

==> Authentication

==> Ownership

==> Troubleshooting procedure

---

# 🔍 39. SIEM Platform Architecture — Conceptual View

Different SIEM platforms-এর terminology এবং internal architecture আলাদা হতে পারে।

তবে conceptual layers অনেক ক্ষেত্রে একই ধরনের:

```text
Data Sources
     ↓
Collection
     ↓
Ingestion
     ↓
Processing
     ↓
Storage / Indexing
     ↓
Search / Analytics
     ↓
Detection
     ↓
Alert / Incident
     ↓
SOC
```

### Wazuh

Conceptually:

```text
Agents / Network Devices
          ↓
      Collection
          ↓
     Wazuh Manager
          ↓
 Rules / Analysis
          ↓
   Indexed / Stored Data
          ↓
       Dashboard
```

### Splunk

একটি conceptual Splunk architecture-এ সাধারণত:

```text
Data Sources
     ↓
Forwarding / Collection
     ↓
Indexing
     ↓
Search / Analytics
     ↓
Dashboards / Alerts
```

### Microsoft Sentinel

Cloud-oriented conceptual architecture:

```text
Cloud / On-Prem Sources
          ↓
       Connectors
          ↓
      Data Platform
          ↓
Analytics / Detection
          ↓
Incidents / Investigation
          ↓
        SOC
```

### Elastic / OpenSearch

Conceptually:

```text
Sources
  ↓
Agents / Collectors
  ↓
Ingestion
  ↓
Processing
  ↓
Indexes
  ↓
Search / Analytics
  ↓
Detection / Dashboard
```

**Important:** এগুলো conceptual architecture। Actual components, deployment models এবং capabilities platform/version অনুযায়ী পরিবর্তিত হতে পারে।

---

# 🎯 40. SIEM Architecture Interview Questions & Answers

## Q1. What is SIEM Architecture?

**Answer:**

SIEM Architecture defines how log sources, collectors, ingestion, processing, storage, indexing, search, detection, dashboards and SOC workflows are connected to provide centralized security monitoring.

---

## Q2. Single-node and distributed SIEM-এর মধ্যে পার্থক্য কী?

**Answer:**

Single-node architecture-এ multiple SIEM functions একই node-এ run করে।

Distributed architecture-এ collection, processing, indexing, search এবং অন্যান্য workloads multiple nodes-এ distribute করা হয়।

Distributed architecture generally provides better scalability and workload separation.

---

## Q3. What is a SIEM Collector?

**Answer:**

A collector receives security events from sources such as servers, firewalls, network devices and applications and forwards them to the SIEM processing or ingestion layer.

---

## Q4. What is an Indexer?

**Answer:**

An indexer processes and organizes events into searchable structures and stores the data so that analysts and detection systems can query it efficiently.

---

## Q5. Why is High Availability important in SIEM?

**Answer:**

SIEM is a critical security monitoring system. If a single component fails, organizations may lose visibility or miss security events. HA reduces dependency on a single component and improves service availability.

---

## Q6. What is the difference between vertical and horizontal scaling?

**Answer:**

Vertical scaling means increasing resources such as CPU, RAM or storage on an existing node.

Horizontal scaling means adding more nodes to distribute the workload.

---

## Q7. What factors do you consider when designing SIEM architecture?

**Answer:**

I consider:

==> EPS

==> Peak EPS

==> Data volume

==> Retention

==> Log sources

==> Network architecture

==> Storage

==> Search workload

==> HA

==> Security

==> DR

==> RPO/RTO

==> Future growth

==> Cost

---

## Q8. Why should peak EPS be considered?

**Answer:**

Average traffic does not represent the workload during incidents or attack periods. Security events can increase significantly during abnormal activity, so architecture should handle expected peak workload with an appropriate safety margin.

---

## Q9. What is RPO?

**Answer:**

RPO stands for Recovery Point Objective. It defines the acceptable amount of data loss measured in time after a failure.

---

## Q10. What is RTO?

**Answer:**

RTO stands for Recovery Time Objective. It defines the target time within which a service should be restored after a failure.

---

## Q11. How would you troubleshoot a SIEM architecture where logs are delayed?

**Answer:**

I would check:

```text
Source
 ↓
Collector
 ↓
Network
 ↓
Ingestion
 ↓
Queue
 ↓
Processing
 ↓
Indexer
 ↓
Search
```

Then check:

==> Source timestamp

==> Network latency

==> Collector health

==> Queue/backpressure

==> Processing latency

==> Indexing performance

==> Storage I/O

==> Search latency

This approach helps identify where the delay occurs.

---

# ✅ 41. SIEM Architecture Checklist

Architecture final করার আগে check করুন:

### Requirements

==> Log sources identified

==> EPS measured

==> Peak EPS identified

==> Retention defined

==> Compliance requirements identified

### Infrastructure

==> CPU planned

==> RAM planned

==> Storage planned

==> Network planned

==> Scaling strategy defined

### Architecture

==> Collector design complete

==> Ingestion design complete

==> Processing design complete

==> Indexing design complete

==> Search design complete

### Availability

==> HA requirement defined

==> Failover tested

==> Load balancing considered

==> Single Points of Failure identified

### Security

==> RBAC configured

==> TLS considered

==> Admin access restricted

==> Secrets protected

==> Audit logging enabled

### DR

==> Backup defined

==> RPO defined

==> RTO defined

==> Restore tested

### Operations

==> Monitoring configured

==> Alerting configured

==> Documentation completed

==> Troubleshooting runbook available

---

# 🔄 42. Complete SIEM Architecture Flow

একজন SIEM Engineer হিসেবে এই flow-টা মনে রাখুন:

```text
                    LOG SOURCES
                         |
                         v
              +--------------------+
              | Collection Layer   |
              +---------+----------+
                        |
                        v
              +--------------------+
              | Ingestion Layer    |
              +---------+----------+
                        |
                        v
              +--------------------+
              | Processing Layer   |
              | Parse / Normalize  |
              | Enrichment         |
              +---------+----------+
                        |
                        v
              +--------------------+
              | Index / Storage    |
              +---------+----------+
                        |
                        v
              +--------------------+
              | Search / Analytics |
              +---------+----------+
                        |
                        v
              +--------------------+
              | Detection Engine   |
              +---------+----------+
                        |
                        v
              +--------------------+
              | Alert / Incident   |
              +---------+----------+
                        |
                        v
              +--------------------+
              | SOC Investigation  |
              +---------+----------+
                        |
                        v
              +--------------------+
              | Response / Closure |
              +--------------------+
```

এটাই SIEM-এর complete logical architecture flow।

---

# 💡 43. What should a SIEM Engineer remember?

একটি SIEM architecture design করার সময় শুধু **"কোন SIEM software ব্যবহার করব?"** এই প্রশ্ন করা যথেষ্ট নয়।

একজন SIEM Engineer-কে ভাবতে হবে:

```text
How much data?
       ↓
Where is data coming from?
       ↓
How will we collect it?
       ↓
How will we transport it?
       ↓
How will we process it?
       ↓
How will we store it?
       ↓
How will analysts search it?
       ↓
How will we detect threats?
       ↓
How will we survive failures?
       ↓
How will we scale?
       ↓
How will we secure the SIEM?
       ↓
How will we recover it?
```

এটাই একজন **SIEM Engineer-এর architecture mindset**।

---

# 🚀 Practical Security Takeaway

SIEM Architecture হলো পুরো SOC/SIEM environment-এর foundation।

একটি ভালো architecture:

==> Reliable log collection নিশ্চিত করে

==> Detection-এর জন্য quality data দেয়

==> Investigation দ্রুত করে

==> Single Point of Failure কমায়

==> Future growth support করে

==> Security এবং compliance requirements support করে

==> Disaster-এর সময় recovery সহজ করে

**Remember:**

> **Good SIEM Architecture = Reliable Data + Scalable Infrastructure + Fast Detection + High Availability + Secure Operations**

---

# 📚 Next in the SIEM Engineer Series

### Previous

==> **#10 — SIEM Infrastructure**

### Current

==> **#11 — SIEM Architecture Design**

### Next

==> **#12 — SIEM Capacity Planning**

Next article-এ আমরা practical calculation শিখব:

==> EPS Calculation

==> Events Per Day

==> GB/day

==> Storage Calculation

==> Retention Planning

==> Peak Load

==> Growth Estimation

==> Capacity Buffer

==> Real-world SIEM sizing example

---


