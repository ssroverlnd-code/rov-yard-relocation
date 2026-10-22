---
title: ADR-002 — Package-Level Tagging (5S)
type: adr
tags: [rov, relocation, adr, tagging, 5s, package-tagging]
updated: 2026-10-22
---

# ADR-002: Package-Level Tagging — Sort, Then Tag (5S)

**Status:** ACCEPTED  
**Raised:** 2026-10-22  
**Raised by:** Yard team (Bashirun, Hammam, Ihsan), confirmed by the Relocation Lead  
**Priority:** HIGH  
**Owner:** Inventory Lead

## 1. Background

Stage 2 of the master moving plan required every item to carry a unique barcode/QR tag before it could move — "nothing moves without a tag". In practice the yard team sorts items into categories first and packs them into containers, crates and bins. Tagging loose items before the wanted / unwanted decision produced tags on items that were then thrown away.

The 21.10.2026 briefing board records the sequence the team actually intends: sort by hydraulic / electric / mechanical, capture dimension and weight, then use the container as temporary storage. Sorting comes first; labelling follows.

## 2. Issue Statement

What is the unit of tagging for the relocation — the individual item, or the packed package?

## 3. Options

| Option | Description | Pros | Cons |
|--------|-------------|------|------|
| **A — Item-level tagging** (original plan) | Every item gets a unique barcode/QR tag | Maximum traceability per item | Slow; tags wasted on discarded items; conflicts with pack-then-label practice; high label and labour cost |
| **B — Package-level tagging** (adopted) | Sort first, then pack and tag each sealed package with a contents list | Matches how the yard already works; far fewer labels; faster; contents list preserves item detail | Item-level traceability depends on the contents list being accurate |
| **C — Zone-level tagging only** | Tag zones, not packages | Fastest | No traceability of individual packages — unacceptable for Class A |

## 4. Recommendation

**Option B.** Tag at package level, applied after sorting, using the 5S sequence: **Sort → Set in order → Shine → Standardise → Sustain**.

- Package tag format `[ZONE]-[CLASS]-PKG-[SEQ]`, e.g. `WH-A-PKG-001`.
- Every package carries a **contents list** naming each item, its quantity, condition code and photo reference.
- Class A packages additionally get a tamper-evident seal, an item-level manifest inside the package, and a photograph of the sealed package with the tag visible.
- Item-level detail stays in the inventory spreadsheet — one row per item, each carrying its package tag.

## 5. Decision

| # | Decision | Decided by | Date |
|---|----------|------------|------|
| 1 | The tagging unit is the **package**, not the item | Relocation Lead | 2026-10-22 |
| 2 | Tagging follows sorting — 5S 1S closes before 2S starts | Relocation Lead | 2026-10-22 |
| 3 | Every package carries a tag and a contents list | Inventory Lead | 2026-10-22 |
| 4 | Class A packages are sealed, manifested and photographed | Security Lead | 2026-10-22 |
| 5 | "Nothing moves without a tag" becomes "nothing moves without a package tag and contents list" | Relocation Lead | 2026-10-22 |

## 6. Consequences

- `01_Planning/master_moving_plan.md` — Stage 2 objective, task 2.1, task 2.3, exit gate and the dependencies table updated.
- `02_Stage_Details/stage_details.md` — Stage 2 objective, daily plan and quality checks rewritten around packages.
- `03_Inventory/inventory_classification.md` — tagging standard rewritten; 5S workflow section added.
- `06_Risk/risk_register.md` — R16 mitigation updated; **R21** added (package contents do not match the contents list).
- `13_Deliverables/Move_Plan_ROV_Relocation.md` (v1.1) and its printable HTML (v1.2) amended.
- `04_Stakeholders/stakeholder_register.md` — inventory team responsibility updated to include 5S sorting and package tagging.
- **Costing is unchanged.** The RM 115,885 total and the `14_Data` dataset still reconcile. Package-level tagging needs fewer labels than the barcode/QR line assumed; any saving is not yet reflected in the approved budget.

## 7. Update Log

| Date | Update | By |
|------|--------|-----|
| 2026-10-22 | Raised and accepted — package-level tagging applied after sorting (5S) | Relocation Lead |
