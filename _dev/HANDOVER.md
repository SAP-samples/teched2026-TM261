# TM261 Session Handover

Use this file to brief a new Claude Code session. Say: "read _dev/HANDOVER.md and pick up from there."

---

## Project

SAP TechEd 2026, Berlin, 28 October 2026.
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

---

## Established workflow

### Normal edit cycle
1. User edits an exercise README directly in VS Code (or Typora/Obsidian)
2. Leaves rough notes inline in `[brackets]` — these are instructions, not content
3. Comes back to Claude and says "done, please process exN"
4. Claude runs `git diff exercises/exN/README.md`, processes the notes, polishes edits
5. Claude runs `py _dev/generate_script.py` — writes directly to `_FINAL SCRIPTS/`, archives previous version, normalises caption numbers in all READMEs

### Regenerating the script
```
py _dev/generate_script.py
```
Outputs written directly to `_FINAL SCRIPTS/`. Previous files archived to `_FINAL SCRIPTS/archive/` automatically.

### Cover page / intro changes
The cover page, agenda, and Introduction (Context + Chapter 0) all live in `exercises/ex_intro/README.md`.
The compiled script starts directly from ex_intro — no separate header file.
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
- No third-level headers (###) inside exercise sections — use `**N.**` bold step numbering instead

---

## Current state

Script: `2026.10.22_TM261_script.*` — 60,498 chars, 0 em-dash warnings, 41 images (01–41).

### Chapter status
- **ex_intro**: Complete ✓ — cover page, agenda, Context + Chapter 0 intro (2 images: 01–02)
- **ex0**: Complete ✓ — Chapters 1–2 Getting Started + Feed the Agents §2.1–2.2 (15 images: 03–17)
- **ex1**: Complete ✓ — Chapter 2 §2.3 Generate Requirements (6 images: 18–23)
- **ex2**: Complete ✓ — Chapter 3 Scope with AI (4 images: 24–27)
- **ex3**: Not yet reviewed — Chapter 4 Plan with AI (6 images: 28–33)
- **ex4**: Not yet reviewed — Chapter 5 Generate Test Cases (4 images: 34–37)
- **ex5**: Not yet reviewed — Chapter 6 Generate Test Data (4 images: 38–41)
- **ex6**: Not yet reviewed — Chapter 7 Recap & Outlook (no images)

### Known outstanding items
- GitHub Pages not yet live — requires SAP-samples org admin to enable settings/pages (source: root of main branch)
- ex3–ex6 not yet reviewed by user
- Root `images/` folder still contains the two intro images (`intro_7_assistants.png`, `intro_agent_architecture.png`) — originals; the canonical copies are now in `exercises/ex_intro/images/`. Root copies can be deleted once confirmed redundant.

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

## Architecture decisions (this project)
- `ex_intro/README.md` is the first chapter: cover page + agenda + Introduction (Context + Chapter 0)
- Compiled script = exact concatenation of exercise READMEs; no separate header; only image path rewriting at compile time
- `generate_script.py` normalises captions globally on every run, writing numbers back into all READMEs
- All dev files live in `_dev/` (generator, HANDOVER, CLAUDE instructions); repo root is clean
- Generator writes directly to `_FINAL SCRIPTS/` — no manual copy step
- ex_intro images in `exercises/ex_intro/images/` (not root `images/`)
- ex2_06 placeholder screenshot dropped; §3.5 Option 1 described without screenshot
- Chapter 2 renamed "Feed the Agents"; no ### sub-headings in any exercise (dissolved to bold steps)
