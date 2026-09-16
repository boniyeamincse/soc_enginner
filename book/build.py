#!/usr/bin/env python3
"""Build the SIEM Engineer book (HTML + PDF) from README + all/ chapters.

Book fixes vs raw concat:
- First H1 of each chapter stays H1 (chapter title); later "# " become "## "
  so the TOC shows ~18 chapters instead of 850 entries.
- Removes per-file web navigation footers (Prev/Index/Next, series lists,
  Follow lines) which make no sense inside one book.
- Inserts Part dividers so it reads like a real book.
Run from repo root:  python3 book/build.py
Then: pandoc ... (see bottom) and weasyprint.
"""
import re, pathlib

ROOT = pathlib.Path(__file__).resolve().parent.parent
ALL = ROOT / "all"
OUT = pathlib.Path("/tmp/soc_book_combined.md")

CHAPTERS = [
    ("all/01_soc.md", None),
    ("all/02_soc.md", None),
    ("all/03_soc.md", None),
    ("all/04_soc.md", None),
    ("all/05_soc.md", None),
    ("all/06_soc.md", None),
    ("all/07_soc.md", None),
    ("all/08_soc.md", None),
    ("all/09_soc.md", None),
    ("all/10_soc.md", None),
    ("all/11_soc.md", None),
    ("all/12_soc.md", None),
    ("all/13_soc.md", None),
    ("all/14_soc.md", None),
    ("all/15_SIEM.md", None),
    ("all/16_SIEM.md", None),
    ("all/17_SIEM.md", None),
]

PARTS = {
    "all/01_soc.md": ("Part I — Foundation", "Logs, platforms and integration: how data reaches the SIEM."),
    "all/04_soc.md": ("Part II — Detection & Investigation", "Queries, detections, hunting: turning data into alerts."),
    "all/06_soc.md": ("Part III — SOC, Intel & Automation", "Operations, threat intelligence and SOAR."),
    "all/09_soc.md": ("Part IV — Reporting & Infrastructure", "Dashboards, architecture, sizing, tuning and data quality."),
    "all/17_SIEM.md": ("Part V — Capstone", "One lab, one dataset, five platforms."),
}

NAV_LINE = re.compile(r"^\*\*(← Previous Article|SIEM Engineer Index|Next Article|You have completed).*")
SERIES_ITEM = re.compile(r"^\*\*#\d{2} —.*\*\*$")
NAV_HEADING = {"### Navigation"}
SERIES_HEADING = {
    "## 📚 SIEM Engineer Learning Series",
    "# 📚 Next in the SIEM Engineer Series",
    "# 📚 SIEM Engineer Series Navigation",
    "# 📚 SIEM Engineer — Complete Learning Series",
}
SKIP_LINE = {
    "**Follow the SIEM Engineer learning series — Boni Yeamin**",
    "**SIEM Engineer Index**",
}
SKIP_SUBHEAD = {"### Previous", "### Current", "### Next"}

FRONT_MATTER = """## Copyright {.front-page}

**SIEM Engineer — Complete Study Notes**
First Edition · September 2026

© 2026 Boni Yeamin. Free for personal learning use.

All commands, queries and detections in this book are for **educational and authorized lab use only**.
Never run scans, attacks or brute-force simulations against systems you do not own or have
explicit written permission to test. Product versions, free-tier limits and install steps change
over time — always verify against the official documentation before building your lab.

## About the Author {.front-page}

**Boni Yeamin** writes practical SOC / SIEM study notes and learns in public through a 17-article
series covering log management, SIEM platforms, detection engineering, SOC operations, threat
intelligence, SOAR, dashboards, infrastructure, architecture design, capacity planning, performance
tuning, threat hunting and data quality — ending with a multi-platform hands-on capstone
(Wazuh, Splunk, Elastic, OpenSearch, Microsoft Sentinel).

GitHub: **boniyeamincse**

# Preface

This book collects the complete 17-article SIEM Engineer series into one volume so you can read
it start to finish like a real book.

**How this book is organized** — five parts:

- **Part I — Foundation (#01–#03):** logs, SIEM platforms, log integration
- **Part II — Detection & Investigation (#04–#05, #14–#15):** queries, detection engineering, threat hunting
- **Part III — SOC, Intel & Automation (#06–#08):** SOC operations, threat intelligence, SOAR
- **Part IV — Reporting & Infrastructure (#09–#13, #16):** dashboards, infrastructure, architecture, sizing, tuning, data quality
- **Part V — Capstone (#17):** one lab, one dataset, same exercises on five platforms

**Conventions used in this book:**

- `text` diagrams show pipelines and flows step by step
- `bash` / `spl` / `kql` / `yaml` blocks are copy-paste starting points for your lab — adapt field names to your data
- Every chapter ends with interview questions, a practical checklist and a takeaway
- Articles #01, #11–#13 and #17 mix Bengali + English (Banglish); the rest are in English

**How to read:** follow #01 → #17 in order, build the Wazuh lab from #17 alongside your reading,
and finish each chapter's checklist before moving on.
"""


def clean_chapter(text: str) -> str:
    lines = text.split("\n")
    out, first_h1_seen = [], False
    i, n = 0, len(lines)
    while i < n:
        ln = lines[i]
        s = ln.strip()
        # drop single-line nav leftovers
        if s in NAV_HEADING or s in SKIP_LINE or NAV_LINE.match(s) or (s in SKIP_SUBHEAD):
            # also swallow a following ==> **#NN item line for Prev/Curr/Next teaser blocks
            i += 1
            while i < n and lines[i].strip() == "":
                i += 1
            if i < n and lines[i].strip().startswith("==> **#"):
                i += 1
            continue
        # drop whole series-list sections
        if s in SERIES_HEADING:
            i += 1
            while i < n:
                t = lines[i].strip()
                if t.startswith("#") or t == "---":
                    break
                i += 1
            continue
        # demote: only the first "# " stays a chapter title
        if s.startswith("# ") and not s.startswith("##"):
            if first_h1_seen:
                ln = "#" + ln  # "# " -> "## "
            else:
                first_h1_seen = True
        out.append(ln)
        i += 1
    # collapse 3+ blank lines, drop trailing empty nav crumbs
    text = re.sub(r"\n{4,}", "\n\n\n", "\n".join(out))
    return text.strip() + "\n"


def main():
    parts = [(ROOT / "README.md").read_text(encoding="utf-8").strip() + "\n"]
    parts.append(FRONT_MATTER.strip() + "\n")
    for rel, _ in CHAPTERS:
        if rel in PARTS:
            title, sub = PARTS[rel]
            parts.append(f"\n---\n\n# {title}\n\n*{sub}*\n")
        body = (ROOT / rel).read_text(encoding="utf-8")
        parts.append(clean_chapter(body))
    OUT.write_text("\n---\n\n".join(p for p in parts), encoding="utf-8")
    h1 = sum(1 for ln in OUT.read_text(encoding="utf-8").split("\n") if ln.startswith("# ") and not ln.startswith("##"))
    print(f"combined -> {OUT}  (H1 chapters: {h1})")


if __name__ == "__main__":
    main()
