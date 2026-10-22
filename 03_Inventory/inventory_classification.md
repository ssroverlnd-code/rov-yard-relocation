---
title: Inventory Classification Guide
type: inventory
tags: [rov, inventory, classification, 5s, package-tagging]
updated: 2026-10-22
---

# Inventory Classification Guide

## Purpose
Every item in the Pasir Gudang yard must be classified **before it moves**, and every **package** must be tagged before it moves. This guide ensures consistent categorisation and tagging across the inventory team.

---

## 5S Workflow — Sort, Then Tag

Tagging happens **after** sorting, not before. A package is tagged once its contents are decided and it is packed and sealed. Tagging loose items before the wanted / unwanted decision produces tags on items that are then thrown away.

| 5S Step | Japanese | What happens in the yard | Evidence |
|---------|----------|--------------------------|----------|
| **1S — Sort** | Seiri | Separate wanted from unwanted at each sorting station. Unwanted items go to the hold area as disposal candidates — nothing is disposed of without technical-owner and Finance approval. | Wanted / unwanted split, salvage list |
| **2S — Set in order** | Seiton | Pack each category into a sealed package (crate, bin, pallet, wrapped bundle, container). **Tag the package** and fix the contents list to it. Stage packages by dispatch priority. | Package tag, contents list, staging plan |
| **3S — Shine** | Seiso | Clean the package and the sorting station as it is packed. Record the condition of each item while the package is still open. | Condition codes on the contents list |
| **4S — Standardise** | Seiketsu | One tag format, one contents list, one condition-code set and one inventory column set, used in every zone. | This guide |
| **5S — Sustain** | Shitsuke | Daily progress report, weekly 5S audit per zone, reconciliation at the new yard. | Daily progress report, audit checklist |

**Sequence rule:** 1S closes before 2S starts in a zone. A zone is only tagged once its wanted / unwanted split is agreed.

---

## Classification Categories

| Class | Definition | Handling | Transport Method | Storage at New Yard |
|-------|------------|----------|------------------|---------------------|
| **A — High Value** | Copper cables, hand tools, precision instruments, ROV critical spares, any item > RM 5,000 value | Tamper-evident sealed packages, item-level manifest, security escort, direct transit | Secure vehicle (dedicated, no intermediate stops) | Locked secure cage / container |
| **B — Heavy** | ROV components, structural steel, skids, large containers, items > 500 kg | Rigging assessment, crane lift, lift plan per item | Low-loader / heavy haulage | Pre-marked heavy zone on hard standing |
| **C — Consumable** | General spares, consumables, small loose items, bulk materials | Standard packing, labelled packages | General vehicle (multiple runs OK) | Shelving/racking by category |
| **D — Office/Furniture** | Office furniture, filing cabinets, non-essential IT, documents | Sort: sell vs. discard; pack IT separately | General vehicle | Document storage area or disposed |

---

## Tagging Standard

**The tagging unit is the package, not the item.**

A package is a sealed crate, bin, pallet, wrapped bundle or container holding one or more items of the same class. Item-level detail is recorded in the inventory spreadsheet and on the package's contents list — it is not printed on a physical tag.

**Tag format:** `[ZONE]-[CLASS]-PKG-[SEQ]`

| Package tag | Meaning |
|-------------|---------|
| `WH-A-PKG-001` | Warehouse, High Value, package 001 |
| `RY-B-PKG-002` | Roofed Yard, Heavy, package 002 |
| `OY-C-PKG-003` | Open Yard, Consumable, package 003 |
| `OF-D-PKG-004` | Office, Furniture, package 004 |
| `OF-F-PKG-005` | Office, Disposal / scrap, package 005 |

**Every package carries two things:**

1. The package tag.
2. A **contents list** fixed to the package, naming each item, its quantity, its condition code and its photo reference.

**Class A packages** additionally get a tamper-evident seal, an item-level manifest inside the package, and a photograph of the sealed package with the tag visible.

| Zone Code | Meaning |
|-----------|---------|
| WH | Warehouse |
| RY | Roofed Yard |
| OY | Open Yard |
| OF | Office Area |

---

## Condition Codes

| Code | Meaning |
|------|---------|
| **SVC** | Serviceable — fit for use |
| **REP** | Requires repair — still worth keeping |
| **OBS** | Obsolete — flag for disposal review |
| **DAM** | Damaged — flag for disposal |
| **UNK** | Unknown condition — requires assessment |

---

## Inventory Spreadsheet Columns

The inventory team must maintain these columns in the master inventory spreadsheet:

| Column | Example |
|--------|---------|
| Package Tag | RY-A-PKG-002 |
| Zone | Roofed Yard |
| Item Description | Copper cable 95mm² (50m coil) |
| Class | A |
| Condition | SVC |
| Quantity | 12 coils |
| Value (RM) | 2,400/each |
| Photo Ref | IMG_0234.jpg |
| Move Priority | 1 (first) |
| Disposition | Relocate / Sell / Dispose |
| New Yard Zone | Secure Cage A3 |

> One row per item, each carrying the **package tag** it has been packed into. The package tag is what gets physically labelled; the item rows are the record.

---

## Special Handling Notes

### Copper Cables (Highest Theft Risk)
- Photograph each sealed Class A package with its tag visible
- Measure and record approximate weight per package
- Transport in locked container with manifest signed at load AND unload
- Consider pre-move insurance notification

### Hand Tools
- Pack in tool rolls or shadow boards where possible
- Count and record each set on the package contents list
- No unmarked bags — every bag labelled with its contents list

### Heavy Items
- Record approximate weight and dimensions
- Note any disassembly required before lifting
- Identify centre of gravity if known

### Consumables
- Group by type (fasteners, seals, lubricants, etc.)
- Note any hazardous material classification (MSDS sheets)
- Check expiry dates where applicable

---

## Disposition Decision Tree

```
Is the item serviceable?
├── NO → Is it valuable as scrap?
│         ├── YES → Sell as scrap metal
│         └── NO  → Dispose via licensed waste collector
└── YES → Is it still in use / needed?
          ├── YES → Relocate to new yard (Class A, B, or C)
          └── NO  → Is it saleable?
                    ├── YES → Sell (add to furniture/equipment sale list)
                    └── NO  → Store at new yard (Class C bulk)
```

---

*All inventory team members must be briefed on this guide before starting Stage 2. Questions to Inventory Lead.*
