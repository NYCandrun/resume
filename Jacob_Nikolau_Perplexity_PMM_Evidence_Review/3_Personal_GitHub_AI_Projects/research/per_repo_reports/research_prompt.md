MANIFEST | research_prompt | PUBLIC | research workflow / reusable agent-orchestration tool (prompt + Python control plane) | complete | 7 commits in one day; pre-repo history of the 3,399-line legacy prompt not present; no live company run in repo; network-using commands (`run --url`, `discovery crawl`) not executed

DISCLOSURE: No credentials found (regex scan of all tips; nothing flagged). No employer-looking material. The legacy prompt (`research_prompt@5fab799:README.md`, later `docs/legacy-prompt.md`) contains personal context: it states the user's purpose (a product-marketing-oriented "company brief" that "can be shared with the company before an offer") and names one third-party company, AirOps, as the subject of an earlier "historical AirOps run" whose corpus is *not* in this repo (`REFACTOR_REPORT.md` "Unresolved issues"). No third-party data, personal data about others, or captured sources are committed. Suitable to share after review; owner may want to note that the public legacy prompt reveals personal job-search intent and names a target company.

# research_prompt — investigation report

## 1. Identity
- Personal repository owned by NYCandrun; visibility PUBLIC; not a fork; created 2026-10-23T15:15Z, last pushed 2026-10-23T19:07Z (repos.json). Default branch is `codex/research-agent-refactor` (no `main`).
- Type: research workflow + reusable agent-orchestration tool. Purpose: give a coding agent (Claude Code or Codex) one public company URL and have it produce a source-captured, fact-store-backed, cited company brief, a public-evidence brand guide and (from v2.1) four architecture diagrams, with completion decided by deterministic gates rather than agent assertion (`1a4d35c:README.md`, `REFACTOR_REPORT.md`).
- Intended user (as stated in the legacy prompt §1): the author, getting "deeply up to speed on a complex, fast-moving company" from a product-marketing point of view.
- Maturity: well-tested framework (45 passing tests at the tip). The repo's own report lists a live run against "two unrelated live companies" as recommended follow-up (`a040d6c:REFACTOR_REPORT.md`).

## 2. Dates and attributable contributions
- All 7 commits are dated 2026-10-23, 11:28–15:07 EDT (about 3h40m). First: `5fab799` "Add maintainable company research agent system". Latest: `1a4d35c` "Create lean operational research workflow".
- Single author/committer identity: `Jacob Nikolau <jacobnikolau@Jacobs-MacBook-Pro-2.local>`. No other authors, no bot accounts, no Co-authored-by or "Generated with" trailers.
- Imported history: the first commit adds 82 files / 10,445 lines at once, including the full 3,399-line legacy prompt as `README.md`, a 1,732-row `REQUIREMENT_INVENTORY.csv`, a 68-entry `FAILURE_REGISTRY.md`, and a complete `research_control/` package. `MIGRATION_MAP.md` refers to "`README.md` on `main`" and to "historical prompt files", and the refactor report mentions "existing one-off scripts" and British file names in historical artifacts. None of these exist here, so this strongly suggests the prompt (and possibly the first refactor) came from an earlier workspace whose history was not imported. The legacy prompt's own evolution (e.g. the appended "Amendment … execution integrity", §19) **cannot be reconstructed** from this repo.

## 3. Branch and history coverage
Remote branches (all `codex/*`), forming one linear stack (`git log --all --graph`):
| branch | tip | contains |
|---|---|---|
| `codex/research-agent-refactor` (default) | `5fab799` | first commit only |
| `codex/operational-research-runner` | `a040d6c` | +1 |
| `codex/dynamic-research-orchestrator` | `717440a` | +5 (`a040d6c`…`717440a`) |
| `codex/lean-operational-workflow` | `1a4d35c` | +6, the newest |
- No merges and no PRs/issues (`gh pr list`/`gh issue list --state all` return empty). Each later branch extends the previous one. As a result, **the default branch holds only the earliest version**, and all later work (≈9k insertions / 7k deletions, `git diff --stat 5fab799 1a4d35c`) is on non-default branches. This looks like stacked agent branches that were never consolidated, not abandoned alternatives.
- Full history is available (not shallow). Nothing is inaccessible beyond the pre-repo history noted above.

## 4. Actual functionality / research workflow
Inspected: all top-level docs at `5fab799` and `1a4d35c`, per-commit stats and REFACTOR_REPORT diffs, `AGENTS.md`/`CLAUDE.md` at `a040d6c` and `1a4d35c`, CLI/runtime/planner/discovery structure, the operational lifecycle test, and the CI workflow.
- **Layers (v1, `5fab799`)**: `RESEARCH_CONSTITUTION.md` (principles), `WORKFLOW.yaml` (JSON-syntax YAML phase contract: capture → facts → synthesis → verification → review → brief → publication checks → release), `prompts/core/*` and `prompts/phases/*` (short role prompts of 9–61 lines for extraction, verification, devil's-advocate, insider, technical and editor reviewers, citation review, visual review, fixer), and `research_control/` (schemas, validators for citations/quotes/dates/tags/sources, reconciliation, phase gates, hashing, staleness, release manifest). Tools such as `tools/check_phase_gate.py` implement the commands the legacy §19 asks for. `tools/audit_refactor.py` maps each of 1,732 atomic legacy requirements to a destination.
- **Operational runner (`a040d6c`)**: adds `python -m research_control` CLI (init/run/status/work claim|start|succeed|fail|heartbeat/release), task packets, a conservative public-page capture helper that rejects private-network targets (`test_capture_helper_rejects_private_network_targets`), and a renderer with dependency-free PDF fallback. It also adds agent adapters (`AGENTS.md`, `CLAUDE.md`) and moves the legacy prompt to `docs/legacy-prompt.md`.
- **Adaptive orchestration (`e24920c`)**: SQLite scheduler (`runtime.py`: tasks, dependencies, attempts, leases, sources, discovery_channels tables), per-channel discovery that ends at "saturation" instead of a source count (`discovery.py`), corpus- and token-sized planning (`planner.py`), and single-writer reducers (`reducers.py`).
- **Publication change (`20cb9ff`)**: the one-page summary is replaced by a validated model registry plus four editable SVG architecture diagrams with evidence bindings (`validators/diagrams.py`, `diagram-models.schema.json`).
- **Brand guide (`91a4018`)**: a concurrent brand-guide packet (`prompts/phases/brand-guide.md`, 156 lines; `validators/brand.py`) kept separate from research evidence (failure modes F069, F070).
- **Efficiency (`717440a`)**: shared content-addressed web cache and URL lead ledger (`web_cache.py`), advisory model-tier routing (`routing.py`), and hash-scoped reuse of renders, validations and visual reviews.
- **Lean (`1a4d35c`)**: deletes migration and traceability scaffolding (legacy prompt, inventory, migration map, failure registry, audit tools; −7,255 lines) and moves framework tests to CI only.
- **Executed (offline, in /tmp copies from `git archive`)**: `unittest discover` passes 25 tests at `5fab799`, 29 at `a040d6c`, 45 at `717440a` and 45 at `1a4d35c`. `tools/audit_refactor.py --require-preserved` at `5fab799` reports PASS for 2002/2002 checks. `preflight` at `1a4d35c` reports PASS, with a warning that no CSS PDF renderer is present. `status` with no run returns a clear error. `check_phase_gate --phase capture` on an empty tree fails closed and lists missing evidence.
- **Not executed**: `run --url` and `discovery crawl`, because they fetch from the network. The end-to-end test (`test_clean_room_url_to_release_control_path`) uses synthetic `acme.example` fixtures. It shows the control path works, not research quality.

## 5. How Jacob uses or builds with AI
- **Agents doing research, governed by code.** The artifact is a specification-and-control system for LLM agents doing company research. The deterministic layer judges the agents: "Model opinion cannot override a failed check" (`5fab799:REFACTOR_REPORT.md`). Reviewer roles are separated ("separate agent contexts even if the same underlying model must be used", legacy §Model use).
- **Using AI to build (direct evidence).** All branches are named `codex/*`, and `AGENTS.md` is titled "Codex execution adapter" (`1a4d35c`). Taken together, this strongly suggests the refactors were carried out by OpenAI Codex under Jacob's direction. Commits carry his identity with no trailers, so the line-level split between human and agent work cannot be determined. The legacy prompt was written for Claude Code (`5fab799:README.md` line 5).
- **Task specification and context management.** These are explicit and highly developed. Examples: the shared-state ownership rules, worker packets with "the packet only, and no inherited status conversation", "Do not load docs/legacy-prompt.md during normal work", concise gate output with full records kept on disk, and advisory model tiers.
- **Verification.** It is fail-closed by design: missing, empty or truncated checks become UNKNOWN and block. The release manifest is bound to artifact hashes, and planted-fault regression tests cover six fact faults and six citation faults.
- **Correction and judgment.** These show up as method reversals across commits (§8), for example dropping fixed source quotas and dropping the heavy traceability scaffolding once it had served its purpose.

## 6. Subjective quality assessment
- **Strengths (high confidence)**: The research design is unusually rigorous: source grades, a verbatim quote plus location receipt for each fact, inference and absence-claim rules, currency/date rules, and separate verification and adversarial review. Failure modes are written as named invariants, each with an enforcement point and a regression test (`FAILURE_REGISTRY.md`). The 1,732-row requirement inventory plus audit is a careful, honest approach to refactoring a large prompt without silently losing requirements. The repo is candid about its limits: it refuses to "retroactively certify" the AirOps run and says stdlib HTTP cannot replace host browser and media tools.
- **Weaknesses**:
  - There is no live run, so the design is unvalidated against real websites (high confidence).
  - The README is now the entry point but is still long, and the control plane is large (about 9k lines added in an afternoon) for a single-user workflow. That raises maintenance cost and makes it unclear how much the author has reviewed (medium confidence).
  - The default branch is stale, so a visitor sees the oldest version (high confidence; likely a shortcut, not a defect).
  - Tests are synthetic and check structure, not research quality, which the repo itself acknowledges.
- **Intentional shortcuts vs defects**: The deterministic PDF fallback and advisory routing are deliberate. Dropping traceability in `1a4d35c` loses the audit trail, but it reads as a deliberate simplification.

## 7. Developmental milestones (all 2026-10-23, EDT)
1. 11:28 `5fab799`: monolithic prompt decomposed into constitution, workflow, prompts and controls, with a full traceability audit.
2. 12:08 `a040d6c`: made runnable as a CLI and packet protocol, with Codex and Claude adapters.
3. 13:00 `e24920c`: adaptive SQLite scheduler and saturation-based discovery.
4. 13:33 `20cb9ff`: one-page summary replaced by architecture diagrams (v2.1).
5. 14:34 `91a4018`: concurrent brand guide.
6. 14:56 `717440a`: caching, model routing and incremental reuse (v2.3).
7. 15:07 `1a4d35c`: lean v2.4 without the migration scaffolding.

## 8. Changes in working method and possible lessons
| # | earlier → later | possible trigger | inferred lesson | evidence strength | alternative |
|---|---|---|---|---|---|
| 1 | Pre-repo: one 3,399-line prompt with an appended §19 "Amendment" (date unknown) → `5fab799`: layered system | Legacy §19 text: completion "could be satisfied by an agent's assertion alone" | Don't let agents self-certify; enforce with code | Explicitly documented (the amendment) | — |
| 2 | `5fab799` policy and checks only → `a040d6c` executable runner | `REFACTOR_REPORT` goal of a "clean-room interaction" from one URL | Specs alone don't drive agents reliably; give them a protocol | Strongly inferred | Natural next step |
| 3 | `a040d6c` "does not attempt … a universal crawler or scheduler" → `e24920c` SQLite scheduler, "Do not ask the user for source, page, batch, or worker counts" | Not documented | Reversal: fixed quotas and agent-chosen counts judged unreliable; coverage measured by saturation | Strongly inferred (explicit reversal of a stated boundary) | Scope growth |
| 4 | One-page summary → diagrams (`20cb9ff`) | "deliberately superseded" (v2.1 note) | Output format changed to fit the reader's need | Explicitly documented (what), speculative (why) | Preference change |
| 5 | Serial phases → concurrent brand guide and shared cache (`91a4018`, `717440a`) | F070 "serializes the research run"; "Observed or anticipated" | Wall-clock cost matters | Speculative as to whether it was observed | Anticipated design |
| 6 | Traceability scaffolding and in-run tests → removed, CI only (`1a4d35c`) | Not documented | Migration proof is a one-time cost; keep runs lean | Strongly inferred | Context-window pressure on agents |

## 9. Demonstrated capabilities, limitations, uncertainties
- **Demonstrated**: decomposing a large agent prompt into enforceable contracts; fail-closed verification design; multi-agent role separation and context isolation; directing a coding agent through rapid, purposeful iterations with tests passing at every inspected tip.
- **Uncertainties**: whether the triggers in §8 came from real run failures (the AirOps run is mentioned but not present).

## 10. Evidence references and verification limits
- Commits: `research_prompt@5fab799`, `@a040d6c`, `@e24920c`, `@20cb9ff`, `@91a4018`, `@717440a`, `@1a4d35c`.
- Files: `@5fab799:README.md` (legacy prompt; §1 Goal, §Model use, §19 amendment, around lines 3235+), `@5fab799:REFACTOR_REPORT.md` (Architecture, Preservation, Scar tissue, Unresolved issues), `@5fab799:MIGRATION_MAP.md`, `@91a4018:FAILURE_REGISTRY.md` (F069–F070), `@a040d6c:AGENTS.md`, `@1a4d35c:AGENTS.md`, `@1a4d35c:CLAUDE.md`, `@1a4d35c:README.md`, `@1a4d35c:research_control/{runtime,planner,discovery,web_cache,cli}.py`, `research_control/tests/test_operational.py`, `.github/workflows/research-integrity.yml`.
- PRs/issues: none.
- Limits: there are no CI run logs and the GitHub Actions history was not queried; network commands were not executed; no rendered artifacts exist to judge.
