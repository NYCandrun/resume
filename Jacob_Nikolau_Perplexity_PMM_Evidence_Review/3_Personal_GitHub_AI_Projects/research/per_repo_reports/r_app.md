MANIFEST | r_app | PRIVATE | small app (iOS product prototype, AI-powered, built primarily by Claude Code agents) | complete (static review only) | No Swift toolchain in sandbox (iOS-only SwiftUI/SwiftData/StoreKit code), so nothing compiled or tested; `gh` unauthenticated so PR bodies/review comments, closed PRs (e.g. missing #10) and deleted head branches not inspectable; history appears imported from an earlier repo under the jacobn-a11y account.

DISCLOSURE: No live credentials found. A history-wide regex scan for Anthropic key / JWT patterns returned nothing; Supabase/Claude config reads env vars, and tests use dummy values (`placeholder-anon-key`, `anon-key`, `secret`). Third-party content: onboarding "showcase" embeds short quoted lines attributed to commercial media (K-drama quotes, K-pop lyric lines such as BTS "DNA", Squid Game, Solo Leveling) per `r_app@d4a4c48`. These are small snippets, but licensing should be checked before any public release. Personal data: commit author emails include a work-domain address for the `jacobn-a11y` identity and local machine hostnames. Per the brief, this is an author identity only. Nothing in the content looks like employer material: it is a consumer Korean-learning app with an original PRD. Naming mismatch: the repo is `r_app` with the description "russian language app", but every file is a **Korean** app ("Hallyu"), and the very first README line was `# k_app` (`r_app@0cffb4d`). Suitable to share after review (remove or confirm media quotes; note the identity emails in history).

# r_app — "Hallyu" Korean-through-media iOS app

## 1. Identity
- Personal repo of NYCandrun, **private** (visibility only). Created 2026-03-20T00:42Z and pushed 00:49Z (repos.json), which is *after* every commit (latest 2026-03-20 00:19Z). Merge commits reference `jacobn-a11y/claude/...` head branches. So the history was built in a different repo (probably `jacobn-a11y/k_app`, going by the first README title) and then pushed here in full. It is not a GitHub fork (`isFork: false`).
- Type: AI-powered consumer app prototype (SwiftUI, iOS 17+). It teaches Korean to adult beginners using authentic media, and Claude acts as a constrained "coach" in 5 roles.
- Maturity: a broad, feature-complete-looking V1 *codebase* (≈31.5K lines of Swift; 590 `@Test`/`func test` occurrences). It has no Xcode project, no CI, no bundled audio, media, fonts or stroke data, and no evidence that it was ever built or run on a device. Call it a late prototype / unverified V1 scaffold.

## 2. Dates & attributable contributions
- First commit: 2026-03-17 12:11 -0400 (`0cffb4d`, "Initial commit", `# k_app`). Latest: 2026-03-19 20:19 -0400 (`5df44b2`, merge of PR #15). The whole history is **about 3.3 days**, 43 commits, on one branch.
- Authors/committers seen:
  - `jacobn-a11y` (GitHub web UI): initial commit, README/PRD, and all 15 PR merges (committer "GitHub").
  - `Jacob Nikolau` (local machine identities `@Jacobs-MacBook-Pro.local`, `@mac.mynetworksettings.com`): 6 direct-to-main commits on 2026-03-19, 02:38–17:51.
  - `Claude <noreply@anthropic.com>`: 22 commits, each with a `https://claude.ai/code/session_…` trailer (13 distinct sessions).
  - No other bots or collaborators.
- Jacob's attributable work:
  - PRD authored or pasted via the web UI, 2026-03-17 12:19 (`3236d8d`, 306 lines). Who drafted the prose is not determinable.
  - Merging every Claude PR, 03-18 00:03 → 03-19 20:19.
  - Local remediation commits, 03-19 02:38 → 17:51 (`15613d0`, `5e598c5`, `01f1f8b`, `c2112de`, `27de0ed`, `ff1aba7`). These carry no AI trailers. Some are very large (`c2112de` touches 50+ files, rewriting 630 lines of MediaPlayerView), so they may have been produced with a local AI tool. **There is no direct evidence either way**, and I do not assign authorship beyond the git identity.
- Activity: 03-17 PRD → plans (03-17/18) → Phases 0–9 (03-18 04:13 → 03-19 05:51) → audit/remediation (03-19 06:11 → 17:51) → scope audit + feed + onboarding redesign (03-19 21:57 → 03-20 00:19). No pauses longer than a few hours, and no activity after 03-20.

## 3. Branch & history coverage
- Remote branches: only `origin/main` (default). All `claude/*` head branches were deleted after merge. The only branch evidence left is merge-commit messages: `claude/readme-to-build-plan-vAs09` (#1), `claude/phase-0-build-plan-viLmV` (#2, #3), `claude/build-implementation-plan-wHLjQ` (#4), `claude/build-phase-4-es13m` (#5, #6), `claude/build-phase-3-MKH5q` (merged into phase-4 at `4fb302a`), `-5-Stac6` (#7), `-6-nwj1M` (#8), `-7-RG4IF` (#9), `-9-U8WKf` (#11), `claude/comprehensive-audit-RZcF7` (#12), `claude/audit-codebase-scope-FRRyE` (#13), `claude/enhance-onboarding-flow-KezfA` (#14), `claude/redesign-onboarding-flow-FhtAK` (#15).
- **PR #10 is absent.** No merge exists for it, and no "Phase 8" commit exists. Phase 8 (Progress/assessments) code appears in later commits, so Phase 8 was probably folded into another session or into a closed PR. I could not verify this (gh unauthenticated).
- Unmerged work: none visible, because every reachable commit is on main. Closed or abandoned PRs and their branches are inaccessible.
- History shape:
  - Phase 3 and Phase 4 ran in parallel sessions, then were reconciled with a merge (`4fb302a`).
  - PR #3 (`ee8e4c6` Phase 2, `f4f9394` Phase 1) shows two phases landing in a single PR.
  - PR #13 (scope audit) branched from `ff1aba7` and was merged after #14 started, giving a criss-cross graph.
- Plans, PRD, audit and code all exist only on main, so no branch diffs are possible.

## 4. Actual functionality
What I inspected: README (PRD), BUILD_PLAN, IMPLEMENTATION_PLAN, AUDIT_REPORT, Package.swift, Environment.swift, SupabaseClient.swift, ClaudeService.swift, ClaudePrompts.swift (index), SRSEngine.swift, all commit messages, and the representative diffs `27de0ed`, `01f1f8b` (BUILD_PLAN), and `c2112de` (README/Package). **Nothing was executed.**
- Structure: MVVM, protocol-driven services with mocks, and a `ServiceContainer` for dependency injection. Feature folders: Hangul, MediaLibrary, MediaLesson, Claude, Review, DailyPlan, Feed, Onboarding, Progress, Settings.
- Claude integration (`Hallyu/Core/Services/ClaudeService.swift`):
  - An actor calling `api.anthropic.com` **directly from the app with an `x-api-key` header** that is read from the process env var `CLAUDE_API_KEY`.
  - Responses are cached under SHA-256 keys built from the context.
  - A 1-second client-side rate limit and a client-side subscription-tier daily cap.
  - Five role prompts in `ClaudePrompts.swift` (333 lines): comprehension, pronunciation, grammar, content adapter, cultural context.
  - This builds an AI-powered product as well as using AI to build it.
- SRS (`SRSEngine.swift`): fixed-multiplier exponential decay, \(P = 2^{-t/h}\), with ×2.0 on correct, ×0.5 on wrong, and a 1.1 speed bonus. The PRD and audit call it "half-life regression / ML-driven", but **no regression or learned weights exist**. It is a hand-tuned heuristic.
- Learner model: the audit describes BKT with fixed parameters, persisted to Keychain.
- Pronunciation: Apple Speech (ko-KR) plus a jamo-level Levenshtein `PronunciationScorer` (`01f1f8b`).
- Backend: a thin Supabase REST client. Config is read from env and falls back to a placeholder; the `ensureConfigured()` guard was added in `27de0ed`. The config struct also accepts a `SUPABASE_SERVICE_ROLE_KEY`, which should never ship in a client. It is only parsed and stored, and I saw no use in requests.
- UX added late:
  - A TikTok-style vertical "learning feed" as the default Today tab, with XP, combo multiplier, streaks, confetti milestones and bonus rounds (`d852dac`, `8c62077`).
  - An 8-step "cinematic" onboarding (`e962e2b`, `d4a4c48`).
- Stubbed or missing:
  - 72 native-speaker audio files and all real media are not bundled (the seeder holds sample data).
  - No app icon, launch screen or TestFlight setup.
  - Snapshot tests are 3 of 30 targeted, UI tests 3 of 10.
  - Morphological analysis is deferred.
  - All of this is self-reported in `AUDIT_REPORT.md`, and it matches the empty `.keep`/`.gitkeep` resource folders.
- Buildability: `Package.swift` defines a library plus tests and *excludes* `App/HallyuApp.swift`. There is no `.xcodeproj`, so as committed the app cannot be launched without extra setup.

## 5. How Jacob works with AI
Direct evidence: Claude Code session trailers on 22 commits, `claude/*` branches, and agent-authored PR merges.
- **Spec-first delegation.** Jacob put a detailed PRD in README (`3236d8d`). He then had Claude turn it into two plans: `IMPLEMENTATION_PLAN.md` (`e86e5e4`, a 16-week milestone plan proposing a Vapor + Postgres + Redis + S3 backend) and `BUILD_PLAN.md` (`e6ea0ad`, a 9-phase plan with acceptance criteria and roughly 250 tests).
- **Choosing between plans.** BUILD_PLAN won: Supabase instead of a custom backend, one AI provider, Apple Speech instead of Whisper. Implementation followed its phase numbering. *Explicitly documented in BUILD_PLAN; it is inferred that the choice was Jacob's.*
- **Designing for agents.** BUILD_PLAN has a section, "Maximize AI-Assisted Development": flat modules, protocols for every service, predictable file names, "No clever abstractions… three similar view models are better than one generic one", and a test target per module so that "AI can run tests after any change". This deliberately shapes the architecture for agent work.
- **One session per phase.** Each phase was a separate Claude session, branch and PR, so context was managed by phase scoping.
- **Audit loops as verification.** Claude ran a "comprehensive audit" and fixed issues by severity (`7c4bb7a` critical → `e32f580` medium → `4fe732b` low). Jacob then pushed further remediation locally. A second Claude session audited scope against PRD + both plans (`2b87df2`), producing AUDIT_REPORT with per-phase completion percentages.
- **Correcting AI and merge damage.** `27de0ed`, "Reconcile overwritten upstream resilience and security fixes", restores guards (Supabase `ensureConfigured`, AuthService `NSLock`, download-manager logic) that the big `c2112de` had overwritten. Jacob noticed that a large change regressed earlier fixes and reinstated them. *Strongly inferred from the message and diff.* `ff1aba7` caps the placement-test length, a small, targeted product-judgment fix.
- **Not visible:** PR review comments, rejected PRs, prompts given to Claude. Verification relied on AI-written audits and there is no CI, so there is no evidence that tests were ever run.

## 6. Quality assessment (qualitative)
- **Strong:**
  - The PRD is unusually specific: personas, competitive matrix, constrained "coach, not wrapper" AI roles with word limits, CEFR progression, risks and mitigations. That gives the agents a clear target.
  - The phased plan with acceptance criteria, and the architecture tuned for agent editing, are thoughtful method choices.
  - Protocol/mock structure and many unit tests.
  - Env-based secrets with explicit "NEVER hardcode" guidance.
  - Candid self-audit that separates code gaps from content gaps.
  - *Confidence medium on structure. Low on runtime correctness (not compiled).*
- **Weaknesses / defects:**
  1. *Security architecture.* The Anthropic API key lives in the mobile client, and tier limits and rate limits are enforced client-side, so a shipped build would expose the key and let users bypass the paywall. The PRD/plan risk tables discuss cost, but no proxy exists. IMPLEMENTATION_PLAN's "Claude Proxy" was dropped when the team switched to BUILD_PLAN's Supabase approach. The audit rates this "strong shape".
  3. *Product drift.* The PRD criticizes Duolingo-style gamification (hearts), but the late feed adds "addictive" XP, combos and streaks. This may be a deliberate engagement pivot; it is undocumented.
  4. *Not runnable as committed.* No Xcode project, no assets.
  5. Very large views (audit cites 700+ line files), plus `@unchecked Sendable` and a global context registry (self-noted debt).
  6. Repo name and description (Russian) do not match the content (Korean).
- The shortcuts that look intentional (deferring content licensing, morphology, Whisper) are documented as such.

## 7. Developmental milestones
1. 03-17: PRD (`3236d8d`).
2. 03-17/18: two competing plans (`e86e5e4`, `e6ea0ad`).
3. 03-18: scaffold (`e058635`), Hangul (`f4f9394`), SRS (`ee8e4c6`), Media library (`abed8cb`), Claude 5 roles (`cbab15c`).
4. 03-19: lessons (`656a2f8`), daily plan (`2019329`), onboarding/StoreKit (`d954a4d`), offline/a11y (`261a426`).
5. 03-19: audit and remediation (`7c4bb7a`…`ff1aba7`).
6. 03-19: scope audit (`2b87df2`).
7. 03-19/20: feed + onboarding redesign (`d852dac`…`d4a4c48`).

## 8. Method changes & possible lessons
| Change | Earlier (date) | Later (date) | Trigger | Lesson | Strength | Alternative |
|---|---|---|---|---|---|---|
| Planning approach | Milestone plan with a custom Vapor/Redis/S3 backend (`e86e5e4`, 03-17) | Minimal-surface 9-phase BUILD_PLAN with Supabase, built for AI-assisted dev (`e6ea0ad`, 03-18) | Not documented | Shrink scope and infrastructure so agents can deliver end to end | Strongly inferred (BUILD_PLAN principles; later phases follow it) | Both plans requested at once, then one picked arbitrarily |
| Build → audit | Feature phases, one PR each (03-18/19) | Severity-tiered security/bug/UX/a11y audit + fixes (`7c4bb7a`, 03-19 06:11) | Phases done | Add a verification pass after bulk generation | Explicitly documented (commit messages) | Routine polish step |
| Agent PRs → direct local commits | PR merges only | 6 local direct-to-main commits (03-19) | The audit's remaining findings | Hands-on finishing and reconciliation | Documented by authorship | Local commits might themselves be AI-generated |
| Regression awareness | `c2112de` overwrote earlier fixes | `27de0ed` restores them (26 min later) | Lost guards | Big rewrites can silently undo fixes; re-check | Strongly inferred | — |
| Plan-doc sync | BUILD_PLAN had a speculative file tree | Tree trimmed or replaced (`01f1f8b`) | Code diverged from the plan | Keep the plan aligned with reality | Strongly inferred | Cosmetic cleanup |
| Scope audit against specs | — | AUDIT_REPORT per phase (`2b87df2`) | Need for a completion picture | Measure against the PRD | Explicit | — |
| Product direction | Survey onboarding + task-list Today tab | TikTok feed + cinematic onboarding (03-19 evening) | Not documented (the message says "demo-able") | Prioritize demo and engagement | Speculative | Polishing for a demo/showcase |

## 9. Capabilities, limitations, uncertainties
- **Demonstrated:**
  - Writing a detailed product spec.
  - Decomposing it into phased agent tasks with acceptance criteria.
  - Designing a codebase for agent edits.
  - Running parallel agent sessions and merging them.
  - Using AI audits as verification.
  - Spotting and repairing regressions.
  - Building an LLM-feature product with constrained prompts, caching and tier limits.
- **Uncertain:** who authored the large local commits; the fate of PR #10 and Phase 8; why the repo is named and described as "Russian".

## 10. Evidence references & verification limits
- Files: `README.md` (PRD), `BUILD_PLAN.md`, `IMPLEMENTATION_PLAN.md`, `AUDIT_REPORT.md`, `Package.swift`, `Hallyu/Core/Networking/Environment.swift`, `Hallyu/Core/Networking/SupabaseClient.swift`, `Hallyu/Core/Services/ClaudeService.swift`, `Hallyu/Core/Services/SRSEngine.swift`, `Hallyu/Features/Claude/ClaudePrompts.swift`.
- Commits:
  - Start and PRD: `r_app@0cffb4d`, `@3236d8d`.
  - Plans: `@e86e5e4`, `@e6ea0ad`.
  - Phases: `@e058635`, `@f4f9394`, `@ee8e4c6`, `@abed8cb`, `@cbab15c`, `@4fb302a`, `@656a2f8`, `@2019329`, `@d954a4d`, `@261a426`.
  - Audit and fixes: `@7c4bb7a`, `@e32f580`, `@4fe732b`.
  - Local commits: `@15613d0`, `@5e598c5`, `@01f1f8b`, `@c2112de`, `@27de0ed`, `@ff1aba7`.
  - Scope audit, feed, onboarding: `@2b87df2`, `@d852dac`, `@8c62077`, `@19e2237`, `@e962e2b`, `@d4a4c48`.
  - Final merge: `@5df44b2`.
- PRs (from merge messages only): #1–#9, #11–#15. #10 is missing.
- Limits:
  - No Swift or Xcode in the sandbox (iOS-only APIs), so no build or tests.
  - `gh` unauthenticated: no PR bodies, comments, closed PRs or issues.
  - Head branches deleted.
  - The pre-transfer origin repo is not inspected.
