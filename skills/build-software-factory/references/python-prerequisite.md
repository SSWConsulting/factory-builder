# Python prerequisite

The scaffold, integrity, gate, status and run helpers need Python 3.9+ and only its standard library. Check for it at the start of setup, before the interview, so nobody spends time on intake and research and then finds the factory cannot be created.

## Check

Find a working interpreter and record its path. Use that same interpreter for every helper.

- Windows: `& <skill-dir>/scripts/run-python.ps1 --version`. The launcher skips Microsoft Store aliases, verifies 3.9+, prints the executable it selected and installs nothing. A plain `python` on Windows may be a Store alias that does not run.
- macOS and Linux: `python3 --version`, or `python --version` where `python3` is absent.

Continue only when the reported version is 3.9 or later.

## If Python is missing or older than 3.9

Stop before research and scaffolding. Tell the user plainly that the factory's helpers need Python 3.9+, with no other packages, and offer ways to get it:

- Windows: `winget install Python.Python.3.12`, then open a new terminal.
- macOS: `brew install python`, or `xcode-select --install`, which provides `python3`.
- Debian or Ubuntu: `sudo apt install python3`. Other Linux distributions: the system package manager.
- A hosted development environment that already includes Python, such as GitHub Codespaces.

Run an install command only after the user explicitly approves that exact command. Invoking this skill does not authorize installing software, elevating privileges or changing system settings. If the machine is managed and the user cannot install software, offer the lite option below. After an install, re-check in a new shell before continuing.

## Lite option: no Python

Offer this only when the user cannot install Python, and use it only after they explicitly choose it knowing the trade-offs. It is guidance for working through the phases by hand. It is not a factory, and it has no helpers, integrity checks, gates, dashboard or run engine.

- Do not create `.software-factory/`, and do not hand-write its contracts, manifest, hashes or helper output. An improvised substitute for a missing helper is not allowed.
- Keep one notes file at a path the user approves, for example `FACTORY-LITE.md`, headed "Lite mode: no helpers, no integrity or gate checks".
- Work through Intake, Plan, Build, Verify, Release and Learn in order, using the intent of each phase:
  - Intake: a confirmed brief with facts, assumptions and unknowns kept separate, and acceptance criteria.
  - Plan: tasks with owners, dependencies and the check each one needs.
  - Build: one small, reviewable change within the agreed scope.
  - Verify: run the project's own tests and record the exact command, revision and outcome.
  - Release: a written handoff stating the revision, target and remaining checks.
  - Learn: what happened and one small improvement to try.
- Record every check as its actual command and outcome, or as NOT RUN. Nothing is PASSED by a gate. Lite results are never readiness, merge or deploy authority, and they are not factory evidence.
- The same boundaries apply as for a full factory: no secrets in notes, no paid agents, publishing, merging or deployment without explicit authorization.
- To upgrade later, install Python and run the normal setup. Lite notes can inform the new intake, but they are not imported as evidence.
