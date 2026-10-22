---
title: Plan 2 — Red Team (Operational Execution)
type: plan-option
tags: [rov, plan, red-team, execution]
updated: 2026-10-22
---

# Plan 2 — Red Team: Operational Execution Plan

**Approach:** Stage-driven, execution-optimised, vendor-rich, detail-heavy operational plan.  
**Source:** `01_Planning/master_moving_plan.md` and supporting documents  
**Duration:** 8 weeks, sequential stages with controlled overlap  
**Status:** For team discussion and decision

---

## 1. Philosophy

Treat this as a **military-style staged operation** — every stage has a checklist, every item has a tag, every vendor has a contract, every risk has a score. Speed through execution detail, not management process. The plan is designed to be printed and used on-site by foremen and workers.

---

## 2. Organization

| Team | Leader | Members | Responsibility |
|------|--------|---------|----------------|
| **Project Management Office (PMO)** | PMO Lead | 2–3 | Overall coordination, timeline, stakeholder communication, budget, authority liaison |
| **Inventory & Classification** | Inventory Lead | 3–4 | Physical count, tagging, classification, photo documentation, inventory spreadsheet |
| **Operations** | Operations Lead | 3–5 | New yard layout, fencing, lighting, utilities, salvage/disposal |
| **Lifting & Rigging** | Rigging Supervisor | 2–4 | Crane operations, lift plans, safe lifting of Class B items |
| **Transport & Logistics** | Logistics Coordinator | 2–3 | Vehicle bookings, route planning, manifests, JPJ permits |
| **Security & Valuables** | Security Lead | 2–3 | Class A handling, security escort, secure cage management, CCTV |
| **IT & Equipment** | IT Lead | 1–2 | IT disconnect, packing, reinstall, network setup |
| **Warehouse & Storage** | Warehouse Lead | 3–4 | Packing, labelling, staging, shelving/racking installation |

**Escalation:** Team Lead → PMO Lead → Project Sponsor

---

## 3. Inventory Classification (4 Categories)

| Class | Definition | Handling | Transport | Storage |
|-------|------------|----------|-----------|---------|
| **A — High Value** | Copper cables, hand tools, precision instruments, ROV critical spares, items > RM 5,000 | Tamper-evident sealed crates, item-level manifest, security escort, direct transit | Secure vehicle, dedicated, no stops | Locked secure cage |
| **B — Heavy** | ROV components, structural steel, skids, large containers, items > 500 kg | Rigging assessment, crane lift, lift plan per item | Low-loader / heavy haulage | Pre-marked heavy zone |
| **C — Consumable** | General spares, consumables, small loose items, bulk materials | Standard packing, labelled bins/crates | General vehicle, multiple runs OK | Shelving/racking by category |
| **D — Office/Furniture** | Office furniture, filing cabinets, non-essential IT, documents | Sort sell vs. discard; pack IT separately | General vehicle | Document storage or disposed |

**Tag format:** `[ZONE]-[CLASS]-[SEQ]` (e.g., `RY-A-001`)  
**Zone codes:** WH (Warehouse) · RY (Roofed Yard) · OY (Open Yard) · OF (Office)  
**Condition codes:** SVC / REP / OBS / DAM / UNK

> **Amended by ADR-002 (2026-10-22):** tagging is now applied at **package level** after sorting, not per item — `[ZONE]-[CLASS]-PKG-[SEQ]` with a contents list on every package. This page is retained as the source plan; the current standard is `03_Inventory/inventory_classification.md` and `10_ADR/ADR-002_Package_Tagging.md`.

---

## 4. Eight-Week Schedule

| Week | Focus | Key Activities |
|------|-------|----------------|
| **W1** | Foundation + Inventory start | Project setup, comms, walkthrough, layout draft, vendor/authority lists, inventory starts |
| **W2** | Inventory complete + Stakeholders | Full inventory, classification, Class A photos, vendor quotes, authority applications, landlord engagement |
| **W3** | Contracts + New yard prep | Vendor contracts signed, authority applications, fence/lighting/cage/racking at new yard, furniture sort |
| **W4** | Valuable items move + Heavy begins | Secure cage ready, **Class A convoy**, heavy items begin (crane lifts), furniture sale |
| **W5** | Heavy + Office equipment | Heavy items continue, IT + cabinets move, IT reinstall |
| **W6** | Heavy finish + Loose items begin | Heavy complete, consumables packing, multiple vehicle runs |
| **W7** | Loose items complete | Final packing and transport, shelving, inventory reconciliation |
| **W8** | Close-out | Full audit, commission infrastructure, old yard clean-up, handover, sign-off |

---

## 5. Stage Detail (10 Stages)

### Stage 1 — Foundation & Planning (W1)

| # | Task | Owner |
|---|------|-------|
| 1.1 | Set up project folder, register, comms channels | PMO Lead |
| 1.2 | Walkthrough all zones + photo/video | Inventory Lead |
| 1.3 | Draft new yard layout concept | Operations Lead |
| 1.4 | Register authorities to contact + vendor shortlist | PMO Lead |
| 1.5 | Kick-off meeting with all internal leads | PMO Lead |

**Exit Gate:** Layout drafted · Walkthrough complete · Lists opened

### Stage 2 — Inventory & Classification (W1–W2)

| # | Task | Owner |
|---|------|-------|
| 2.1 | Physical inventory — all items tagged | Inventory Lead |
| 2.2 | Classify each item A/B/C/D | Inventory Lead |
| 2.3 | Photograph + condition-note every Class A item | Inventory Lead |
| 2.4 | Verify quantities of copper, tools, metal against records | Operations Lead |
| 2.5 | Flag items for salvage/disposal | Operations Lead |

**Exit Gate:** 100% tagged · Class A photo-documented

### Stage 3 — Stakeholder Setup & Compliance (W2–W3)

**Vendors (6 types):**

| Vendor | Action |
|--------|--------|
| Heavy haulage / low-loader | 3 quotes → evaluate → sign |
| General moving company | 3 quotes → evaluate → sign |
| Crane & rigging services | Confirm availability + quote |
| Security escort firm | Confirm availability + quote |
| Scrap metal collector | Arrange for disposal |
| E-waste recycler | Arrange for disposal |

**Authorities (6):**

| Authority | Application |
|-----------|-------------|
| MPPG (Pasir Gudang) | Move-out notification |
| MPMT (Masjid Tanah) | Trade licence / occupancy permit |
| JPJ | Oversized load permit (if needed) |
| Insurance provider | Goods-in-transit + storage policy |
| Bomba / Fire & Safety | Storage compliance |
| DOE | Scrap/e-waste disposal licence |

**New yard landlord:** Lease review → handover date → power/water/fencing → restrictions

### Stage 4 — New Yard Preparation (W3–W4)

| # | Task | Owner |
|---|------|-------|
| 4.1 | Perimeter fence upgrade/repair | Operations Lead |
| 4.2 | Secure cage installed for Class A | Security Lead |
| 4.3 | Zone floor markings painted | Warehouse Lead |
| 4.4 | Shelving and racking installed | Warehouse Lead |
| 4.5 | Power, water, welfare confirmed | Operations Lead |
| 4.6 | CCTV / alarm test | Security Lead |

**Zones:** Zone 1 Secure Cage (Red) · Zone 2 Heavy Hard Standing (Yellow) · Zone 3 Shelving (Blue) · Zone 4 Documents (Green) · Zone 5 Loading (White)

### Stage 5 — Sale & Disposal of Office Furniture (W3–W4)

| # | Task | Owner |
|---|------|-------|
| 5.1 | Sort furniture: sell vs. discard | Operations Lead |
| 5.2 | Advertise saleable items | PMO Lead |
| 5.3 | Arrange scrap/e-waste collector | Operations Lead |
| 5.4 | Disconnect and pack all IT equipment | IT Lead |
| 5.5 | Filing cabinet contents: keep / archive / shred | Warehouse Lead |
| 5.6 | Confirm old yard office cleared | PMO Lead |

### Stage 6 — Valuable Items Move (W4)

**Packing protocol:**
1. Item-by-item manifest — every tag recorded in/out
2. Tamper-evident seals on all crates
3. Photograph sealed crate before loading
4. Dual-signature at loading (Security Lead + Logistics Coordinator)

**Convoy protocol:**
| Step | Detail |
|------|--------|
| Vehicle | Dedicated secure van or small truck |
| Escort | Security escort vehicle |
| Route | Direct — no intermediate stops |
| Communication | 30-min checkpoint calls to PMO |
| Arrival | Security Lead receives, signs manifest |
| Offload | Direct into secure cage, no staging in open |

### Stage 7 — Big & Heavy Items Move (W4–W6)

**Lift plan per item:** Tag · Description · Weight · Lift method · Special notes

**Pre-move:**
- Crane booked for each lift day
- Lift plan reviewed by Rigging Supervisor
- JPJ permit if dimensions exceed limits
- Police/authority notification if required
- New yard heavy zone clear and ready

**Safety briefing every lift day:** Exclusion zone · PPE · Banksman + radio · Pre-move brief

### Stage 8 — Office Equipment & Filing Cabinets (W5–W6)

| Item | Packing | Destination |
|------|---------|-------------|
| Computers / monitors | Anti-static wrap + box | Office desk area |
| Network equipment | Original packaging | IT rack / cabinet |
| Cables / accessories | Labelled bags in crate | IT storage |
| Filing cabinets | Upright, secured in vehicle | Zone 4 document storage |

### Stage 9 — Loose Items & Consumables Move (W6–W7)

| Item Type | Packing | Label |
|-----------|---------|-------|
| Fasteners, small parts | Bins with dividers | Category + size |
| Seals, O-rings | Labelled boxes | Type + size |
| Lubricants, chemicals | Original containers + secondary containment | MSDS reference |
| Hand tools | Tool rolls / shadow boards | Tool list inside |
| General spares | Crates by category | Category + tag range |

### Stage 10 — Settle, Commission & Close-Out (W8)

| # | Task | Owner |
|---|------|-------|
| 10.1 | Full audit — physical count vs. inventory | Inventory Lead |
| 10.2 | Commission new yard infrastructure | Security Lead |
| 10.3 | Old yard final clean-up | Operations Lead |
| 10.4 | Old yard handover to landlord | PMO Lead |
| 10.5 | Close all authority licences and permits | PMO Lead |
| 10.6 | Final project review — lessons learned | PMO Lead |
| 10.7 | Project sign-off and archive | PMO Lead |

---

## 6. Communication Plan

| Channel | Purpose | Participants |
|---------|---------|--------------|
| WhatsApp group | Daily coordination, quick updates | All internal leads |
| Email thread | Vendors, authorities, landlords | PMO + Logistics |
| Weekly status report | Progress, upcoming, issues, decisions | All stakeholders |

**Meetings:** Daily stand-up (execution weeks, 15 min) · Weekly review (Friday, 30 min) · Vendor coordination (≥ 48h before each move) · Authority follow-up (weekly)

**Weekly report template:** Completed · On track · Issues/risks · Milestones · Budget · Decisions needed

---

## 7. Risk Register (Quantified)

| ID | Risk | L | I | Score | Mitigation |
|----|------|---|---|-------|------------|
| R01 | Theft/loss of Class A in transit | 4 | 5 | **20** | Security escort, sealed crates, direct route, dual-signature, insurance |
| R02 | Damage to heavy items during lifting | 3 | 4 | **12** | Professional rigging, lift plan, exclusion zones, pre-lift inspection |
| R03 | Authority delays (JPJ, MPMT, MPPG) | 3 | 4 | **12** | Submit early, follow up weekly, escalate to sponsors |
| R04 | New yard not ready | 3 | 4 | **12** | Layout W3, weekly readiness check, hold move if cage not ready |
| R05 | Vendor no-show / breakdown | 2 | 3 | **6** | 2 backup vendors, penalty clauses, confirm 48h before |
| R06 | Copper theft at old yard during move | 4 | 4 | **16** | Move Class A first, increase security until cleared |
| R07 | Furniture disposal takes too long | 3 | 2 | **6** | Start W3, engage scrap early, extend to W7 if needed |
| R08 | Undocumented items discovered | 3 | 3 | **9** | Buffer time, classify on the spot, escalate if high value |
| R09 | Adverse weather delays heavy lifts | 2 | 3 | **6** | Monitor forecast, schedule on clear days, contingency dates |
| R10 | Insurance claim dispute | 2 | 3 | **6** | Photo before/after, item-level manifests, immediate reporting |
| R11 | New yard landlord delays handover | 3 | 4 | **12** | Signed lease with penalty, weekly contact, contingency storage |
| R12 | Road accident during transit | 2 | 4 | **8** | Experienced drivers, maintained vehicles, GPS, insurance |
| R13 | Hazardous consumables spill | 2 | 3 | **6** | MSDS review, secondary containment, trained personnel |
| R14 | Team member injury during heavy lift | 2 | 5 | **10** | PPE, exclusion zones, banksman, safety briefing, first aid |
| R15 | Budget overrun | 3 | 3 | **9** | 10% contingency, 3 quotes per vendor, weekly cost tracking |
| R16 | Incomplete inventory | 3 | 4 | **12** | Zone-by-zone count, secondary verification, spot-checks |
| R17 | IT equipment damage / data loss | 2 | 4 | **8** | Anti-static packaging, backup before disconnect, IT Lead supervision |
| R18 | Old landlord disputes condition | 2 | 3 | **6** | Move-in walkthrough photos, written condition report |

**Top 5 immediate attention:** R01 (20) · R06 (16) · R14 (10) · R16 (12) · R02 (12)

**Incident response:** Stop work → Report (15 min) → Document (photos, witnesses) → Assess → Escalate (injury/theft → Sponsor) → Insurance (24h) → Record

---

## 8. Proposed New Yard Layout

**5 zones with colour-coded markings:**

| Zone | Purpose | Colour |
|------|---------|--------|
| Zone 1 | Secure Cage — Class A valuables | Red |
| Zone 2 | Heavy Items Hard Standing — Class B | Yellow |
| Zone 3 | Shelving / Racking — Class C consumables | Blue |
| Zone 4 | Document & Filing Storage | Green |
| Zone 5 | Loading & Vehicle Access | White |

**Security:** Perimeter fence 2.4 m · CCTV 4+ cameras · Motion-sensor floodlights · Alarm on Zone 1 · Fire extinguishers each zone · Sign-in/sign-out board

**Vehicle flow:** One-way loop — enter → load/unload → exit

**Expansion:** Each zone sized 20% above current inventory

---

## 9. Strengths & Weaknesses

| Strengths | Weaknesses |
|-----------|------------|
| Actionable stage checklists — print and use | **No IMCA compliance — critical gap for ROV training** |
| 6 named vendor types + engagement schedule | **No HSE Officer — safety folded into Rigging Supervisor** |
| Communication plan + weekly report template | No document custody chain (verified → packed → authorized → dispatched → received → updated) |
| 5-zone yard layout with schematic | No KPI targets beyond "100% accounted" |
| Quantified risk register (18 risks, scored) | No acceleration strategy |
| Packing protocols per item class | No technical confirmation required for disposals |
| Dependency mapping + critical path | Only 4 inventory categories (documents/IT merged with office) |
| Gantt with daily granularity | No escalation path beyond PMO |

---

*Plan 2 of 3 — For team discussion and decision.*
