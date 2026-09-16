# 🟢🟡🔴 SIEM Engineer #17 — Hands-On SIEM: Complete Multi-Platform Practical Guide

## 🛡️ Introduction

পর্যন্ত আমরা যা শিখেছি তার বেশিরভাগই **theory**।

এই article-এর মূল কথা একটাই:

> **শুধু Wazuh নয় — একটি unified lab দিয়ে overall SIEM practical শেখা, যেখানে একই exercise একাধিক platform-এ করা যায়।**

একজন SIEM Engineer-এর জন্য দরকার:

==> একটি platform ভালোভাবে জানা (primary skill)

==> অন্য platform-গুলোতে একই কাজ করতে পারা (adaptability)

==> কোন platform-এ কোন কাজ কীভাবে হয় তার ধারণা (concept portability)

এই guide-এ আমরা **একটি lab, একটি dataset, এবং একই workflow** ব্যবহার করে শিখব:

**Wazuh → Splunk → Elastic Security → OpenSearch → Microsoft Sentinel**

সবগুলো একসাথে — একটাই structured plan-এ।

---

# 🧠 1. Platform-Independent Core Skills

প্রথমে বুঝুন — platform বদলালেও **skill বদলায় না**।

প্রতিটি SIEM-এ আপনাকে একই ৮টি কাজ করতে হয়:

```text
1. Data Onboarding    → logs ঢুকানো
2. Parsing            → fields বের করা
3. Normalization      → common schema-তে map করা
4. Searching          → data খোঁজা
5. Detection          → rule লেখা
6. Investigation      → alert তদন্ত করা
7. Dashboard          → visualize করা
8. Tuning             → false positive কমানো
```

তাই আমাদের lab plan হবে:

> **একই ৮টি কাজ → ৫টি platform-এ practice।**

Platform শেখা সহজ হয়ে যাবে, কারণ আপনি আগেই জানবেন **কী করতে হবে** — শুধু **কীভাবে** খুঁজে নিতে হবে।

---

# 🏗️ 2. The Unified Lab Architecture

একটি lab environment দিয়েই সব platform test করা যাবে:

```text
┌─────────────────────────────────────────────────┐
│                  LAB NETWORK                     │
│                                                  │
│  ┌──────────────┐    ┌──────────────────────┐   │
│  │ Attacker VM  │    │   Windows VM         │   │
│  │ (Kali/Ubuntu)│    │   (Win10/Server)     │   │
│  │ brute-force  │    │   Winlogbeat/Agent   │   │
│  │ generator    │    └──────────┬───────────┘   │
│  └──────┬───────┘               │               │
│         │                       │               │
│  ┌──────▼───────────────────────▼───────────┐   │
│  │         Ubuntu Server (Log Source)       │   │
│  │   SSH + syslog + /var/log/auth.log       │   │
│  └──────────────────┬───────────────────────┘   │
│                     │                            │
│      ┌──────────────┼──────────────┐             │
│      ▼              ▼              ▼             │
│ ┌─────────┐   ┌──────────┐   ┌──────────┐       │
│ │  Wazuh  │   │  Splunk  │   │  Elastic │       │
│ │ Server  │   │  (Free)  │   │ Security │       │
│ └─────────┘   └──────────┘   └──────────┘       │
│      ▼              ▼              ▼             │
│ ┌──────────┐  ┌────────────┐                     │
│ │OpenSearch│  │ Sentinel   │  (Azure Cloud)      │
│ │(Docker)  │  │ (Free tier)│                     │
│ └──────────┘  └────────────┘                     │
└─────────────────────────────────────────────────┘
```

### Minimum hardware requirement

```text
Option A — সব একসাথে (challenging):
  32 GB RAM host

Option B — Recommended (প্র্যাকটিক্যাল):
  16 GB RAM host
  একসময়ে এক/দুইটি SIEM চালান, বাকিগুলো stop করুন
  Exercise শেষ হলে পরের platform-এ যান

Option C — Low resource:
  Wazuh (VM) + Sentinel (cloud, নিজের মেশিনে resource লাগে না)
```

### VM specification (recommended)

```text
Ubuntu Server (log source + Wazuh)  → 4 GB RAM, 2 vCPU
Windows VM                          → 4 GB RAM, 2 vCPU
Attacker VM                         → 2 GB RAM, 1 vCPU
SIEM platform (per platform)        → 4-8 GB RAM
```

> 💡 **Cloud alternative:** AWS/Azure free tier-এ Ubuntu VM নিয়েও lab করা যায়, কিন্তু brute-force simulation নিজের isolated lab-এই করা ভালো।

---

# 📦 3. Platform Setup — কোনটা কীভাবে

## 3.1 Wazuh (Free, Open-Source) — Primary

সবচেয়ে সহজ start:

```bash
# Ubuntu Server-এ all-in-one install
curl -sO https://packages.wazuh.com/4.9/wazuh-install.sh
sudo bash ./wazuh-install.sh -a
```

Components:

```text
Wazuh Manager  → analysis + rules
Wazuh Indexer  → storage (OpenSearch-based)
Dashboard      → web UI (port 443)
Agent          → Windows/Linux endpoint-এ
```

## 3.2 Splunk (Free = 500 MB/day)

```bash
# Docker (easiest)
docker run -d -p 8000:8000 -p 8088:8088 -p 9997:9997 \
  -e SPLUNK_START_ARGS="--accept-license" \
  -e SPLUNK_PASSWORD="YourStrongPass123" \
  --name splunk splunk/splunk:latest
```

অথবা direct install: `splunk.com` → Splunk Enterprise Free trial → পরে Free license।

```text
Web UI      → http://localhost:8000
HEC port    → 8088 (HTTP Event Collector)
UF port     → 9997 (Universal Forwarder)
```

## 3.3 Elastic Security (Free Basic license)

```bash
# Docker Compose (official quickstart - see elastic.co docs for current URL)
curl -sO https://raw.githubusercontent.com/elastic/elasticsearch/main/docs/reference/setup/install/docker/docker-compose.yml 
# অথবা simplified:
docker network create elastic
docker run -d --name es01 --net elastic -p 9200:9200 \
  -e "discovery.type=single-node" \
  -e "xpack.security.enabled=false" \
  docker.elastic.co/elasticsearch/elasticsearch:8.15.0
docker run -d --name kibana --net elastic -p 5601:5601 \
  docker.elastic.co/kibana/kibana:8.15.0
```

তারপর Kibana → **Security → Install Elastic Agent** → endpoint-এ agent install।

## 3.4 OpenSearch (Fully Free)

```bash
# Docker Compose
git clone https://github.com/opensearch-project/opensearch-devops
# অথবা simple:
docker run -d -p 9200:9200 -p 9600:9600 \
  -e "discovery.type=single-node" \
  -e "OPENSEARCH_INITIAL_ADMIN_PASSWORD=StrongPass123!" \
  opensearchproject/opensearch:latest
docker run -d -p 5601:5601 \
  -e "OPENSEARCH_HOSTS=[\"https://opensearch:9200\"]" \
  opensearchproject/opensearch-dashboards:latest
```

## 3.5 Microsoft Sentinel (Cloud)

```text
1. Azure Free Account ($200 credit + free services)
2. Create → Log Analytics Workspace
3. Microsoft Sentinel → ওই workspace-এ attach করুন
4. Data Connectors → প্রয়োজনীয় connector enable করুন
   - Windows Security Events (via AMA agent)
   - Syslog (via CEF/AMA)
   - SigninLogs / AuditLogs (Entra ID)
```

> 💡 Sentinel-এ data ingestion cost হয়। Lab-এ ছোট volume রাখুন, কাজ শেষে connector disable করুন।

---

# 🎯 4. The One-Dataset Approach — একই Data, সব Platform

এটাই এই guide-এর সবচেয়ে দরকারী trick:

> **একই attack simulation চালান, একই logs ৫টি platform-এ পাঠান, একই ৮টি exercise করুন।**

## 4.1 Standard Dataset — যা generate করবেন

```text
┌────────────────────────────────────────────────────┐
│  DATASET 1 — SSH Brute Force                       │
│  → Ubuntu-তে attacker থেকে 30টি failed SSH login   │
│                                                    │
│  DATASET 2 — Successful Login After Failures      │
│  → শেষে একটি successful login (attack chain)      │
│                                                    │
│  DATASET 3 — Windows Failed Logins (Event 4625)   │
│  → Windows-এ ভুল password দিয়ে 10 বার login try   │
│                                                    │
│  DATASET 4 — Account Creation (Event 4720)        │
│  → Windows-এ নতুন user তৈরি                       │
│                                                    │
│  DATASET 5 — Firewall Traffic (optional)          │
│  → pfSense/Fortigate demo syslog                  │
└────────────────────────────────────────────────────┘
```

## 4.2 Attack Simulation Script (SSH Brute Force)

Attacker VM থেকে:

```bash
#!/bin/bash
# brute.sh — controlled lab simulation ONLY
TARGET="192.168.56.10"    # আপনার lab Ubuntu-র IP
USER="admin"

for i in $(seq 1 30); do
  sshpass -p "WrongPass$i" ssh -o StrictHostKeyChecking=no \
    $USER@$TARGET exit 2>/dev/null
  sleep 1
done
```

> ⚠️ **শুধুমাত্র নিজের isolated lab-এ চালান।** অন্য কারো system-এ চালানো আইনত অপরাধ।

Ubuntu-র `/var/log/auth.log`-এ দেখবেন:

```text
Failed password for admin from 192.168.56.20 port 44812 ssh2
Failed password for admin from 192.168.56.20 port 44814 ssh2
...
```

এই **একই dataset** এখন প্রতিটি SIEM-এ যাবে।

## 4.3 Log Delivery — কোন platform-এ কীভাবে পৌঁছাবে

```text
Ubuntu SSH logs
   │
   ├── Wazuh Agent (Ubuntu-তে install)      → Wazuh Manager
   ├── Universal Forwarder                   → Splunk Indexer
   ├── Elastic Agent / Filebeat              → Elasticsearch
   ├── Fluentbit / Logstash                  → OpenSearch
   └── Syslog (rsyslog → collector/AMA)      → Sentinel Log Analytics
```

Windows events-এর জন্য:

```text
Windows Event Log
   │
   ├── Wazuh Agent          → Wazuh
   ├── Splunk UF            → Splunk
   ├── Winlogbeat / Elastic Agent → Elastic
   └── AMA agent            → Sentinel
```

> 💡 **One source, many destinations:** rsyslog দিয়ে একই log একাধিক জায়গায় পাঠানো যায় (`@@remote-host` multiple action lines)। তাই একই একটি failed login ঘটনা ৫টি SIEM-এই দেখা যাবে।

---

# 🔄 5. Same Task, Different Platform — Mapping Table

এই table-টা ধরে রাখুন। এটাই **overall SIEM শেখার shortcut**:

| Task | Wazuh | Splunk | Elastic | OpenSearch | Sentinel |
|------|-------|--------|---------|------------|----------|
| **Onboard agent** | Wazuh Agent | Universal Forwarder | Elastic Agent | Fluentbeat/Filebeat | AMA / Connector |
| **Syslog input** | `remote` connection | TCP/UDP input | Logstash input | Ingest pipeline | CEF connector |
| **Search language** | Dashboard filter / DQL | **SPL** | **KQL (Lucene-style)** / DSL | **DQL** | **KQL (Kusto)** |
| **Failed login field** | `data.srcip`, `rule.id:5710` | `EventCode=4625` | `event.action:ssh_login_failed` | `event.action:failed` | `EventID == 4625` |
| **Detection** | Custom rule (XML) | Correlation Search | Detection Rule (EQL/Threat) | Security Analytics rule | Analytics Rule (KQL) |
| **Dashboard** | Modules / Visualize | Dashboard Studio | Kibana Lens | Dashboards | Workbooks |
| **Case management** | Basic | ES + SOAR | Elastic Cases | — | Incidents |
| **Automation** | Active Response | SOAR app | Connector/Watcher | Notification/ISM | Logic Apps Playbooks |
| **MITRE mapping** | Rule `mitre` field | ES ATT&CK content pack | Rule references | — | Rule tactics/techniques |

---

# 🔎 6. Exercise 1 — Search: Same Query, 4 Languages

**প্রশ্ন:** *"কোন source IP সবচেয়ে বেশি failed SSH login করেছে?"*

## Wazuh

Dashboard → Security events → filter:

```text
rule.groups: authentication_failed
```

অথবা API:

```bash
curl -k -H "Authorization: Bearer $TOKEN" \
  "https://localhost:55000/events?rule.groups=authentication_failed"
```

## Splunk (SPL)

```spl
index=linux sourcetype=linux_secure "Failed password"
| rex "Failed password for \w+ (?<user>\S+) from (?<src_ip>\S+)"
| stats count by src_ip
| sort - count
```

## Elastic (Kibana KQL)

```text
event.module:system AND event.dataset:system.auth AND message:"Failed password"
```

Aggregation (Lens/Timeline):

```text
Group by: source.ip → Count → Sort desc
```

## Sentinel (Kusto KQL)

```kql
Syslog
| where ProcessName == "sshd" and SyslogMessage contains "Failed password"
| extend SrcIp = extract(@"from (\d+\.\d+\.\d+\.\d+)", 1, SyslogMessage)
| summarize FailedCount = count() by SrcIp
| order by FailedCount desc
```

> 💡 লক্ষ্য করুন — **logic identical**: filter → extract field → group → count → sort। শুধু syntax আলাদা। এটাই "query language শেখা" আসলে সহজ — একবার mindset বুঝলেই হয়।

---

# 🚨 7. Exercise 2 — Detection: Brute Force Rule Everywhere

**Logic:**

```text
IF failed_ssh >= 10
FROM same src_ip
WITHIN 5 minutes
THEN alert (severity: high)
```

## 7.1 Wazuh Custom Rule

`/var/ossec/etc/rules/local_rules.xml`:

```xml
<group name="linux,sshd,brute_force,">
  <!-- Frequency-based brute force using if_matched_sid -->
  <rule id="100100" level="10" frequency="10" timeframe="300">
    <if_matched_sid>5710</if_matched_sid>  <!-- sshd auth failed -->
    <description>SSH brute force: multiple failures from same IP.</description>
    <mitre><id>T1110</id></mitre>
  </rule>
</group>
```

```bash
sudo systemctl restart wazuh-manager
```

Test: brute.sh চালান → Dashboard-এ `rule.id:100100` alert দেখুন।

## 7.2 Splunk Correlation Search

```spl
index=linux sourcetype=linux_secure "Failed password"
| rex "from (?<src_ip>\S+)"
| stats count by src_ip, index, host
| where count >= 10
```

Save as **Alert** → Trigger when number of results > 0 → Cron/real-time window 5 min।

## 7.3 Elastic Detection Rule

Kibana → Security → Rules → **Create new rule → Threshold**:

```text
Query:    event.module:system AND message:"Failed password"
Group by: source.ip
Threshold: count >= 10
Window:   5 minutes
Severity: High
```

## 7.4 OpenSearch Security Analytics

Dashboards → Security Analytics → Detector:

```text
Input:    syslog index
Workflow: ssh_brute_force
Trigger:  count >= 10 in 5m → Notification channel (email/slack)
```

## 7.5 Sentinel Analytics Rule (KQL)

```kql
Syslog
| where SyslogMessage contains "Failed password"
| extend SrcIp = extract(@"from (\d+\.\d+\.\d+\.\d+)", 1, SyslogMessage)
| where isnotempty(SrcIp)
| summarize FailCount = count() by SrcIp, bin(TimeGenerated, 5m)
| where FailCount >= 10
```

```text
Query scheduling: every 5 minutes, lookback 5 minutes
Incident: create, severity High
MITRE:    Credential Access → T1110 Brute Force
```

> 🎯 **একই rule ৫ ভাষায় লেখা শেষ** — একবার করলে detection engineering আর ভুলবেন না।

---

# 🕵️ 8. Exercise 3 — Investigation: Attack Chain খোঁজা

Scenario: brute force-এর পরে একটা **successful login** হয়েছে (Dataset 2)।

প্রতিটি platform-এ এই pivot chain চালান:

```text
Step 1: Alert-এর src_ip নিন
Step 2: ওই IP-র সব activity দেখুন
Step 3: Successful login খুঁজুন (Accepted password / 4624)
Step 4: Login-এর পরে কী হয়েছে (command, process, sudo)
Step 5: Timeline বানান
```

## Splunk version:

```spl
index=linux src_ip="192.168.56.20"
| sort _time
| table _time, action, user, src_ip, dest, message
```

## Sentinel version:

```kql
union Syslog, SecurityEvent
| where TimeGenerated > ago(1h)
| where SourceIP == "192.168.56.20" or IpAddress == "192.168.56.20"
| project TimeGenerated, EventType, Account, SourceIP, Activity
| order by TimeGenerated asc
```

Timeline (খাতায় লিখুন):

```text
14:20:01  Failed password (attempt 1)
14:20:35  Failed password (attempt 30)
14:21:10  Accepted password for admin   ← breach point
14:21:15  sudo: admin : TTY=pts/0 ; COMMAND=/bin/whoami
14:22:40  new user created (if Dataset 4 exists)
```

এই exercise-টা প্রতিটি platform-এ করুন। **Investigation মানেই এটা** — #05 article-এর practical রূপ।

---

# 📊 9. Exercise 4 — Dashboard: একই Panel, সব Platform

প্রতিটি SIEM-এ এই ৫টি panel বানান:

```text
1. Failed logins over time      (time-series line)
2. Top 10 source IPs            (bar/table)
3. Top targeted usernames       (bar)
4. Successful vs Failed ratio   (pie/metric)
5. Rule-wise alert count        (table)
```

| Platform | কোথায় বানাবেন |
|----------|----------------|
| Wazuh | Dashboard → Visualize / module override |
| Splunk | Dashboard Studio (SPL-backed panels) |
| Elastic | Kibana Lens (drag-drop fields) |
| OpenSearch | Dashboards → Visualize |
| Sentinel | Workbooks (KQL-backed) |

> 💡 Dashboard বানানোর আগে query validate করুন — #09 article-এর validation flow follow করুন।

---

# 🤖 10. Exercise 5 — Automation: SOAR Mini-Lab

## 10.1 Webhook Alert → Python Script

Wazuh Integration (একটি উদাহরণ):

`/var/ossec/etc/ossec.conf`:

```xml
<integration>
  <name>custom-webhook</name>
  <hook_url>http://192.168.56.30:5000/alert</hook_url>
  <level>10</level>
  <alert_format>json</alert_format>
</integration>
```

Python listener:

```python
from flask import Flask, request
import requests

app = Flask(__name__)

TI_API = "https://api.example-ti.com/v1/ip/"   # যেকোনো TI source

@app.route("/alert", methods=["POST"])
def alert():
    data = request.json
    src_ip = (data.get("data") or {}).get("srcip")
    if src_ip:
        rep = requests.get(TI_API + src_ip, timeout=5)
        print(f"[ALERT] {src_ip} → TI: {rep.status_code}")
    return "ok", 200

app.run(host="0.0.0.0", port=5000)
```

## 10.2 Sentinel Playbook (Logic App)

```text
Incident created
   ↓
Get incident entity (IP)
   ↓
HTTP → TI lookup
   ↓
Add comment to incident
```

## 10.3 Shuffle (Free SOAR)

```text
Wazuh → webhook → Shuffle workflow:
  Extract IP → TI lookup → Create case (TheHive/Google Sheet) → Notify
```

> ⚠️ মনে রাখুন — automated containment (firewall block, account disable) শুধু **approval-এর পরে**। Human-in-the-loop!

---

# 🌍 11. Exercise 6 — Threat Intel Integration

## MISP Lab (Free TIP)

```bash
# MISP docker
git clone https://github.com/MISP/misp-docker
cd misp-docker && docker compose up -d
```

```text
1. MISP-এ event create করুন → আপনার lab attacker IP add করুন
2. API key নিন
3. SIEM-এ connect করুন:
   - Wazuh   → CDB list / integration script
   - Splunk  → Threat Intel Management
   - Elastic → Threat Intel connector (IOC index)
   - Sentinel→ TI connector (STIX/TAXII)
4. Attacker IP দিয়ে traffic জেনারেট করুন → TI match alert দেখুন
```

---

# 📅 12. 6-Week Combined Learning Plan — সব একসাথে

```text
WEEK 1 — Foundation Lab
├── Lab setup: Ubuntu + Windows + Attacker VM
├── Wazuh install + agents (Ubuntu, Windows)
├── Dataset 1-2 generate (SSH brute force + success)
└── Exercise: search + verify logs in Wazuh

WEEK 2 — Detection on Wazuh
├── Custom brute-force rule (XML)
├── Windows rule test (4720 account creation)
├── Investigation: attack chain timeline
└── Dashboard: 5 panels

WEEK 3 — Splunk
├── Install (Docker), UF on Ubuntu + Windows
├── Same dataset ingest → SPL search
├── Brute-force alert (SPL)
└── Dashboard + same investigation

WEEK 4 — Elastic + OpenSearch
├── Docker setup, agents
├── KQL/DSL search, threshold rule
├── Same investigation, same dashboard
└── (Optional) OpenSearch detector

WEEK 5 — Sentinel (Cloud)
├── Azure free account + workspace
├── Connectors: Syslog(AMA) + Windows Events
├── KQL: same queries, analytics rules
├── Incident + Playbook (Logic App)
└── ⚠️ কাজ শেষে connector off / data cleanup

WEEK 6 — Advanced + Portfolio
├── MISP TI integration → IOC match alert
├── Shuffle/Python automation
├── Sigma rules লিখুন → convert → deploy
└── Portfolio: GitHub repo + screenshots + writeup
```

---

# 🗂️ 13. Sigma — একবার লিখুন, সব জায়গায় চালান

আগের exercise-এর rule-টাই Sigma-তে:

```yaml
title: SSH Brute Force Detection
id: 100100-bf-ssh
status: stable
description: Multiple failed SSH logins from same source in short window
author: Your Name
date: 2026/09/16
logsource:
  product: linux
  service: auth
detection:
  keywords:
    - 'Failed password'
  condition: keywords | count() by source.ip >= 10
falsepositives:
  - Approved security scanner
level: high
tags:
  - attack.credential_access
  - attack.t1110
```

```bash
pip install sigma-cli pySigma
sigma convert -t splunk -p splunk rule.yml   # → SPL
sigma convert -t lucene -p ecs-elastic rule.yml  # → Elastic query
```

> 💡 এটাই **Detection-as-Code** — rule একবার লিখুন, Git-এ রাখুন, যেকোনো SIEM-এ convert করুন।

---

# 📝 14. Windows Event ID Cheat Sheet (Lab-এ যা collect করবেন)

```text
4624  Successful logon
4625  Failed logon          → brute force detection
4634  Logoff
4648  Explicit credential logon
4663  File/object access attempt
4672  Special privileges assigned
4688  Process creation       → command-line monitoring
4720  User account created
4722  User account enabled
4724  Password reset
4726  User account deleted
4728  Member added to security group
4732  Member added to local group
4740  Account locked out
1102  Audit log cleared      → tampering indicator
```

Wazuh rule test:

```bash
# Windows VM-এ test user বানান → 4720 → SIEM-এ verify
net user testuser Pass123! /add
```

---

# 🚫 15. Common Multi-Platform Lab Mistakes

### ❌ Mistake 1 — সব platform একসাথে চালানো

RAM শেষ, সব slow। একসময়ে এক/দুইটা।

### ❌ Mistake 2 — শুধু install করে থেমে যাওয়া

Install ≠ learning। Exercise complete করুন।

### ❌ Mistake 3 — একই dataset না ব্যবহার করা

আলাদা data মানে তুলনা করতে পারবেন না।

### ❌ Mistake 4 — Alert tune না করে পরের platform-এ যাওয়া

Tuning-ই আসল skill। Scanner IP exclude করার practice করুন।

### ❌ Mistake 5 — Documentation না রাখা

প্রতিটি step screenshot + note। এটাই portfolio।

### ❌ Mistake 6 — Cloud cost ignore করা

Sentinel-এর ingestion budget মনিটর করুন। Lab শেষে বন্ধ করুন।

---

# ✅ 16. Multi-Platform SIEM Checklist

```text
[ ] Lab VMs ready (Ubuntu, Windows, Attacker)
[ ] Dataset scripts ready (brute force, windows events)
[ ] Wazuh installed + 2 agents
[ ] Splunk installed + UF
[ ] Elastic installed + agent
[ ] (Optional) OpenSearch detector tested
[ ] Sentinel workspace + connectors
[ ] Same dataset ingested in each platform
[ ] Brute-force rule written in each platform
[ ] Attack-chain investigation done in each platform
[ ] 5-panel dashboard built in each platform
[ ] Webhook/SOAR automation tested
[ ] MISP TI integration tested
[ ] Sigma rules written + converted
[ ] GitHub portfolio repo created
[ ] README + screenshots + detection rules committed
```

---

# 🎤 17. Interview Questions

### Q1. আপনি কোন কোন SIEM platform-এ কাজ করেছেন?

**Answer:**
আমি প্রাথমিকভাবে Wazuh-এ hands-on কাজ করেছি — agent deployment, custom rules, decoders, dashboards। এছাড়াও একই use cases Splunk (SPL), Elastic Security এবং Microsoft Sentinel (KQL)-এ implement করেছি — যেমন SSH brute-force detection, Windows event monitoring, dashboards এবং basic automation। আমার approach হলো concept-first: platform আলাদা হলেও onboarding, detection, investigation workflow একই।

### Q2. Splunk আর Sentinel-এ একই detection কীভাবে লিখবেন?

**Answer:**
Logic একই থাকে — failed login events filter করা, source IP দিয়ে group করা, threshold apply করা। Splunk-এ SPL (`stats count by src_ip | where count >= 10`) আর Sentinel-এ KQL (`summarize count() by IpAddress`) ব্যবহার করি। Splunk-এ Alert/Scheduled Search, Sentinel-এ Analytics Rule হিসেবে deploy করি।

### Q3. Wazuh-এর সীমাবদ্ধতা কী, আর enterprise SIEM কোথায় এগিয়ে?

**Answer:**
Wazuh দুর্দান্ত open-source endpoint monitoring ও compliance platform, কিন্তু বড় scale-এ advanced correlation, SOAR integration, long-term retention ও compliance reporting-এ enterprise platform যেমন Splunk/Sentinel বেশি mature। Lab ও small environment-এ Wazuh খুব শক্তিশালী।

### Q4. একটি নতুন SIEM platform শিখতে কতদিন লাগবে?

**Answer:**
Core concept জানা থাকলে — onboarding, search, detection, dashboard — এই ৪টি কাজ প্রথম সপ্তাহেই করা যায়। Platform-specific deep features (SOAR, data models, cost management) আরও ৩-৪ সপ্তাহ। আমি প্রতিবার একই dataset দিয়ে same exercise করি, তাই শেখা দ্রুত হয়।

### Q5. Sigma rule কেন ব্যবহার করবেন?

**Answer:**
Sigma দিয়ে detection logic platform-independent ভাবে লেখা যায়। একই rule Splunk, Elastic, Sentinel-এ convert করা যায়, Git-এ version control করা যায়, team-এ share করা যায়। এটা Detection-as-Code-এর ভিত্তি।

---

# 🚀 Final Takeaway

```text
একটি Lab     →  একটি Dataset
একই Exercise →  ৫টি Platform
একটি Skill   →  Overall SIEM
```

মনে রাখুন:

> **SIEM শেখা মানে কোনো product-এর menu মুখস্থ করা নয়।
> SIEM শেখা মানে — data onboard করা, threat detect করা, incident investigate করা — যেকোনো platform-এ।**

Platform বদলাবে, skill থাকবে।

**Wazuh দিয়ে শুরু করুন, বাকিগুলোতে repeat করুন — ৬ সপ্তাহ পরে আপনি "overall SIEM" practical জানবেন।**

---

## 📚 SIEM Engineer Learning Series

**#01 — Log Management**
**#02 — SIEM Platforms**
**#03 — Log Integration**
**#04 — Detection Engineering**
**#05 — Query & Investigation**
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
**#17 — Hands-On SIEM: Multi-Platform Practical Guide ← You are here**

---

### Navigation

**← Previous Article: #16 — SIEM Data Quality & Troubleshooting**

**SIEM Engineer Index**

**You have completed the full #01–#17 series 🎉**

---
