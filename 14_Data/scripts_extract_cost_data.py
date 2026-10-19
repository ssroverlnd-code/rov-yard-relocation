#!/usr/bin/env python3
"""Extract the numeric cost dataset from the ROV yard-relocation vault.

Source: 11_Costing/Plan_3_Hybrid_Costing_Report.md  (section 4, line-item detail)
Output: dataset_raw.csv  -- one row per costed line item
"""
import csv
import re
import sys
from pathlib import Path

VAULT = Path(r"C:\YARD")
SRC = VAULT / "11_Costing" / "Plan_3_Hybrid_Costing_Report.md"
OUT = Path(sys.argv[1]) if len(sys.argv) > 1 else Path("dataset_raw.csv")

text = SRC.read_text(encoding="utf-8")

# --- split into category sections: "### A. PROJECT MANAGEMENT & GOVERNANCE — RM 20,100"
sec_re = re.compile(r"^###\s+([A-Z])\.\s+(.+?)\s+—\s+RM\s+([\d,]+)\s*$", re.M)
sections = []
for m in sec_re.finditer(text):
    sections.append((m.group(1), m.group(2).strip(), int(m.group(3).replace(",", "")), m.start(), m.end()))
for i, s in enumerate(sections):
    s_end = sections[i + 1][3] if i + 1 < len(sections) else len(text)

def num(s):
    """'1,000/week' -> 1000.0 ; '8 weeks' -> 8.0 ; '4 x 10 days' -> 40.0 ; '—' -> None"""
    s = s.strip()
    if s in ("—", "-", "", "TBD"):
        return None
    s = s.replace(",", "")
    # "4 x 10 days"  -> product
    mx = re.match(r"^(\d+(?:\.\d+)?)\s*[x×]\s*(\d+(?:\.\d+)?)", s)
    if mx:
        return float(mx.group(1)) * float(mx.group(2))
    m2 = re.match(r"^(\d+(?:\.\d+)?)", s)
    return float(m2.group(1)) if m2 else None

rows = []
for i, (code, title, stated_total, start, end) in enumerate(sections):
    s_end = sections[i + 1][3] if i + 1 < len(sections) else len(text)
    block = text[start:s_end]
    for line in block.splitlines():
        line = line.strip()
        if not line.startswith("|"):
            continue
        cells = [c.strip() for c in line.strip("|").split("|")]
        if len(cells) != 6:
            continue
        no, rtype, desc, rate, qty, total = cells
        # skip header + separator rows
        if no in ("No.", "") or set(no) <= set("-: "):
            continue
        if not re.match(r"^[A-Z]\d+$", no):
            continue
        rate_n, qty_n, total_n = num(rate), num(qty), num(total)
        calc = None
        if rate_n is not None and qty_n is not None:
            calc = round(rate_n * qty_n, 2)
        rows.append({
            "line_id": no,
            "category_code": code,
            "category": title,
            "category_stated_total": stated_total,
            "resource_type": rtype,
            "rate_raw": rate,
            "qty_raw": qty,
            "rate_value": rate_n,
            "qty_value": qty_n,
            "total_rm": total_n,
            "recomputed_total": calc,
            "arithmetic_ok": (calc is None) or (abs(calc - total_n) < 0.01),
            "description": desc,
        })

# --- category-level check: do line items sum to the stated category total?
cat_check = []
for code, title, stated, _, _ in sections:
    items = [r for r in rows if r["category_code"] == code]
    s = sum(r["total_rm"] for r in items if r["total_rm"] is not None)
    cat_check.append((code, title, stated, round(s, 2), round(s - stated, 2), len(items)))

fields = ["line_id", "category_code", "category", "category_stated_total", "resource_type",
          "rate_raw", "qty_raw", "rate_value", "qty_value", "total_rm",
          "recomputed_total", "arithmetic_ok", "description"]
with OUT.open("w", newline="", encoding="utf-8") as f:
    w = csv.DictWriter(f, fieldnames=fields)
    w.writeheader()
    w.writerows(rows)

print(f"wrote {OUT}  ({len(rows)} line items)")
print()
print("=== PER-CATEGORY RECONCILIATION (stated vs sum of line items) ===")
print(f"{'Cat':<4}{'Stated':>10}{'SumItems':>11}{'Delta':>9}{'N':>4}  Title")
bad = 0
for code, title, stated, s, delta, n in cat_check:
    flag = "" if abs(delta) < 0.01 else "   <<< MISMATCH"
    if abs(delta) >= 0.01:
        bad += 1
    print(f"{code:<4}{stated:>10,}{s:>11,.0f}{delta:>9,.0f}{n:>4}  {title[:44]}{flag}")
print()
print(f"categories with stated-total mismatch: {bad}")
print(f"line items failing rate x qty = total : {sum(1 for r in rows if not r['arithmetic_ok'])}")
