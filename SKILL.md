---
name: testgen
description: Scan a Next.js or React repository to identify what is testable and install a minimal Vitest foundation. Use when Codex needs to count server actions, API routes, components, and existing tests, then add a basic Vitest config and setup file without generating application-specific tests.
---

# TestGen Lite

Scan the repo first, then install the smallest useful Vitest setup. Stop there.

## Workflow

1. Scan the repo.
- Run `scripts/scan_testable.py <repo-path>`.
- Report how many server actions, API routes, components, and test files were detected.
- Call out the biggest coverage gap in plain language.

2. Add the setup only.
- Copy `templates/vitest.config.ts` into the repo and adapt aliases if needed.
- Copy `templates/setup.ts` into the repo and adjust only the mocks the repo actually needs.
- Add the smallest dependency set required for Vitest plus React Testing Library.

3. Stop at the foundation.
- Do not generate application-specific tests.
- Do not add Playwright, CI workflows, reference pattern packs, or coverage gates.
- Hand off real test generation to the paid version.

## Deliverables

- repo scan summary
- `vitest.config.ts`
- `setup.ts`
- package scripts if needed

## Constraints

- Keep the setup minimal and readable.
- Prefer Vitest for modern Next.js and React repos.
- Do not pretend the repo has coverage just because the runner is installed.
