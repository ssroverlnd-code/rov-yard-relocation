---
title: Daily Progress Report Template
type: template
tags: [rov, relocation, daily-progress-report, template]
updated: 2026-10-22
---

# Daily Progress Report Template — ROV Yard Relocation

> Copy this file into `Photos/<DD.MM.YYYY>/`, rename it `<DD.MM.YYYY> daily progress report.md`, and fill in every section.
> Keep §1–2 in the yard team's own words — clean up spelling and grammar for circulation, but do not change what was actually said.
> Sections 3–7 are the standing structure that ties the day back to the moving plan.
> Delete the guidance lines (in `*italics*`) once a section is filled.

---

```
---
title: Daily Progress Report — DD.MM.YYYY
type: daily-progress-report
date: YYYY-MM-DD
day: [N]
week: [N]
location: KM Yard (origin)
tags: [rov, relocation, daily-progress-report]
updated: YYYY-MM-DD
---

# Daily Progress Report — DD Month YYYY

**Day [N] of the 8-week plan · Week [N]**
**Yard:** KM Yard, Kota Masai (origin) · **Team on site:** [names]
**Status:** 🟢 / 🟡 / 🔴 [one line]

---

## 1. Briefing

**Priority for this round**

- [what is being prioritised today]

**Next in the queue** — [what follows]

- [standing instructions: disposal, container staging, package tagging after the sort]

**Issues raised**

- [issue] — [who owns it]

---

## 2. Work done today

- [what was actually done, in the team's own words]

---

## 3. Photo evidence

| # | Photo | Area | Caption |
|---|-------|------|---------|
| 1 | `[filename].jpeg` | [area] | [what it shows — state plainly if tags/labels are absent] |

*One row per photo taken today. Photos are stored in the same folder as this report.*

---

## 4. Plan status

| Plan item | Reference | Status today |
|-----------|-----------|--------------|
| 5S sequence — Sort (1S) then package tagging (2S) | Stage 2 | 🟢 / 🟡 / 🔴 [note] |
| [plan task] | Stage [x.y] | 🟢 / 🟡 / 🔴 [note — flag deviations explicitly] |

---

## 5. Issues and risks

| Issue | Register |
|-------|----------|
| [issue] | R[nn] |

*Reference risk IDs from `06_Risk/risk_register.md` where one exists.*

---

## 6. Decisions needed

| Decision | Owner | By when |
|----------|-------|---------|
| Package tag format and who applies the tags (ZONE-CLASS-PKG-SEQ) | Inventory Lead | Before package tagging starts |
| [decision needed] | [owner] | [date] |

---

## 7. Next

- [next day's work]

---

## 8. Source

- Raw notes: [filename].md (same folder)
- Photos: [n] images in this folder
- Plan: `01_Planning/master_moving_plan.md`, `02_Stage_Details/stage_details.md`, `03_Inventory/inventory_classification.md`, `06_Risk/risk_register.md`

---

*Circulation copy: `13_Deliverables/Daily_Progress_Report_<DD.MM.YYYY>.html`*
```

---

## Conventions

- **One folder per day** — `Photos/<DD.MM.YYYY>/`, no spaces in the folder name.
- **One report per day** — `<DD.MM.YYYY> daily progress report.md` inside that folder, plus the day's photos.
- **Photo filenames** — `<Area / activity> - <detail>.jpeg`, e.g. `Sorting - Technical Area.jpeg`.
- **Images stay local** — `.jpeg` files are excluded by `.gitignore`; only the `.md` report is tracked in git.
- **Plan position** — always state the week, the stage and the task so the day can be tied back to the master plan.
- **Deviations are explicit** — if the day's work differs from the Stage 2 daily plan or the dependency rules, say so in §4.
- **Circulation copy** — render the same content as a printable HTML with the photos embedded (base64) in `13_Deliverables/`, so it survives email and WhatsApp without broken links.
