# TestGen Lite

Scan your repo, see what is testable, and install a minimal Vitest foundation.

**TestGen Lite is free on GitHub.**  
It helps you understand your testing surface and get the runner in place.

**TestGen Full is available on Gumroad for $39:**  
[marinedep.gumroad.com/l/testgen](https://marinedep.gumroad.com/l/testgen)

The public version is intentionally limited.
It shows you what is testable and gets Vitest running.
It does **not** generate the actual tests.

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

That alone tells you whether the repo is:

- basically untested
- partially covered
- worth pushing into a full test-generation workflow

## Installation

### Manual

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

Install the minimum dependencies.

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

Add scripts in `package.json`:

```json
{
  "scripts": {
    "test": "vitest",
    "test:watch": "vitest",
    "test:run": "vitest --run",
    "test:coverage": "vitest --coverage"
  }
}
```

### With AI Coding Tools

This repo is not only for Codex.

`SKILL.md` is included for Codex-style skill workflows, but the scanner and templates are tool-agnostic.

You can use it with:

- Codex
- Claude Code
- ChatGPT coding sessions
- Cursor-style agent workflows
- manual developer setup

Example prompt:

```text
Use this repository as guidance. Run scripts/scan_testable.py on my repo, summarize what is testable, then copy templates/vitest.config.ts and templates/setup.ts into my project without generating tests.
```

## What TestGen Lite Includes

### TestGen Lite (free — GitHub)

| Feature | Description |
| --- | --- |
| Framework detection | Identifies Next.js, React, Vite, Express, and the router style when obvious from the codebase |
| Stack detection | Detects Supabase, Prisma, NextAuth, Stripe, React Query, and Zustand from dependencies and imports |
| Test runner detection | Checks whether Vitest, Jest, Playwright, or another runner is already present |
| Scan of testable targets | Counts and categorizes Server Actions, API routes, utils, components, and middleware-like files |
| Priority scoring | Labels target categories as high, medium, or low priority based on risk and structure |
| Critical path detection | Flags likely auth, payment, and CRUD flows in the codebase |
| Automatic Vitest setup | Ships a starter `vitest.config.ts` adapted for modern frontend repos |
| Basic mock setup | Ships a starter `setup.ts` with `fetch`, RTL, and test env defaults |
| Package script guidance | Gives you the scripts to add for `test`, `test:watch`, and `test:coverage` |

## What TestGen Lite Does Not Include

TestGen Lite does **not**:

- generate tests
- generate Server Action tests
- generate API route tests
- generate component tests
- add Playwright
- add CI workflows
- execute coverage and findings flows
- ship the internal reference files and adapters from the full version

That gap is deliberate.

Lite gives you visibility and setup.
Full gives you the actual QA acceleration.

## TestGen Full ($39 — Gumroad)

Get it here: [marinedep.gumroad.com/l/testgen](https://marinedep.gumroad.com/l/testgen)

Everything in Lite, plus:

### Audit

| Feature | Description |
| --- | --- |
| `TEST-AUDIT.md` | Full audit of repo layout, package manager, test stack, and recommendations |
| Top 5 scored targets | The 5 highest-value files or modules to test next, ranked with reasoning |
| Boundary mapping | Identifies system boundaries such as external APIs, DB, auth, and required mocks |
| Stack recommendations | Suggests the right testing stack for the project: Vitest vs Jest, MSW vs manual mocks, and more |

### Generation — Utilities

| Feature | Description |
| --- | --- |
| Pure function tests | Valid input, edge cases, invalid input, and return contract coverage |
| Zod validator tests | Verifies schemas accept valid input and reject bad input cleanly |
| Custom hook tests | Uses `renderHook` and checks state changes plus side effects |

### Generation — Server Actions

| Feature | Description |
| --- | --- |
| Auth checks | Verifies unauthenticated users are rejected and the mutation is not executed |
| Input validation | Verifies invalid input returns a structured error instead of crashing |
| Happy path | Verifies valid input plus auth executes the mutation and calls revalidation |
| Error handling | Verifies DB or dependency failures are caught and returned cleanly |

### Generation — API Route Handlers

| Feature | Description |
| --- | --- |
| Unsupported method test | `GET` on a `POST`-only endpoint should return `405` |
| Missing auth test | Request without session should return `401` |
| Invalid input test | Malformed body should return `400` with a useful message |
| Happy path test | Valid request should return `200` with the correct payload |
| Error handling test | Server error should return `500` with a safe message and no stack trace |

### Generation — Components

| Feature | Description |
| --- | --- |
| Form tests | Submit, client validation, loading state, and error display |
| Conditional rendering tests | Verifies loading, error, empty, and data branches |
| Data-driven component tests | Verifies behavior with mocked data and boundary conditions |
| Skip visual-only components | Avoids wasting time on components with no meaningful logic |

### Generation — E2E (optional)

| Feature | Description |
| --- | --- |
| Playwright config | Generates a `playwright.config.ts` adapted to the repo |
| Auth flow | `signup -> login -> dashboard -> logout` |
| CRUD flow | `create -> list -> edit -> delete` |
| Payment flow | `checkout -> confirmation` with Stripe-aware mocking strategy |

### Adapters

| Feature | Description |
| --- | --- |
| App Router (Next.js 15+) | Mocks `cookies()`, `headers()`, `redirect()`, `notFound()`, and `revalidatePath()` |
| Supabase | Mocks server and browser clients, `auth.getUser()`, and common query chains |
| NextAuth | Mocks `getServerSession()` and `useSession()` |
| Prisma | Mocks the Prisma client with reusable factory-style patterns |
| Stripe | Mocks `constructEvent()` for webhooks and checkout session creation |
| React Query | Ships patterns for `useQuery` and `useMutation` with a `QueryClientProvider` wrapper |
| Zustand | Ships isolated store mocking patterns with `createStore()` |

### Execution

| Feature | Description |
| --- | --- |
| One-shot runner | `run_full_testgen.py` runs scan, audit, execute, and report in one command |
| Vitest execution | Runs generated tests and captures the results |
| Playwright execution | Runs E2E tests when requested |

### Diagnostic

| Feature | Description |
| --- | --- |
| `TEST_FINDINGS.md` | Post-execution report with structured results |
| Pass/fail count | Counts what passed vs failed |
| Probable product bugs | Flags tests that failed because the code likely has a real bug |
| Infra and mock gaps | Identifies missing or misconfigured mocks and harness issues |
| Coverage notes | Summarizes likely coverage by category: actions, routes, utils, components |

### CI/CD

| Feature | Description |
| --- | --- |
| GitHub Actions workflow | Ships a ready-to-use `test.yml` for PR validation |

### References

| File | Description |
| --- | --- |
| `unit-patterns.md` | Unit-testing patterns and framework-specific examples |
| `integration-patterns.md` | API route, Server Action, and webhook testing patterns |
| `e2e-patterns.md` | Playwright patterns for hydration, auth, and navigation |
| `test-antipatterns.md` | Common AI-generated testing mistakes to avoid |

## Lite vs Full, In One Sentence

- **Lite** tells you what is testable and sets up Vitest.
- **Full** writes the tests, runs them, and tells you what broke.

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

## Why This Repo Is Minimal

This repo does not pretend that:

- setup equals coverage
- counting files equals testing
- a config template equals a QA workflow

It gives you the smallest honest slice of the product.

If you want the real leverage, the full version is here:

[marinedep.gumroad.com/l/testgen](https://marinedep.gumroad.com/l/testgen)
