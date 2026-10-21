---
title: Photos — Index
type: index
tags: [rov, relocation, photos, daily-report]
updated: 2026-10-22
---

# Photos — Daily Photo Evidence & Reports

Photo evidence for the ROV yard relocation, one folder per day. Each day's folder holds the site photos plus the day's report in markdown.

> Images are **not** tracked in git (`.gitignore` excludes `*.jpeg`) — they stay in the local workspace / Google Drive. Only the `.md` reports are committed.

---

## Convention

| Item | Rule |
|------|------|
| Folder | `Photos/<DD.MM.YYYY>/` — one per day, no spaces |
| Report | `<DD.MM.YYYY> daily report.md` inside the day's folder |
| Photos | `<Area / activity> - <detail>.jpeg`, stored beside the report |
| Format | `Photos/DAILY_REPORT_TEMPLATE.md` — copy, rename, fill in |

---

## Daily reports

| Date | Report | Photos | Status |
|------|--------|--------|--------|
| 21.10.2026 | [[Photos/21.10.2026/21.10.2026 daily report]] | 5 | 🟡 Sorting started — tagging not started |

---

## How the reports link to the plan

Each daily report carries:

1. **Briefing / Activity / Next** — the yard team's raw notes, as recorded on the day.
2. **Photo evidence** — one row per photo, tied to the stage it supports.
3. **Against the moving plan** — the day mapped to `01_Planning/master_moving_plan.md` stages and `02_Stage_Details/stage_details.md` daily plans, with deviations flagged.
4. **Issues / risks** — cross-referenced to `06_Risk/risk_register.md` risk IDs.
5. **Decisions required** — owner and due date, feeding `00_Index/README.md` open items.

---

## Related

- [[00_Index/README|Project MOC]]
- [[01_Planning/master_moving_plan|Master Moving Plan]]
- [[02_Stage_Details/stage_details|Stage Detail Sheets]]
- [[06_Risk/risk_register|Risk Register]]
