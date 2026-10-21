# TM261 Session Handover

Use this file to brief a new Claude Code session. Say: "read HANDOVER.md and pick up from there."

---

## Project

SAP TechEd 2026, Berlin, 29 October 2026.
Session TM261 – Agent-Led Test Management: Hands-on Lab with Joule in SAP Cloud ALM.
Presenters: Christina Pickhardt · Niclas Weidner · Tobias Keller · Daniel Lorenz.
Scenario: BJ5_simple – Make-to-Stock Production – Discrete Manufacturing.

---

## What exists

### Source files (edit these)
- `exercises/ex_intro/README.md` → Cover page, agenda, Introduction (Context + Chapter 0)
- `exercises/ex0/README.md` → Chapters 1–2 (Getting Started + Feed the Agents §2.1–2.2)
- `exercises/ex1/README.md` → Chapter 2 continued (§2.3 – Generate Requirements)
- `exercises/ex2/README.md` → Chapter 3 – Scope with AI
- `exercises/ex3/README.md` → Chapter 4 – Plan with AI
- `exercises/ex4/README.md` → Chapter 5 – Generate Test Cases
- `exercises/ex5/README.md` → Chapter 6 – Generate Test Data
- `exercises/ex6/README.md` → Chapter 7 – Recap & Outlook

### Generated outputs
- `_FINAL SCRIPTS/2026.10.22_TM261_script.{md,html,pdf}` — compiled session guide (written directly by generator)
- `_FINAL SCRIPTS/archive/` — previous dated versions
- `docs/index.html` — GitHub Pages version

### Key scripts
- `py _dev/generate_script.py` — compiles all READMEs into script, normalises caption numbers in-place, writes all outputs including docs/
- `header.md` (repo root) — intentionally empty; cover page now lives in ex_intro

---

## Established workflow

### Normal edit cycle
1. User edits an exercise README directly in VS Code (or Typora/Obsidian)
2. Leaves rough notes inline in `[brackets]` — these are instructions, not content
3. Comes back to Claude and says "done, please process exN"
4. Claude runs `git diff exercises/exN/README.md`, processes the notes, polishes edits
5. Claude runs `py generate_script.py` — writes directly to `_FINAL SCRIPTS/`, archives previous version, normalises caption numbers in all READMEs

### Regenerating the script
```
py _dev/generate_script.py
```
Outputs written directly to `_FINAL SCRIPTS/`. Previous files archived to `_FINAL SCRIPTS/archive/` automatically.

### Header / cover page changes
The cover page, agenda, and Introduction (Context + Chapter 0) all live in `exercises/ex_intro/README.md`.
`header.md` (repo root) is empty (intentionally) — the compiled script starts directly with ex_intro.
To change presenters, date, or agenda: edit `exercises/ex_intro/README.md`.

---

## Writing rules (non-negotiable)
- **No em-dashes (—)** anywhere in prose. Use commas, semicolons, or parentheses. N-dashes (–) only in headings.
- Workstation placeholder: always `###` (never real numbers). Screenshots use `099` as example.
- Step headings: `## N.M – Title`
- Bold labels: `**Label**: description` (colon, not dash)
- Image captions: `<p style="font-size:9pt;color:#888;margin-top:-0.5em"><em>NN – description</em></p>`
- Caption numbers: written by `generate_script.py` automatically — don't edit manually, just use any placeholder number; the generator fixes them on every run
- Numbered steps with images between them: use `**1.**`, `**2.**` bold format (not markdown `1.` lists, which restart at 1 after every image)

---

## Current state

Script: `2026.10.22_TM261_script.*` — 60,519 chars, 0 em-dash warnings, 42 images (01–42).

### Chapter status
- **ex_intro**: Complete ✓ — cover page, agenda, Context + Chapter 0 intro (2 images)
- **ex0**: Complete ✓ — Chapters 1–2 Getting Started + Feed the Agents §2.1–2.2 (15 images: 03–17)
- **ex1**: Not yet reviewed — Chapter 2 §2.3 Generate Requirements (6 images: 18–23)
- **ex2**: Not yet reviewed — Chapter 3 Scope with AI (5 images: 24–28, ex2_06 TODO placeholder)
- **ex3**: Not yet reviewed — Chapter 4 Plan with AI (6 images: 29–34)
- **ex4**: Not yet reviewed — Chapter 5 Generate Test Cases (4 images: 35–38)
- **ex5**: Not yet reviewed — Chapter 6 Generate Test Data (4 images: 39–42)
- **ex6**: Not yet reviewed — Chapter 7 Recap & Outlook (no images)

### Known outstanding items
- `ex2_06_revise_button.png` — screenshot still TODO (Select → Revise Scope button, Chapter 3 §3.5)
- GitHub Pages not yet live — requires SAP-samples org admin to enable settings/pages (source: root of main branch)
- ex1–ex6 not yet reviewed by user

---

## Scenario facts (keep consistent)
- Process: BJ5_simple – Beta_Straight Make-to-Stock Production – Discrete Manufacturing
- Backstory: company adapting standard BJ5 to their needs, custom variant called BJ5_simple, focus on role changes
- 7 user stories: BJ5_US-01 through BJ5_US-07 (system IDs 3-153 through 3-159)
- Two roles: Production Planner + Warehouse Clerk
- Four agents: Scoping, Preparation (2 phases), Test Data Management (Phase 1), Execution Management (planned)
- HITL Gate 1: scope confirmation (Chapter 3)
- HITL Gate 2: plan approval (Chapter 4)
- Test case ID format: `8-1-123` (General Information tab → Object section)
- TDM agent prompt: `"Please suggest test data for test case [ID] in project "###_TestProject""`
- Credentials shown in exercises: `tm261-###@education.cloud.sap` / `Acce$$teched26` (OK as-is)
- Tenant URL: `https://tm261-000-l2fw0ndj.eu10-004.alm.cloud.sap/launchpad`
- Screenshots use `099` as workstation placeholder

---

## Architecture decisions made this session
- `ex_intro/README.md` created as first chapter (new): contains cover page + agenda + Introduction section
- `Script staging/header.md` emptied: compiled script now starts directly from ex_intro (no separate header)
- `generate_script.py` updated: reads 8 files (ex_intro + ex0–ex6), normalises captions globally on every run, handles empty header.md gracefully
- Chapter 2 renamed from "Build Your Input" / "Generate Requirements" to **"Feed the Agents"**
- ex0_05 image removed from §1.3 (replaced by text callout)
- Compiled document = exact concatenation of exercise READMEs; no separate transforms except image path rewriting
