# 🛡️ SIEM Engineer — Study Notes

A complete study-note series covering the **SIEM Engineer** learning path — from log management fundamentals to enterprise SIEM architecture design. Written for SOC/SIEM engineer interview preparation and hands-on lab practice.

> **Languages:** Articles #01–#03, #11–#13, #17 are written in **Bengali + English (Banglish)**.
> Articles #04–#10 and #14–#16 are in **English**.

> 📁 **Note:** The full series (all 17 articles) lives in the [`all/`](all/) folder.

---

## 📚 Series Index

| # | File | Topic | Status |
|---|------|-------|--------|
| 01 | [01_soc.md](all/01_soc.md) | Log Management | ✅ Complete |
| 02 | [02_soc.md](all/02_soc.md) | SIEM Platforms | ✅ Complete |
| 03 | [03_soc.md](all/03_soc.md) | Log Integration | ✅ Complete |
| 04 | [04_soc.md](all/04_soc.md) | Detection Engineering | ✅ Complete |
| 05 | [05_soc.md](all/05_soc.md) | Query & Investigation | ✅ Complete |
| 06 | [06_soc.md](all/06_soc.md) | SOC Operations | ✅ Complete |
| 07 | [07_soc.md](all/07_soc.md) | Threat Intelligence | ✅ Complete |
| 08 | [08_soc.md](all/08_soc.md) | Automation & SOAR | ✅ Complete |
| 09 | [09_soc.md](all/09_soc.md) | Dashboard & Reporting | ✅ Complete |
| 10 | [10_soc.md](all/10_soc.md) | SIEM Infrastructure | ✅ Complete |
| 11 | [11_soc.md](all/11_soc.md) | SIEM Architecture Design | ✅ Complete |
| 12 | [12_soc.md](all/12_soc.md) | SIEM Capacity Planning | ✅ Complete |
| 13 | [13_soc.md](all/13_soc.md) | SIEM Performance Tuning | ✅ Complete |
| 14 | [14_soc.md](all/14_soc.md) | Advanced Detection Engineering | ✅ Complete |
| 15 | [15_SIEM.md](all/15_SIEM.md) | Threat Hunting with SIEM | ✅ Complete |
| 16 | [16_SIEM.md](all/16_SIEM.md) | SIEM Data Quality & Troubleshooting | ✅ Complete |
| 17 | [17_SIEM.md](all/17_SIEM.md) | 🆕 Hands-On SIEM: Multi-Platform Practical Guide | ✅ Complete |

---

## 🗂️ Topic Summaries

> Each summary follows the same format: **what it covers → key flow → hands-on outcome**. Click the title to open the full note.

**Phase 1 — Foundation (#01–#03)**

### [#01 — Log Management](all/01_soc.md)
> What logs are and how they reach the SIEM.
- **Covers:** Log sources (Firewall, Windows, Linux, AD, VPN, Proxy, IDS/IPS, EDR, Cloud, App, DB, Network), Syslog / Agent / API collection, parsing, normalization, enrichment
- **Key flow:** `Collect → Transport → Parse → Normalize → Enrich → Store → Search → Monitor → Retain`
- **Hands-on:** EPS basics, data quality, log loss & duplicates, retention, missing-log troubleshooting

### [#02 — SIEM Platforms](all/02_soc.md)
> How the major SIEMs work and how concepts map across them.
- **Covers:** Splunk (SPL, Forwarder / Indexer / Search Head), Sentinel (KQL, Analytics Rules), QRadar (DSM, Offenses, AQL), Elastic, OpenSearch, Wazuh
- **Key idea:** `Log Sources → Collection → SIEM Platform → Search / Detection / Alert → Investigation → Dashboard`
- **Hands-on:** Compare the same workflow on different platforms, platform-health checks, lab with Wazuh

### [#03 — Log Integration](all/03_soc.md)
> Connecting a new source and making it usable in the SIEM.
- **Covers:** Syslog (facility / severity, UDP vs TCP vs TLS), CEF, API (auth / pagination / rate limits), Agents, Forwarders, WEF, file-based, cloud connectors, custom parsers
- **Key flow:** `Identify → Configure → Transport → Parse → Normalize → Test Search → Detect → Monitor`
- **Hands-on:** 10-step data onboarding, parsing vs normalization, end-to-end validation, troubleshooting

**Phase 2 — Detection & Investigation (#04–#05, #14–#15)**

### [#04 — Detection Engineering](all/04_soc.md)
> Turning telemetry into reliable detections.
- **Covers:** Detection lifecycle, threshold / sequence / behavioral / anomaly / correlation types, Sigma rules, MITRE ATT&CK mapping (e.g. `T1059.001`, `T1110`), severity vs confidence
- **Key flow:** `Hypothesis → Data → Logic → Rule → Test → Tune → Deploy → Monitor → Improve`
- **Hands-on:** SSH brute-force, Windows failed-login, PowerShell rules, FP tuning, deduplication, Detection-as-Code

### [#05 — Query & Investigation](all/05_soc.md)
> Finding the story in the data with SPL / KQL.
- **Covers:** Filtering, aggregation, `group by`, sorting, pivoting (`IP → User → Host → Process → Network`), timeline analysis, before / during / after method
- **Key flow:** `Alert → Validate → Filter → Pivot → Correlate → Scope → Escalate / Close`
- **Hands-on:** IP / user / host / process / auth investigations, TP vs FP verdicts, IOC hunting, query-performance pitfalls

### [#14 — Advanced Detection Engineering](all/14_soc.md)
> Accurate, context-aware detections beyond single events.
- **Covers:** Single-event vs correlation vs behavioral vs risk-based detections, baselines, entity-based logic, allowlists, suppression, FP-rate reduction
- **Key idea:** `Risk = Event + Behavior + TI + Context`
- **Hands-on:** Brute-force, PowerShell, privesc, lateral-movement, scanning detections + Sigma YAML structure

### [#15 — Threat Hunting with SIEM](all/15_SIEM.md)
> Proactively looking for what alerts missed.
- **Covers:** Hypothesis-driven hunting, IOC vs TTP hunting, MITRE-based hunts, time / baseline / user / host / process / DNS / auth hunting, pivoting
- **Key flow:** `Hypothesis → Search → Evidence → Verdict → New / Improved Detection`
- **Hands-on:** 6 starter hunts, hunt notebook template, TI enrichment, hunt → detection promotion

**Phase 3 — SOC, Intel & Automation (#06–#08)**

### [#06 — SOC Operations](all/06_soc.md)
> How a SOC turns alerts into resolved incidents.
- **Covers:** L1 / L2 / L3 roles, **Event vs Alert vs Incident**, triage, severity vs priority vs confidence, ticketing, escalation, RCA, attack-chain analysis
- **Key flow:** `Detect → Validate → Investigate → Scope → Contain → Eradicate → Recover → Document`
- **Hands-on:** Suspicious-login runbook, runbook vs playbook, MTTD / MTTR, shift handover, evidence handling

### [#07 — Threat Intelligence](all/07_soc.md)
> Giving alerts context with IOCs and intel lifecycle.
- **Covers:** IOC types (IP, domain, URL, hash, email), strategic / tactical / operational / technical intel, CTI lifecycle, STIX / TAXII, TIPs, enrichment & correlation
- **Key flow:** `Direction → Collection → Processing → Analysis → Dissemination → Feedback`
- **Hands-on:** IP / domain / URL / hash / email intel, feed quality, freshness & confidence, internal IOCs

### [#08 — Automation & SOAR](all/08_soc.md)
> Automating the repetitive SOC work safely.
- **Covers:** Orchestration, playbooks, enrichment, auto-ticketing, notification, automated response risks, **human-in-the-loop**, fully vs semi-automated, APIs, idempotency, rollback
- **Key flow:** `Alert → Enrich → Decide → Act → Ticket → Notify → Audit`
- **Hands-on:** Suspicious-IP, phishing & compromised-account workflows, decision matrix, automation metrics

**Phase 4 — Reporting & Infrastructure (#09–#13, #16)**

### [#09 — Dashboard & Reporting](all/09_soc.md)
> Making SOC activity visible and measurable.
- **Covers:** Dashboard vs report, analyst / manager / executive views, alert trends, severity, auth / endpoint / network / firewall panels, MITRE coverage, drill-down design
- **Key metrics:** MTTD / MTTR, EPS & source-health, detection coverage
- **Hands-on:** Time-series / geo / table visualizations, filters, dashboard → investigation workflow

### [#10 — SIEM Infrastructure](all/10_soc.md)
> What the SIEM runs on and how to keep it healthy.
- **Covers:** Collectors, forwarders, ingestion, EPS & data-volume math, `Hot → Warm → Cold` storage, retention, CPU / memory / disk / network monitoring
- **Key topics:** HA & clustering, load balancing, failover, queues / buffers, DR, backup & restore testing, RPO / RTO, upgrades
- **Hands-on:** Storage estimation (`~172 GB/day` example), health monitoring, scaling vertical vs horizontal

### [#11 — SIEM Architecture Design](all/11_soc.md)
> Designing small, medium and enterprise SIEMs.
- **Covers:** Design principles, centralized vs distributed, single-node vs multi-node, collector / ingestion / processing / indexer / search / dashboard / detection layers
- **Key topics:** HA, scalability, network & security architecture, RBAC, on-prem vs cloud vs hybrid, observability, DR
- **Hands-on:** Real-world design example, common architecture mistakes, sizing inputs for #12

### [#12 — SIEM Capacity Planning](all/12_soc.md)
> Sizing the SIEM with real numbers.
- **Covers:** EPS, events/day (`EPS × 86400`), GB/day, retention sizing, peak vs average, growth, replication & buffer
- **Key formulas:** `Events/day = EPS × 86400` → `GB/day = events × avg size` → `Retention = GB/day × days`
- **Hands-on:** Planning worksheet, `2000 EPS × 1KB × 30d ≈ 5.18TB` example, capacity alerts (80% warn / 90% crit)

### [#13 — SIEM Performance Tuning](all/13_soc.md)
> Finding and fixing slowness.
- **Covers:** Bottlenecks (ingestion, storage, query, CPU, memory, indexing), ingestion delay, slow-search analysis, time-range & filter-early optimization, index / shard tuning
- **Key flow:** `Identify → Measure Baseline → Tune → Before / After Test → Monitor`
- **Hands-on:** Slow-search, delayed-logs & high-CPU scenarios, queue & latency checks

### [#16 — SIEM Data Quality & Troubleshooting](all/16_SIEM.md)
> Making sure the data is trustworthy for detection.
- **Covers:** Availability, completeness, accuracy, timeliness, parsing & field mapping, timestamps, duplicates, latency, drops
- **Key flow:** `Source → Network → Collector → Ingestion → Parsing → Search → Detection`
- **Hands-on:** Silence detection, EPS-drop alerts, parsing-failure triage, example SLAs (99.5% availability, ≤5 min latency)

**Capstone (#17)**

### [#17 — Hands-On SIEM: Multi-Platform Practical Guide 🆕](all/17_SIEM.md)
> One lab, one dataset, same exercises on 5 platforms.
- **Covers:** Unified lab (Ubuntu + Windows + Attacker VM), Wazuh / Splunk / Elastic / OpenSearch / Sentinel setup, one-dataset approach
- **Key work:** Same brute-force detection in 5 query languages, attack-chain investigation, dashboards, SOAR / Python automation, MISP intel, Sigma rules, Windows Event ID cheat sheet
- **Hands-on:** 6-week plan (`Wazuh → Splunk → Elastic → Sentinel`), portfolio-ready screenshots & write-up

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
3. **Every article ends with:**
   - 🎤 Interview questions & answers
   - 📋 Practical checklist
   - 🚀 Final takeaway
4. **Build a lab alongside reading** — the recommended setup used across the series:
   - Windows VM + Linux VM + Firewall (or pfSense) + **Wazuh** as the SIEM
   - Practice: generate failed SSH/Windows logins → collect → parse → detect → investigate → tune → dashboard
5. **Interview prep:** review the Q&A sections of each article, plus the checklists.

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
