# ROV Yard Relocation — Pasir Gudang → Masjid Tanah

**Project Reference:** SSR-YARD-RELOC-2026  
**Duration:** 8 weeks (19 Oct – 14 Dec 2026)  
**Status:** Planning phase — team decision pending on plan selection  
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
├── 03_Inventory/               # A/B/C/D classification guide, tagging standard
│   └── inventory_classification.md
│
├── 04_Stakeholders/            # Internal teams, vendors, authorities, escalation
│   └── stakeholder_register.md
│
├── 05_Timeline/                # 8-week Gantt, milestones, critical path
│   └── gantt_timeline.md
│
├── 06_Risk/                    # 18 scored risks, mitigations, incident response
│   └── risk_register.md
│
├── 07_Communication/           # Channels, meetings, reporting templates
│   └── communication_plan.md
│
├── 08_Layout/                  # 5-zone yard layout, security infrastructure
│   └── proposed_yard_layout.md
│
├── 09_Plan_Options/            # Three standalone plans — Hybrid recommended
│   ├── Plan_1_Blue.md
│   ├── Plan_2_Red.md
│   └── Plan_3_Hybrid.md
│
├── 10_ADR/                     # Architecture Decision Records
│   ├── README.md
│   └── ADR-001_IMCA_Relocation.md
│
├── 11_Costing/                 # Full resource & cost tables — RM 103,265 revised
│   ├── Plan_3_Hybrid_Costing_Report.md
│   ├── Blue_vs_Red_Costing_Discussion.md
│   └── Archive_Moving_Plan_3_Initial_Draft.md
│
└── 99_Archive/                 # Superseded plans, IDEA notes
    ├── IDEA.md
    └── initial_plan_superseded.md
```

---

## 🔑 Key Deliverables

| Deliverable | Path | Status |
|-------------|------|--------|
| Master Moving Plan | `01_Planning/master_moving_plan.md` | ✅ Complete |
| 8-Week Gantt Timeline | `05_Timeline/gantt_timeline.md` | ✅ Complete |
| Risk Register (18 risks) | `06_Risk/risk_register.md` | ✅ Complete |
| Stakeholder Register | `04_Stakeholders/stakeholder_register.md` | ✅ Complete |
| Inventory Classification | `03_Inventory/inventory_classification.md` | ✅ Complete |
| Proposed Yard Layout | `08_Layout/proposed_yard_layout.md` | ✅ Complete |
| Plan 3 Hybrid (Recommended) | `09_Plan_Options/Plan_3_Hybrid.md` | ✅ Complete |
| Plan 3 Costing — RM 103,265 | `11_Costing/Plan_3_Hybrid_Costing_Report.md` | ✅ Complete |
| IMCA ADR-001 | `10_ADR/ADR-001_IMCA_Relocation.md` | 🔴 Open — blocks training equipment moves |

---

## ⚠️ Key Open Items

| Item | Status | Owner | Priority |
|------|--------|-------|----------|
| IMCA training establishment relocation | 🔴 OPEN | Training Management | CRITICAL |
| Plan 3 Hybrid costing approval | 🟡 Pending senior management review | Finance / Director | HIGH |
| Vendor contracts | 🟡 Not started — 3 quotes per vendor required | Procurement | HIGH |
| Authority applications (MPPG, MPMT, JPJ) | 🟡 Not started | PM | MEDIUM |
| New yard lease signing | 🟡 Not started | PM | MEDIUM |

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

*Last updated: 2026-10-19*
