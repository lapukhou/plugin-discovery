#!/usr/bin/env python3
"""
save_use_case.py — upsert a Use Case Map into the Supabase `use_case_maps` table.

Usage:
    python3 save_use_case.py --payload payload.json   # read payload from file
    python3 save_use_case.py < payload.json           # or from stdin
    python3 save_use_case.py --check                  # verify creds + table reachable

Payload: a single JSON object. The script does NOT parse markdown — the
caller composes all fields.
    Required: slug, title, content_md
    Optional: problem, persona, alternatives (array of strings),
              why_motivation, why_differentiator, frequency,
              frequency_zone ("habit" | "forgettable" | null),
              risks, evidence

Credential resolution order:
    1. env SUPABASE_FAMB_URL / SUPABASE_FAMB_SECRET_KEY
    2. macOS Keychain items `discovery-supabase-url` / `discovery-supabase-secret-key`

Stdout on success is pure JSON (id, slug, created_at, updated_at); all
diagnostics go to stderr.

Exit codes: 0 ok · 1 HTTP/network error · 2 invalid payload · 3 credentials missing
"""
import argparse
import json
import os
import subprocess
import sys
import urllib.error
import urllib.request

TABLE = 'use_case_maps'
REQUIRED = ('slug', 'title', 'content_md')
OPTIONAL = ('problem', 'persona', 'alternatives', 'why_motivation',
            'why_differentiator', 'frequency', 'frequency_zone', 'risks', 'evidence')

SETUP_HINT = """Supabase credentials not found. Store them in the macOS Keychain
(run these yourself in your own terminal, so the key never enters a transcript):

  security add-generic-password -U -a famb -s discovery-supabase-url \\
    -w 'https://<project-ref>.supabase.co'
  security add-generic-password -U -a famb -s discovery-supabase-secret-key \\
    -w 'sb_secret_...'

The secret key is in the Supabase dashboard: Project Settings -> API Keys.
Env vars SUPABASE_FAMB_URL / SUPABASE_FAMB_SECRET_KEY override the Keychain."""


def keychain_read(service):
    try:
        out = subprocess.run(
            ['security', 'find-generic-password', '-s', service, '-w'],
            capture_output=True, text=True, timeout=15)
    except (FileNotFoundError, subprocess.TimeoutExpired):
        return None
    return out.stdout.strip() if out.returncode == 0 else None


def resolve_credentials():
    url = os.environ.get('SUPABASE_FAMB_URL') or keychain_read('discovery-supabase-url')
    key = os.environ.get('SUPABASE_FAMB_SECRET_KEY') or keychain_read('discovery-supabase-secret-key')
    if not url or not key:
        print(f'❌ {SETUP_HINT}', file=sys.stderr)
        sys.exit(3)
    return url.rstrip('/'), key


def request(url, key, method, path, body=None, extra_headers=None):
    headers = {
        'apikey': key,
        'Authorization': f'Bearer {key}',
        'Content-Type': 'application/json',
    }
    headers.update(extra_headers or {})
    data = json.dumps(body).encode() if body is not None else None
    req = urllib.request.Request(f'{url}{path}', data=data, headers=headers, method=method)
    try:
        with urllib.request.urlopen(req, timeout=30) as r:
            raw = r.read()
            return json.loads(raw) if raw else None
    except urllib.error.HTTPError as e:
        print(f'❌ HTTP {e.code} from PostgREST:\n{e.read().decode("utf-8", errors="replace")}',
              file=sys.stderr)
        sys.exit(1)
    except urllib.error.URLError as e:
        print(f'❌ Network error: {e.reason}', file=sys.stderr)
        sys.exit(1)


def check(url, key):
    rows = request(url, key, 'GET', f'/rest/v1/{TABLE}?select=id&limit=1')
    n = 'at least 1' if rows else '0'
    print(f'OK: credentials found, table reachable ({n} known row(s))')


def validate(payload):
    if not isinstance(payload, dict):
        print('❌ Payload must be a JSON object', file=sys.stderr)
        sys.exit(2)
    missing = [f for f in REQUIRED if not payload.get(f)]
    if missing:
        print(f'❌ Payload is missing required field(s): {", ".join(missing)}', file=sys.stderr)
        sys.exit(2)
    unknown = [f for f in payload if f not in REQUIRED + OPTIONAL]
    if unknown:
        print(f'❌ Unknown payload field(s): {", ".join(unknown)}', file=sys.stderr)
        sys.exit(2)
    alts = payload.get('alternatives')
    if alts is not None and (not isinstance(alts, list) or
                             not all(isinstance(a, str) for a in alts)):
        print('❌ "alternatives" must be an array of strings', file=sys.stderr)
        sys.exit(2)


def save(url, key, payload):
    rows = request(
        url, key, 'POST', f'/rest/v1/{TABLE}?on_conflict=slug', body=payload,
        extra_headers={'Prefer': 'resolution=merge-duplicates,return=representation'})
    row = rows[0]
    print(json.dumps({k: row.get(k) for k in ('id', 'slug', 'created_at', 'updated_at')},
                     indent=2))


def main():
    p = argparse.ArgumentParser(description=__doc__,
                                formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument('--payload', default=None, help='Path to payload JSON file (default: stdin)')
    p.add_argument('--check', action='store_true',
                   help='Verify credentials and table reachability, then exit')
    args = p.parse_args()

    url, key = resolve_credentials()

    if args.check:
        check(url, key)
        return

    try:
        if args.payload:
            with open(args.payload, encoding='utf-8') as f:
                payload = json.load(f)
        else:
            payload = json.load(sys.stdin)
    except (OSError, json.JSONDecodeError) as e:
        print(f'❌ Cannot read payload: {e}', file=sys.stderr)
        sys.exit(2)

    validate(payload)
    save(url, key, payload)


if __name__ == '__main__':
    main()
