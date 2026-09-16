# 🛡️ SIEM Engineer — Study Notes

A complete study-note series covering the **SIEM Engineer** learning path — from log management fundamentals to enterprise SIEM architecture design. Written for SOC/SIEM engineer interview preparation and hands-on lab practice.

> **Languages:** Articles #01–#03, #11–#13, #17 are written in **Bengali + English (Banglish)**.
> Articles #04–#10 and #14–#16 are in **English**.

> 📁 **Note:** The full series (all 16 articles) also lives in the [`all/`](all/) folder. Files `12_soc.md`–`14_soc.md` exist only there; the root folder holds #01–#11 plus this README.

---

## 📚 Series Index

| # | File | Topic | Status |
|---|------|-------|--------|
| 01 | [01_soc.md](01_soc.md) | Log Management | ✅ Complete |
| 02 | [02_soc.md](02_soc.md) | SIEM Platforms | ✅ Complete |
| 03 | [03_soc.md](03_soc.md) | Log Integration | ✅ Complete |
| 04 | [04_soc.md](04_soc.md) | Detection Engineering | ✅ Complete |
| 05 | [05_soc.md](05_soc.md) | Query & Investigation | ✅ Complete |
| 06 | [06_soc.md](06_soc.md) | SOC Operations | ✅ Complete |
| 07 | [07_soc.md](07_soc.md) | Threat Intelligence | ✅ Complete |
| 08 | [08_soc.md](08_soc.md) | Automation & SOAR | ✅ Complete |
| 09 | [09_soc.md](09_soc.md) | Dashboard & Reporting | ✅ Complete |
| 10 | [10_soc.md](10_soc.md) | SIEM Infrastructure | ✅ Complete |
| 11 | [11_soc.md](11_soc.md) | SIEM Architecture Design | ✅ Complete |
| 12 | [all/12_soc.md](all/12_soc.md) | SIEM Capacity Planning | ✅ Complete |
| 13 | [all/13_soc.md](all/13_soc.md) | SIEM Performance Tuning | ✅ Complete |
| 14 | [all/14_soc.md](all/14_soc.md) | Advanced Detection Engineering | ✅ Complete |
| 15 | [all/15_SIEM.md](all/15_SIEM.md) | Threat Hunting with SIEM | ✅ Complete |
| 16 | [all/16_SIEM.md](all/16_SIEM.md) | SIEM Data Quality & Troubleshooting | ✅ Complete |
| 17 | [all/17_SIEM.md](all/17_SIEM.md) | 🆕 Hands-On SIEM: Multi-Platform Practical Guide | ✅ Complete |

---

## 🗂️ Topic Summaries

### #01 — Log Management
What a log is, common SIEM log sources (Firewall, Windows, Linux, AD, VPN, Proxy, IDS/IPS, EDR, Cloud, Application, Database, Network devices), the log pipeline
(**Collect → Transport → Parse → Normalize → Enrich → Store → Search → Monitor → Retain**), Syslog/Agent/API collection, EPS, data quality, log loss & duplicates, retention, troubleshooting missing logs.

### #02 — SIEM Platforms
Splunk (SPL, Forwarder/Indexer/Search Head), Microsoft Sentinel (KQL, Analytics Rules), IBM QRadar (DSM, Offenses, AQL), Elastic Security, OpenSearch, Wazuh architecture, and how the same concepts map across platforms.

### #03 — Log Integration
Integration methods (Syslog, CEF, API, Agents, Forwarders, WEF, file-based, cloud connectors), Syslog facility/severity, UDP vs TCP vs TLS, API auth/pagination/rate limits, custom parsers, parsing vs normalization, 10-step data onboarding, integration troubleshooting & monitoring.

### #04 — Detection Engineering
Detection lifecycle (**Hypothesis → Data → Logic → Rule → Test → Tune → Deploy → Monitor → Improve**), detection types (threshold, sequence, behavioral, anomaly, correlation), Sigma rules, MITRE ATT&CK mapping, false positives & tuning, alert deduplication, Detection-as-Code, detection testing.

### #05 — Query & Investigation
SPL and KQL examples, filtering/aggregation/grouping/sorting, pivoting (**IP → User → Host → Process → Network**), timeline analysis, before/during/after investigation, IP/user/host/process/auth investigation, threat hunting, IOC investigation, common query mistakes, query performance.

### #06 — SOC Operations
SOC team structure (L1/L2/L3), **Event vs Alert vs Incident**, incident response lifecycle (**Detect → Validate → Investigate → Scope → Contain → Eradicate → Recover → Document**), triage, severity vs priority vs confidence, ticketing, escalation, runbooks vs playbooks, MTTD/MTTR, shift handover, evidence handling, SOC metrics.

### #07 — Threat Intelligence
IOC types (IP, domain, URL, hash, email), strategic/tactical/operational/technical intelligence, CTI lifecycle (**Direction → Collection → Processing → Analysis → Dissemination → Feedback**), STIX/TAXII, TIPs, IOC enrichment & correlation, feed quality, freshness & confidence, internal intelligence.

### #08 — Automation & SOAR
SOAR concepts, orchestration, playbooks, alert enrichment automation, automatic ticket creation, automated response risks, **human-in-the-loop**, fully vs semi-automated workflows, decision matrix, API auth/rate limits/retries, idempotency, error handling, rollback, audit logging, automation maturity levels.

### #09 — Dashboard & Reporting
Dashboard vs report, analyst/manager/executive dashboards, alert trends, severity dashboards, auth/endpoint/network/firewall dashboards, detection & MITRE coverage dashboards, MTTD/MTTR metrics, EPS & log-source health monitoring, drill-down, dashboard design principles & common mistakes, SOC reports.

### #10 — SIEM Infrastructure
Infrastructure components, collectors/forwarders/ingestion, EPS & data-volume calculation, storage planning & tiering (**Hot → Warm → Cold → Archive**), retention, CPU/memory/disk/network monitoring, HA & clustering, load balancing, failover, queues/buffers, DR, backup & restore testing, RPO/RTO, upgrades & patching, capacity planning, scaling (vertical vs horizontal).

### #11 — SIEM Architecture Design
Design principles, small/medium/enterprise architectures, centralized vs distributed, single-node vs multi-node, collector/forwarder/ingestion/processing/indexer/search/dashboard/detection layers, HA & load balancing, scalability, network & security architecture, RBAC, on-prem vs cloud vs hybrid, DR (RPO/RTO), observability, common architecture mistakes, real-world design example.

### #12 — SIEM Capacity Planning
Practical SIEM sizing: EPS calculation, events per day, GB/day estimation, storage planning, retention sizing, peak load, growth estimation, capacity buffer, and a real-world SIEM sizing example.

### #13 — SIEM Performance Tuning
Why SIEM performance matters for SOC operations, finding bottlenecks (ingestion, storage, query, CPU, memory, indexing), ingestion delay, slow search analysis, query optimization, resource monitoring, and performance tuning best practices.

### #14 — Advanced Detection Engineering
Beyond single-event detection: building detections that are accurate and context-aware, attack-pattern matching, correlation logic, behavioral detections, detection quality improvement, and advanced detection design principles.

### #15 — Threat Hunting with SIEM
Proactive hunting mindset (**What should I expect? What is unusual? What evidence do I have?**), hypothesis-driven hunting, hunting with SIEM queries, MITRE ATT&CK-based hunting, pivoting, detection gap discovery, and the Threat Hunter + SIEM Engineer mindset.

### #16 — SIEM Data Quality & Troubleshooting
Ensuring security data is available, complete, accurate, timely, parsed, normalized, searchable, and reliable: log-arrival checks, timestamp validation, duplicate detection, ingestion delay, dropped events, field parsing validation, and data-trustworthiness for detection.

### #17 — Hands-On SIEM: Multi-Platform Practical Guide 🆕
The complete practical article: one unified lab (Ubuntu + Windows + Attacker VM), one dataset, same 8 exercises on **Wazuh, Splunk, Elastic, OpenSearch & Sentinel** together — installation commands, the same brute-force detection written in 5 platform query languages, attack-chain investigation, dashboards, SOAR/Python automation, MISP threat intel, Sigma rules, Windows Event ID cheat sheet, and a 6-week combined learning plan.

---

## 🔁 Core Flow to Remember

The single pipeline that connects the whole series:

```text
Log Source → Collection → Transport → Parsing → Normalization → Enrichment
    → Indexing → Storage → Detection → Alert → Investigation
    → Response → Automation → Dashboard → Reporting
```

---

## 🎯 How to Use These Notes

1. **Read in order (#01 → #17)** — each article builds on the previous one.
2. **#17 is the hands-on capstone** — do its 6-week lab plan alongside everything else.
2. **Every article ends with:**
   - 🎤 Interview questions & answers
   - 📋 Practical checklist
   - 🚀 Final takeaway
3. **Build a lab alongside reading** — the recommended setup used across the series:
   - Windows VM + Linux VM + Firewall (or pfSense) + **Wazuh** as the SIEM
   - Practice: generate failed SSH/Windows logins → collect → parse → detect → investigate → tune → dashboard
4. **Interview prep:** review the Q&A sections of each article, plus the checklists.

---

## 🧪 Suggested Lab Progression

```text
Theory (#01–#03)  →  Build Wazuh lab & onboard logs
Detection (#04, #14) → Write & test detection rules
Investigation (#05) → Pivot and build timelines
SOC (#06)         →  Run full alert triage workflow
TI + SOAR (#07–#08) → Enrich alerts & automate
Reporting (#09)   →  Build SOC dashboard
Infra (#10–#13)   →  Size, tune, scale & document the architecture
Hunting (#15)     →  Run hypothesis-driven threat hunts
Quality (#16)     →  Validate data quality end-to-end
Hands-On (#17)    →  Same exercises on Wazuh + Splunk + Elastic + Sentinel
```

---

## 📖 Key Terms Glossary (Quick Reference)

| Term | Meaning |
|------|---------|
| **SIEM** | Security Information and Event Management |
| **SOC** | Security Operations Center |
| **EPS** | Events Per Second — ingestion rate metric |
| **IOC** | Indicator of Compromise (IP, domain, hash, URL…) |
| **CEF** | Common Event Format — standardized log format |
| **DSM** | QRadar Device Support Module (log parsing) |
| **SPL / KQL / AQL** | Query languages: Splunk / Sentinel / QRadar |
| **Sigma** | SIEM-independent detection rule format |
| **MITRE ATT&CK** | Adversary tactics & techniques knowledge base |
| **SOAR** | Security Orchestration, Automation and Response |
| **STIX / TAXII** | Threat intel representation / exchange standards |
| **TIP** | Threat Intelligence Platform |
| **WEF** | Windows Event Forwarding |
| **MTTD / MTTR** | Mean Time to Detect / Respond (or Resolve) |
| **RPO / RTO** | Recovery Point / Time Objective |
| **HA** | High Availability |
| **RBAC** | Role-Based Access Control |
| **FIM** | File Integrity Monitoring |
| **IOC Enrichment** | Adding context to an indicator (source, confidence, freshness) |
| **Data Onboarding** | Connecting a new log source & making it usable in the SIEM |

---

## ⏭️ Next Steps

- [x] ~~Write **#12 — SIEM Capacity Planning**~~ → [all/12_soc.md](all/12_soc.md)
- [ ] Practice hands-on: complete the Wazuh lab exercises from each article
- [ ] Review all interview Q&A sections before applying
- [ ] Build a SOC dashboard project from #09 concepts
- [ ] Run a full threat-hunt exercise (#15) in the lab and document findings
- [ ] Complete the **#17 multi-platform lab plan** (Wazuh → Splunk → Elastic → Sentinel) and build a GitHub portfolio

---

*Last updated: September 2026*
