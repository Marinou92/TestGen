# TestGen Lite

Find what is testable in a Next.js or React repo, then set up a minimal Vitest foundation.

This is the public lite version of TestGen.

It is designed to give you a fast win:

- scan a repo and surface the main testable targets
- show how much logic exists versus how few tests are present
- drop in a clean Vitest setup

It deliberately stops before test generation.

## What You Get

### 1. Repo Scan

Run:

```bash
python3 scripts/scan_testable.py /path/to/repo
```

You get a quick summary like:

```text
Repo: my-app
Server Actions: 4
API routes: 3
Components: 12
Existing tests: 0
Largest gap: High-value application logic exists, but no test suite is present yet.
```

### 2. Basic Vitest Setup

Copy the templates:

```bash
cp templates/vitest.config.ts /path/to/repo/vitest.config.ts
cp templates/setup.ts /path/to/repo/setup.ts
```

Then install your dependencies and wire the scripts you want in `package.json`.

## What The Lite Version Does Not Do

TestGen Lite does **not**:

- generate tests for your business logic
- generate tests for Server Actions
- generate tests for API routes
- generate tests for form components
- add Playwright flows
- add CI workflows
- add coverage automation
- include the internal reference packs and adapters used in the full version

That gap is intentional.

The lite repo helps you see the problem and get the runner in place.
The full version solves the expensive part: actually generating the useful tests.

## Lite vs Full Version

| Capability | Lite | Full |
| --- | --- | --- |
| Scan what is testable | yes | yes |
| Count actions, routes, components, tests | yes | yes |
| Basic Vitest setup | yes | yes |
| Generate app-specific tests | no | yes |
| Generate Server Action tests | no | yes |
| Generate API route tests | no | yes |
| Generate logic-heavy component tests | no | yes |
| Produce `TEST-AUDIT.md` | no | yes |
| Produce `TEST_FINDINGS.md` | no | yes |
| Coverage execution and findings | no | yes |
| Mock adapters for common stacks | no | yes |
| One-shot runner | no | yes |
| Playwright patterns | no | yes |
| CI templates | no | yes |

## Who This Is For

- developers who want to know what is testable before committing to a full test push
- teams that need a lightweight Vitest starting point
- people evaluating whether the full product would save them real time

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

## Positioning

TestGen Lite is a lead-in product, not the whole system.

Use it when you want:

- visibility on testable surface area
- a fast setup for Vitest
- a simple way to evaluate the idea

Use the full version when you want:

- the actual tests written for you
- prioritization of the highest-value targets
- bug-finding from failing tests
- a proper audit and findings workflow

## Codex Skill

`SKILL.md` is included so the repo can be used directly as a Codex skill.

The skill behavior is intentionally narrow:

- scan
- set up
- stop

No fake “AI magic”, no empty test generation, no pretending that setup equals coverage.
