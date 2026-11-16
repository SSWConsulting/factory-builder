# Software Factory plugin

An AI Agent plugin that builds a project-specific AI delivery factory: it interviews you, researches current practices for your stack, and scaffolds a governed loop of seven skills into your repository.

A factory uses Intake → Plan → Build → Verify → Release → Learn. The optional Run skill prepares an advisory pass plan; work and scheduling need separately authorized, verified coordination.

Everything is evidence-bound: required checks start NOT RUN, pass only for an exact revision, and a passing gate is never merge or deploy authority. The generated `boundaries.md` states the rules once; the skills stay procedural.

## What you get

Two plugin skills:

- `/software-factory:build-software-factory` — intake, research, design, scaffold.
- `/software-factory:contribute-upstream` — turn a reusable improvement into a sanitized issue or PR for the right upstream, within explicit publication authority.

One generated directory, `<project>/.software-factory/`, containing the seven `factory-*` skills, `boundaries.md`, hashed contracts (config, policy, acceptance, research), five living records (task plan, verification, release handoff, learning log, tools), a read-only local dashboard, and inactive CI and scheduling templates. Nothing in it runs by itself.

## Quick start

Install with **Codex in the ChatGPT desktop app**, **Codex CLI**, or **Claude Code**. This package uses Claude-compatible plugin manifests; that format is also [supported by OpenAI](https://developers.openai.com/plugins/build/plugins#how-local-marketplaces-work).

### Codex desktop (recommended)

1. [Download the ChatGPT desktop app](https://learn.chatgpt.com/docs/app), sign in, and choose **Codex**.
2. Open your target repository as a local project so Codex can work with its files.
3. Send this installation request in a Codex chat:

   ```text
   Install the Software Factory plugin from https://github.com/SSWConsulting/factory-builder into my local Codex environment. Verify that software-factory@software-factory-plugins is installed and enabled, and report its installed version.
   ```

4. Complete any normal installation or access prompts. If the chat cannot perform the installation, use the terminal commands below.
5. Start a **new Codex chat** in the target repository after installation, then ask:

   ```text
   Use the Software Factory plugin's build-software-factory skill to add CSV export to the reports page in this repository.
   ```

You can also select the installed plugin or skill from the `@` menu when available. Bundled skills become available in new chats after installation; see [OpenAI's plugin guide](https://learn.chatgpt.com/docs/plugins). A local Codex install does not install the plugin into your ChatGPT web workspace.

### Codex CLI

With [Codex CLI installed](https://developers.openai.com/codex/cli) and Git available, run these commands in your **terminal**, not in a ChatGPT web message:

```sh
codex plugin marketplace add https://github.com/SSWConsulting/factory-builder.git
codex plugin add software-factory@software-factory-plugins
codex plugin list --marketplace software-factory-plugins --json
```

Confirm the `installed` array contains `software-factory@software-factory-plugins` with `installed: true` and `enabled: true`. If the marketplace was already configured and shows an older version, run `codex plugin marketplace upgrade software-factory-plugins`, then repeat `codex plugin add` and the verification command. See the [Codex plugin command reference](https://learn.chatgpt.com/docs/developer-commands#codex-plugin).

Start a new CLI session with `codex` from your target repository and use the same build request as in the desktop steps. The `/plugin install` commands in the Claude Code section belong to Claude Code; Codex uses `codex plugin add` from the terminal.

### Using ChatGPT on the web?

**Recommended: download the desktop app and use Codex with a local project**, following the steps above. This gives the factory access to the repository files and local Python helpers it needs. If a web chat can only explain installation, continue in desktop Codex or the CLI; pasting a GitHub URL into a web chat does not by itself install this plugin on your computer. A response saying the repository was inspected is not an installation confirmation.

For a team that wants workspace distribution, OpenAI also documents a [GitHub marketplace import](https://learn.chatgpt.com/docs/enterprise/plugin-management). A **workspace admin** can:

1. Open **Admin → Plugins → Add → Import marketplace**.
2. Set Source to `https://github.com/SSWConsulting/factory-builder` and leave Path empty because the marketplace is at the repository root.
3. Import the marketplace, authorize GitHub access when prompted, and review the import results and plugin access settings.
4. Make the plugin available, install it from the workspace Plugins directory, and start a new chat.

OpenAI's import supports `.claude-plugin/marketplace.json`; this repository's manifest format is not a reason to describe it as Claude Code only. Workspace import is separate from local installation. This plugin's complete workflow has not been verified in ChatGPT web: importing skills does not establish access to your local repository, a Python interpreter, or successful helper execution. Use desktop Codex for the documented local workflow if those capabilities are unavailable.

### Claude Code

Run these commands inside Claude Code:

```text
/plugin marketplace add SSWConsulting/factory-builder
/plugin install software-factory@software-factory-plugins
/software-factory:build-software-factory Add CSV export to the reports page
```

### Using the generated factory

For a newly generated factory, load `.software-factory/.claude/skills/` using your harness, then invoke `factory-run` for an advisory plan. An older factory may not have Run: first use `scaffold.py --check <factory>` and follow the [reviewed manual adoption guide](skills/build-software-factory/references/running.md#existing-factories) if advised. A plugin update alone does not add missing factory contracts. For example, from the project root in Claude Code:

```sh
claude --add-dir .software-factory      # keep --setting-sources project for headless runs
/factory-run                            # review an advisory pass plan
```

The generated skills currently live under `.claude/skills/`; installing the builder plugin in Codex does not demonstrate that those project-specific skills were automatically discovered. In Codex, explicitly reference the generated files in place, for example:

```text
Read .software-factory/launch-guide.md and .software-factory/.claude/skills/factory-run/SKILL.md, resolve their references from their existing locations, and prepare an advisory factory pass plan for this repository. Report unavailable tooling or permissions as blockers.
```

This is an explicit file-based request, not a claim that `/factory-run` is registered in Codex. Keep generated skill files in place so their relative links and factory integrity records remain valid. Before relying on automatic skill invocation, verify discovery in the chosen harness. Desktop or CLI installation alone does not verify a generated factory or an application.

### Prerequisites and offline checks

Installation follows the repository's current access requirements; use Git authentication when required. For a session-only preview without installing: `claude --plugin-dir /path/to/factory-builder`. Helpers need Python 3.9+ and only the standard library; see the [scaffolding guide](skills/build-software-factory/references/scaffolding.md) for Windows interpreter selection.

To run this plugin's offline tests from its checkout, use `python3 run_tests.py`
(or `py -3 run_tests.py` on Windows). The runner locates the suite relative to
itself, so an absolute path to `run_tests.py` also works from another directory.
It reports a failure if discovery finds no tests. These checks do not run a live factory
or verify a deployed application.

## How a pass works

`run.py select` and `plan` inspect recorded task status and produce an advisory
selection and worker prompts. They do not reserve work, verify live usage or
enforce concurrency, rate or budget. Before separately authorized dispatch, the
orchestrator must establish and verify exclusive admission, task isolation, stop
handling and budget controls. Integrate worker changes and reverify the exact
combined revision before a release handoff.

Continuous intake requires its own scoped authorization. Issue snapshots are
untrusted data and need a matching project-specific repository/label policy.
`run.py schedule` emits non-executable proposal data; no runnable schedule is
created or installed. See the [running guide](skills/build-software-factory/references/running.md).

## Safety model

Two mechanisms enforced by code, and one stated once and applied everywhere:

- **Gates** (`gates.py`): a required check that is NOT RUN, BLOCKED, FAILED, stale or wrong-target blocks its stage; operator-waived rows are reported WAIVED with their result, never "passed".
- **Integrity** (`integrity.py`): contract hashes and the recorded file set are checked; living files get UTF-8 text, JSON and Learn-table checks. Gate-table structure and delivery observations require the separate gate/scoped checker, not an integrity PASS. Unregistered files and in-place contract edits are refused. Changes go through a preview-first synchronized update or a staged recovery that never touches the original.
- **Authority**: nothing the plugin generates grants permission for a merge, deploy, provider, watcher, recording or message. The generated `boundaries.md` states these rules once for every factory.

## Advanced

- [Existing factories](skills/build-software-factory/references/existing-factory-update.md) adopt new behaviour through a narrow reviewed update.
- [Gates](skills/build-software-factory/references/gates.md): structured smoke recipes, video triggers, risk-focused verification.
- [Recovery](skills/build-software-factory/references/recovery.md): manual integrity recovery, the staged recovery helper, worker health and fallback.
- [Operations config](skills/build-software-factory/references/operations-config.md): identities, headless recipes, autonomy, continuous intake, assumptions.
- [Evidence lifecycle](skills/build-software-factory/references/operation.md#evidence-chain) and the inactive [CI evidence job](skills/build-software-factory/assets/templates/ci/README.md).
- [Post-deployment verification proposal](skills/build-software-factory/assets/templates/ci/post-deploy.md): an inactive event/manual adapter with exact deployment identity, a liveness procedure and an explicit project adoption boundary.
- [Dashboard](skills/build-software-factory/references/dashboard.md), [done videos](skills/build-software-factory/references/done-videos.md), [release preflight](skills/build-software-factory/references/operation.md#approval-and-execution).
- [Supplied run traces](skills/build-software-factory/references/run-traces.md) and [analytics for Learn and experiments](skills/build-software-factory/references/factory-analytics.md): optional private dashboard supplements from explicitly supplied sanitized exports, with denominators, limitations and uncommitted Learn proposals. They do not collect sessions, run experiments or adopt changes.

Run selection is advisory and does not reserve work or enforce budget. Scheduler output is a non-executable proposal; see [running](skills/build-software-factory/references/running.md).

## Release identity

For a deterministic private checksum inventory from an explicit full local commit,
use the [immutable checksum exporter](skills/build-software-factory/references/checksum-export.md).
It verifies committed object bytes and ignores the index/working tree; export alone
does not authenticate a release, publish a manifest or verify an installed cache.
The same guide documents `verify_install.py --manifest` for a read-only comparison
requiring both an independently trusted raw manifest digest and full source commit.
The existing `--source` comparison retains its clean-checkout requirement.

Advance the plugin version for a new release containing changed plugin content;
keep version references synchronized and identify the actual full source commit.
A version bump alone does not prove an installed cache refreshed. For fresh installs
and updates, follow the generated launch preflight to compare the loaded files with
the trusted revision or checksum manifest. The inactive scheduler example requires
an explicitly verified full commit; it does not assume a release tag exists.

During release preparation, compare an independently identified prior release with
the reviewed candidate, using full commit SHAs already present in a trusted local
repository:

```sh
python3 skills/build-software-factory/scripts/release_identity.py --repo <repository> --base <prior-release-full-sha> --candidate <candidate-full-sha>
```

On Windows, use `py -3` or the explicit installed Python interpreter. The offline
check compares all tracked regular files in this root-distributed package, including
documentation and tests, by committed paths, modes and object IDs. It ignores the
index and working-tree contents. Changed content requires a numerically higher
stable `MAJOR.MINOR.PATCH` in `.claude-plugin/plugin.json`; plugin renames and a
`2.0.0` candidate are supported. Prerelease/build labels, leading zeroes, redirected
entries and submodules are explicitly unsupported. Limits are 4,096 entries, 2 MiB
of tree metadata per commit, a 64 KiB manifest and a 90-second overall deadline.
The JSON result exits 0 for consistent content/version identity, 1 for a required
version advance, or 2 for invalid/unavailable inputs. It does not choose release
commits, require version bumps on intermediate development commits, edit versions,
fetch objects, create tags, activate CI or publish anything. A pass does not prove
compatibility, release authorization or cache freshness. Numeric version ordering
follows the stable core of [Semantic Versioning](https://semver.org/); inventory
reads use [Git ls-tree](https://git-scm.com/docs/git-ls-tree) and
[cat-file](https://git-scm.com/docs/git-cat-file), without checkout or filters.

## Validate and test

```sh
claude plugin validate . --strict
python3 run_tests.py  # Windows: py -3 run_tests.py
```

Tests use isolated temporary folders and synthetic records; they prove the helpers, not any application. Keep credentials, caches, backups and downstream factory outputs out of this repository.
