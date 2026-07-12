# Database Setup (one-time): Supabase project `famb`

The use-case-map skill can save maps to a Supabase table. This is a one-time
provisioning guide. Walk the user through it when `save_use_case.py` exits
with code 3 (credentials missing) or when they ask to set up the database.

The runtime write path never uses MCP — only the REST API with credentials
from the macOS Keychain, so saving works from any directory on the machine.

## 1. Create the project

Dashboard route: [supabase.com](https://supabase.com) → **New project** →
name `famb`, free tier, pick the closest region. Note the **Project URL**
(`https://<ref>.supabase.co`).

Alternative: if the official Supabase MCP plugin is enabled in the current
Claude Code project, Claude can create the project and run the DDL via MCP —
but this is optional and only for setup.

## 2. Create the table

Paste into **SQL Editor** → Run:

```sql
create table public.use_case_maps (
  id                 uuid primary key default gen_random_uuid(),
  slug               text not null unique,
  title              text not null,
  problem            text,
  persona            text,
  alternatives       jsonb not null default '[]'::jsonb,  -- array of strings
  why_motivation     text,
  why_differentiator text,
  frequency          text,
  frequency_zone     text check (frequency_zone in ('habit', 'forgettable')),
  risks              text,
  evidence           text,
  content_md         text not null,      -- full raw markdown document
  created_at         timestamptz not null default now(),
  updated_at         timestamptz not null default now()
);

-- keep updated_at fresh on upsert-updates
create extension if not exists moddatetime with schema extensions;
create trigger set_updated_at
  before update on public.use_case_maps
  for each row execute procedure extensions.moddatetime(updated_at);

-- RLS on, zero policies: the publishable/anon key can do NOTHING;
-- the sb_secret key bypasses RLS. This is intentional — do not add policies.
alter table public.use_case_maps enable row level security;
```

## 3. Get the secret key

**Project Settings → API Keys** → reveal (or create) a **secret key**
(`sb_secret_...`). Do not use the publishable key.

## 4. Store credentials in the macOS Keychain

The user must run these **themselves in their own terminal** so the key never
appears in the Claude Code transcript. Never ask the user to paste the key
into the chat:

```sh
security add-generic-password -U -a famb -s discovery-supabase-url \
  -w 'https://<ref>.supabase.co'

security add-generic-password -U -a famb -s discovery-supabase-secret-key \
  -w 'sb_secret_...'
```

(`-U` updates the item if it already exists, so re-running after key rotation
just works.)

For testing or non-macOS machines, the environment variables
`SUPABASE_FAMB_URL` and `SUPABASE_FAMB_SECRET_KEY` override the Keychain.

## 5. Verify

Claude can run this from any directory:

```sh
python3 <skill-dir>/scripts/save_use_case.py --check
# → OK: credentials found, table reachable (...)
```

## 6. Rotation / teardown

- After rotating the key in the dashboard: re-run the `add-generic-password -U`
  command with the new value.
- To remove credentials:
  `security delete-generic-password -s discovery-supabase-url` and
  `security delete-generic-password -s discovery-supabase-secret-key`.
