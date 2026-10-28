MANIFEST | genesis | PRIVATE | research workflow / reusable agent-orchestration tool (mixed: tool on `main`, live research run on branch) | complete (local evidence); PRs/issues not checked | `gh` unauthenticated (PRs/issues unverified); history before the 3,399-line prompt is not in this repo; some large branch blobs not fetched; live run not re-executed (network/agents)

DISCLOSURE: No credentials found (regex sweep of `main` and the research branch for common key/token patterns: no hits). The research branch commits roughly 1,400 files of **third-party public web content** about the research subject, Genesis Computing (genesiscomputing.com): raw HTML/XML caches (`01-sources/discovery-cache/`), captured pages (`01-sources/captures/`), screenshots of its site, its SVG logos, and a non-official "brand guide" HTML/PDF built from its visual identity. Discovery notes also name company executives and quote public job postings (`06-checks/discovery-coverage.md`). All of this is public-web material about an external company that is the *research subject*. Nothing suggests the repo holds that company's internal or proprietary data, so I do not flag it as employer-owned material. The branch also commits run-state binaries (`tools/outputs/runtime.sqlite3`, `-wal`, `-shm`, plus a stray Finder duplicate `runtime 2.sqlite3-shm`). Shareability: `main` (the tool) looks fine to share after a normal review. Before sharing the research branch, remove or review the copied third-party pages, logos and screenshots (copyright and trademark), and drop the SQLite binaries.

---

## 1. Identity
- **Context:** Personal project under NYCandrun. Private visibility (`repos.json`: created 2026-10-23T17:52:31Z, pushed 2026-10-25T01:53:06Z, not a fork, default `main`).
- **Type:** A reusable, host-neutral **company-research agent system**. Python control plane `research_control/` (about 9.4k lines including tests), a constitution, a `WORKFLOW.yaml` phase contract, 26 phase prompts, and 16 JSON schemas. One branch holds a real research run against genesiscomputing.com.
- **Purpose (README):** "Give the agent one public company URL." The system discovers evidence until channels saturate, then plans and dispatches task packets to LLM workers. The intended outputs are a cited company brief, a brand guide, and four "evidence-bounded architecture diagrams", all behind a fail-closed release manifest.
- **Intended user:** Jacob, running it through Codex or Claude Code (`AGENTS.md` = "Codex execution adapter", `CLAUDE.md` = "Claude Code execution adapter"). The scope file states "Point of view: product marketing" (branch `00-scope.md`).
- **Maturity:** The tool is substantial and tested (45 tests pass on `main`, 49 on the branch). The flagship end-to-end output is **not yet demonstrated**: the run stopped mid-capture with no brief, facts, diagrams or release.

## 2. Dates and attributable contributions
- **First commit:** `5fab799` 2026-10-23 11:28 -0400. **Latest commit:** `7c2fff2` 2026-10-24 21:52 -0400 (branch). **Latest on `main`:** `1a4d35c` 2026-10-23 15:07.
- **Authors/committers (author = committer on every commit):** "Jacob Nikolau <jacobnikolau@Jacobs-MacBook-Pro-2.local>" made all 7 `main` commits. "Jacob Nikolau <jacobnikolau767@gmail.com>" made all 8 branch commits. No bot authors and no `Co-authored-by` or "Generated with" trailers.
- **Activity:** One burst of about 38 hours. On 10-23 from 11:28 to 15:07 (7 commits) the tool was built. Branch run commits came 17:46–17:49 on 10-23 and 20:30–21:52 on 10-24. Run event timestamps span 2026-10-23T21:41Z to 2026-10-25T01:52Z (`tools/outputs/runtime-events.jsonl`).
- **Inherited history:** The first commit is a **refactor of a pre-existing 3,399-line prompt**. `README.md`@`5fab799` *is* that prompt, written in Jacob's first-person voice ("The company URL is in my chat message", "designed to run in **Claude Code**"). `MIGRATION_MAP.md` says "`README.md` on `main` is the only normative source for this refactor", which implies an earlier repo or branch that is not present here. The prompt's own evolution therefore cannot be reconstructed.

## 3. Branch and history coverage
- **Branches:** `main` (default) and `origin/research/genesiscomputing-2026-10-23`.
- `git log main..origin/research/...` lists 8 commits, none merged:
  - **Code fixes:** `d073470` robots fetch, `7c9d11d` controlled retry for transient blocks, `3ee0288` exclude social share URLs.
  - **Run data:** `4e76e95` scope, then four capture checkpoints `d166d67` (542 files added), `d652d1c` (323), `2f010c4` (265), `7c2fff2` (179).
- The branch changes `capture.py`, `cli.py`, `discovery.py`, `runtime.py`, adds `test_capture.py` and extends `test_discovery.py`. These are genuine, run-driven fixes that **never reached `main`**.
- **PRs/issues:** not verifiable. `gh` is unauthenticated in the sandbox.
- **Limits:** One `git log --stat` failed because a promisor blob could not be fetched. File-level evidence came from `diff-tree --name-status` and `git show`, which worked.

## 4. Actual functionality / research workflow
**Inspected:** README, AGENTS/CLAUDE, `REFACTOR_REPORT.md`/`FAILURE_REGISTRY.md`/`MIGRATION_MAP.md`/`REQUIREMENT_INVENTORY.csv`@`5fab799`, the README diffs between commits, the branch code diff, and the branch run state.

**Executed:**
- The unittest suite on `main` (45 OK) and on a `git archive` copy of the branch in `/tmp` (49 OK).
- `python3 -m research_control preflight` on the branch copy. It passed, with a warning that no CSS PDF renderer was present.

**Not executed:** the agent run itself (needs network and LLM workers).

**Design as implemented:**
- **Durable scheduler and dispatch.** A SQLite scheduler (`runtime.py`, 971 lines) is paired with an append-only event log. It manages task states (planned → ready → leased → running → validating → succeeded/retryable/failed/blocked, plus stale), leases with heartbeats, and global and per-host concurrency (12 and 2 on the run). Workers receive immutable packets and are dispatched through `work claim/start/succeed/fail`.
- **Separation of writers and reviewers.** Workers write isolated parts and reducers are the only writers of shared state. Review contexts (technical, devil's-advocate, insider, editor, citation, visual) are separate.
- **Adaptive discovery.** `discovery.py` covers 10 evidence channels, each ending at a documented fixed point ("saturated" after two consecutive no-new passes) rather than a source quota. Numeric limits act as circuit breakers that yield an explicit incomplete state.
- **Capture controls.** `capture.py` handles robots-respecting capture with a public-host guard. A shared web cache keeps "leads not evidence" separate from research and brand purposes.
- **Validation and release.** Deterministic validators cover citations, quotes, dates, tags, writing rules, diagrams, brand and exhibits. Validation reuse is hash-aware, and release acceptance is fail-closed and bound to exact artifact hashes.
- **Real run (branch):**
  - Bootstrap and scope gates passed.
  - All 10 discovery channels reached `saturated`, cataloguing 930 sources.
  - Of 788 planned tasks, 246 were leased: 231 succeeded and 15 failed.
  - The brand guide was produced (`07-final-report/brand-guide.html`/`.pdf`, 31 PDF page renders, and an `acceptance-check.md` PASS with documented desktop/mobile QA fixes).
  - `WORKFLOW_STATE.md` shows capture "ready" and every later phase pending. No company brief, facts, verification, diagrams or release manifest exists.

## 5. How Jacob uses or builds with AI
Primarily **directing coding and research agents through a specification he controls**, and turning his long natural-language prompt into enforceable code. The direct evidence:
- **Agent instruction files.** `AGENTS.md` (Codex) and `CLAUDE.md` tell the agent to use subagents, unique worker IDs and "no inherited status conversation", and never to edit scheduler state directly.
- **Origin prompt.** A first-person, Claude Code-targeted 3,399-line prompt (`docs/legacy-prompt.md`@`a040d6c`) is the source requirement.
- **Recorded worker models.** Worker telemetry in `tools/outputs/worker-ledger.jsonl` records `model: gpt-5` (38× high effort, 1× medium) and one `gpt-5.6-sol`. The other 206 entries have no model recorded, which is consistent with README's "routing is advisory".
- **Agent-side failure records** (events log):
  - "account-wide subagent usage limit was reached" (2×).
  - "sandbox DNS could not resolve … external fetch escalation was denied" (about 12×).
  - The narrative "after escalation review disconnected" in `06-checks/discovery-coverage.md`.

  Together these show sandboxed agent workers (consistent with Codex) doing discovery and capture.
- **Refactor artifacts.** The refactor's 1,732-row requirement inventory, migration map and 68-entry failure registry read as agent-produced artifacts. Commit metadata does not prove who wrote them, so authorship of the code itself is **unattributed**, not "AI-written".

Context management is explicit: packets carry "only the task packet and files named by that packet", and listings are paginated "for prompt efficiency". Verification is designed in through deterministic gates, an UNKNOWN status that blocks, and independent reviewer identities.

## 6. Subjective quality assessment
**Strong decisions** (high confidence):
- Treating agent messages as non-evidence. F001: "Agent messages are never execution evidence."
- Using saturation instead of quotas, which replaced the legacy prompt's fixed caps ("Cap around 400 pages per competitor").
- Single-writer reducers, explicit `completed_zero` dispositions, and hash-bound staleness.
- Keeping brand observations out of the fact record.
- Fixes driven by real failures, each with a test. Examples: robots fetch treats 401/403 as disallow and other errors as allowed; `retry_blocked_sources` and `exclude_sources` require evidence and refuse captured or terminal items.
- CI (`.github/workflows/research-integrity.yml`) runs schema checks, preflight and tests without credentials.
- The scope document is careful about evidence: grades, namesake exclusions, separating partner products from Genesis capabilities, and treating vendor customer stories as Grade P.

**Weaknesses:**
- **Heavy process relative to output.** About 2 days of run time and 930 sources produced only the capture stage plus a brand guide. The research deliverable is undemonstrated. This may be an intentional "complete before synthesis" choice, but discovery breadth (31 independent-web passes) looks costly.
- **Fixes stranded on the branch.** Run-time fixes live only on the branch, so `main` lacks them.
- **Binaries in git.** SQLite and WAL files are committed, along with a duplicate `runtime 2.sqlite3-shm`. This is a hygiene defect, not a design choice.
- **Saturation is self-certified.** Channel saturation is asserted in worker-written evidence prose. The controller checks pass counts but cannot verify that the searches were done.
- **Unrecoverable requirements trail.** The provenance artifacts (requirement inventory, failure registry) were deleted in `1a4d35c`, so README-to-code traceability exists only in history. A lean repo is a defensible trade-off.

**Confidence:** high on architecture and test status; medium on run-quality judgments (I sampled state files rather than reading all captures); low on semantic accuracy of captures (not checked).

## 7. Developmental milestones
1. `5fab799` (10-23 11:28) takes the 3,399-line prompt and adds the constitution, workflow, prompts, validators, schemas, 68-entry failure registry and CI.
2. `a040d6c` (12:08) replaces the README with a 147-line operational entry point and moves the old prompt to `docs/legacy-prompt.md`.
3. `e24920c` (13:00) adds the adaptive planner, SQLite runtime, discovery-pass schema and a single `run` command (replacing `init/check/next`).
4. `20cb9ff` (13:33) replaces `one-page.md` with four fixed-title architecture SVGs.
5. `91a4018` (14:34) adds a concurrent brand-guide packet.
6. `717440a` (14:56) adds a shared web cache and validation cache.
7. `1a4d35c` (15:07) deletes 7,255 lines of refactor scaffolding.
8. Branch (10-23 to 10-24): scope, then three bug fixes, then four capture checkpoints.

## 8. Changes in working method and possible lessons
1. **Monolithic prompt → layered constitution + executable contract + code-enforced validators** (`5fab799`).
   - *Trigger:* `REFACTOR_REPORT.md` cites a "3,399-line mixed-concern prompt". The failure registry lists failures such as "claimed success without output".
   - *Lesson:* prose instructions don't enforce themselves. Move the checkable parts into code.
   - *Evidence strength:* explicitly documented. *Alternative:* a planned rewrite rather than a reaction to specific failures. The registry says "observed or anticipated", so these are not necessarily incidents.
2. **Fixed caps and a phase-by-phase `next` → adaptive saturation with a durable scheduler** (`a040d6c` to `e24920c`, same day).
   - *Trigger:* README now says "Do not ask the user how many pages, sources, batches, or workers".
   - *Lesson:* agents were asking for or inventing quotas.
   - *Evidence strength:* strongly inferred. *Alternative:* a design preference.
3. **One-page summary → four evidence-bounded diagrams** (`20cb9ff`).
   - *Trigger:* undocumented.
   - *Evidence strength:* speculative (a change in output preference).
4. **Serial phases → concurrent brand work and shared caches** (`91a4018`, `717440a`).
   - *Trigger:* the README says the brand work "overlaps the longest research stage instead of becoming a serial phase".
   - *Evidence strength:* strongly inferred (speed and cost).
5. **Provenance-heavy refactor → lean repo** (`1a4d35c`).
   - *Lesson (inferred):* scaffolding docs were context and maintenance burden once preserved in history.
   - *Evidence strength:* speculative.
6. **Running the system → patching the controller for real-world failures** (branch, 10-23 and 10-24). Examples: robots handling, DNS-blocked retry, share-intent links polluting discovery.
   - *Evidence strength:* explicitly documented by commit names, tests and event-log failure reasons.

## 9. Demonstrated capabilities, limitations, uncertainties
**Demonstrated in this repository:**
- Turning a long spec into a tested control plane.
- Fail-closed verification design.
- Multi-agent orchestration contracts that work across Codex and Claude Code.
- Provenance-aware research scoping.
- Iterative, test-backed fixes after real runs.
- A browser-QA'd brand-guide artifact.

**Uncertainties:**
- Who typed which code (no trailers).
- The prior history of the original prompt.
- Whether the run was abandoned or simply paused (the last checkpoint was 10-24 and no completion was recorded).

## 10. Evidence references and verification limits
**Files on `main`:**
- `genesis@1a4d35c:README.md`
- `genesis@1a4d35c:AGENTS.md`
- `genesis@1a4d35c:CLAUDE.md`
- `genesis@1a4d35c:.github/workflows/research-integrity.yml`

**Files from earlier `main` commits:**
- `genesis@5fab799:README.md` (3,399-line prompt)
- `genesis@5fab799:REFACTOR_REPORT.md`
- `genesis@5fab799:FAILURE_REGISTRY.md`
- `genesis@5fab799:MIGRATION_MAP.md`
- `genesis@5fab799:REQUIREMENT_INVENTORY.csv` (1,732 rows)
- `genesis@a040d6c:docs/legacy-prompt.md`

**Research branch commits:**
- `genesis@7c2fff2:00-scope.md`
- `genesis@7c2fff2:WORKFLOW_STATE.md`
- `genesis@7c2fff2:06-checks/discovery-coverage.md`
- `genesis@7c2fff2:tools/outputs/discovery/status.json`
- `genesis@7c2fff2:tools/outputs/worker-ledger.jsonl`
- `genesis@7c2fff2:tools/outputs/runtime-events.jsonl`
- `genesis@7c2fff2:05-synthesis/brand-guide/evidence/acceptance-check.md`
- Fix commits: `d073470`, `7c9d11d`, `3ee0288`

**Verification limits:**
- PRs and issues were not checked (`gh` unauthenticated).
- Captured page contents and brand-guide visuals were not opened.
- The live pipeline was not run.
- Running the tests on `main` may have created gitignored `__pycache__` in the clone. No tracked files were changed.
