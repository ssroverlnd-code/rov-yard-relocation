---
title: Data — Cleaned Dataset & Quality Reports
type: index
tags: [rov, relocation, data, dataset, quality]
updated: 2026-10-19
---

# 14 — Data

Cleaned dataset, outlier analysis and data-quality reporting for the ROV yard relocation project.

---

## Contents

| File | What it is |
|---|---|
| `dataset_raw.csv` | 72 cost line items as extracted from the costing report — **unmodified** |
| `dataset_cleaned.csv` | 72 standardised records + `z_score`, `iqr_flag`, `status` columns |
| `outliers_flagged.csv` | Every record flagged by IQR or z-score, with verdict |
| `analysis_results.json` | Machine-readable statistics for both analysed series |
| `OUTLIER_REPORT.md` | Outlier removal process, method, results and recommendations |
| `DATA_QUALITY_REPORT.md` | 14 data-quality defects with severity, status and fixes applied |
| `scripts_extract_cost_data.py` | Extraction + per-category reconciliation (regression check) |
| `scripts_analyze_outliers.py` | IQR / z-score implementation (stdlib only) |
| `scripts_verify_vault.py` | Vault integrity gate — frontmatter, canvas refs, link resolution, map coverage, dataset reconciliation |

---

## Headline results

| | |
|---|---|
| Records extracted | 72 line items across 15 categories |
| Categories reconciling to stated subtotals | **15 / 15 — zero variance** |
| Records satisfying `rate × qty = total` | **72 / 72** |
| Cleaned dataset total | **RM 115,885.00** |
| Costing report stated total | **RM 115,885** |
| Variance | **RM 0.00** |
| Records flagged by IQR (1.5×) or \|z\| ≥ 3 | 5 — all legitimate large cost items, **retained** |
| Records flagged in the competing-totals series | **0** — the method could not detect the inconsistency |
| Records actually removed | **2** (M1 duplicate RM 10,000; O2 double-count RM 500) — found by arithmetic reconciliation |

> **The statistical outlier methods you asked for did not find this dataset's bad records.** IQR and z-score flagged only legitimate large budget lines and nothing at all in the conflicting-totals series. The six real defects were caught by reconciling stated totals against the sum of their own line items. Full explanation in `OUTLIER_REPORT.md` §2 and §3.

---

## House data conventions

Apply these when adding records.

| Field | Rule | Example |
|---|---|---|
| Dates | ISO 8601. Ranges as `YYYY-MM-DD/YYYY-MM-DD` | `19 Oct 2026` → `2026-10-19` |
| Currency | Integer RM, no separators, no symbol inside data cells; unit in the header | `RM 10,285` → `10285` |
| Rate | `rate_value_rm` numeric + `rate_unit` text | `1,000/week` → `1000.00` / `week` |
| Quantity | `qty_value` numeric + `qty_unit` text; compounds resolved to a product | `4 × 10 days` → `40` / `person-day` |
| Nulls | Explicit empty string — never `—`, `TBD`, `N/A` | `—` → `""` |
| Booleans | `True` / `False` | `arithmetic_ok` |
| Line IDs | `[A-Z]\d+`, unique across the dataset | `A1`, `B1`, `N1` |
| Milestones | Prefix `MS-` to avoid colliding with cost line IDs | `MS-1`, not `M1` |
| Origin yard | `Kota Masai, Pasir Gudang, Johor` *(pending confirmation — see below)* | |
| Destination yard | `Pengkalan Balak Yard, Masjid Tanah, Melaka` | |

---

## Open decisions blocking full standardisation

Three defects could not be resolved without a business decision. I did not guess — writing a wrong value into the source of truth is worse than leaving it flagged.

| # | Question | Why it matters |
|---|---|---|
| 1 | Is the origin yard **Kota Masai** or **Pasir Gudang** — or are they the same site? | The vault uses both (37 vs 15 mentions). If they are the same place, one canonical form should replace both. |
| 2 | Does the move run to **7 Nov 2026** (move plan) or **14 Dec 2026** (master plan)? | Five weeks apart. Either the move plan covers only physical relocation, or one schedule is wrong. |
| 3 | Are **syamsul.azmee / nizam / noorfarah.mustaffa** the same people as **Syamsul Nizam (MD) / Nizam Kamal (Ops Mgr) / Noorfarah Izza (Proc Mgr)**? | If yes, the move plan's blank email fields can be filled from `contacts.json`. |

See `DATA_QUALITY_REPORT.md` §2 D1, D7, D12.

---

## Re-running the checks

```bash
cd C:/YARD

# vault integrity gate — run from the vault root, exits 1 on any failure
python 14_Data/scripts_verify_vault.py

# dataset checks
python 14_Data/scripts_extract_cost_data.py 14_Data/dataset_raw.csv
python 14_Data/scripts_analyze_outliers.py
```

`scripts_verify_vault.py` checks five things and exits non-zero if any fail:

1. every `.md` file carries YAML frontmatter
2. `Program_Map.canvas` is valid JSON and every file ref + edge endpoint resolves
3. every `[[wikilink]]` and `](x.md)` link resolves to a real file
4. every `.md` file is represented in the canvas
5. the cleaned dataset reconciles to RM 115,885 with all `rate × qty` checks passing

`scripts_extract_cost_data.py` prints a per-category reconciliation table and reports any
category whose line items stop summing to its stated subtotal. Run it whenever the costing
report changes — it is the control that actually catches this dataset's defect class.

Requires Python 3 only; no third-party packages.

---

*Prepared by Hermes Agent for Bashirun Che — 2026-10-19*
