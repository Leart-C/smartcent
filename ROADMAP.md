# SmartCent learning roadmap

This roadmap is intentionally progressive. Later phases may change as we learn
what SmartCent should become.

## Phase 0 — Development setup

Learn the terminal, Python interpreter, scripts, virtual environments, uv, Git,
and how to read an error message.

Deliverable: a working project environment and a first manually typed script.

## Phase 1 — Personal finance calculator

Learn values, variables, strings, numbers, booleans, input/output, operators,
conditions, loops, and basic debugging.

Deliverable: a command-line program that records income and expenses in memory
and prints a balance and simple summary.

## Phase 2 — Functions and collections

Learn functions, parameters, return values, scope, lists, dictionaries, tuples,
sets, comprehensions, and decomposition.

Deliverable: a menu-driven tracker with categories, validation, and reports.

## Phase 3 — Files, modules, and errors

Learn imports, modules, packages, paths, JSON/CSV files, exceptions, context
managers, and logging.

Deliverable: transactions persist between runs, with import and export support.

## Phase 4 — Reliable financial code

Learn `Decimal`, dates and times, type hints, docstrings, pytest, test design,
linting, formatting, and refactoring.

Deliverable: correctly tested money calculations and a maintainable project
structure.

## Phase 5 — Object-oriented design

Learn classes, dataclasses, properties, composition, protocols, and the tradeoffs
between object-oriented and functional styles.

Deliverable: domain models for accounts, transactions, categories, and budgets.

## Phase 6 — Database application

Learn SQL, relational modeling, SQLite, migrations, repositories, transactions,
and PostgreSQL fundamentals.

Deliverable: durable multi-account storage with budgets and recurring entries.

## Phase 7 — Web API

Learn HTTP, REST, FastAPI, validation, dependency injection, authentication,
authorization, configuration, and API testing.

Deliverable: a secure SmartCent backend API.

## Phase 8 — Production engineering

Learn async programming, background jobs, caching, observability, security,
Docker, CI, deployment, profiling, and architecture decisions.

Deliverable: a deployed, monitored application with production-quality checks.

## Rhythm for every lesson

1. Explain one small concept with an example.
2. Give the learner a task to type from scratch.
3. Ask the learner to predict what the program will do.
4. Run and review the learner's code together.
5. Fix issues through hints before showing a solution.
6. Add or run tests.
7. Finish with two or three questions and a small commit.

## Git skills practiced throughout

- Phase 0: status, staging, commits, branches, diffs, and log
- Phases 1–2: feature branches and merging into `dev`
- Phases 3–4: merge conflicts, `.gitignore`, and useful commit history
- Phases 5–6: pull-request review, rebasing, and database migration safety
- Phases 7–8: tags, releases, CI checks, and production hotfixes

We use `main` for stable work, `dev` for integration, and short-lived
`feat/<name>` or `fix/<name>` branches for focused changes.
