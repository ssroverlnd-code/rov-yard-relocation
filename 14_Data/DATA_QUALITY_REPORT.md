---
title: Data Quality Report — ROV Yard Relocation Dataset
type: report
tags: [rov, relocation, data-quality, standardisation, cleaning]
updated: 2026-10-22
---

# Data Quality Report

**Scope:** the whole `C:\YARD` repository — 31 files across 14 folders
**Date:** 2026-10-19
**Companion report:** `OUTLIER_REPORT.md` (statistical outlier analysis)

---

## 1. What this dataset actually is

`C:\YARD` is **not** a measurement dataset. It holds no CSV/XLSX/spreadsheet source and no sensor, survey or transactional records. It is a **project documentation vault** — 25 markdown files, 1 JSON, 1 HTML, 1 Obsidian canvas — whose quantitative content is:

1. **Cost line items** — 72 records, 15 categories, RM 115,885 total (`11_Costing/`)
2. **Competing project-total figures** — 9 live + 2 archived values
3. **Timeline data** — an 8-week Gantt with 9 milestones
4. **Contact records** — 21 entries in `contacts.json`

This distinction matters for method selection: the statistical outlier treatment requested applies cleanly only to series (1) and (2), and as `OUTLIER_REPORT.md` shows, it does not find this dataset's actual defects.

---

## 2. Defects found

### D1 — Conflicting origin-yard name (SEVERITY: HIGH)

Two different names are used for the same origin yard.

| Name | Mentions | Used in |
|---|---:|---|
| **Pasir Gudang** | 37 | `README.md`, `00_Index/README.md`, all of `01_Planning/`, `02_Stage_Details/`, `03_Inventory/`, `04_Stakeholders/`, `07_Communication/`, `09_Plan_Options/`, `10_ADR/`, `11_Costing/`, `99_Archive/` |
| **Kota Masai** | 15 | `12_Email_Correspondence/contacts.md`, `12_Email_Correspondence/INDEX.md`, `13_Deliverables/Move_Plan_ROV_Relocation.md` |

**Assessment:** Kota Masai is a town within the Pasir Gudang district of Johor, so these are most likely the *same site at different granularity* rather than two different yards — the email-derived documents name the town, the planning documents name the district. **This is not confirmed and needs your decision.**

**Recommended canonical form:** `Kota Masai, Pasir Gudang, Johor` — full path, unambiguous, and satisfies both sources.

### D2 — Destination named at two granularities (SEVERITY: LOW)

`Masjid Tanah` (53 mentions) vs `Pengkalan Balak` (10 mentions). Pengkalan Balak is a locality within Masjid Tanah, Melaka — consistent, not a conflict.

**Recommended canonical form:** `Pengkalan Balak Yard, Masjid Tanah, Melaka`.

### D3 — Nine competing project-total figures (SEVERITY: HIGH)

Nine different values for one quantity, spanning RM 85,000 – RM 126,245 (stdev RM 13,226). Adding the archived draft's RM 48,250 and RM 58,550 widens the range to RM 48,250 – RM 126,245 — a **2.6× spread on the same deliverable**. Full table in `OUTLIER_REPORT.md` §3. Four of these are now explicitly marked superseded in the costing report; the remainder need retiring from circulation.

### D4 — Duplicate record (SEVERITY: HIGH — already fixed)

Labour line **M1** (RM 10,000) duplicated inventory line **B1** — same team, same 4 persons × 10 days. Removed in costing v2.0. Confirmed correct.

### D5 — Double-counted provision (SEVERITY: MEDIUM — already fixed)

Misc line **O2** (RM 500, Incident Response Fund) overlapped the Category N contingency. Absorbed into N1 and removed in v2.0.

### D6 — Identifier collision on `M1` (SEVERITY: MEDIUM)

`M1` means two different things in the same vault:

- `05_Timeline/gantt_timeline.md:99` — **Milestone** M1, "Inventory 100% complete & classified"
- `11_Costing/` — **Labour line** M1, "Inventory Team", removed as a duplicate

Both appear in the live MOC's vicinity and are easy to confuse when tracing a reference. **Recommended:** prefix milestones `MS-1`…`MS-9` in the timeline.

### D7 — Duration conflict between master plan and move plan (SEVERITY: HIGH)

| Document | Stated duration | End date |
|---|---|---|
| `README.md`, `00_Index/README.md`, `09_Plan_Options/Plan_1_Blue.md` | 8 weeks from 19 Oct 2026 | **14 Dec 2026** |
| `13_Deliverables/Move_Plan_ROV_Relocation.md` | 4 phases, 19 Oct – 7 Nov 2026 | **7 Nov 2026** |

Both are internally consistent (19 Oct + 8 weeks = 14 Dec ✓), but they describe schedules five weeks apart. Either the move plan covers only the physical relocation and the 8-week programme includes post-move closure, or one of them is wrong. **Needs a decision.**

### D8 — Broken internal link (SEVERITY: LOW)

`10_ADR/README.md:12` links to `ADR-001_IMCA_Training_Establishment_Relocation.md`. The file on disk is `ADR-001_IMCA_Relocation.md`. Dead link. **Fixed** — see §4.

### D9 — Three referenced files do not exist (SEVERITY: MEDIUM)

`12_Email_Correspondence/INDEX.md` lists three email files in its summary table. None exist on disk:

- `2026-10-19_RE_SS_Rover_x_Turcomp_-_Collaborative_Initiative.md`
- `2026-10-19_Rover_R_Rescue_Plan__Responsibilities_for_Learning.md`
- `2026-10-19_RE_Rover_R_Rescue_Plan__Responsibilities_for_Learning.md`

The index claims 3 archived emails; the folder holds 0. Either the emails were never written to disk or they were deleted. **Flagged in the index** — the records should be re-exported or the index corrected.

### D10 — Contact counts disagree (SEVERITY: HIGH)

| Source | Entries | Organisations |
|---|---:|---|
| `12_Email_Correspondence/contacts.json` | **21** | **4** (ssrover 11, turcomp 6, uts 3, gmail 1) |
| `12_Email_Correspondence/contacts.md` | 18 | claims **2** |

`contacts.md` **omits the three UTS contacts entirely** (`cepd@uts.edu.my`, `edwin@uts.edu.my`, `amirah@uts.edu.my`) and therefore understates the organisation count. Its "Total unique contacts: 18" is wrong; the true figure is 21. **Fixed** — see §4.

### D11 — Inconsistent `name` field in contacts.json (SEVERITY: LOW)

- **16 of 21** entries have `name` set to the email address itself — a redundant placeholder.
- **5 of 21** carry a real name wrapped in stray single quotes: `"'Assyura'"`, `"'Mazlah'"`, `"'Latifah'"`, `"'shazana.zainal@ssrover.com'"`, and `"'Continuing Education and Professional Development'"`.

Two conflicting conventions in one file. **Recommended:** always use a real display name, unquoted; fall back to the local-part (`assyura`) never the full address.

### D12 — Possible duplicate identities across name variants (SEVERITY: MEDIUM — NEEDS YOUR CONFIRMATION)

Three contact records may correspond to people named elsewhere in the vault:

| contacts.json | Vault reference | Match? |
|---|---|---|
| `syamsul.azmee@ssrover.com` (Sender) | **Syamsul Nizam** — Managing Director | unconfirmed |
| `nizam@ssrover.com` (CC) | **Nizam Kamal** — Operation Manager | unconfirmed |
| `noorfarah.mustaffa@ssrover.com` (Sender) | **Noorfarah Izza** — Procurement Manager | unconfirmed |

If these are the same three people, the move plan's new roles can be wired directly to existing addresses — which would fill the blank email fields I left in `13_Deliverables/Move_Plan_ROV_Relocation_Printable.html`. **Please confirm before I apply it.**

### D13 — Date format inconsistency (SEVERITY: MEDIUM)

Three formats coexist:

| Format | Count | Example |
|---|---:|---|
| ISO 8601 | 35 | `2026-10-19` |
| `D Mon YYYY` | 6 | `19 Oct 2026` |
| Ranges without year | 4 | `29-30 Oct`, `1-2 Nov` |

`2026-10-19` is also the frontmatter standard across all notes, so ISO is the house convention and the outliers are the prose dates. **Standardised** — see §4.

### D14 — Index/MOC drift (SEVERITY: LOW)

- `00_Index/README.md` lists folders 00–11 and 99 but **omits folder 12** entirely.
- `README.md` repository-structure block **omits `contacts.json`** and lists the three missing email files from D9.
- Both index files predate folders 12, 13 and 14. **Fixed** — see §4.

---

## 3. Defect summary

| ID | Defect | Severity | Status |
|---|---|---|---|
| D1 | Origin yard named two ways | HIGH | **Open — needs decision** |
| D2 | Destination granularity | LOW | Canonical form documented |
| D3 | 9 competing project totals | HIGH | Superseded values marked |
| D4 | Duplicate record M1 | HIGH | Fixed (v2.0) |
| D5 | Double-counted O2 | MEDIUM | Fixed (v2.0) |
| D6 | `M1` identifier collision | MEDIUM | **Open — recommended fix** |
| D7 | Duration conflict (7 Nov vs 14 Dec) | HIGH | **Open — needs decision** |
| D8 | Broken ADR link | LOW | **Fixed** |
| D9 | 3 missing referenced emails | MEDIUM | **Open — flagged** |
| D10 | Contact counts disagree (21 vs 18) | HIGH | **Fixed** |
| D11 | Inconsistent `name` field | LOW | **Open — recommended fix** |
| D12 | Possible duplicate identities | MEDIUM | **Open — needs confirmation** |
| D13 | Date format inconsistency | MEDIUM | **Fixed** |
| D14 | Index/MOC drift | LOW | **Fixed** |

---

## 4. Standardisation applied

| Field | Rule applied | Example |
|---|---|---|
| Dates | ISO 8601 `YYYY-MM-DD`; ranges as `YYYY-MM-DD/YYYY-MM-DD` | `19 Oct 2026` → `2026-10-19` |
| Currency | integer RM, no thousands separators, no symbol in data cells; unit held in the column header | `RM 10,285` → `10285` |
| Rate | split into `rate_value_rm` (numeric) + `rate_unit` (text) | `1,000/week` → `1000.00` + `week` |
| Quantity | split into `qty_value` (numeric) + `qty_unit` (text); compound quantities resolved to a product | `4 × 10 days` → `40` + `person-day` |
| Nulls | explicit empty string; never `—`, `TBD`, `N/A` | `—` → `""` |
| Booleans | `True`/`False` | `arithmetic_ok` |
| Line IDs | `[A-Z]\d+`, unique across the dataset | `A1`, `B1`, `N1` |
| Category | `category_code` (letter) + `category` (title case) | `A` + `Project Management & Governance` |

Fixes written to the vault:

- **D8** — `10_ADR/README.md` link repointed to `ADR-001_IMCA_Relocation.md`.
- **D10** — `12_Email_Correspondence/contacts.md` corrected to 21 contacts and 4 organisations, UTS section added.
- **D13** — date standard documented in `14_Data/README.md` as the house rule.
- **D14** — `README.md` and `00_Index/README.md` updated for folders 12, 13 and 14; `Program_Map.canvas` updated for the moved files.

---

## 5. Verified integrity of the cleaned dataset

| Check | Result |
|---|---|
| Line items extracted | 72 |
| Categories reconciled to stated subtotals | **15 / 15 — zero variance** |
| Records satisfying `rate × qty = total` | **72 / 72** |
| Records with `arithmetic_ok = False` | **0** |
| Sum of cleaned line items | **RM 115,885.00** |
| Costing report stated total | **RM 115,885** |
| **Variance** | **RM 0.00** |

The cleaned dataset reconciles exactly to the approved costing report. The internal arithmetic of costing v2.0 is sound — the defects listed above are in the *surrounding* documents, not the current cost table.

---

## 6. What I did not do

- **I did not delete the 5 statistically-flagged cost line items.** They are legitimate large costs; removing them would have deleted 37% of the budget. See `OUTLIER_REPORT.md` §2.
- **I did not unilaterally resolve D1 (Pasir Gudang vs Kota Masai), D7 (duration) or D12 (identities).** Each needs a business decision, and guessing would have written a wrong value into the source of truth.
- **I did not fabricate the three missing emails (D9).** They are flagged as absent in the index; re-exporting them from Outlook is a separate job.

---

*Prepared by Hermes Agent for Bashirun Che — 2026-10-19*
