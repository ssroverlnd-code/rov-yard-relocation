---
title: Photos — Index
type: index
tags: [rov, relocation, photos, daily-progress-report]
updated: 2026-10-22
---

# Photos — Daily Photo Evidence & Progress Reports

Photo evidence for the ROV yard relocation, one folder per day. Each day's folder holds the site photos, the raw notes and the day's progress report in markdown.

> Images are **not** tracked in git (`.gitignore` excludes `Photos/**/*.jpeg`) — they stay in the local workspace / Google Drive. Only the `.md` reports are committed.

---

## Convention

| Item | Rule |
|------|------|
| Folder | `Photos/<DD.MM.YYYY>/` — one per day, no spaces |
| Report | `<DD.MM.YYYY> daily progress report.md` inside the day's folder |
| Raw notes | `<DD.MM.YYYY> activity summary.md` — the team's notes as written on the day |
| Photos | `<Area / activity> - <detail>.jpeg`, stored beside the report |
| Template | `Photos/DAILY_PROGRESS_REPORT_TEMPLATE.md` — copy, rename, fill in |
| Circulation | `13_Deliverables/Daily_Progress_Report_<DD.MM.YYYY>.html` — printable HTML with the photos embedded |

---

## Daily progress reports

| Date | Report | Photos | Circulation copy | Status |
|------|--------|--------|------------------|--------|
| 21.10.2026 | [[Photos/21.10.2026/21.10.2026 daily progress report]] | 5 | `Daily_Progress_Report_21.10.2026.html` | 🟡 Sorting started — tagging not started |

---

## How the reports link to the plan

Each daily progress report carries:

1. **Briefing / Work done / Next** — the yard team's notes, cleaned up for circulation but not reworded.
2. **Photo evidence** — one row per photo with a caption, tied to the stage it supports.
3. **Plan status** — the day mapped to `01_Planning/master_moving_plan.md` stages and `02_Stage_Details/stage_details.md` daily plans, with deviations flagged.
4. **Issues and risks** — cross-referenced to `06_Risk/risk_register.md` risk IDs.
5. **Decisions needed** — owner and due date, feeding `00_Index/README.md` open items.

---

## Related

- [[00_Index/README|Project MOC]]
- [[01_Planning/master_moving_plan|Master Moving Plan]]
- [[02_Stage_Details/stage_details|Stage Detail Sheets]]
- [[06_Risk/risk_register|Risk Register]]
- [[13_Deliverables/Move_Plan_ROV_Relocation|Move Plan deliverable]]
