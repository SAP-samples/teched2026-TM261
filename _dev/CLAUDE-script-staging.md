# TM261 Presenter Script – AI Instructions

## Project overview

**Session:** TM261 – Agent-Led Test Management: Hands-on Lab with Joule in SAP Cloud ALM  
**Date:** Wednesday, 28 October 2026 · SAP TechEd 2026, Berlin  
**Presenters:** Christina Pickhardt · Niclas Weidner · Tobias Keller · Daniel Lorenz  
**Scenario:** BJ5_simple – Make-to-Stock Production – Discrete Manufacturing

See `HANDOVER.md` for the human-readable workflow guide.

---

## Script generation – technical reference

### Source of truth

- **Exercise READMEs:** `exercises/ex_intro/README.md` + `exercises/ex0–ex6/README.md` (edit these directly)
- **Header:** `header.md` (repo root) — intentionally empty; cover page and intro live in `exercises/ex_intro/README.md`
- **Exercise images:** `exercises/exN/images/` (including `exercises/ex_intro/images/`)

### Step index

| Chapter | Steps | File |
|---|---|---|
| Introduction | Cover page, agenda, Context + Chapter 0 | `exercises/ex_intro/README.md` |
| Chapter 1 – Getting Started | 1.1–1.3 | `exercises/ex0/README.md` |
| Chapter 2 – Feed the Agents | 2.1–2.2 | `exercises/ex0/README.md` (continued) |
| Chapter 2 – Feed the Agents | 2.3 | `exercises/ex1/README.md` |
| Chapter 3 – Scope with AI | 3.1–3.5 | `exercises/ex2/README.md` |
| Chapter 4 – Plan with AI | 4.1–4.4 | `exercises/ex3/README.md` |
| Chapter 5 – Generate Test Cases | 5.1–5.4 | `exercises/ex4/README.md` |
| Chapter 6 – Generate Test Data | 6.1–6.5 | `exercises/ex5/README.md` |
| Chapter 7 – Recap & Outlook | 7.1–7.3 | `exercises/ex6/README.md` |

### Output rules

- All generated files go to `_FINAL SCRIPTS/` with prefix `YYYY.MM.DD_`
- Existing files of the same name are archived to `_FINAL SCRIPTS/archive/` before writing
- Always generate all three formats (.md, .html, .pdf) unless user specifies otherwise
- Use `generate_script.py` — run with: `py _dev/generate_script.py`

### HTML base href

The HTML file lives in `_FINAL SCRIPTS/` but references images relative to the repo root.
Always include this tag in `<head>`:
```html
<base href="file:///C:/Users/D050168/Projects/teched2026-TM261/">
```
This makes all relative paths (`exercises/exN/images/...`) resolve correctly for both browser preview and Chrome headless PDF generation.

### CSS style (embed in `<style>`)

```css
body{font-family:'Segoe UI',Arial,sans-serif;font-size:11pt;line-height:1.5;margin:0;padding:0;color:#1a1a1a}
.pw{max-width:900px;margin:0 auto;padding:20mm}
h1{color:#0070f2;font-size:18pt;page-break-before:always;margin-top:0}
h1:first-of-type{page-break-before:avoid}
h2{color:#0057b8;font-size:13pt;margin-top:1.8em}
h3{color:#333;font-size:11pt;margin-top:1.4em}
table{border-collapse:collapse;width:100%;margin:1em 0;font-size:10pt}
th{background:#0070f2;color:#fff;padding:6px 10px;text-align:left}
td{padding:5px 10px;border-bottom:1px solid #ddd;vertical-align:top}
tr:nth-child(even) td{background:#f5f9ff}
img{max-width:100%;height:auto;display:block;margin:1em 0;border:1px solid #ddd;border-radius:4px}
blockquote{border-left:4px solid #0070f2;margin:1em 0;padding:.5em 1em;background:#f0f6ff;color:#333}
code{background:#f4f4f4;padding:1px 4px;border-radius:3px;font-size:9.5pt}
pre{background:#f4f4f4;padding:1em;border-radius:4px;overflow-x:auto}
hr{border:none;border-top:1px solid #ccc;margin:2em 0}
details summary{cursor:pointer;color:#0070f2}
```

### Chrome headless PDF command

```
"C:/Program Files/Google/Chrome/Application/chrome.exe" --headless=new --print-to-pdf="C:/Users/D050168/Projects/teched2026-TM261/_FINAL SCRIPTS/YYYY.MM.DD_TM261_script.pdf" --print-to-pdf-no-header --no-sandbox --disable-gpu "file:///C:/Users/D050168/Projects/teched2026-TM261/_FINAL SCRIPTS/YYYY.MM.DD_TM261_script.html"
```

---

## Screenshots workflow

When the user pastes a screenshot in chat or names a file in `Prep & Material/Screenshots/`:
1. Save/move to `Prep & Material/Screenshots/YYYY.MM.DD_exN_NN_descriptive_name.png`
2. Copy to `exercises/exN/images/exN_NN_descriptive_name.png`
3. Update the corresponding step in `exercises/exN/README.md`
4. Regenerate the script

Image tag format in READMEs (main-flow screenshots, always inline):
```html
<br><img src="images/exN_NN_descriptive_name.png" />
```

Supplementary/optional screenshots (collapsible):
```html
<details>
    <summary>📷 View screenshot</summary>
    <br><img src="images/exN_NN_descriptive_name.png" />
</details>
```

---

## Screenshot dimensions

Target viewport: **1440×900 px**. Actual captured size will be ~1481×903 due to browser chrome — this is expected and consistent. Do not resize or crop screenshots.

## Writing conventions

- **Workstation ID placeholder:** always `###` (never real numbers)
- **Credentials shown in README:** `tm261-###@education.cloud.sap` / `Acce$$teched26` (OK as-is)
- **Step headings:** n-dash: `## N.M – Title`
- **List labels:** colon, not dash: `- **Label**: description`
- **No em-dashes anywhere:** use n-dash in headings, commas/semicolons in prose
- **Image naming:** `exN_NN_descriptive_name.png` (exercise prefix + step number + description)
- **Image paths in README:** relative from README: `images/exN_NN_foo.png`
- **Image paths in compiled script:** `exercises/exN/images/exN_NN_foo.png` (rewritten at compile time)
- **Numbered steps with images between them:** use `**1.**`, `**2.**` bold format (not `1.` markdown lists, which restart after images)
- **Caption numbers:** written by `generate_script.py` automatically — don't edit manually
