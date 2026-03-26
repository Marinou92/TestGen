#!/usr/bin/env python3
from __future__ import annotations

import argparse
import os
import re
from pathlib import Path

IGNORED_DIRS = {
    ".git",
    ".next",
    "build",
    "coverage",
    "dist",
    "node_modules",
    "out",
}

CODE_SUFFIXES = {".js", ".jsx", ".ts", ".tsx", ".mjs", ".cjs"}


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Scan a repo and report what looks testable."
    )
    parser.add_argument("repo", help="Path to the repository to scan.")
    return parser.parse_args()


def walk_files(root: Path) -> list[Path]:
    files: list[Path] = []

    for current_root, dirs, filenames in os.walk(root):
        dirs[:] = [name for name in dirs if name not in IGNORED_DIRS]

        for filename in filenames:
            files.append(Path(current_root) / filename)

    return files


def read_text(path: Path) -> str:
    try:
        return path.read_text(encoding="utf-8")
    except UnicodeDecodeError:
        return path.read_text(encoding="utf-8", errors="ignore")
    except OSError:
        return ""


def relative(path: Path, root: Path) -> str:
    return path.relative_to(root).as_posix()


def is_test_file(path: str) -> bool:
    return bool(re.search(r"(\.test\.|\.(spec)\.)", path))


def count_server_actions(files: list[Path], root: Path) -> int:
    count = 0
    for path in files:
        if path.suffix not in CODE_SUFFIXES:
            continue
        text = read_text(path).lower()
        rel = relative(path, root)
        if "/actions/" in rel or "'use server'" in text or '"use server"' in text:
            count += 1
    return count


def count_api_routes(files: list[Path], root: Path) -> int:
    count = 0
    for path in files:
        if path.name.startswith("route.") and "/api/" in relative(path, root):
            count += 1
    return count


def count_components(files: list[Path], root: Path) -> int:
    count = 0
    for path in files:
        if path.suffix not in CODE_SUFFIXES:
            continue
        rel = relative(path, root)
        if "/components/" not in rel:
            continue
        text = read_text(path)
        if "<" in text and ("export function" in text or "export default function" in text):
            count += 1
    return count


def count_tests(files: list[Path], root: Path) -> int:
    return sum(1 for path in files if is_test_file(relative(path, root)))


def largest_gap(server_actions: int, api_routes: int, components: int, tests: int) -> str:
    total_targets = server_actions + api_routes + components

    if total_targets == 0:
        return "No obvious test targets were detected. This repo may be too small or use an unusual structure."

    if tests == 0:
        return "High-value application logic exists, but no test suite is present yet."

    if tests < max(3, total_targets // 3):
        return "Some tests exist, but coverage is likely far behind the amount of testable application logic."

    return "The repo has both testable logic and existing tests, so the next step is prioritization rather than setup."


def main() -> int:
    args = parse_args()
    root = Path(args.repo).expanduser().resolve()

    if not root.exists():
        raise SystemExit(f"Repo path does not exist: {root}")

    files = walk_files(root)
    server_actions = count_server_actions(files, root)
    api_routes = count_api_routes(files, root)
    components = count_components(files, root)
    tests = count_tests(files, root)

    print(f"Repo: {root.name}")
    print(f"Server Actions: {server_actions}")
    print(f"API routes: {api_routes}")
    print(f"Components: {components}")
    print(f"Existing tests: {tests}")
    print(f"Largest gap: {largest_gap(server_actions, api_routes, components, tests)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
