# decrypt_responses.py — post-session survey decryption
#
# Requirements: pip install cryptography
#
# Run from the repo root after `git pull`:
#   py -I _dev/decrypt_responses.py
#
# Output: _responses/_decrypted.csv

import base64, csv, glob, hashlib, json, sys
from pathlib import Path

# ─── CONFIG — must match survey.html ────────────────────────────────────────
PASSPHRASE = 'TM261-Berlin-2026'
SALT       = b'TM261-survey-salt-2026'
ITERATIONS = 100_000

# ─── DECRYPTION ──────────────────────────────────────────────────────────────
def derive_key():
    return hashlib.pbkdf2_hmac('sha256', PASSPHRASE.encode(), SALT, ITERATIONS, dklen=32)

def decrypt_file(path: Path) -> dict:
    from cryptography.hazmat.primitives.ciphers.aead import AESGCM
    payload = json.loads(path.read_text(encoding='utf-8'))
    iv  = base64.b64decode(payload['iv'])
    ct  = base64.b64decode(payload['data'])
    key = derive_key()
    plaintext = AESGCM(key).decrypt(iv, ct, None)
    return json.loads(plaintext)

# ─── MAIN ────────────────────────────────────────────────────────────────────
def main():
    files = sorted(Path('tm261-survey').glob('ws*.json'))
    if not files:
        print('No response files found in _responses/')
        sys.exit(0)

    rows, errors = [], []
    for f in files:
        try:
            rows.append(decrypt_file(f))
            print(f'  OK  {f.name}')
        except Exception as e:
            errors.append(f.name)
            print(f'  ERR {f.name}: {e}')

    if not rows:
        print('\nNo responses decrypted.')
        sys.exit(1)

    out = Path('_responses/_decrypted.csv')
    # Union of all keys, ws + timestamp first
    keys = ['ws', 'timestamp'] + [k for k in rows[0] if k not in ('ws', 'timestamp')]
    with open(out, 'w', newline='', encoding='utf-8-sig') as f:
        w = csv.DictWriter(f, fieldnames=keys, extrasaction='ignore')
        w.writeheader()
        w.writerows(rows)

    print(f'\n{len(rows)} responses → {out}')
    if errors:
        print(f'{len(errors)} failed: {", ".join(errors)}')

if __name__ == '__main__':
    main()
