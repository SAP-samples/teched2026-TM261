# Script Staging – TM261 Presenter Script

Generated outputs, incoming screenshots, and archived prior versions live here.

## Folder structure

```
Script staging/
  README.md                    ← this file
  YYYY.MM.DD_TM261_script.md   ← latest compiled script (markdown)
  YYYY.MM.DD_TM261_script.html ← latest styled HTML
  YYYY.MM.DD_TM261_script.pdf  ← latest presenter script (PDF)
  archive/                     ← older versions, automatically moved here
  Screenshots/                 ← incoming screenshots (from chat or physical drop-in)
```

## Naming convention

All generated files use the creation date as prefix: **`YYYY.MM.DD_[name]`**

Examples: `2026.10.19_TM261_script.md`, `2026.10.29_TM261_script.pdf`

## Generating the script

Every generation run produces three files unless otherwise specified:
1. `.md` — compiled Markdown (source exercises → joined script)
2. `.html` — styled HTML with SAP Blue headings and Segoe UI font
3. `.pdf` — final presenter script via Chrome headless

**Trigger:** say _"Generate the script"_ or _"Regenerate the script"_

Before writing, any existing version of the same file type automatically moves to `archive/`.

## Source of truth

Exercise content lives in `exercises/exN/README.md`; these are the files to edit:

| Steps | Exercise file |
|---|---|
| 1, 2, 3, 4, 4C | `exercises/ex0/README.md` |
| 5 | `exercises/ex1/README.md` |
| 6–10 | `exercises/ex2/README.md` |
| 11–14 | `exercises/ex3/README.md` |
| 15–18 | `exercises/ex4/README.md` |
| 19–23 | `exercises/ex5/README.md` |
| 24–26 | `exercises/ex6/README.md` |

The script header (cover page, agenda, intro sections) is preserved from the previous script and not regenerated from READMEs.

## Screenshots

**Incoming screenshots** (pasted in chat or dropped into this folder physically):
1. Saved to `Script staging/Screenshots/YYYY.MM.DD_exN_NN_description.png`
2. Also copied to `exercises/exN/images/exN_NN_description.png` for use in the README
3. README updated to reference the new image
4. Say _"Regenerate the script"_ to compile the updated output

**To replace a screenshot physically:** drop the new file into `Screenshots/` and say _"Use [filename] for step N"_.

## Step-by-step review

To review and update the script step by step:
- _"Take me through the script step by step"_ — shows each step's current content and waits for feedback
- _"Show me step N"_ — shows that specific step's current text and image list
- _"Update step N with..."_ — applies the change to the README and regenerates

## Updating the script

| Change type | What to do |
|---|---|
| Text correction | Say what to change; it gets applied to the relevant README |
| New screenshot | Paste image in chat + specify which step |
| Replace screenshot | Drop new image in `Screenshots/` + say which step to apply it to |
| Structural change (add/remove step) | Describe the change; README is updated, then regenerate |

After any change: _"Regenerate the script"_ compiles `.md`, `.html`, and `.pdf`.
