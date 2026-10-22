---
title: ROV Yard Relocation — Repository README
type: README
tags: [rov, relocation, pasir-gudang, masjid-tanah, yard]
updated: 2026-10-22
---

# ROV Yard Relocation — Pasir Gudang → Masjid Tanah

> Start with the [[00_Index/README|Map of Content]] · visual map in `Program_Map.canvas`

**Project Reference:** SSR-YARD-RELOC-2026  
**Duration:** 8 weeks (19 Oct – 14 Dec 2026)  
**Status:** Plan 3 (Hybrid) adopted — Blue-team governance over the Red-team execution baseline  
**Owner:** SSRover L&D (SSRover Sdn Bhd)

---

## 📋 Project Summary

Relocation of the ROV yard from **Pasir Gudang, Johor** to **Masjid Tanah, Melaka**. The existing yard has suffered repeated burglaries resulting in theft of hand tools, metal stock, and copper cabling. The move includes a complete new yard layout designed for safekeeping of engineering equipment and materials.

### Objectives

1. **Zero loss / zero theft** during relocation — every item accounted for
2. **Complete relocation within 8 weeks** (two months or earlier)
3. **Categorised, organised storage** at the new yard upon arrival
4. **Full compliance** with local authorities at both Pasir Gudang and Masjid Tanah
5. **Sale or disposal** of all office furniture before final handover of the old yard

---

## 📁 Repository Structure

```
.
├── .gitignore                  # Excludes binary/native files from git
├── README.md                   # This file
├── Program_Map.canvas          # Obsidian visual knowledge graph (open in Obsidian)
│
├── 00_Index/                   # Map of Content — project index & open items
│   └── README.md
│
├── 01_Planning/                # Project overview, master plan, comparisons
│   ├── project_overview.md
│   ├── master_moving_plan.md
│   └── blue_vs_red_comparison.md
│
├── 02_Stage_Details/           # 10-stage detail sheets with checklists
│   └── stage_details.md
│
├── 03_Inventory/               # A/B/C/D classification guide, 5S + package tagging standard
│   └── inventory_classification.md
│
├── 04_Stakeholders/            # Internal teams, vendors, authorities, escalation
│   └── stakeholder_register.md
│
├── 05_Timeline/                # 8-week Gantt, milestones, critical path
│   └── gantt_timeline.md
│
├── 06_Risk/                    # 22 scored risks, mitigations, incident response
│   └── risk_register.md
│
├── 07_Communication/           # Channels, meetings, reporting templates
│   └── communication_plan.md
│
├── 08_Layout/                  # 5-zone yard layout, security infrastructure
│   └── proposed_yard_layout.md
│
├── 09_Plan_Options/            # Three plans — Plan 3 Hybrid adopted
│   ├── Plan_1_Blue.md
│   ├── Plan_2_Red.md
│   └── Plan_3_Hybrid.md
│
├── 10_ADR/                     # Architecture Decision Records
│   ├── README.md
│   ├── ADR-001_IMCA_Relocation.md
│   └── ADR-002_Package_Tagging.md
│
├── 11_Costing/                 # Full resource & cost tables — RM 115,885 revised
│   ├── Plan_3_Hybrid_Costing_Report.md
│   └── Blue_vs_Red_Costing_Discussion.md
│
├── 12_Email_Correspondence/    # Yard-relocation email threads & contacts
│   ├── INDEX.md
│   ├── contacts.md
│   └── contacts.json
│
├── 13_Deliverables/            # Issued documents — move plan + daily progress reports + team checklist
│   ├── Move_Plan_ROV_Relocation.md
│   ├── Move_Plan_ROV_Relocation_Printable.html
│   ├── Daily_Progress_Report_21.10.2026.html
│   └── Team_Todo_Checklist.md / .html
│
├── 14_Data/                    # Cleaned dataset, outlier & data-quality reports
│   ├── README.md               # House data conventions, headline results, open decisions
│   ├── dataset_raw.csv
│   ├── dataset_cleaned.csv
│   ├── outliers_flagged.csv
│   ├── analysis_results.json
│   ├── OUTLIER_REPORT.md
│   ├── DATA_QUALITY_REPORT.md
│   └── scripts_*.py            # extract / outliers / vault gate (re-runnable checks)
│
├── Photos/                     # Daily photo evidence + daily progress reports
│   ├── README.md               # Photo log index & convention
│   ├── DAILY_PROGRESS_REPORT_TEMPLATE.md
│   ├── 21.10.2026/             # One folder per day — photos + progress report
│   │   ├── 21.10.2026 daily progress report.md
│   │   ├── 21.10.2026 activity summary.md
│   │   └── *.jpeg              # site photos (local only, not tracked)
│   └── 22.10.2026/             # raw notes + 15 photos + progress report
│       ├── 22.10.2026 daily progress report.md
│       └── 22.10.2026 activity summary.md
│
└── 99_Archive/                 # Superseded plans, drafts, IDEA notes
    ├── IDEA.md
    ├── initial_plan_superseded.md
    └── Moving_Plan_3_Initial_Draft.md
```

---

## 🔑 Key Deliverables

| Deliverable | Path | Status |
|-------------|------|--------|
| Master Moving Plan | `01_Planning/master_moving_plan.md` | ✅ Complete |
| 8-Week Gantt Timeline | `05_Timeline/gantt_timeline.md` | ✅ Complete |
| Risk Register (22 risks) | `06_Risk/risk_register.md` | ✅ Complete |
| Stakeholder Register | `04_Stakeholders/stakeholder_register.md` | ✅ Complete |
| Inventory Classification | `03_Inventory/inventory_classification.md` | ✅ Complete |
| Proposed Yard Layout | `08_Layout/proposed_yard_layout.md` | ✅ Complete |
| Plan 3 Hybrid (Recommended) | `09_Plan_Options/Plan_3_Hybrid.md` | ✅ Complete |
| Plan 3 Costing — RM 115,885 | `11_Costing/Plan_3_Hybrid_Costing_Report.md` | ✅ Complete |
| ROV Move Plan (print-ready) | `13_Deliverables/Move_Plan_ROV_Relocation_Printable.html` | ✅ Complete |
| Cleaned cost dataset (72 records) | `14_Data/dataset_cleaned.csv` | ✅ Complete |
| Outlier removal report | `14_Data/OUTLIER_REPORT.md` | ✅ Complete |
| Data quality report | `14_Data/DATA_QUALITY_REPORT.md` | ✅ Complete |
| Daily progress reports | `Photos/<date>/<date> daily progress report.md` | 🟢 21.10.2026 · 22.10.2026 |
| Daily progress report (circulation) | `13_Deliverables/Daily_Progress_Report_<date>.html` | 🟢 21.10.2026 · 22.10.2026 |
| Team to-do checklist | `13_Deliverables/Team_Todo_Checklist.md` / `.html` | 🟢 Started — 22.10.2026 |
| IMCA ADR-001 | `10_ADR/ADR-001_IMCA_Relocation.md` | 🔴 Open — blocks training equipment moves |

---

## ⚠️ Key Open Items

| Item | Status | Owner | Priority |
|------|--------|-------|----------|
| IMCA training establishment relocation | 🔴 OPEN | Training Management | CRITICAL |
| Plan 3 Hybrid costing | ✅ Rerun complete — RM 115,885 (see costing report §5) | Finance | — |
| Plan 3 Hybrid costing approval | 🟡 Ready for senior management approval — RM 115,885 | Finance / Director | HIGH |
| Vendor contracts | 🟡 Not started — 3 quotes per vendor required | Procurement | HIGH |
| Authority applications (MPPG, MPMT, JPJ) | 🟡 Not started | PM | MEDIUM |
| New yard lease signing | 🟡 Not started | PM | MEDIUM |
| Package tagging not started while sorting is underway | 🔴 OPEN — R08/R16/R20/R21 | Inventory Lead | HIGH |
| Limited manpower vs planned sorting volume (22.10) | 🟡 OPEN — potential delay · **R22** | PMO / Operations | HIGH |
| Mixed-up box contents at racks — usable vs faulty unknown (22.10) | 🟡 OPEN | Inventory Lead | MEDIUM |
| Management confirmation on "not sure" items held aside | 🟡 OPEN | Management / PM | HIGH |

---

## 📦 What Is NOT in This Repository

This repository contains **text-based project documentation only**. The following file types are **intentionally excluded** (via `.gitignore`) and are stored in the local workspace or Google Drive backup:

- **Presentations** — `.pptx`
- **Documents** — `.docx`
- **Spreadsheets** — `.xlsx`, `.gsheet`
- **PDFs** — `.pdf`
- **Images** — `.png`, `.jpg`, `.jpeg`
- **Video** — `.mp4`, `.mov`

These binary files reside in the **Google Drive shared folder**:  
`G:\Shared drives\ROVER GROUP-TRAINING`

**Exception — `Photos/`:** the daily photo evidence lives in `Photos/<DD.MM.YYYY>/` in the local workspace. The images are excluded from git by the `.gitignore` rule `Photos/**/*.jpeg`, but the **daily report `.md` files inside those folders are tracked**.

---

## 🛠️ Tech Stack & Tools

- **Project Planning:** Markdown + Obsidian (knowledge graph via `Program_Map.canvas`)
- **Version Control:** Git + GitHub
- **Cloud Backup:** Google Drive (Shared Drive)
- **Communication:** WhatsApp group, email threads

---

## 📄 License

Internal project documentation — SSRover Sdn Bhd. Not for public distribution.

---

*Last updated: 2026-10-19 — reorganised: `13_Deliverables/` and `14_Data/` added; `12_Email_Correspondence/` now holds correspondence only; all 6 files missing YAML frontmatter fixed; canvas and links re-verified at 0 broken.*

*2026-10-22 — `Photos/` added: daily photo evidence + daily progress reports, with `Photos/DAILY_PROGRESS_REPORT_TEMPLATE.md` for the recurring routine; `.gitignore` updated so images stay local while the report `.md` files are tracked.*

*2026-10-22 — report condensed to a daily progress report; circulation copy rendered as printable HTML with the photos embedded (`13_Deliverables/Daily_Progress_Report_21.10.2026.html`).*

*2026-10-22 — tagging amended from item level to **package level**, applied after sorting (5S: Sort → Set in order). New `10_ADR/ADR-002_Package_Tagging.md`; master plan, stage details, inventory guide, risk register (R21) and the issued move plan (v1.1 / printable v1.2) updated.*

*2026-10-22 — team to-do checklist added (`13_Deliverables/Team_Todo_Checklist.md` + printable HTML): 22 Oct deadlines, Week 1 close-out, 5S package-tagging sequence D1–D10, decisions, risks and daily routine.*

*2026-10-22 — 22 Oct raw notes (`Photos/22.10.2026/22.10.2026 activity summary.md`, 15 photos) imported from the Drive copy into the repo with frontmatter and a canvas node; the day's progress report is still pending.*

*2026-10-22 — reorganisation pass: duplicate `Move_Plan_ROV_Relocation_Printable.html` removed from the repository root (the deliverable lives in `13_Deliverables/`); structure tree corrected (22.10.2026 day folder, `14_Data` scripts and index); `updated:` frontmatter corrected on 14 files still carrying 2026-10-19; R22 (limited manpower) registered; open items synced with the 22.10.2026 site notes.*
