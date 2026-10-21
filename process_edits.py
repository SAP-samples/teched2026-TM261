"""
TM261 Edit Processor
Run with:  py process_edits.py

Scans all exercise README.md files for inline editing markers, calls the
Claude API to execute them, renumbers local captions, removes markers, then
regenerates the script (generate_script.py).

Supported markers
-----------------
  <!-- EDIT: move this picture down two paragraphs -->
  <!-- EDIT: shorten this section by 30% -->
  <!-- EDIT: tone this paragraph down -->
  Any structural or textual instruction placed as an HTML comment.

  <!-- POLISH -->
  Placed after a paragraph the user edited directly. Claude refines the
  language to match the document's style without changing the substance.

Git diff review
---------------
Run with:  py process_edits.py --diff
Prints a git diff of all exercise READMEs and exits without modifying files.
Use this to review what a collaborator changed before deciding to process.

Requirements
------------
  pip install anthropic python-dotenv
  ANTHROPIC_API_KEY in environment or .env file
"""

import re
import os
import sys
import subprocess

BASE = r"C:\Users\D050168\Projects\teched2026-TM261"

EXERCISES = [
    "exercises/ex0/README.md",
    "exercises/ex1/README.md",
    "exercises/ex2/README.md",
    "exercises/ex3/README.md",
    "exercises/ex4/README.md",
    "exercises/ex5/README.md",
    "exercises/ex6/README.md",
]

STYLE_GUIDE = """You are editing a presenter script for SAP TechEd 2026 (session TM261).
Style rules:
- No em-dashes (—). Use commas, semicolons, or parentheses instead.
- N-dashes (–) only in headings.
- Second person ("you"), present tense, direct and professional.
- Step headings: ## N.M – Title
- Bold labels: **Label**: description (colon, not dash)
- Workstation placeholder is always ### (never real numbers).
- Image captions: <em>NN – Short description</em> (exercise-local numbering).
- No trailing summaries or meta-commentary. Write content only."""


def _get_client():
    try:
        from dotenv import load_dotenv
        load_dotenv(os.path.join(BASE, ".env"))
    except ImportError:
        pass
    try:
        import anthropic
    except ImportError:
        print("ERROR: anthropic package not installed. Run: pip install anthropic")
        sys.exit(1)
    key = os.environ.get("ANTHROPIC_API_KEY")
    if not key:
        print("ERROR: ANTHROPIC_API_KEY not set in environment or .env")
        sys.exit(1)
    return anthropic.Anthropic(api_key=key)


def _call_claude(client, instruction, context):
    """Send one editing instruction to Claude and return the replacement text."""
    prompt = f"""{STYLE_GUIDE}

The section to edit is between the markers below.
Instruction: {instruction}

--- BEGIN SECTION ---
{context}
--- END SECTION ---

Return only the edited section. No explanation, no markers, no preamble."""
    message = client.messages.create(
        model="claude-opus-4-5",
        max_tokens=4096,
        messages=[{"role": "user", "content": prompt}],
    )
    return message.content[0].text.strip()


def _process_edit_markers(text, client):
    """Execute <!-- EDIT: instruction --> markers.

    Each marker applies to the paragraph immediately before it.
    The marker and the paragraph are replaced by the edited paragraph.
    """
    # Pattern: paragraph text, blank line, <!-- EDIT: ... -->, blank line
    pattern = re.compile(
        r'((?:(?!<!--).)+?)\n\n<!-- EDIT: (.+?) -->',
        re.DOTALL,
    )

    def replace(m):
        section = m.group(1).strip()
        instruction = m.group(2).strip()
        print(f"  EDIT: {instruction[:60]}...")
        result = _call_claude(client, instruction, section)
        return result

    return pattern.sub(replace, text)


def _process_polish_markers(text, client):
    """Refine paragraphs marked with <!-- POLISH -->.

    The marker is placed after the paragraph to polish.
    """
    pattern = re.compile(
        r'((?:(?!<!--).)+?)\n\n<!-- POLISH -->',
        re.DOTALL,
    )

    def replace(m):
        section = m.group(1).strip()
        print(f"  POLISH: {section[:60].strip()}...")
        result = _call_claude(client, "Polish this paragraph to match the document style. Keep all facts unchanged.", section)
        return result

    return pattern.sub(replace, text)


def _renumber_captions(text):
    """Renumber <em>NN – description</em> captions sequentially (01, 02, ...)
    within a single README file, based on order of appearance."""
    counter = [0]

    def inc(m):
        counter[0] += 1
        return f'<em>{counter[0]:02d} – '

    return re.sub(r'<em>\d{1,2} – ', inc, text)


def _process_file(path, client):
    with open(path, encoding="utf-8") as f:
        original = f.read()

    text = original
    has_edits = bool(re.search(r'<!-- EDIT:', text))
    has_polish = bool(re.search(r'<!-- POLISH -->', text))

    if has_edits:
        text = _process_edit_markers(text, client)
    if has_polish:
        text = _process_polish_markers(text, client)

    # Always renumber captions in case images were moved
    text = _renumber_captions(text)

    if text != original:
        with open(path, "w", encoding="utf-8") as f:
            f.write(text)
        return True
    return False


def _show_diff():
    """Print git diff for all exercise READMEs and exit."""
    paths = [os.path.join(BASE, p.replace("/", os.sep)) for p in EXERCISES]
    result = subprocess.run(
        ["git", "diff", "--", *paths],
        capture_output=True, text=True, cwd=BASE,
    )
    if result.stdout.strip():
        print(result.stdout)
    else:
        print("No uncommitted changes in exercise READMEs.")


def main():
    if "--diff" in sys.argv:
        _show_diff()
        return

    print("\nTM261 Edit Processor")
    client = _get_client()

    changed = []
    for rel in EXERCISES:
        path = os.path.join(BASE, rel.replace("/", os.sep))
        if not os.path.exists(path):
            continue
        print(f"Scanning {rel}...")
        if _process_file(path, client):
            changed.append(rel)

    if changed:
        print(f"\nModified: {', '.join(changed)}")
        print("Regenerating script...")
        subprocess.run(["py", "generate_script.py"], cwd=BASE, check=True)
    else:
        print("\nNo markers found; no changes made.")
        print("Tip: add <!-- EDIT: instruction --> after a paragraph to trigger editing.")
        print("     add <!-- POLISH --> after a paragraph you edited directly.")
        print("     run with --diff to review collaborator changes.")

    print("Done.\n")


if __name__ == "__main__":
    main()
