---
title: Inventory Classification Guide
type: inventory
tags: [rov, inventory, classification]
updated: 2026-10-19
---

# Inventory Classification Guide

## Purpose
Every item in the Pasir Gudang yard must be classified **before it moves**. This guide ensures consistent categorisation across the inventory team.

---

## Classification Categories

| Class | Definition | Handling | Transport Method | Storage at New Yard |
|-------|------------|----------|------------------|---------------------|
| **A — High Value** | Copper cables, hand tools, precision instruments, ROV critical spares, any item > RM 5,000 value | Tamper-evident sealed crates, item-level manifest, security escort, direct transit | Secure vehicle (dedicated, no intermediate stops) | Locked secure cage / container |
| **B — Heavy** | ROV components, structural steel, skids, large containers, items > 500 kg | Rigging assessment, crane lift, lift plan per item | Low-loader / heavy haulage | Pre-marked heavy zone on hard standing |
| **C — Consumable** | General spares, consumables, small loose items, bulk materials | Standard packing, labelled bins/crates | General vehicle (multiple runs OK) | Shelving/racking by category |
| **D — Office/Furniture** | Office furniture, filing cabinets, non-essential IT, documents | Sort: sell vs. discard; pack IT separately | General vehicle | Document storage area or disposed |

---

## Tagging Standard

Every item (or grouped set of identical items) receives a **unique tag** at inventory stage:

```
TAG FORMAT: [ZONE]-[CLASS]-[SEQ]

Examples:
  WH-A-001  = Warehouse, High Value, item 001
  RY-B-002  = Roofed Yard, Heavy, item 002
  OY-C-003  = Open Yard, Consumable, item 003
  OF-D-004  = Office, Furniture, item 004
```

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
| Tag | RY-A-001 |
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

---

## Special Handling Notes

### Copper Cables (Highest Theft Risk)
- Photograph each coil with tag visible
- Measure and record approximate weight
- Transport in locked container with manifest signed at load AND unload
- Consider pre-move insurance notification

### Hand Tools
- Pack in tool rolls or shadow boards where possible
- Count and record each set
- No unmarked bags — every bag labelled with contents list

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
