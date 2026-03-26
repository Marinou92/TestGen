# TestGen Lite

See what is testable in a Next.js or React repo, then install a minimal Vitest foundation.

TestGen Lite is the public, free version of TestGen.

It helps you answer two questions fast:

1. What in this repo is actually worth testing?
2. How do I get a clean Vitest setup in place without overengineering it?

It stops there on purpose.

The paid version is the one that generates the actual tests.

## What It Does

- scans a repo and counts obvious test targets
- surfaces the biggest testing gap in plain language
- gives you a minimal Vitest config
- gives you a basic setup file for RTL, `fetch`, and test env defaults

## What It Does Not Do

- generate tests
- generate Server Action tests
- generate API route tests
- generate form component tests
- add Playwright
- add CI workflows
- run coverage
- ship the internal reference files and adapters from the full product

That gap is the product boundary.

## Quick Example

Run:

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

That is enough to tell you whether the repo is:

- basically untested
- already partially covered
- worth pushing into a full test-generation workflow

## Installation

You can use this repo in three ways.

### 1. Manual Use

Clone the repo:

```bash
git clone https://github.com/Marinou92/TestGen.git
cd TestGen
```

Run the scanner:

```bash
python3 scripts/scan_testable.py /path/to/your/repo
```

Copy the templates:

```bash
cp templates/vitest.config.ts /path/to/your/repo/vitest.config.ts
cp templates/setup.ts /path/to/your/repo/setup.ts
```

Install a minimal dependency set in your project.

For `npm`:

```bash
npm install -D vitest @testing-library/react @testing-library/jest-dom jsdom
```

For `pnpm`:

```bash
pnpm add -D vitest @testing-library/react @testing-library/jest-dom jsdom
```

For `yarn`:

```bash
yarn add -D vitest @testing-library/react @testing-library/jest-dom jsdom
```

Then add scripts in `package.json`:

```json
{
  "scripts": {
    "test": "vitest",
    "test:run": "vitest --run"
  }
}
```

### 2. Use With Codex

`SKILL.md` is included so this repo can be used directly as a Codex skill.

Typical prompt:

```text
Use the TestGen Lite skill in this repo to scan my codebase and set up Vitest, but do not generate tests.
```

### 3. Use With Other AI Coding Tools

Even if your tool does not support `SKILL.md`, the repo is still usable.

The scanner and templates are tool-agnostic.

You can ask any coding agent something like:

```text
Use this repository as guidance. Run scripts/scan_testable.py on my repo, summarize what is testable, then copy templates/vitest.config.ts and templates/setup.ts into my project without generating tests.
```

This works with:

- Codex
- Claude Code
- ChatGPT coding sessions
- Cursor or similar agent workflows
- manual developer use

## Suggested Setup Flow

1. Run the scanner.
2. Check whether the repo has a meaningful amount of testable logic.
3. Copy the Vitest templates.
4. Install the minimum dependencies.
5. Stop.

If you now want the tests written for you, that is the handoff point to the full product.

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

## Who This Is For

- developers who want quick visibility on testable surface area
- teams that want a lightweight Vitest setup without buying into a full framework
- buyers evaluating whether the full version would save them enough time

## Positioning

TestGen Lite is intentionally useful, but incomplete.

It gives you:

- visibility
- setup
- momentum

It does not give you:

- the real test-writing work
- prioritized coverage expansion
- bug-finding via generated failing tests
- structured audit and findings outputs

That is what the full version is for.

## Why The Repo Is Minimal

There is no fake “AI magic” here.

This repo does not pretend that:

- setup equals coverage
- counting files equals testing
- a template equals a finished QA workflow

It gives you the smallest honest slice of the product.
