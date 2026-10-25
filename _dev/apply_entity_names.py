import re, glob

files = sorted(glob.glob('exercises/*/README.md'))

# Protect bold, italic, code, HTML tags, markdown links from replacement
TOKEN_RE = re.compile(
    r'(\*{1,3}[^*\n]+\*{1,3}'       # *italic*, **bold**, ***bold-italic***
    r'|`[^`\n]+`'                    # `code`
    r'|<[^>\n]+>'                    # <html tags>
    r'|\[[^\]\n]*\]\([^)\n]*\)'      # [link](url)
    r')'
)

# Core entity replacements (italic + capitalize) — plural before singular
ITALIC = [
    (re.compile(r'\btest cases\b', re.I), '*Test Cases*'),
    (re.compile(r'\btest case\b',  re.I), '*Test Case*'),
    (re.compile(r'\btest plans\b', re.I), '*Test Plans*'),
    (re.compile(r'\btest plan\b',  re.I), '*Test Plan*'),
    (re.compile(r'\buser stories\b', re.I), '*User Stories*'),
    (re.compile(r'\buser story\b',   re.I), '*User Story*'),
    (re.compile(r'\bsolution processes\b', re.I), '*Solution Processes*'),
    (re.compile(r'\bsolution process\b',   re.I), '*Solution Process*'),
    (re.compile(r'\bscope items\b', re.I), '*Scope Items*'),
    (re.compile(r'\bscope item\b',  re.I), '*Scope Item*'),
    (re.compile(r'\brequirements\b', re.I), '*Requirements*'),
    (re.compile(r'\brequirement\b',  re.I), '*Requirement*'),
    (re.compile(r'\bdefects\b', re.I), '*Defects*'),
    (re.compile(r'\bdefect\b',  re.I), '*Defect*'),
]

# Capitalize-only replacements
CAP_ONLY = [
    (re.compile(r'\bacceptance criteria\b', re.I), 'Acceptance Criteria'),
    (re.compile(r'\btest steps\b',       re.I), 'Test Steps'),
    (re.compile(r'\btest step\b',        re.I), 'Test Step'),
    (re.compile(r'\btest preparation\b', re.I), 'Test Preparation'),
    (re.compile(r'\btest execution\b',   re.I), 'Test Execution'),
    (re.compile(r'\btest management\b',  re.I), 'Test Management'),
]

ALL = ITALIC + CAP_ONLY


def transform_segment(text):
    for pat, repl in ALL:
        text = pat.sub(repl, text)
    return text


def transform_line(line):
    if line.startswith('#'):            return line  # headings: skip
    if '<p style=' in line:            return line  # captions: skip
    if line.strip().startswith('<br>'): return line  # image lines: skip
    parts = TOKEN_RE.split(line)
    result = []
    for i, part in enumerate(parts):
        result.append(part if i % 2 == 1 else transform_segment(part))
    return ''.join(result)


for filepath in files:
    with open(filepath, 'r', encoding='utf-8') as f:
        lines = f.readlines()
    new_lines = [transform_line(l) for l in lines]
    if new_lines != lines:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.writelines(new_lines)
        n = sum(1 for a, b in zip(lines, new_lines) if a != b)
        print(f'Updated ({n} lines): {filepath}')
    else:
        print(f'No change: {filepath}')
