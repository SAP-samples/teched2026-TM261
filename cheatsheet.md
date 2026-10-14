# TechEd Hands-On Recorder — Cheatsheet

## Overall Flow

| Step | Who | Command |
|------|-----|---------|
| 1. Start recording | Claude runs | `hands-on-record ex0` |
| 2. Navigate & click through exercise | You, in the browser | — |
| 3. Quit & save | You, in terminal UI | `q` |
| 4. Generate screenshots | Claude runs | `hands-on-capture ex0` |
| 5. Write README | Claude | — |
| 6. Commit | Claude runs | `git commit` |

---

## While Recording — Keyboard Shortcuts

| Key | What it does |
|-----|-------------|
| `g` | Go to a URL (type address, browser navigates + logs in) |
| `c` | Record a click (then click the element in the browser) |
| `f` | Fill a text field (pick field, type value) |
| `s` | Take a screenshot + add annotation bubble |
| `w` | Wait / pause for N seconds |
| `z` | Undo last step |
| `e` | Jump to a step / edit it |
| `q` | **Quit and save** |
| `Esc` | Cancel current operation |

---

## Fixing Mistakes

| Situation | Command |
|-----------|---------|
| Undo last step (during recording) | `z` |
| Resume a recording you quit | `hands-on-record --resume ex0` |
| Resume from a specific step | `hands-on-record --resume --step 3 ex0` |
| Redo all screenshots (no re-recording) | `hands-on-capture ex0` |

---

## Tips

- After each action, the UI asks **"Screenshot here?"** — say yes for steps participants need to see, no for in-between steps
- Login happens **automatically** via your `.env` credentials — no need to record login steps
- `recording.json` is saved after **every step** — safe to quit anytime
