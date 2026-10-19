#!/usr/bin/env python3
"""Vault integrity gate for the ROV yard-relocation repository.

Run from the vault root:   python 14_Data/scripts_verify_vault.py

Checks (exit 1 on any failure):
  1. every .md file carries YAML frontmatter
  2. Program_Map.canvas is valid JSON, and every file ref + edge endpoint resolves
  3. every [[wikilink]] and ](x.md) link resolves to a real file
  4. every .md file is represented in the canvas
  5. the cleaned dataset reconciles to the approved costing total

Pure stdlib -- no third-party packages required.
"""
import csv
import json
import re
import sys
from pathlib import Path

ROOT = Path.cwd()


def rel(p):
    """Vault-relative posix path -- the canvas and links both use this form."""
    return p.relative_to(ROOT).as_posix()


def strip_code(text):
    """Drop fenced blocks and inline code before scanning for links.

    Documentation that *shows* a link syntax inside backticks is not a link.
    """
    text = re.sub(r"```.*?```", "", text, flags=re.S)
    return re.sub(r"`[^`]*`", "", text)


CANVAS = ROOT / "Program_Map.canvas"
CLEANED = ROOT / "14_Data" / "dataset_cleaned.csv"
EXPECTED_TOTAL = 115885.00

failures = []


def hdr(n, title):
    print()
    print(f"=== {n}. {title} ===")


# ---------------------------------------------------------------- gather
md_files = sorted(p for p in ROOT.rglob("*.md") if ".git" not in rel(p))
all_files = {rel(p) for p in ROOT.rglob("*") if p.is_file() and ".git/" not in rel(p)}
filenames = {Path(f).name for f in all_files}      # WITH extension
stems = {Path(f).stem for f in all_files}          # WITHOUT extension
full = {Path(f).with_suffix("").as_posix() for f in all_files}

# ---------------------------------------------------------------- 1
hdr(1, "FRONTMATTER COVERAGE")
nofm = [rel(p) for p in md_files if not p.read_text(encoding="utf-8").startswith("---")]
print(f"  md files: {len(md_files)} | missing frontmatter: {len(nofm)} {nofm or '(none)'}")
if nofm:
    failures.append(f"{len(nofm)} file(s) missing YAML frontmatter")

# ---------------------------------------------------------------- 2
hdr(2, "CANVAS INTEGRITY")
canvas = None
broken = []
try:
    canvas = json.loads(CANVAS.read_text(encoding="utf-8"))
except Exception as exc:                                   # noqa: BLE001
    failures.append(f"canvas is not valid JSON: {exc}")
    print(f"  INVALID JSON: {exc}")
if canvas:
    ids = {n["id"] for n in canvas["nodes"]}
    broken += [f"node {n['id']} -> {n['file']}" for n in canvas["nodes"]
               if n.get("type") == "file" and n["file"] not in all_files]
    broken += [f"edge {e['id']} -> {e[k]}" for e in canvas["edges"]
               for k in ("fromNode", "toNode") if e[k] not in ids]
    print(f"  valid JSON | nodes: {len(canvas['nodes'])} | edges: {len(canvas['edges'])} "
          f"| broken refs: {len(broken)} {broken or '(none)'}")
    if broken:
        failures.append(f"{len(broken)} broken canvas reference(s)")

# ---------------------------------------------------------------- 3
hdr(3, "LINK RESOLUTION")
unresolved = []
for p in md_files:
    text = strip_code(p.read_text(encoding="utf-8"))
    for m in re.finditer(r"\[\[([^\]|#]+)", text):
        x = m.group(1).strip()
        if x in all_files or x in full or Path(x).stem in stems:
            continue
        unresolved.append((rel(p), f"[[{x}]]"))
    for m in re.finditer(r"\]\((?!http)([^)]*\.md)\)", text):
        x = m.group(1)
        # compare the FILENAME (with extension) -- stems never match a .md target
        if x in all_files or Path(x).name in filenames:
            continue
        unresolved.append((rel(p), f"({x})"))
print(f"  unresolved links: {len(unresolved)} {unresolved or '(none)'}")
if unresolved:
    failures.append(f"{len(unresolved)} unresolved link(s)")

# ---------------------------------------------------------------- 4
hdr(4, "KNOWLEDGE MAP COVERAGE")
if canvas:
    in_map = {n["file"] for n in canvas["nodes"] if n.get("type") == "file"}
    md_set = {rel(p) for p in md_files}
    unmapped = sorted(md_set - in_map)
    print(f"  md files in canvas: {len(md_set & in_map)}/{len(md_set)} | not mapped: {unmapped or '(none)'}")
    if unmapped:
        failures.append(f"{len(unmapped)} .md file(s) absent from the canvas")

# ---------------------------------------------------------------- 5
hdr(5, "DATASET RECONCILIATION")
if CLEANED.exists():
    rows = list(csv.DictReader(CLEANED.open(encoding="utf-8")))
    total = sum(float(r["total_rm"]) for r in rows)
    arith = sum(1 for r in rows if r["arithmetic_ok"] == "True")
    print(f"  records: {len(rows)} | sum: RM {total:,.2f} | arithmetic_ok: {arith}/{len(rows)} "
          f"| variance vs RM {EXPECTED_TOTAL:,.0f}: {total - EXPECTED_TOTAL:.2f}")
    if abs(total - EXPECTED_TOTAL) >= 0.01:
        failures.append(f"dataset total RM {total:,.2f} does not reconcile to RM {EXPECTED_TOTAL:,.2f}")
    if arith != len(rows):
        failures.append(f"{len(rows) - arith} record(s) fail rate x qty = total")
else:
    failures.append(f"missing {CLEANED}")

# ---------------------------------------------------------------- verdict
print()
if failures:
    print("VERIFICATION GATE: FAIL")
    for f in failures:
        print(f"  - {f}")
    sys.exit(1)
print("VERIFICATION GATE: PASS")
