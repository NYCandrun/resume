MANIFEST | etta_app | PRIVATE | small app (AI-powered desktop learning app, Tauri/Rust + React) | complete | PR bodies/review threads not accessible (PRs lived on the pre-import repo jacobn-a11y/*; `gh pr list -R NYCandrun/etta_app` returns `[]`); Rust not compiled/tested (no cargo in sandbox); app not run (needs macOS + Claude API key); release zip not opened

DISCLOSURE: No credentials found in the tree or history (searched for `sk-ant-` patterns across `git log --all -p`; the API key goes to the macOS Keychain via `src-tauri/src/keychain.rs`). Commit metadata includes personal emails: `jacobnikolau@Jacobs-MacBook-Pro.local`, `jacobnikolau@mac.lan`, and the GitHub merge identity `jacobn-a11y <jacobn@mosaicapp.com>`. That email domain is an identity detail only. Nothing in the content looks employer-owned: it is a self-study math/physics tutor, and the PRD says "Prepared for Jacob Nikolau". No third-party or customer data. The repo includes a committed 6.4 MB binary, `release/Astrolabe_0.1.0_aarch64_app.zip`. After review it looks suitable to share. Before sharing, consider removing the binary and checking the commit emails.

# etta_app (product name "Astrolabe")

## 1 Identity
- A personal project in the NYCandrun account. Visibility is PRIVATE. According to repos.json it was created and pushed 2026-06-11, but every commit is dated 2026-03-10 to 03-13, so the history was imported from an earlier repo (merge messages reference `jacobn-a11y/claude/*` branches). It is not a GitHub fork. A sibling repo named `etta_app_update` exists and was not reviewed.
- Purpose: "Astrolabe — Product Requirements Document … From Algebra to Astrophysics", a native macOS app for "a self-motivated adult learner" that goes from algebra through 12 domains to astrophysics (README.md). The intended user appears to be Jacob himself ("Prepared for Jacob Nikolau").
- Type: an AI-powered small app. Claude is the content, tutoring and grading engine. It uses spaced repetition (SM-2), mastery gating, interleaving and gamification.
- Stack: Tauri 2, a Rust backend (rusqlite, reqwest to the Anthropic API, macOS Keychain), React 19, Tailwind, Zustand, KaTeX, D3 and Recharts.
- Maturity: a working v0.1.0 prototype with a built aarch64 app bundle. It went through several audit-and-fix cycles. Not production-hardened.

## 2 Dates & attributable contributions
- First commit: `7a4a1eb` 2026-03-10 20:23 -0400, "Add Astrolabe PRD as README" (Jacob Nikolau). Latest: `3d49273` 2026-03-13 16:33 -0400, merge of PR #30. Every branch falls inside this window. Commits per day: 03-10: 2, 03-11: 57, 03-12: 18, 03-13: 27. There was no later activity in this repo.
- Authors and committers (all branches, 104 commits):
  - `Claude <noreply@anthropic.com>`: 68 commits. All 68 carry a `https://claude.ai/code/session_…` trailer, covering 25 distinct sessions.
  - `jacobn-a11y <jacobn@mosaicapp.com>` (committer GitHub): 30 PR merge commits.
  - `Jacob Nikolau` (local machine): 6 commits.
- Jacob's direct commits:
  - PRD v1.0 and v1.1 (`7a4a1eb`, `2848342`, 03-10).
  - Multi-agent audit reports (`97a382e`, 03-11, on `codex/macos-qc-integration`).
  - App bundle builds (`06fa521`, `18d43b6`, `7ec518e`, 03-11).
- Jacob's latest attributable action is the merge of PR #30 on 03-13. No human-authored source-code commits were found. All application code is authored by Claude.

## 3 Branch & history coverage
- The default branch is `main`, plus 27 remote branches. 25 are `claude/*` branches named after tasks (e.g. `plan-roadmap-implementation`, `security-audit-fixes`, `fix-context-data-loss`, `analyze-code-complexity`, `gamification-curriculum-rewards`). There is also one `codex/macos-qc-integration`.
- Unmerged work, from `git log main..origin/X`:
  - `codex/macos-qc-integration` (+1, `97a382e`, Jacob-authored): `audit-reports/2026-03-11-multi-agent/00–05`. This is a consolidated prioritized action report "Generated from 5 parallel agents on commit `403e644`", plus security, UI/UX, functionality, prompt-optimization and learning-quality agent reports (401 lines).
  - `claude/parallel-agents-issue-evaluation-0PiJn` (+1, `ce7308b`): `audits/2026-03-11-parallel-evaluation/00–05` (514 lines). Here 5 parallel agents re-checked 85 deduplicated findings against `main@82a8863` and found 20 FIXED, 32 PARTIAL and 33 NOT ADDRESSED.
  - `claude/optimize-prompt-tokens-SBVo3` (+1, `d4e28de`, 405+/67−). An earlier prompt-split attempt. Its approach reappeared on main through PR #14 (`d4b9bb2`).
  - `claude/fix-math-accessibility-RgXjv` (+2): XP-duplication and daily-progress fixes. `fix-security-issues-eeH8H` (+1, `a10e5ea`): a `content_hash` struct-literal fix. Both look superseded or squash-equivalent, because later main commits fix the same symptoms (this was not verified line by line).
- PRs #1 to #30 show up only as merge commits. Their bodies and reviews are inaccessible from this repo. There are no issues.

## 4 Actual functionality
Inspected: README/PRD, `src-tauri/resources/tutor_prompt.txt` (204 lines), `api/prompt.rs`, `api/client.rs`, `engine/*.rs`, `commands/ai_cmds.rs`, the audit files, and the commit bodies.

**Executed**, in a scratch clone (`/tmp/etta_app_check_470`, with `npm install --ignore-scripts`):
- `tsc --noEmit` passed with no errors.
- `vite build` succeeded, with a warning about a chunk over 500 kB.
- `eslint src` passed with no output.

**Not run:**
- The Rust build and its 25 `#[test]` functions in `engine/*` and `curriculum/graph.rs`, because the sandbox has no cargo.
- The Tauri app itself, which needs macOS and a key.

**Implemented**, per the code:
- **Data and curriculum:** a SQLite schema (`resources/schema.sql`) and 12 domain curriculum JSON files with a prerequisite DAG and validation (`curriculum/graph.rs`).
- **Learning engine:** mastery scoring weighted 0.50 accuracy, 0.25 latency consistency and 0.25 transfer (`engine/mastery.rs`), SM-2 spaced repetition, decay, a session builder with interleaving (wired in at `session_builder.rs:122`), and struggle detection.
- **Lessons and quizzes:** lesson, quiz, explain, evaluate and review modes, quiz types MC, fill-in-blank and free-response, and a diagnostic.
- **Projects:** file uploads (PDF, DOCX, images, text) sent to Claude natively.
- **Gamification:** XP, streaks and badges.
- **Offline cache:** HMAC integrity (`cache_integrity.rs`) and rate limiting (`rate_limit.rs`).
- **Settings:** model selection across Haiku 4.5, Sonnet 4, Sonnet 4.6 and Opus 4.6, with an Opus "escalation" model (`ai_cmds.rs:16-17`).

**Prompt design:**
- One tutor prompt with `### Mode:` sections. `extract_mode_prompt()` sends only the shared preamble plus the active mode section (`prompt.rs:187-211`).
- Learner context goes in as XML tags, with `xml_escape` to resist injection.
- Output token caps are set per mode.

**Late features:**
- A reinforcement loop that adapts lessons to the learner's specific quiz mistakes (`e371737`, `8c6aeb8`, `f1b0975`).
- `error_patterns` filled in across all curriculum JSON (`bae9469`…`2f0b0cd`).
- Milestone-based XP stored in a `curriculum_rewards` table with a UNIQUE constraint (`4ad3b46`).

**Drift from the PRD:**
- The PRD names `claude-sonnet-4-6`, but the code defaults to `claude-sonnet-4-20250514`.
- The PRD says to reward review recalls with XP. The final design rewards curriculum milestones instead.
- PRD v1.1 called for "four tables, no migrations". The code later added tables (snapshots, xp_events, quiz_answers, curriculum_rewards, lesson_views) through `db/init.rs`.

## 5 How Jacob works with AI
Direct evidence: Claude Code session trailers on all 68 Claude commits, the `claude/*` and `codex/*` branch names, and audit reports that describe themselves as generated by parallel agents. The repo shows two things together: an AI-powered product (Claude as tutor and grader) built almost entirely by delegating to an AI agent.

- **Specification first.** Jacob wrote a detailed PRD (v1.0, then a v1.1 "Minimal Surface Area" revision 7 minutes later). Claude then produced "Phases 1-7 scaffolding" in one session (`67d3d6b`).
- **Audit-driven verification loop.**
  1. Claude wrote security, UI/UX and functionality audits (`d571fa0`, `af73d72`, `33d94dc`).
  2. Jacob added a 5-agent audit with a P0/P1/P2 plan and exit criteria (`97a382e`, codex branch).
  3. Fix PRs #3 to #6 followed.
  4. 5 parallel agents then re-evaluated main against all 85 findings (`ce7308b`).
  5. That re-evaluation was followed by matching fix PRs:
     - #11 "Fix 12 security issues"
     - #12 "Fix 11 UI/UX issues"
     - #13 "Fix 5 partial functionality issues"
     - #14 prompt optimization, which matches eval rows #18 and #19
     - #15 and #16, mastery inflation and grading fairness, which match rows #4 and #22
- **Branch-per-task with human merges.** Jacob merged every PR. In the evening of 03-11 there are merges roughly every 10 to 15 minutes. That pace suggests merging after a quick check rather than deep review. This is inferred; no review artifacts are available.
- **Manual testing as the steering signal.** From 03-11 evening to 03-13, PR titles name specific runtime symptoms: math rendering duplication, LaTeX parsing, a quiz that "fail[s] silently", table rendering, quiz resumption, and a "build-breaking quiz cache call" (`f42eb06`). This strongly suggests Jacob ran the built app and reported problems back to the agent.
- **Packaging done by hand.** Jacob rebuilt and committed the macOS zip three times.

## 6 Quality assessment (moderate confidence)
**Strengths:**
- A clear, well-reasoned product spec grounded in learning science.
- A sensible minimal architecture: local-first, Keychain storage, no backend.
- A thoughtful prompt design: mode sections, XML context, escaping, per-mode budgets, and mastery-banded cache keys.
- Unusually systematic quality control for a 3-day personal project. Audits were deduplicated into a status matrix, and that matrix drove targeted fixes.
- The frontend typechecks, lints and builds cleanly. Integrity fixes went in late, such as server-side grading, XP idempotency through UNIQUE constraints, and path sandboxing.

**Weaknesses:**
- Very compressed agent-generated churn. Many PRs fix regressions introduced earlier, such as the build-breaking cache call and duplicated math rendering.
- The audits themselves recorded that many issues stayed partial after the first fix wave, including client-authoritative grading and mastery reaching 1.0 after one answer.
- Rust tests exist only in the engine modules. There are no frontend or contract tests, and no CI config was found, even though the agent plan required CI as an exit criterion.
- A binary is committed to git.
- The PRD and the code drift apart (section 4).
- Several audit and evaluation reports stayed on unmerged branches, so main's documentation trails what was actually done.
- Whether each fix truly worked was not independently verified here.

## 7 Developmental milestones
1. **03-10:** PRD v1.0, then v1.1.
2. **03-11 01:16:** Full scaffold (PR #1).
3. **03-11 06:00:** App sweep, AI commands and the first audit trio (PR #2).
4. **03-11 07:12:** Jacob's 5-agent action plan.
5. **03-11 10:00–12:36:** Security, math, functionality and adaptive-learning fixes (PRs #3–#7). First app bundle built.
6. **03-11 16:56:** Parallel re-evaluation (unmerged).
7. **03-11 21:37 to 03-12 00:43:** Fix wave keyed to the evaluation (PRs #11–#16), then UX and rendering fixes (PRs #17–#23).
8. **03-13:** Reinforcement pipeline (PR #25), build-warning cleanup (#26), error_patterns (#27–#28), path order and pre-generation (#29), milestone XP (#30).

## 8 Method changes & possible lessons
- **Single prompt to mode-sliced prompt.**
  - Before (PRD v1.1, 03-10): "a single 'tutor' system prompt… One prompt to maintain."
  - After (`d4b9bb2`, 03-12): the same file, but only the relevant section is sent.
  - Trigger: audit finding "Full 180-line prompt sent for every mode; ~800-1000 wasted tokens".
  - Lesson: keep one maintainable source, but compose prompts per call to control cost.
  - Evidence strength: explicitly documented.
- **One-pass audit to audit plus independent re-verification.**
  - Before: the first audits (03-11 06:3x) were followed by fixes.
  - After (03-11 16:56): parallel agents re-checked every finding, and only 31% were fully fixed.
  - Lesson: agent "fixed" claims need independent checking.
  - Evidence strength: strongly inferred from the sequence and the evaluation text. Alternative explanation: it may simply have been a routine second pass.
- **XP per answer to milestone XP.**
  - Before: the PRD design, and per-answer XP up to 03-13.
  - Trigger: XP-duplication and inflation findings (P0 #2/#23) and earlier idempotency fixes.
  - After (`4ad3b46`): once-only milestone rewards.
  - Evidence strength: strongly inferred. Alternative explanation: a product-taste change.
- **Generic lessons to mistake-aware reinforcement.**
  - Before: the explain mode with fixed strategies.
  - After (03-13, `e371737`, `f1b0975`, `6f94997`): the learner's actual errors and curated `error_patterns` are fed into every mode.
  - Trigger: the evaluation noted "Adaptive context too thin".
  - Evidence strength: strongly inferred.
- **Quiz size and budgets.** `c75fe32` raised quizzes to 10 questions and "doubled token budgets", which reversed part of the earlier token tightening. Possible trigger: truncated quiz JSON. Evidence strength: speculative.

## 9 Capabilities, limitations, uncertainties
**Demonstrated:**
- Writing a detailed product spec.
- Delegating a full-stack build to Claude Code.
- Orchestrating parallel specialist audit agents and synthesizing their output into a prioritized plan.
- Driving fixes from that plan and its verification.
- Steering through manual product testing.
- Building an LLM product with structured prompts, context injection, model selection and cost controls.

**Uncertain:**
- How thoroughly Jacob reviewed each PR.
- Whether the Rust code compiles and its tests pass.
- Whether the shipped app works end-to-end.

## 10 Evidence references & verification limits
**Files and commits:**
- `etta_app@3d49273:README.md` (PRD)
- `etta_app@3d49273:src-tauri/resources/tutor_prompt.txt`
- `…:src-tauri/src/api/prompt.rs`, lines 5, 30-40, 187-211
- `…:src-tauri/src/commands/ai_cmds.rs`, lines 16-17 and 273-285
- `…:src-tauri/src/engine/mastery.rs`
- `…:src-tauri/src/engine/session_builder.rs:122`
- `etta_app@97a382e:audit-reports/2026-03-11-multi-agent/00-consolidated-prioritized-action-report.md` (branch `codex/macos-qc-integration`)
- `etta_app@ce7308b:audits/2026-03-11-parallel-evaluation/00-consolidated-evaluation-report.md` (branch `claude/parallel-agents-issue-evaluation-0PiJn`)
- Commits `67d3d6b`, `d4b9bb2`, `4ad3b46`, `2a81350`, `f42eb06` and `c75fe32`
- PR merges #1 to #30 (bodies inaccessible)

**Verification limits:**
- I did not compile the Rust code, run the app, or unpack the zip.
- The PR and issue APIs return nothing for this repo, so review behaviour is inferred from merge timing and commit messages only.
