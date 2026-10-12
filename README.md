# SmartCent

SmartCent is a money-management platform that we will grow from a tiny Python
program into a production-style application. The main purpose of the repository
is learning: every feature should introduce a small number of Python concepts.

## Learning agreement

- The learner writes the application code by hand.
- The coach explains the next concept and gives a small, precise task.
- The coach reviews the code, runs it, and explains errors without immediately
  replacing the learner's solution.
- Each milestone ends with automated tests, a short quiz, and a reflection.
- We prefer understanding over speed and refactor old code as knowledge grows.

## Tooling

- Python 3.14: the programming language and runtime
- uv: Python installation, virtual environments, and dependency management
- Ruff: formatting and linting
- pytest: automated testing
- mypy: static type checking
- Git: version history

## Common commands

```bash
uv run python --version
uv run python path/to/file.py
uv run ruff format .
uv run ruff check .
uv run pytest
uv run mypy .
```

Do not memorize these yet. We will introduce each command when it becomes useful.

## Git learning workflow

We will practice a small team-style workflow throughout the project:

- `main` represents stable, releasable work.
- `dev` integrates completed features before they reach `main`.
- `feat/<short-name>` contains one focused feature or lesson.
- `fix/<short-name>` contains one focused bug fix.

The usual path is `feat/...` → `dev` → `main`. We will make small commits,
inspect diffs, resolve merge conflicts, and eventually practice pull requests,
tags, releases, and safe ways to undo mistakes.

See [ROADMAP.md](ROADMAP.md) for the course and product plan.
