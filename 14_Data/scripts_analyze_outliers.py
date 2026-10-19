#!/usr/bin/env python3
"""Outlier detection + standardisation for the ROV yard-relocation dataset.

Methods implemented in pure stdlib (no numpy/pandas on this host):
  * IQR  -- Tukey fences, 1.5x (outlier) and 3.0x (extreme outlier)
  * z-score -- |z| >= 3.0 on sample stdev (n-1)
Quantiles use linear interpolation between closest ranks (R type 7 / numpy default).

Inputs : dataset_raw.csv          (72 cost line items, from the costing report)
Outputs: dataset_cleaned.csv      standardised records
         outliers_flagged.csv     every flagged record with method + verdict
         analysis_results.json    machine-readable summary
"""
import csv
import json
import math
import statistics
from pathlib import Path

HERE = Path(__file__).parent
RAW = HERE / "dataset_raw.csv"
OUT_CLEAN = HERE / "dataset_cleaned.csv"
OUT_FLAG = HERE / "outliers_flagged.csv"
OUT_JSON = HERE / "analysis_results.json"


# ---------------------------------------------------------------- statistics
def quantile(sorted_vals, p):
    """Linear interpolation between closest ranks (type 7)."""
    n = len(sorted_vals)
    if n == 0:
        return None
    if n == 1:
        return float(sorted_vals[0])
    idx = p * (n - 1)
    lo = math.floor(idx)
    hi = math.ceil(idx)
    if lo == hi:
        return float(sorted_vals[lo])
    return sorted_vals[lo] + (sorted_vals[hi] - sorted_vals[lo]) * (idx - lo)


def iqr_analysis(values, k_outlier=1.5, k_extreme=3.0):
    v = sorted(float(x) for x in values)
    q1, q2, q3 = quantile(v, 0.25), quantile(v, 0.50), quantile(v, 0.75)
    iqr = q3 - q1
    return {
        "n": len(v), "q1": q1, "median": q2, "q3": q3, "iqr": iqr,
        "lower_fence": q1 - k_outlier * iqr,
        "upper_fence": q3 + k_outlier * iqr,
        "lower_extreme": q1 - k_extreme * iqr,
        "upper_extreme": q3 + k_extreme * iqr,
    }


def zscore_analysis(values):
    v = [float(x) for x in values]
    mean = statistics.fmean(v)
    sd = statistics.stdev(v) if len(v) > 1 else 0.0
    return {"n": len(v), "mean": mean, "stdev": sd,
            "zscores": [((x - mean) / sd if sd else 0.0) for x in v]}


# ---------------------------------------------------------------- load raw
with RAW.open(encoding="utf-8") as f:
    rows = list(csv.DictReader(f))
for r in rows:
    r["total_rm"] = float(r["total_rm"]) if r["total_rm"] else None
    r["recomputed_total"] = float(r["recomputed_total"]) if r["recomputed_total"] else None
    r["arithmetic_ok"] = (r["arithmetic_ok"] == "True")

costed = [r for r in rows if r["total_rm"] is not None]
totals = [r["total_rm"] for r in costed]

iq = iqr_analysis(totals)
zs = zscore_analysis(totals)
zmap = {r["line_id"]: z for r, z in zip(costed, zs["zscores"])}

# ---------------------------------------------------------------- flagging
flagged = []
for r in costed:
    lid, t = r["line_id"], r["total_rm"]
    z = zmap[lid]
    iqr_out = t < iq["lower_fence"] or t > iq["upper_fence"]
    iqr_ext = t < iq["lower_extreme"] or t > iq["upper_extreme"]
    z_out = abs(z) >= 3.0
    methods = []
    if iqr_out:
        methods.append("IQR-extreme" if iqr_ext else "IQR-1.5")
    if z_out:
        methods.append("z>=3")
    if methods:
        # statistical extreme, but a cost line item is a legitimate large cost,
        # NOT a corrupt observation -> quarantine for review, never auto-delete
        verdict = "REVIEW-HIGH-VALUE (valid cost line, retained)"
        if not r["arithmetic_ok"]:
            verdict = "REMOVE (arithmetic failure)"
        flagged.append({
            "line_id": lid, "category": r["category"], "resource_type": r["resource_type"],
            "total_rm": t, "z_score": round(z, 3), "methods": "+".join(methods),
            "arithmetic_ok": r["arithmetic_ok"], "verdict": verdict,
        })

# ---------------------------------------------------------------- cleaning
def normalise_unit(raw):
    """'1,000/week' -> (1000.0,'week'); '8 weeks' -> (8.0,'week'); '4 x 10 days' -> (40.0,'person-day')"""
    s = raw.strip()
    if s in ("—", "-", "", "TBD"):
        return None, None
    s = s.replace(",", "")
    m = __import__("re").match(r"^(\d+(?:\.\d+)?)\s*[x×]\s*(\d+(?:\.\d+)?)\s*(.*)$", s)
    if m:
        return float(m.group(1)) * float(m.group(2)), (m.group(3).strip().rstrip("s") or None)
    m = __import__("re").match(r"^(\d+(?:\.\d+)?)\s*(.*)$", s)
    if not m:
        return None, None
    unit = m.group(2).strip().rstrip("s") or None
    return float(m.group(1)), unit


clean = []
for r in costed:
    rv, ru = normalise_unit(r["rate_raw"])
    qv, qu = normalise_unit(r["qty_raw"])
    clean.append({
        "line_id": r["line_id"],
        "category_code": r["category_code"],
        "category": r["category"].strip(),
        "resource_type": r["resource_type"].strip(),
        "rate_value_rm": f"{rv:.2f}" if rv is not None else "",
        "rate_unit": ru or "",
        "qty_value": f"{qv:.0f}" if qv is not None else "",
        "qty_unit": qu or "",
        "total_rm": f"{r['total_rm']:.2f}",
        "recomputed_total_rm": f"{r['recomputed_total']:.2f}" if r["recomputed_total"] is not None else "",
        "arithmetic_ok": r["arithmetic_ok"],
        "z_score": f"{zmap[r['line_id']]:.3f}",
        "iqr_flag": "extreme" if (r["total_rm"] < iq["lower_extreme"] or r["total_rm"] > iq["upper_extreme"])
                    else ("outlier" if (r["total_rm"] < iq["lower_fence"] or r["total_rm"] > iq["upper_fence"]) else ""),
        "status": "retained",
    })

with OUT_CLEAN.open("w", newline="", encoding="utf-8") as f:
    w = csv.DictWriter(f, fieldnames=list(clean[0].keys()))
    w.writeheader()
    w.writerows(clean)

with OUT_FLAG.open("w", newline="", encoding="utf-8") as f:
    w = csv.DictWriter(f, fieldnames=["line_id", "category", "resource_type", "total_rm",
                                      "z_score", "methods", "arithmetic_ok", "verdict"])
    w.writeheader()
    w.writerows(flagged)

# ---------------------------------------------------------------- figure series
# Competing *project-total* figures found across the vault. Each is one
# observation of the same quantity (total relocation cost), so IQR/z-score
# on this series is a genuine consistency test -- unlike the line items.
FIGURES = [
    (85000,   "Blue team target (lower bound)", "Blue_vs_Red_Costing_Discussion.md §2"),
    (95000,   "Blue team target (upper bound)", "Blue_vs_Red_Costing_Discussion.md §2"),
    (99290,   "Draft summary total", "Plan_3_Hybrid_Costing_Report.md §5"),
    (103265,  "Revised stated total (pre-rerun)", "Blue_vs_Red_Costing_Discussion.md §6"),
    (104165,  "Blue vs Red revised column, summed", "Plan_3_Hybrid_Costing_Report.md §5"),
    (114665,  "Revised, contingency held at original", "Plan_3_Hybrid_Costing_Report.md §5"),
    (115885,  "Revised estimate (current, v2.0)", "Plan_3_Hybrid_Costing_Report.md §1"),
    (123165,  "Original stated total", "Plan_3_Hybrid_Costing_Report.md §5"),
    (124065,  "Original line items, summed", "Plan_3_Hybrid_Costing_Report.md §5"),
]
fig_vals = [v for v, _, _ in FIGURES]
fig_iqr = iqr_analysis(fig_vals)
fig_zs = zscore_analysis(fig_vals)
fig_rows = []
for (v, label, src), z in zip(FIGURES, fig_zs["zscores"]):
    iqr_out = v < fig_iqr["lower_fence"] or v > fig_iqr["upper_fence"]
    iqr_ext = v < fig_iqr["lower_extreme"] or v > fig_iqr["upper_extreme"]
    z_out = abs(z) >= 3.0
    methods = []
    if iqr_out:
        methods.append("IQR-extreme" if iqr_ext else "IQR-1.5")
    if z_out:
        methods.append("z>=3")
    fig_rows.append({
        "value_rm": v, "label": label, "source": src,
        "z_score": round(z, 3), "methods": "+".join(methods) or "-",
        "iqr_outlier": iqr_out, "z_outlier": z_out,
        "status": "STALE/SUPERSEDED" if v not in (115885,) else "CURRENT",
    })

results = {
    "dataset": "ROV yard relocation — cost line items",
    "source_file": "11_Costing/Plan_3_Hybrid_Costing_Report.md §4",
    "n_records": len(costed),
    "iqr": iq,
    "zscore": {"mean": zs["mean"], "stdev": zs["stdev"]},
    "flagged_count": len(flagged),
    "figures_series": {"iqr": fig_iqr, "zscore": {"mean": fig_zs["mean"], "stdev": fig_zs["stdev"]},
                       "rows": fig_rows},
}
OUT_JSON.write_text(json.dumps(results, indent=2), encoding="utf-8")

# ---------------------------------------------------------------- console
print("=" * 78)
print("DATASET A — COST LINE ITEMS  (n=%d)" % len(costed))
print("=" * 78)
print(f"  Q1              RM {iq['q1']:>10,.2f}")
print(f"  Median          RM {iq['median']:>10,.2f}")
print(f"  Q3              RM {iq['q3']:>10,.2f}")
print(f"  IQR             RM {iq['iqr']:>10,.2f}")
print(f"  Lower fence     RM {iq['lower_fence']:>10,.2f}   (1.5x)")
print(f"  Upper fence     RM {iq['upper_fence']:>10,.2f}   (1.5x)")
print(f"  Extreme upper   RM {iq['upper_extreme']:>10,.2f}   (3.0x)")
print(f"  Mean            RM {zs['mean']:>10,.2f}")
print(f"  Stdev (n-1)     RM {zs['stdev']:>10,.2f}")
print()
print(f"  flagged by IQR(1.5) or |z|>=3 : {len(flagged)} of {len(costed)}")
for f_ in sorted(flagged, key=lambda x: -x["total_rm"]):
    print(f"    {f_['line_id']:<4} RM {f_['total_rm']:>8,.0f}  z={f_['z_score']:>6.2f}  {f_['methods']:<16} {f_['resource_type'][:40]}")
print()
print("=" * 78)
print("DATASET B — COMPETING PROJECT-TOTAL FIGURES  (n=%d)" % len(FIGURES))
print("=" * 78)
print(f"  Q1 RM {fig_iqr['q1']:,.0f} | Median RM {fig_iqr['median']:,.0f} | Q3 RM {fig_iqr['q3']:,.0f} | IQR RM {fig_iqr['iqr']:,.0f}")
print(f"  Fences: lower RM {fig_iqr['lower_fence']:,.0f}  upper RM {fig_iqr['upper_fence']:,.0f}")
print(f"  Mean RM {fig_zs['mean']:,.0f} | Stdev RM {fig_zs['stdev']:,.0f}")
print()
for r in sorted(fig_rows, key=lambda x: x["value_rm"]):
    mark = "OUTLIER" if r["methods"] != "-" else "       "
    print(f"    RM {r['value_rm']:>8,}  z={r['z_score']:>6.2f}  {mark} {r['methods']:<12} {r['label'][:42]}")
print()
print(f"wrote: {OUT_CLEAN.name}, {OUT_FLAG.name}, {OUT_JSON.name}")
