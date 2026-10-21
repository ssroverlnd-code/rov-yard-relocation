---
title: Daily Report Template
type: template
tags: [rov, relocation, daily-report, template]
updated: 2026-10-22
---

# Daily Report Template — ROV Yard Relocation

> Copy this file into `Photos/<DD.MM.YYYY>/`, rename it `<DD.MM.YYYY> daily report.md`, and fill in every section.
> Keep sections 1–2 in the yard team's raw-notes style; sections 3–7 are the standing structure that ties the day back to the moving plan.
> Delete the guidance lines (in `*italics*`) once the section is filled.

---

```
---
title: Daily Report — DD.MM.YYYY
type: daily-report
date: YYYY-MM-DD
day: [N]
week: [N]
location: KM Yard (origin)
tags: [rov, relocation, daily-report]
updated: YYYY-MM-DD
---

# Daily Report — DD.MM.YYYY (Day [N] of the 8-week plan)

**Yard:** KM Yard — origin (Kota Masai / Pasir Gudang) · **Day:** [day name]
**Team on site:** [names]
**Plan position:** Week [N] · Stage [N] — [stage name] (task [x.y])
**Overall status:** 🟢 / 🟡 / 🔴 [one line]

---

## 1. Briefing

**a. Priority**
- [what is being prioritised today, and what is next in the queue]

**b. Highlighted issues**
- [issue] — [who owns it]

**c.** [open items carried forward from yesterday]

---

## 2. Activity
- [what was actually done, in the team's own words]

---

## 3. Photo evidence

| # | Photo | Area | What it shows | Plan link |
|---|-------|------|---------------|-----------|
| 1 | `[filename].jpeg` | [area] | [what it shows — note if tags/labels are absent] | Stage [x.y] |

*One row per photo taken today. Photos are stored in the same folder as this report.*

---

## 4. Against the moving plan

| Plan item | Reference | Status today |
|-----------|-----------|--------------|
| [plan task] | Stage [x.y] | 🟢 / 🟡 / 🔴 [note — flag deviations explicitly] |

---

## 5. Issues / risks

| # | Issue | Register | Note |
|---|-------|----------|------|
| 1 | [issue] | R[nn] | [mitigation or what is missing] |

*Reference risk IDs from `06_Risk/risk_register.md` where one exists.*

---

## 6. Decisions required

| # | Decision | Who | By when |
|---|----------|-----|---------|
| 1 | [decision needed] | [owner] | [date] |

---

## 7. Next

- [next day's work]

---

## 8. Source

- Raw notes: [filename].md (same folder)
- Photos: [n] images in this folder
- Plan references: `01_Planning/master_moving_plan.md`, `02_Stage_Details/stage_details.md`, `03_Inventory/inventory_classification.md`, `06_Risk/risk_register.md`

---

*Compiled [DD.MM.YYYY] from the KM Yard team's activity summary and the day's site photos.*
```

---

## Conventions

- **One folder per day** — `Photos/<DD.MM.YYYY>/`, no spaces in the folder name.
- **One report per day** — `<DD.MM.YYYY> daily report.md` inside that folder, plus the day's photos.
- **Photo filenames** — `<Area / activity> - <detail>.jpeg`, e.g. `Sorting - Technical Area.jpeg`.
- **Images stay local** — `.jpeg` files are excluded by `.gitignore`; only the `.md` report is tracked in git.
- **Plan position** — always state the week, the stage and the task so the day can be tied back to the master plan.
- **Deviations are explicit** — if the day's work differs from the Stage 2 daily plan or the dependency rules, say so in §4.
