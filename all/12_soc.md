# 🟢🟡🔴 SIEM Engineer #12 — SIEM Capacity Planning

A SIEM Engineer-এর জন্য শুধু SIEM install করা যথেষ্ট নয়।

একটি SIEM environment-এ কতগুলো **events per second (EPS)** আসবে, প্রতিদিন কত **GB/TB data** তৈরি হবে, কতদিন data retain করতে হবে, কত storage লাগবে এবং future-এ workload কতটা বাড়তে পারে—এসব আগে থেকেই plan করতে হয়।

এই process-কে বলা হয় **SIEM Capacity Planning**।

এই article-এ আমরা practicalভাবে শিখব:

==> EPS Calculation
==> Events Per Day
==> GB/day
==> Storage Planning
==> Retention
==> Peak Load
==> Growth Estimation
==> Capacity Buffer
==> Real-world SIEM sizing

---

# 🧠 1. What is SIEM Capacity Planning?

**SIEM Capacity Planning** হলো future এবং current workload অনুযায়ী SIEM-এর required compute, storage, network এবং processing capacity নির্ধারণ করার process।

সহজভাবে:

```text
How much data?
       ↓
How fast?
       ↓
How long?
       ↓
How much storage?
       ↓
How much CPU/RAM?
       ↓
How much network?
       ↓
How much future growth?
```

---

# 💡 2. Why does Capacity Planning matter?

Capacity ঠিকভাবে plan না করলে SIEM environment-এ বিভিন্ন সমস্যা হতে পারে।

==> Logs drop হতে পারে

==> Events delayed হতে পারে

==> Search slow হতে পারে

==> Storage full হতে পারে

==> Detection delayed হতে পারে

==> CPU/RAM saturation হতে পারে

==> Network congestion হতে পারে

==> Investigation difficult হতে পারে

==> Future growth handle করা কঠিন হতে পারে

একজন SIEM Engineer-এর লক্ষ্য হলো **আজকের workload এবং আগামী দিনের growth—দুটোই বিবেচনা করা।**

---

# 📊 3. Key Capacity Metrics

SIEM capacity planning-এর সময় কয়েকটি metric সবচেয়ে গুরুত্বপূর্ণ।

==> EPS

==> Peak EPS

==> Events Per Day

==> Average Event Size

==> GB/day

==> Retention Period

==> Storage Requirement

==> Search Workload

==> CPU

==> RAM

==> Network Bandwidth

==> Growth Rate

---

# ⚡ 4. What is EPS?

**EPS = Events Per Second**

এটি প্রতি second-এ SIEM কতগুলো events receive/process করছে তা বোঝায়।

উদাহরণ:

```text
Average EPS = 1,000
Peak EPS    = 3,000
```

অর্থাৎ সাধারণ সময়ে প্রায় 1,000 events/sec আসতে পারে, কিন্তু peak period-এ 3,000 events/sec পর্যন্ত যেতে পারে।

---

# 🧮 5. EPS Calculation

ধরুন:

```text
Total Events = 86,400,000
Time         = 24 hours
```

24 hours:

```text
24 × 60 × 60
= 86,400 seconds
```

তাহলে:

```text
EPS = Total Events / Total Seconds

EPS = 86,400,000 / 86,400

EPS = 1,000
```

অর্থাৎ average EPS = **1,000 EPS**।

---

# 📅 6. Events Per Day

যদি EPS জানা থাকে:

```text
Events/day = EPS × 86,400
```

Example:

```text
EPS = 1,000

Events/day
= 1,000 × 86,400
= 86,400,000 events/day
```

অর্থাৎ প্রতিদিন প্রায় **86.4 million events**।

---

# 📦 7. Average Event Size

Storage planning-এর জন্য event size জানা দরকার।

ধরুন average event size:

```text
1 KB
```

এবং:

```text
EPS = 1,000
```

তাহলে প্রতি second:

```text
1,000 × 1 KB
= 1,000 KB/sec
```

অর্থাৎ প্রায়:

```text
1 MB/sec
```

---

# 💾 8. GB Per Day Calculation

ধরুন:

```text
EPS = 1,000
Average Event Size = 1 KB
```

Events/day:

```text
86,400,000
```

Raw data:

```text
86,400,000 × 1 KB
= 86,400,000 KB
```

Decimal storage হিসেবে এটি প্রায়:

```text
86.4 GB/day
```

অর্থাৎ:

**1,000 EPS × 1 KB event ≈ 86.4 GB/day raw data**

এটি একটি simplified estimation।

Actual SIEM storage raw data-এর চেয়ে বেশি বা কম হতে পারে, কারণ indexing, metadata, replication, compression এবং platform-specific overhead থাকতে পারে।

---

# 🧮 9. General Storage Formula

একটি basic estimation:

```text
Daily Storage
=
EPS × Average Event Size × 86,400
```

তারপর retention:

```text
Retention Storage
=
Daily Storage × Retention Days
```

Example:

```text
Daily Data = 100 GB
Retention = 30 days

100 × 30
= 3,000 GB

≈ 3 TB
```

এটি raw-data estimate।

Actual provisioned storage-এর জন্য additional overhead এবং safety margin consider করতে হবে।

---

# 📦 10. Storage Planning

SIEM storage planning-এর সময় শুধু raw data calculate করলেই হবে না।

Consider করুন:

==> Raw event data

==> Index overhead

==> Metadata

==> Replication

==> Compression

==> Hot/warm/cold storage

==> Backup

==> Temporary files

==> Free-space requirement

==> Growth buffer

---

# 🔥 11. Hot Storage

Hot storage-এ frequently searched data রাখা হয়।

উদাহরণ:

```text
Last 7 days
```

এখানে SOC analyst frequently investigation করতে পারে।

Advantages:

==> Fast search

==> Fast investigation

==> Recent incidents সহজে analyse করা যায়

---

# 🌡️ 12. Warm Storage

Warm storage তুলনামূলকভাবে কম frequently accessed data-এর জন্য ব্যবহার করা যায়।

উদাহরণ:

```text
8–30 days
```

এটি organization-এর retention এবং platform architecture অনুযায়ী পরিবর্তিত হবে।

---

# ❄️ 13. Cold Storage

Long-term retention-এর জন্য cold storage ব্যবহার করা যেতে পারে।

উদাহরণ:

```text
30–180 days
```

এখানে data সাধারণত hot data-এর মতো frequently queried হয় না।

---

# 🗄️ 14. Archive

কিছু organization compliance বা investigation requirement-এর জন্য আরও দীর্ঘ সময় data রাখতে পারে।

Example:

```text
Primary SIEM
     ↓
Hot
     ↓
Warm
     ↓
Cold
     ↓
Archive
```

Retention policy business এবং compliance requirements অনুযায়ী নির্ধারণ করতে হবে।

---

# ⏳ 15. Retention Planning

Retention মানে কতদিন security logs রাখা হবে।

উদাহরণ:

```text
Hot     = 7 days
Warm    = 23 days
Archive = 1 year
```

এটি শুধু example।

প্রতিটি organization-এর requirements আলাদা।

Retention নির্ধারণের সময় consider করুন:

==> Compliance

==> Legal requirements

==> Incident investigation

==> Threat hunting

==> Business requirements

==> Storage cost

==> Privacy requirements

---

# 📈 16. Growth Estimation

আজ আপনার SIEM:

```text
1,000 EPS
```

কিন্তু আগামী বছর:

```text
1,500 EPS
```

হতে পারে।

কারণ:

==> New servers

==> New applications

==> More endpoints

==> Cloud adoption

==> New branches

==> More security tools

==> Increased logging

তাই capacity planning-এ growth estimate রাখতে হবে।

---

# 📊 17. Simple Growth Example

বর্তমান:

```text
1,000 EPS
```

ধরি annual growth:

```text
20%
```

তাহলে next year:

```text
1,000 × 1.20
= 1,200 EPS
```

দুই বছর পরে:

```text
1,200 × 1.20
= 1,440 EPS
```

অর্থাৎ capacity planning-এ শুধু current EPS ব্যবহার করা উচিত নয়।

---

# 🚨 18. Average EPS vs Peak EPS

এটি খুব গুরুত্বপূর্ণ।

ধরুন:

```text
Average EPS = 2,000
Peak EPS    = 8,000
```

যদি architecture শুধু 2,000 EPS-এর জন্য design করা হয়, attack বা incident-এর সময় সমস্যা হতে পারে।

Peak হতে পারে:

==> Authentication storm

==> Malware outbreak

==> DDoS-related logging

==> Firewall event spike

==> Large-scale scanning

==> Incident response activity

তাই:

**Capacity Planning = Average Workload + Peak Workload + Growth**

---

# 🛡️ 19. Capacity Buffer

Production SIEM-এ পুরো capacity 100% ব্যবহার করে design করা ভালো practice নয়।

ধরুন:

```text
Expected Peak = 8,000 EPS
```

তারপর architecture-এ additional capacity রাখা হলো।

Conceptually:

```text
Expected Peak
      +
Safety Margin
      =
Planned Capacity
```

Safety margin organization-এর risk tolerance, workload variability এবং platform behavior অনুযায়ী নির্ধারণ করা উচিত।

---

# 🌐 20. Network Capacity Planning

শুধু storage নয়, network bandwidth-ও plan করতে হবে।

ধরুন:

```text
SIEM traffic
= 20 MB/sec
```

তাহলে network architecture-এ এই traffic-এর জন্য adequate capacity রাখতে হবে।

Consider করুন:

==> Log traffic

==> Management traffic

==> Search traffic

==> Replication traffic

==> Backup traffic

==> API traffic

একই network link-এ সব traffic থাকলে congestion হতে পারে।

---

# 🧠 21. CPU Planning

CPU requirement depend করে:

==> EPS

==> Parsing

==> Normalization

==> Correlation

==> Detection

==> Enrichment

==> Compression

==> Indexing

==> Search workload

একটি SIEM-এর CPU requirement শুধু log volume দিয়ে determine করা যায় না।

---

# 🧠 22. RAM Planning

RAM গুরুত্বপূর্ণ হতে পারে:

==> Search

==> Caching

==> Indexing

==> Query processing

==> Detection

==> Application services

==> Buffers

==> JVM/runtime workloads যেখানে প্রযোজ্য

তাই RAM planning workload-based হওয়া উচিত।

---

# 💽 23. Disk I/O Planning

High-volume SIEM-এর জন্য শুধু disk capacity নয়, **disk performance**-ও গুরুত্বপূর্ণ।

Consider করুন:

==> Write IOPS

==> Read IOPS

==> Throughput

==> Latency

==> Concurrent searches

একটি storage-এর capacity অনেক TB হতে পারে, কিন্তু I/O performance কম হলে SIEM search এবং ingestion slow হতে পারে।

এটি পরের **#13 SIEM Performance Tuning**-এ আরও বিস্তারিত দেখব।

---

# 🔁 24. Replication Factor

Distributed SIEM environment-এ data replication থাকতে পারে।

Conceptually:

```text
Original Data
     |
     +----> Copy 1
     |
     +----> Copy 2
```

যদি replication factor বাড়ে:

```text
Storage Requirement ↑
Availability        ↑
```

অর্থাৎ redundancy বাড়লে storage requirement-ও বাড়তে পারে।

Exact behavior platform অনুযায়ী আলাদা।

---

# 📐 25. Complete Storage Estimation Example

ধরি:

```text
Average EPS       = 2,000
Average Event     = 1 KB
Retention         = 30 days
```

Events/day:

```text
2,000 × 86,400
= 172,800,000 events/day
```

Raw data/day:

```text
172,800,000 × 1 KB
≈ 172.8 GB/day
```

30 days:

```text
172.8 × 30
≈ 5,184 GB
≈ 5.18 TB
```

এটি **raw-data estimate**।

Actual storage planning-এ additional consideration:

```text
Raw Data
   +
Index Overhead
   +
Replication
   +
Metadata
   +
System Overhead
   +
Growth Buffer
   =
Provisioned Storage
```

---

# 🏢 26. Real-World Example

ধরুন একটি company-এর:

==> 1,500 Windows endpoints

==> 100 Linux servers

==> 20 network devices

==> 5 firewalls

==> Active Directory

==> Web applications

==> Cloud services

প্রথমে source অনুযায়ী event generation estimate করতে হবে।

```text
Windows       → 1,500 EPS
Linux         →   300 EPS
Network       →   200 EPS
Firewall      →   500 EPS
Applications  →   700 EPS
Cloud         →   300 EPS
--------------------------------
Total         → 3,500 EPS
```

এটি example estimate।

তারপর:

```text
Average EPS = 3,500
Peak EPS    = measured/projected peak
```

এরপর calculate করতে হবে:

==> Events/day

==> GB/day

==> Retention

==> Storage

==> Network

==> CPU

==> RAM

==> Indexing

==> Search workload

---

# 📋 27. Capacity Planning Worksheet

একজন SIEM Engineer এই ধরনের table maintain করতে পারেন:

| Metric             |     Value |
| ------------------ | --------: |
| Average EPS        |     3,500 |
| Peak EPS           |     8,000 |
| Average Event Size |      1 KB |
| Events/Day         |    302.4M |
| Raw Data/Day       | ~302.4 GB |
| Retention          |   30 days |
| Raw Retention      |  ~9.07 TB |
| Growth             |       20% |
| HA/Replication     |  Required |
| Backup             |  Required |

**Note:** এটি example planning data; production sizing-এর আগে real measurements এবং platform-specific sizing guidance ব্যবহার করা উচিত.

---

# ✅ Capacity Planning Checklist

```text
[ ] Average EPS and Peak EPS measured from real sources
[ ] Events/day calculated: EPS x 86400
[ ] GB/day calculated: events/day x avg event size
[ ] Retention storage calculated: GB/day x retention days
[ ] Index + replication + buffer overhead added (see #10 storage tiers)
[ ] Hot / Warm / Cold / Archive split defined
[ ] CPU / RAM / Disk IOPS and network sized for peak + 20-30% buffer
[ ] Capacity alerts set (e.g. 80% warn, 90% critical)
[ ] Worksheet reviewed before procurement / expansion
```

---

# 🔍 28. Capacity Monitoring

Capacity planning একবার করে শেষ হয়ে যায় না।

Continuously monitor করুন:

==> EPS trend

==> Daily GB

==> Storage utilization

==> CPU utilization

==> RAM utilization

==> Disk I/O

==> Search latency

==> Ingestion latency

==> Queue size

==> Event drops

==> Network utilization

---

# 🚦 29. Capacity Alerting

Threshold-based monitoring করা যেতে পারে।

Example:

```text
Storage > 80%
      ↓
Warning

Storage > 90%
      ↓
Critical
```

আরও monitor করা যায়:

```text
EPS > Planned Capacity
        ↓
Alert
```

এতে capacity issue হওয়ার আগেই SIEM Engineer action নিতে পারে।

---

# 🔄 30. Capacity Planning Lifecycle

একটি practical lifecycle:

```text
Measure
   ↓
Analyze
   ↓
Calculate
   ↓
Design
   ↓
Deploy
   ↓
Monitor
   ↓
Forecast
   ↓
Scale
   ↓
Review
```

এটি continuous process।

---

# 🧪 31. Practical Lab

একটি ছোট lab তৈরি করুন।

### Step 1

5–10টি log source তৈরি করুন।

```text
Windows
Linux
Firewall
Web Server
Application
```

### Step 2

প্রতিটি source থেকে event rate measure করুন।

### Step 3

Average EPS বের করুন।

### Step 4

Peak EPS record করুন।

### Step 5

Average event size estimate করুন।

### Step 6

GB/day calculate করুন।

### Step 7

30/90-day retention-এর storage estimate করুন।

### Step 8

Growth factor যোগ করুন।

### Step 9

Storage এবং infrastructure utilization monitor করুন।

### Step 10

Capacity threshold configure করুন।

---

# 🎯 32. Interview Questions & Answers

## Q1. What is SIEM Capacity Planning?

**Answer:**

SIEM Capacity Planning is the process of estimating the compute, storage, network and processing resources required to handle current and future SIEM workloads.

---

## Q2. What is EPS?

**Answer:**

EPS means Events Per Second. It represents how many events a SIEM receives or processes per second.

---

## Q3. How do you calculate events per day?

**Answer:**

```text
Events/day = EPS × 86,400
```

because one day contains 86,400 seconds.

---

## Q4. What factors affect SIEM storage?

**Answer:**

==> EPS

==> Event size

==> Retention

==> Index overhead

==> Replication

==> Compression

==> Metadata

==> Backup

==> Growth

---

## Q5. Why is peak EPS important?

**Answer:**

Average EPS does not represent the maximum workload. During security incidents, authentication storms or large event spikes, EPS can increase significantly. Therefore, SIEM architecture should account for expected peak workload.

---

## Q6. What is retention?

**Answer:**

Retention defines how long SIEM data is stored and available according to business, security, legal and compliance requirements.

---

## Q7. Is raw GB/day enough for SIEM storage planning?

**Answer:**

No. Raw data is only the starting point. I also consider indexing overhead, metadata, replication, compression behavior, backups, system overhead and future growth.

---

## Q8. How would you handle future SIEM growth?

**Answer:**

I would monitor historical EPS and data-volume trends, estimate growth, maintain a capacity buffer, and design the architecture so that additional resources or nodes can be added when required.

---

## Q9. What happens if SIEM storage becomes full?

**Answer:**

Depending on the platform and configuration, ingestion may fail, indexing may stop, services may become unhealthy, or data retention behavior may be affected. I would immediately check storage utilization, ingestion health, retention policies and platform-specific safeguards.

---

## Q10. Which metrics do you monitor for capacity?

**Answer:**

I monitor:

==> EPS

==> Peak EPS

==> GB/day

==> Storage utilization

==> CPU

==> RAM

==> Disk I/O

==> Network

==> Search latency

==> Ingestion latency

==> Queue size

==> Event drops

---

# ❌ 33. Common Capacity Planning Mistakes

### Mistake 1

শুধু average EPS calculate করা।

### Mistake 2

Event size consider না করা।

### Mistake 3

Retention ভুল estimate করা।

### Mistake 4

Index overhead ignore করা।

### Mistake 5

Replication/storage overhead ignore করা।

### Mistake 6

Future growth consider না করা।

### Mistake 7

Peak workload ignore করা।

### Mistake 8

Disk I/O ignore করা।

### Mistake 9

Network capacity ignore করা।

### Mistake 10

Capacity monitor না করা।

---

# 🧠 34. SIEM Engineer Mindset

একজন SIEM Engineer যখন শুনবে:

> "আমাদের 5,000 EPS SIEM লাগবে।"

তখন শুধু server কিনবে না।

বরং প্রশ্ন করবে:

```text
5,000 EPS average or peak?
        ↓
Average event size কত?
        ↓
GB/day কত?
        ↓
Retention কতদিন?
        ↓
Search workload কত?
        ↓
Replication লাগবে?
        ↓
HA লাগবে?
        ↓
Backup কোথায়?
        ↓
Growth কত?
        ↓
Peak-এর জন্য capacity কত?
```

এই mindset-টাই একজন **SIEM Engineer**-কে আলাদা করে।

---

# 🔄 35. Complete Capacity Planning Flow

```text
Log Sources
     ↓
Measure EPS
     ↓
Find Peak EPS
     ↓
Measure Event Size
     ↓
Calculate Events/Day
     ↓
Calculate GB/Day
     ↓
Define Retention
     ↓
Calculate Raw Storage
     ↓
Add Index/Replication Overhead
     ↓
Add Growth Buffer
     ↓
Plan CPU/RAM
     ↓
Plan Network
     ↓
Plan Disk I/O
     ↓
Deploy
     ↓
Monitor
     ↓
Forecast
     ↓
Scale
```

---

# 💡 Final Takeaway

SIEM Capacity Planning-এর মূল বিষয় হলো:

**Data Volume + EPS + Peak Load + Retention + Storage + Growth**

একজন ভালো SIEM Engineer আগে থেকে বুঝতে পারে:

==> কত data আসবে

==> কত দ্রুত আসবে

==> কতদিন রাখতে হবে

==> কত storage লাগবে

==> কত processing power লাগবে

==> কখন capacity বাড়াতে হবে

**Remember:**

> **Don't size a SIEM only for today. Design it for today's workload, tomorrow's growth, and incident-time peaks.**

---

# 📚 SIEM Engineer Series Navigation

### Previous

==> **#11 — SIEM Architecture Design**

### Current

==> **#12 — SIEM Capacity Planning**

### Next

==> **#13 — SIEM Performance Tuning**

পরের article-এ আমরা দেখব:

==> Slow Queries

==> CPU/RAM Bottlenecks

==> Disk I/O

==> Index Optimization

==> Search Optimization

==> Query Performance

==> Ingestion Performance

==> Troubleshooting

---

