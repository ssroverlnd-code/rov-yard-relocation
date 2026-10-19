---
title: Outlier Removal Report — ROV Yard Relocation Dataset
type: report
tags: [rov, relocation, data-quality, outliers, iqr, z-score]
updated: 2026-10-19
---

# Outlier Removal Report

**Dataset:** ROV Yard Relocation — costed line items and competing project totals
**Source:** `11_Costing/Plan_3_Hybrid_Costing_Report.md`, `11_Costing/Blue_vs_Red_Costing_Discussion.md`, `99_Archive/Moving_Plan_3_Initial_Draft.md`
**Methods:** Tukey IQR fences (1.5× and 3.0×) and z-score (|z| ≥ 3.0, sample stdev n−1)
**Date:** 2026-10-19

---

## Headline finding

**Statistical outlier detection did not identify the corrupt records in this dataset.**

- On the 72 cost line items, IQR/z-score flagged **5 records — every one of them a legitimate large cost item**, not an error.
- On the 9 competing project-total figures, IQR/z-score flagged **0 records**, even though those figures conflict by up to **RM 39,065**.

The genuinely bad records were found by **arithmetic reconciliation**, not by statistics. Details in §4.

---

## 1. Method

Both methods were implemented in pure Python (no numpy/pandas on this host). Quantiles use linear interpolation between closest ranks (R type 7 / numpy default).

| Method | Rule | Interpretation |
|---|---|---|
| IQR (Tukey) | outside `Q1 − 1.5·IQR` … `Q3 + 1.5·IQR` | outlier |
| IQR (extreme) | outside `Q1 − 3.0·IQR` … `Q3 + 3.0·IQR` | extreme outlier |
| z-score | `\|z\| ≥ 3.0`, `z = (x − x̄)/s`, `s` = sample stdev | outlier |

---

## 2. Dataset A — 72 cost line items

| Statistic | Value |
|---|---:|
| n | 72 |
| Q1 | RM 400.00 |
| Median | RM 600.00 |
| Q3 | RM 2,100.00 |
| IQR | RM 1,700.00 |
| Lower fence (1.5×) | RM −2,150.00 |
| Upper fence (1.5×) | RM 4,650.00 |
| Upper extreme fence (3.0×) | RM 7,200.00 |
| Mean | RM 1,609.51 |
| Stdev (n−1) | RM 2,207.31 |

### Flagged records — 5 of 72

| Line | RM | z | Flagged by | Item | Verdict |
|---|---:|---:|---|---|---|
| N1 | 10,285 | 3.93 | IQR-extreme + z≥3 | General Contingency (10%) | **Retained** — derived value, 10% of A–M base |
| B1 | 10,000 | 3.80 | IQR-extreme + z≥3 | Inventory Team (3–4 persons) | **Retained** — legitimate, largest genuine cost |
| A1 | 8,000 | 2.90 | IQR-extreme | PM (Project Manager) | **Retained** — agreed at RM 1,000/wk × 8 wk |
| E1 | 7,500 | 2.67 | IQR-extreme | Low-Loader / Heavy Haulage | **Retained** — RM 2,500/trip × 3 |
| A2 | 7,200 | 2.53 | IQR-1.5 | HSE / Safety Officer | **Retained** — RM 900/wk × 8 wk |

### Why none were removed

A cost line item is a **legitimate observation**, not a corrupt one. A relocation budget is *expected* to be right-skewed: many small line items (labels, tape, permits) and a few large ones (haulage, crane, contingency). Removing the top 5 would delete **RM 42,985 — 37% of the budget** — and destroy the dataset's integrity.

The correct action for a legitimate extreme is **flag and retain**, which is what the `status` and `iqr_flag` columns in `dataset_cleaned.csv` now carry.

> **Corollary:** on this dataset IQR at 1.5× is too aggressive a fence. The right-skew is intrinsic to cost data. A 3.0× fence, or a log transform before z-scoring, would be the defensible choice if a numeric outlier gate is required.

---

## 3. Dataset B — 9 competing project-total figures

Every project-total figure found across the vault. These are all observations of *the same quantity* (total relocation cost), so a consistency test is genuinely meaningful here.

| Statistic | Value |
|---|---:|
| n | 9 |
| Q1 | RM 99,290 |
| Median | RM 104,165 |
| Q3 | RM 115,885 |
| IQR | RM 16,595 |
| Lower fence (1.5×) | RM 74,398 |
| Upper fence (1.5×) | RM 140,778 |
| Mean | RM 107,167 |
| Stdev (n−1) | RM 13,226 |

| Figure (RM) | z | Outlier? | Label | Source |
|---:|---:|---|---|---|
| 85,000 | −1.68 | no | Blue team target (lower bound) | Blue_vs_Red §2 |
| 95,000 | −0.92 | no | Blue team target (upper bound) | Blue_vs_Red §2 |
| 99,290 | −0.60 | no | Draft summary total | Costing Report §5 |
| 103,265 | −0.29 | no | Revised stated total (pre-rerun) | Blue_vs_Red §6 |
| 104,165 | −0.23 | no | Blue vs Red revised column, summed | Costing Report §5 |
| 114,665 | 0.57 | no | Revised, contingency held at original | Costing Report §5 |
| **115,885** | 0.66 | no | **Revised estimate (current, v2.0)** | Costing Report §1 |
| 123,165 | 1.21 | no | Original stated total | Costing Report §5 |
| 124,065 | 1.28 | no | Original line items, summed | Costing Report §5 |

**Zero records flagged.** The two historical archives add two more figures for context — RM 48,250 and RM 58,550 from `99_Archive/Moving_Plan_3_Initial_Draft.md` — which would widen the spread to **RM 48,250 – 124,065**.

### Why the method failed here

IQR fences scale with the spread of the sample. When *every* value in a series is a different attempt at the same number, the disagreement inflates the IQR and pushes the fences out until nothing is an outlier. The series is not contaminated by a few extremes — **it is uniformly inconsistent**. Statistics can describe that (stdev RM 13,226 ≈ 12% of the mean) but cannot name which value is wrong. Naming the wrong one requires reconciliation against the line items, which §4 does.

---

## 4. Records actually removed, and how they were found

| # | Record | Value | Defect | Detection method | Action |
|---|---|---:|---|---|---|
| 1 | Labour line **M1** — Inventory Team | RM 10,000 | Exact duplicate of B1 (same team, 4 persons × 10 days, budgeted twice) | Cross-category reconciliation: B1 and M1 had identical rate × qty | **Removed** — already applied in costing v2.0, confirmed correct |
| 2 | Misc line **O2** — Incident Response Fund | RM 500 | Double-counted risk provision; absorbed into N1 contingency | Overlap analysis against Category N | **Removed** — already applied in costing v2.0, confirmed correct |
| 3 | Stated total **RM 123,165** | 123,165 | RM 900 below the sum of its own line items | Summed line items vs stated figure | **Superseded** by RM 124,065 |
| 4 | Stated total **RM 103,265** | 103,265 | RM 900 below the sum of its own revised column | Summed revised column vs stated figure | **Superseded** by RM 104,165 |
| 5 | Draft summary total **RM 99,290** | 99,290 | Built on a different, earlier set of category subtotals (A = 8,400 vs detailed 21,700) | Category subtotal comparison | **Superseded** |
| 6 | Category B revised figure **RM 1,800** | — | Inventory-team removal applied twice (B −10,000 *and* M −10,000) | Reconciliation of adjustment list vs category table | **Corrected** — B holds RM 11,800; only M1 removed |

**Net effect of removal: −RM 10,500** (M1 RM 10,000 + O2 RM 500), plus four superseded figures retired from the live series.

**Verification of the cleaned result:** the 72 retained line items sum to exactly **RM 115,885.00**, which reconciles to the costing report's stated total with zero variance. All 15 category subtotals reconcile to their line items, and all 72 records satisfy `rate × qty = total`.

---

## 5. Artefacts

| File | Contents |
|---|---|
| `dataset_raw.csv` | 72 extracted line items, unmodified |
| `dataset_cleaned.csv` | 72 standardised records + `z_score`, `iqr_flag`, `status` columns |
| `outliers_flagged.csv` | Every record flagged by either method, with verdict |
| `analysis_results.json` | Machine-readable statistics for both datasets |
| `scripts_extract_cost_data.py` | Extraction + per-category reconciliation |
| `scripts_analyze_outliers.py` | IQR / z-score implementation |

---

## 6. Recommendation

Do not apply an automated outlier gate to this dataset. It is a **budget**, not a measurement series — extremes are expected and meaningful. The control that actually works here is **arithmetic reconciliation**, which caught all six real defects above. Run `scripts_extract_cost_data.py` as a regression check whenever the costing report changes; it fails loudly on any category that stops reconciling.

---

*Prepared by Hermes Agent for Bashirun Che — 2026-10-19*
