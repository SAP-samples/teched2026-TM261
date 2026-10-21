"""
TM261 Presenter Script Generator
Run with:  py generate_script.py

Reads exercise READMEs, compiles the presenter script, and writes:
  Script staging/YYYY.MM.DD_TM261_script.md
  Script staging/YYYY.MM.DD_TM261_script.html
  Script staging/YYYY.MM.DD_TM261_script.pdf

Previous versions of the same file type are archived in Script staging/archive/.
"""

import re, os, glob, shutil, subprocess
from datetime import date
import markdown as md_lib

BASE = r"C:\Users\D050168\Projects\teched2026-TM261"
STAGING = os.path.join(BASE, "Script staging")
ARCHIVE = os.path.join(STAGING, "archive")
TODAY = date.today().strftime("%Y.%m.%d")
PREFIX = f"{TODAY}_TM261_script"

EXERCISES = [
    ("ex0", "exercises/ex0/README.md"),
    ("ex1", "exercises/ex1/README.md"),
    ("ex2", "exercises/ex2/README.md"),
    ("ex3", "exercises/ex3/README.md"),
    ("ex4", "exercises/ex4/README.md"),
    ("ex5", "exercises/ex5/README.md"),
    ("ex6", "exercises/ex6/README.md"),
]

CSS = """body{font-family:'Segoe UI',Arial,sans-serif;font-size:11pt;line-height:1.5;margin:0;padding:0;color:#1a1a1a}
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
details summary{cursor:pointer;color:#0070f2}"""

CHROME = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
DOCS_DIR = os.path.join(BASE, "docs")
PAGES_BASE = "https://sap-samples.github.io/teched2026-TM261/"


def _write_pages_html(script_md):
    """Write docs/index.html for GitHub Pages (web-compatible base href)."""
    os.makedirs(DOCS_DIR, exist_ok=True)
    body = md_lib.markdown(script_md, extensions=["tables", "fenced_code", "nl2br"])
    base_href = f'<base href="{PAGES_BASE}">'
    html = (
        f'<!DOCTYPE html><html><head><meta charset="utf-8">{base_href}'
        f'<title>TM261 Script</title><style>{CSS}</style></head>'
        f'<body><div class="pw">{body}</div></body></html>'
    )
    path = os.path.join(DOCS_DIR, "index.html")
    with open(path, "w", encoding="utf-8") as f:
        f.write(html)
    print(f"  wrote: docs/index.html ({len(html):,} chars) — GitHub Pages")


def _archive_existing():
    """Move any existing dated script files to archive/."""
    os.makedirs(ARCHIVE, exist_ok=True)
    for ext in ("md", "html", "pdf"):
        for f in glob.glob(os.path.join(STAGING, f"*_TM261_script.{ext}")):
            dest = os.path.join(ARCHIVE, os.path.basename(f))
            if os.path.exists(dest):
                os.remove(dest)
            shutil.move(f, dest)
            print(f"  archived: {os.path.basename(f)}")


def _read_header():
    """Extract the header from the most recent staged script (before first '# Getting Started')."""
    candidates = sorted(glob.glob(os.path.join(ARCHIVE, "*_TM261_script.md")), reverse=True)
    if not candidates:
        raise FileNotFoundError("No previous script found in archive to read header from.")
    with open(candidates[0], encoding="utf-8") as f:
        text = f.read()
    m = re.search(r"\n# Chapter 1", text) or re.search(r"\n# Getting Started", text)
    if not m:
        raise ValueError("Header boundary '# Chapter 1' not found in previous script.")
    return text[: m.start()].rstrip() + "\n\n"


def _compile_body():
    parts = []
    for ex, rel in EXERCISES:
        path = os.path.join(BASE, rel.replace("/", os.sep))
        with open(path, encoding="utf-8") as f:
            content = f.read()
        content = re.sub(r'src="images/', f'src="exercises/{ex}/images/', content)
        content = re.sub(r"\n\*Back to \[Table of Contents\][^\n]*\n?", "", content)
        parts.append(content.strip())
    body = "\n\n---\n\n".join(parts) + "\n"
    # Globally renumber image captions so the compiled script has a single ascending sequence
    counter = [0]
    def _inc(m):
        counter[0] += 1
        return f'<em>{counter[0]:02d} – '
    body = re.sub(r'<em>\d{1,2} – ', _inc, body)
    return body


def _write_md(script_md):
    path = os.path.join(STAGING, f"{PREFIX}.md")
    with open(path, "w", encoding="utf-8") as f:
        f.write(script_md)
    size = len(script_md)
    print(f"  wrote: {PREFIX}.md ({size:,} chars)")
    return path


def _write_html(script_md):
    body = md_lib.markdown(script_md, extensions=["tables", "fenced_code", "nl2br"])
    base_href = f'<base href="file:///{BASE.replace(chr(92), "/").rstrip("/")}/">'
    html = (
        f'<!DOCTYPE html><html><head><meta charset="utf-8">{base_href}'
        f'<title>TM261 Script</title><style>{CSS}</style></head>'
        f'<body><div class="pw">{body}</div></body></html>'
    )
    path = os.path.join(STAGING, f"{PREFIX}.html")
    with open(path, "w", encoding="utf-8") as f:
        f.write(html)
    print(f"  wrote: {PREFIX}.html ({len(html):,} chars)")
    return path


def _write_pdf(html_path):
    pdf_path = os.path.join(STAGING, f"{PREFIX}.pdf")
    file_url = "file:///" + html_path.replace("\\", "/")
    result = subprocess.run(
        [
            CHROME,
            "--headless=new",
            f"--print-to-pdf={pdf_path}",
            "--print-to-pdf-no-header",
            "--no-sandbox",
            "--disable-gpu",
            file_url,
        ],
        capture_output=True,
        text=True,
    )
    if os.path.exists(pdf_path):
        size_mb = os.path.getsize(pdf_path) / 1_048_576
        print(f"  wrote: {PREFIX}.pdf ({size_mb:.2f} MB)")
    else:
        print("  ERROR: PDF not generated")
        print(result.stderr[-500:])


def main():
    print(f"\nGenerating TM261 script — {TODAY}")
    print("Archiving existing files...")
    _archive_existing()
    print("Reading header...")
    header = _read_header()
    print("Compiling exercise body...")
    body = _compile_body()
    script_md = header + body
    em_count = script_md.count("\u2014")
    if em_count:
        print(f"  WARNING: {em_count} em-dash(es) remain in compiled script")
    print("Writing outputs...")
    _write_md(script_md)
    html_path = _write_html(script_md)
    _write_pdf(html_path)
    _write_pages_html(script_md)
    print("Done.\n")


if __name__ == "__main__":
    main()
