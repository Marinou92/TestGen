# TestGen Lite

Scan your codebase, see what is testable, and set up a minimal Vitest foundation.

This public version is intentionally limited.

It helps you:

- scan a Next.js or React repo
- count Server Actions, API routes, components, and existing tests
- identify the biggest testing gap
- install a basic Vitest config and setup file

It does **not**:

- generate tests
- ship test patterns or reference files
- add Playwright flows
- add CI workflows
- run coverage checks

That gap is deliberate. The paid version generates the actual tests.

## Repo Structure

```text
testgen/
├── SKILL.md
├── scripts/
│   └── scan_testable.py
├── templates/
│   ├── vitest.config.ts
│   └── setup.ts
├── README.md
└── LICENSE
```

## What The Lite Version Does

Run the scanner:

```bash
python3 scripts/scan_testable.py /path/to/repo
```

Example output:

```text
Repo: my-app
Server Actions: 4
API routes: 3
Components: 12
Existing tests: 0
Largest gap: High-value application logic exists, but no test suite is present yet.
```

Then copy the templates into your repo:

```bash
cp templates/vitest.config.ts /path/to/repo/vitest.config.ts
cp templates/setup.ts /path/to/repo/setup.ts
```

Install your test dependencies and wire scripts in `package.json`.

## Who This Is For

- developers who want quick visibility on what is testable
- teams that need a lightweight starting point for Vitest
- people evaluating the paid version before buying

## What To Expect

This repo is a teaser, not the full product.

You will know:

- what is testable
- where the main gaps are
- how to get the runner in place

You will still need to write the actual tests yourself.
