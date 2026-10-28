MANIFEST | etta_app_update | PUBLIC | small app (native desktop AI-tutor app; AI-built) | complete | Rust/Tauri backend not compiled or tested (no cargo in sandbox); app never launched; no live Anthropic calls; the external spec ("Appendix A–E", "blocklist #N", "H10/H20…") referenced throughout is not in the repo; the git history doesn't show who reviewed what

DISCLOSURE: No real credentials found. The only `sk-ant-…` strings are dummy test fixtures (`src-tauri/src/keychain.rs:101`, `src-tauri/src/export.rs:425`, `src/pages/OnboardingPage.test.tsx:112`). Agent commits carry the identity `Etta Agent <agent@etta.app>`. The July commits carry the email `jacobnikolau@Jacobs-MacBook-Pro-2.local` / `…@macbookpro.mynetworksettings.com`, a local-hostname leak with low sensitivity. No third-party data, no personal learner data, and nothing that looks like employer material. The curriculum JSON is generic math/physics content. It appears suitable to share after a light review. Note that the README is out of date on the default model (see §6).

## 1 Identity
- A personal project on the NYCandrun account. It is PUBLIC, not a fork, and was created 2026-06-11T04:36Z (`repos.json`). Default branch: `main`.
- **What it is:** "Etta", an adaptive, gamified, offline-first macOS desktop learning app. It takes an adult learner from algebra up to university-level astrophysics (12 domains). Claude generates all lessons and quizzes on demand. State lives in local SQLite, with no server or accounts (`README.md` L1–19).
- **Type:** small app, an AI-powered product built almost entirely through AI coding agents.
- **Stack:** Tauri 2, React 19, TypeScript, Tailwind, Vite and Zustand on the front end; Rust (rusqlite, reqwest) on the back end; OS keychain; Anthropic Messages API.
- **Maturity:** the README says "slim v1, all milestones landed". This is a substantial, feature-complete v1 with heavy tests. The Progress page is still a placeholder (`src/pages/placeholders.tsx`). Gamification item #25 is deferred (`src-tauri/src/gamification.rs:10`). The signed .dmg, notarization and auto-updater are documented but were never shown to have been built ("macOS universal binary cannot be produced in the Linux sandbox", PR #2).
- **Relationship to another repo:** the name and content imply this is a rebuild of an earlier version. Commit and PR text mentions "Conflict fixes vs prior revision" (PR #2), "v1 hardcoded it false" (README mastery section), and "zero 'Astrolabe' references" (ec64a1e). A separate `etta_app` repo exists on the account; I noted it by name only and did not examine it.

## 2 Dates & attributable contributions
- **First commit:** `d138379` on 2026-06-11 04:46Z, "Initial commit: project stub", by Etta Agent. **Latest:** `bd613b6` on 2026-07-03 15:49 -0400. There are 27 commits on all refs.
- **Authors and committers:**
  - `Etta Agent <agent@etta.app>`: 12 commits on 2026-06-11. These are all milestone and bugsweep commits plus the stub, with the UTC timezone and Linux-sandbox wording.
  - `NYCandrun <jacobnikolau767@gmail.com>`: 11 PR merge commits on 2026-06-11, committed by GitHub.
  - `Jacob Nikolau` (local MacBook hostnames): 4 commits on 2026-07-03.
- **AI trailers:** every non-merge, non-stub commit carries a `Co-Authored-By: Claude …` trailer: Opus 4.7 ×11, Sonnet 5 ×1 (be2d460), Opus 4.8 ×3. PRs #1–#2 end with "Generated with Claude Code".
- **Jacob's attributable activity:** he merged PRs #1–#11 on 2026-06-11 (05:23Z to 08:59Z) and authored, as git author, the 4 commits on 2026-07-03. All 4 are co-authored with Claude.
- **Activity periods:**
  - (a) A burst of roughly 4.2 hours on 2026-06-11: stub, then M0–M5, then 5 bugsweeps.
  - (b) A pause of about 3 weeks.
  - (c) 2026-07-03, 13:01–15:49 local time: a full-app audit and refactor, then three feature commits.
- No imported or squashed foreign history, and no fork.

## 3 Branch & history coverage
- **Remote branches (12 plus main):** `milestone-0-foundation`, `milestone-1-foundation-data`, `milestone-2-ai-curriculum`, `milestone-3-learning-loop`, `milestone-4-onboarding-dashboard`, `milestone-5-polish-ship`, `bugsweep-1-data-layer` … `bugsweep-5-design-config`.
- Running `git log main..origin/X` gives 0 commits for every branch. All branch work is merged, and nothing is left unmerged or abandoned.
- **PRs:** #1–#11, all MERGED (lead-provided `prs/etta_app_update.prs.json`; `gh pr list` returned the same). No issues.
- Each PR was merged 2–5 seconds after it was created (e.g. #11 created 08:59:12Z, merged 08:59:16Z; #1 created 05:23:22Z, merged 05:23:27Z). There is no GitHub review activity. Merges look either automated by the agent session or done immediately. I can't reconstruct any human review from GitHub.
- PR #1/#2 bodies include test-plan checklists. #3–#11 have one-line bodies.
- **Mismatch:** PR #7–#11 bodies say "Opus 4.8 bug sweep", but the commit trailers say Opus 4.7. The labeling is inconsistent and I can't resolve it.
- The July commits went straight to `main`, with no branch or PR.
- **Inaccessible:** the driving spec/prompt, i.e. the "Appendix A/B/C/E", "blocklist #0–#50" and "H10/H14/H20/H21…" item numbering cited throughout code and README. Also the "154 findings" audit from be2d460. Neither is committed.

## 4 Actual functionality
Code size: about 11.2k lines of Rust in `src-tauri/src` with 141 `#[test]` fns, 23 frontend test files, and 141 tracked files.

**Inspected:**
- the README (54 KB)
- all commit messages
- PR bodies
- `ai/system_prompt.txt` (213 lines)
- the curriculum data
- file and stat diffs for every commit

**Implemented, based on the code and README cross-checked against the diffs:**
- **Curriculum:** 12 domain JSON files with about 400 concepts (the M2 commit says 402; I counted 414 `prerequisites` keys). They form a prerequisite DAG validated at startup (id regex, prerequisite resolution, cycle check).
- **AI layer** (`src-tauri/src/ai/`):
  - one shared reqwest client; API key read from the keychain per request
  - prompt caching of the system block; `xml_escape` on every interpolated field (prompt-injection defense)
  - SSE streaming over a per-invocation Tauri Channel, with cancellation
  - idle-based timeouts; one retry on 429/5xx, only before the first byte
  - truncated (`max_tokens`) output treated as an error and never cached
  - ~30 requests/min sliding-window limiter
  - model list from `GET /v1/models` with a fallback list
- **Grading** (`grading/`): server-authoritative.
  - Multiple choice is graded from the canonical `isCorrect`.
  - Fill-in-the-blank uses mathematical equivalence (`math_eq.rs`).
  - Free response is graded by the model against a rubric, with the score clamped.
  - The quiz schema repairs stray types and rejects quizzes with fewer than 3 questions.
  - The wire types hide answer keys until after grading. Submissions must be an exact permutation of the canonical question ids.
- **Adaptive engine** (`adaptive/`):
  - mastery = 0.5·accuracy + 0.25·consistency + 0.25·transfer over 20 attempts
  - "corrected SM-2" spaced repetition
  - decay and prerequisite gating; a session builder
  - XP, streak and daily-goal ring
- **Data:** SQLite in WAL mode, an allowlist of typed settings, a content cache with side-band metadata, daily `VACUUM INTO` backups, and a JSON export that filters out secrets and paths.
- **UX:** onboarding, a 5-question placement micro-quiz, a dashboard with a build-time SVG curriculum map, and lesson/quiz pages. KaTeX and a hand-rolled markdown renderer (tables, lists, rules added in f720fa5). Inline `etta-chart` SVG charts use a hand-rolled recursive-descent expression evaluator with no eval (714dfb9). Also offline gating, dark mode and a11y work.
- **Security config:** CSP limited to `connect-src api.anthropic.com`; the fs scope was narrowed twice (37009aa, be2d460).

**Executed, on a scratch clone in /tmp with `npm ci --ignore-scripts`:**
- `vitest run`: **23 files, 204 tests passed**
- `tsc --noEmit`: pass
- `eslint .`: pass
- `vite build`: success (one chunk >500 kB warning)

**Not executed:** cargo fmt/clippy/test (no Rust toolchain), the Tauri app itself, and any AI call. I have not verified the backend claims beyond reading the code and commit text.

## 5 How Jacob builds with AI
This is both an AI-powered product (Claude is the content engine and the free-response grader) and an app built by AI agents. Direct evidence:
- **Delegation by milestone:** the work was split into numbered milestones (M0–M5) on separate branches/PRs, each with a scoped commit message. They cite spec item numbers ("Blocklist items addressed: #8, #12…", "Appendix C", "bug 0a/0e", "H10/H20/H21"). This strongly suggests a detailed external spec plus a list of known failures from a prior version ("blocklist", "Conflict fixes vs prior revision"). The agent was then directed to satisfy it item by item. The spec itself isn't in the repo.
- **Structured verification passes:** after M5, five "bug sweep" PRs targeted one subsystem each (data layer, AI layer, adaptive engine, frontend flows, design/config). Each produced one small, well-reasoned fix: the cache tie-break, score-denominator inflation, a missing transaction, stale stream deltas, and the over-broad `$HOME` fs scope. PR #7 reports "1 fixed, 1 deferred".
- **Second-round adversarial audit (July):** be2d460, authored by Jacob, with Sonnet 5 as co-author. It reports "Audited every subsystem (154 findings), adversarially verified the critical/high issues". It fixed serious defects that had shipped through the June "All Linux CI gates pass" milestones: an onboarding redirect loop, dashboard commands that "crash 100% of the time" because of a wrong SQLite column index, lessons that were never actually cached, a score-forging path, and timeouts that killed healthy streams. Answer keys had been exposed to the webview through the `$APPDATA` fs scope. This is direct evidence that green unit tests didn't establish runtime correctness, and that a later audit pass caught it.
- **Model awareness inside the product:** bd613b6 replaced stale or fake model ids with discovery (newest Sonnet by `created_at`) and added a Refresh button.
- **What the history doesn't show:**
  - whether Jacob read or edited any agent output by hand (every commit has a Claude trailer)
  - any review comments
  - his prompt or spec text
- PR merge timing (seconds) suggests he didn't review each PR on GitHub before merging.

## 6 Quality assessment
Purpose-appropriate criteria: does it work, and is the architecture sound?

**Strengths** (medium-high confidence from code and tests):
- Unusually deliberate security and integrity design for a hobby app: server-side grading, redacted wire types, an exact-permutation gate, keychain-only key storage, a locked CSP, injection escaping, and caching that refuses truncated or invalid output.
- A clear FE/BE type contract with a round-trip fixture test.
- Disciplined commit messages that explain each defect's mechanism and fix.
- The frontend gates pass cleanly.

**Weaknesses:**
- **The June "done" state was materially broken** (stated outright in be2d460). Milestone PRs claimed green CI while core flows crashed or misbehaved, so the CI gates were mostly unit-level. Confidence is high that this happened; the July fixes are claimed but not verified by me at runtime.
- **README drift:** it still says the default model is `claude-sonnet-4-6` with a fallback list of `claude-sonnet-4-6, claude-opus-4-8, claude-haiku-4-5` (README L268, L287–292). Code and tests now use `claude-sonnet-5` (bd613b6). The README is a 54 KB spec-like document that is easy to let go stale.
- **Heavy hand-rolled pieces** (markdown renderer, expression evaluator, math equivalence) carry correctness risk. They are an intentional choice, explained in the commit messages (CSP forbids eval, zero new deps).
- **Unproven distribution:** macOS signing and the auto-updater were never shown working.
- The model-labeling inconsistency (4.7 vs 4.8) weakens how much the PR text can be trusted as a record.
- Overall it reads as a capable, coherent v1 whose real-world runtime reliability is unverified. My Rust-side confidence is moderate, because I couldn't compile it.

## 7 Developmental milestones
1. 2026-06-11 05:21Z, `ea14e6d` (M0): scaffold, contract, design system, CI gates.
2. 06:04Z, `6a147aa` (M1): SQLite data layer, keychain, cache.
3. 06:26Z, `7af872c` (M2): AI client, prompt, curriculum and DAG.
4. 07:27Z, `49ad50e` (M3): learning loop, SM-2, mastery, gamification.
5. 07:50Z, `02aaf75` (M4): onboarding, placement, dashboard.
6. 08:24Z, `ec64a1e` (M5): a11y, offline, export, shipping documentation.
7. 08:35–08:58Z: bugsweeps 1–5 (`6993553`, `e685300`, `258abfd`, `6fcb22f`, `37009aa`).
8. 2026-07-03, `be2d460`: full refactor (96 files, +18.2k/−3.0k lines, README rewritten).
9. Same day: `f720fa5` (tables/lists), `714dfb9` (charts), `bd613b6` (model discovery).

## 8 Changes in working method
1. **Build first, then sweep** (both 2026-06-11). Earlier approach: milestone-scoped feature PRs (M0–M5). Later approach: subsystem-scoped bug-hunt PRs (#7–#11).
   - Trigger: undocumented, though the sweep PRs are explicitly framed as "bug sweep of …".
   - Lesson: build verification passes into the delegation.
   - Evidence: explicitly documented as a sequence; the motive is speculative. Alternatively, the sweeps may simply have been planned steps in the original spec.
2. **Shallow sweeps replaced by a broad adversarial audit** (06-11 to 07-03). Earlier approach: five sweeps that produced about one fix each. Later approach: "Audited every subsystem (154 findings), adversarially verified the critical/high issues".
   - Trigger: documented severe defects that the sweeps missed (100% crash in dashboard commands, onboarding loop, uncached lessons).
   - Inferred lesson: CI green plus narrow sweeps weren't enough. The approach moved to exhaustive audits plus verification of each finding.
   - Evidence: strongly inferred, since the defects are explicitly listed. Alternatively, actually running the app on a Mac after the sandbox build may have surfaced the problems; the commit doesn't say how they were found.
3. **Environment and agent shift.** June work came from a Linux sandbox under the "Etta Agent" identity, going through branches and PRs, with Opus 4.7. July work came from Jacob's local machine, committed directly to main, with Sonnet 5 and Opus 4.8.
   - Evidence: explicit (author metadata and trailers).
   - Reason: speculative (tool or model availability, or a move to hands-on local iteration).
4. **Model ids:** hardcoded fallbacks (M2) were replaced by account-based discovery (bd613b6), triggered by "stale/fake default and fallback ids". This is explicitly documented.
5. **Prompt evolution:** `system_prompt.txt` changed only twice: created in M2, then extended in 714dfb9 to teach the `etta-chart` block, plus guidance on when to use a chart, a table or prose. Earlier prompt drafts, if any existed, aren't in the repo.

## 9 Capabilities, limitations, uncertainties
**Demonstrated in this repo:**
- decomposing a large app spec into staged agent deliverables
- running targeted, then exhaustive, AI-driven audits
- security-conscious product design (server-authoritative grading, injection defense, least-privilege capabilities)
- designing an LLM-backed product with caching, rate-limit and failure semantics
- frontend tests and build that pass

**Uncertain:**
- whether the July fixes are correct at runtime (the Rust side wasn't run)
- how the June defects were discovered
- the true model behind the PR #7–#11 sweeps

## 10 Evidence references & verification limits
**Commits:**
- `etta_app_update@d138379` (stub)
- `@ea14e6d:Makefile` (CI gates)
- `@7af872c:src-tauri/src/ai/system_prompt.txt`
- `@ec64a1e`
- `@6993553:src-tauri/src/cache.rs`
- `@e685300`, `@258abfd`, `@6fcb22f`
- `@37009aa:src-tauri/capabilities/default.json`
- `@be2d460` (audit/refactor message)
- `@f720fa5:src/components/markdown.ts`
- `@714dfb9:src/lib/plotExpr.ts`
- `@bd613b6:src-tauri/src/ai/models.rs`

**HEAD files:**
- `README.md` L13–19 and L284–292 (stale model default)
- `src/pages/placeholders.tsx` (Progress stub)
- `src-tauri/src/gamification.rs:10` (#25 deferred)

**PRs:** #1–#11, with bodies in `/home/user/workspace/research/github/prs/etta_app_update.prs.json`. Issues: none (`etta_app_update.issues.json` = []).

**Verification:**
- Frontend vitest (204/204), tsc, eslint and vite build all passed on a /tmp scratch clone. The source clone was untouched.
- Rust tests and clippy, the Tauri runtime and the AI behavior were not verified.
- The external spec and audit artifacts are unavailable.
