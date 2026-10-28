PRIVATE — internal research file. Not for distribution without disclosure review.

# Evolution timeline — personal GitHub AI practice (2026-03-10 to 2026-10-24)

**Window.** All personal repos fall between 2026-03-10 (`etta_app`, earliest commit) and 2026-10-24 (`genesis` run branch, latest commit). The window is about 7 months, and there are no personal repos before 2026. Activity is bursty: March (about 10 days), June to July (dense), a gap in August with no commits found, then September and October. "Evolution" here means change over 7 months in one person's hobby and self-directed work. It is not a multi-year trajectory.

**Attribution rules.** Agent authorship is credited only from `Co-Authored-By`/`Claude-Session` trailers, bot accounts (`google-labs-jules[bot]`, `Etta Agent`), agent instruction files (`AGENT_BRIEF.md`, `.claude/agents/*`, `AGENTS.md`, `CLAUDE.md`), `codex/*`/`claude/*` branch names, or explicit commit-message statements. Model names are copied from trailers as written.

**Evidence labels.**
- [E] = explicitly documented in the repo.
- [I] = inferred by synthesis from sequence.
- [N] = newer-tool capability: a change that may reflect a new tool or model rather than learned practice.

## Phase 1 — Spec-first app delegation and AI self-audit (March)

| Date | Event | Evidence | Label |
|---|---|---|---|
| 03-10→03-11 | Jacob writes a PRD ("Minimal Surface Area" v1.1). Claude Code web sessions build a macOS tutor app through PRs that Jacob merges | `etta_app@7a4a1eb`, `etta_app@2848342`; 68 `Claude` commits across 25 session trailers | E |
| 03-11 | Multi-agent audit and consolidated action plan. A later parallel agent re-evaluation of 85 findings shows 20 fixed, 32 partial, 33 not fixed. Both sit on unmerged branches | `etta_app@97a382e`, `etta_app@ce7308b` | E |
| 03-12 | Prompt mode-slicing. The stated trigger is token waste ("~800-1000 tokens saved per call") | `etta_app@d4b9bb2` | E |
| 03-18 | Second app. The build plan has a section "Maximize AI-Assisted Development" | `r_app@e6ea0ad:BUILD_PLAN.md` | E |
| 03-19 | Jacob's own commit "Reconcile overwritten upstream resilience and security fixes", restoring work that a later agent commit (`c2112de`) had overwritten | `r_app@27de0ed` | E |
| 03-19 | Scope audit against PRD/BUILD_PLAN. No build is possible (no xcodeproj) | `r_app@2b87df2:AUDIT_REPORT.md` | E |

**Characteristics.** Jacob writes the spec. Agents build. Verification is mainly AI-on-AI audit with self-reported status, and there is no CI. Human review shows up as merges plus a manual reconcile commit.

## Gap — April and May

No commits in any personal repo. Whatever happened in this period is not visible.

## Phase 2 — Research synthesis, AI-product prototypes, first deterministic gates (June)

| Date | Event | Evidence | Label |
|---|---|---|---|
| 06-09 | Browser game uploaded through the web UI. No AI evidence | `ai_game` main, PRs #1–6 | E |
| 06-11 | Same day: etta rebuild (M0–M5, bugsweeps, PRs merged in 2–5 s); Liquid AI prep course with Opus fact-check waves and verdict taxonomy; study guide built with 22 parallel agents, each owning an isolated chunk, plus locked facts and invariants | `etta_app_update` (Etta Agent identity); `liquid-ai-prep-course` PR #3–5; `liquid-ai-study-guide@1c4a924` | E |
| 06-11 | Provenance honesty: the source description changes from "internal briefs" to "AI-generated research reports … not insider knowledge" | `liquid-ai-prep-course@603753d` | E |
| 06-11 | Hoverable citation layer; a revert and re-land through a PR | `liquid-ai-study-guide@b7050eb`, `@55c154e` | E |
| 06-14 | AI-product prototype moves from prompt-only hints to hints grounded in parsed world data | `Liquid_SDK_Test@a3c3294` | E |
| 06-15 | Spec→bulk build of a platform plus "LLM as compiler" content. **Synthesis re-ran the playtest: concierge fails (room-13 unreachable)** | `TextAdventures@4cc5000`; `TextAdventures-Content@03afa34:games/concierge/game.json` | E (claim) / verified failure |
| 06-15 | TextAdventures family abandoned after one session | last commit `TextAdventures` 05:35Z | E |
| 06-28 | Gated research pipelines: single writer (`a9ecbb9`), 13+ deterministic gates, golden set with negative controls | `chip@a9ecbb9`, `chip` golden/selftests | E |
| 06-28 | **Agents bypassed the hardened path.** Re-ingestion plus an `AGENT_BRIEF.md` "no dataset writes / no git" boundary | `chip@75d4fa1:AGENT_BRIEF.md` | E |
| 06-28 | Root-cause and precision commits, e.g. "tighten availability scan to high-precision lifecycle phrases" | `chip@24358dd`, `b6f9c30`, `ce9119c`, `fa14273` | E |
| 06-28 | Tiered Haiku/Sonnet/Opus subagents with G1–G8 gates. Then a reshape to categorical profiles from model knowledge, without quote gates (precision traded for coverage) | `OEM@52648ce:.claude/agents/oem-extractor-*.md` | E |

**Characteristics.** Two techniques appear for the first time: parallel-agent partitioning with invariants (06-11), and code-enforced gates with negative controls (06-28). On 06-15 the TextAdventures repos lack both, so adoption is inconsistent. The chip boundary commit is the first explicitly recorded "agents don't follow prose instructions" lesson.

## Phase 3 — Evaluation rigor, agent comparison, triangulation (July)

| Date | Event | Evidence | Label |
|---|---|---|---|
| 07-01→07-02 | VLM demo. Reframed after real outputs proved noisy. Public unauthenticated GPU endpoint removed as a denial-of-wallet risk | `liquid-token-budget-slider@90927bc`, `@18bcd91` | E |
| 07-02→07-05 | Pinned, provenance-strict benchmark with a referee lane and a numbered change log including self-correction and root cause. HANDOFF.md written; write-up unfinished | `Liquid-Moondream-450M-Benchmark` (46 Opus 4.8 commits); pytest 198 pass (synthesis re-run) | E |
| 07-02→07-03 | Synthetic benchmark. Breadth-first budget planner; negative lens-axis finding recorded, with fixes marked UNVALIDATED; steps 3–5 never built | `home_security_benchmark@61eb1cb`, `@068e7e6:FINDINGS_lens_axis.md` | E |
| 07-03 | etta rebuild revisited: "154 findings, adversarially verified". Fixes include a 100% dashboard crash and an infinite onboarding loop that had shipped behind June's green gates | `etta_app_update@be2d460` | E (**regression revealed**) |
| 07-03 | Empty repo created | `token-budget-liquid` | E (abandoned) |
| 07-07 | **Same PRD given to Claude and to Jules** (identical md5) | `marketplace_prototype@16f93c7`, `prototype_Jules@f912077` | E |
| 07-07→07-08 | Claude path: adversarial spec review with 25 findings fixed; CI against real Postgres | `marketplace_prototype@b660d77`, `@48e1a8c:.github/workflows/ci.yml` | E |
| 07-07→07-20 | Jules path: 29 PRs, 4 merged, 25 left open, including real security fixes | `prototype_Jules` PR JSON | E (inconsistent follow-through) |
| 07-19 | Methodology comparison against two outside builds; exact reproduction verified by the investigator | `billboard@486ddd0:output/METHODOLOGY_COMPARISON.md` | E |
| 07-19→07-22 | Two parallel sessions left unmerged; strategy reversal not reconciled in docs | `billboard` branches | E (plateau: doc drift) |

**Characteristics.** Verification shifts toward independent instruments: a referee harness, cross-build comparison, and CI against real services. Cost and security awareness becomes explicit (`18bcd91`). The `be2d460` July fix is the clearest regression in the portfolio: June's process passed defects that a later adversarial pass found [E]. Whether the improved July audit reflects practice learned since June or a newer model (`Sonnet 5` trailer) cannot be separated [N].

## Gap — August

No commits in any personal repo.

## Phase 4 — Large orchestrated research with line-pinned provenance (September)

| Date | Event | Evidence | Label |
|---|---|---|---|
| 09-15 | PRD-first browser game. Answer surface correlations removed; a double-tap bug fixed | `ashby@65f4e0e`, `@cbcb985`, `@f8d33bf` | E |
| 09-23→09-24 | KB and site research. 24 analysts (15 working from templates), source isolation, `[[kb:path#Lnn]]` citation tokens, 158 conflicts, a workbook live-checked line by line and then deduplicated | `pmm@2718b66`, `@2071a24`, `@a907067` (= Clearly-Rated shared history) | E |
| 09-24 | Parallel product-tour branch with an expert-panel review; left unmerged | `Clearly-Rated@e8989a0` | E |

**Characteristics.** Commits now come from the `Claude` identity directly, and Jacob's visible hand is the repo setup and the direction recorded in commit messages [E]. Line-level citation tokens extend the June citation layer [I].

## Phase 5 — From one research run to a reusable, code-enforced method (October)

| Date | Event | Evidence | Label |
|---|---|---|---|
| 10-01→10-02 | Withheld repo; staged agent document reconciliation (process only) | `BTCsecrets` | E (withheld) |
| 10-19→10-21 | Large research run on an unmerged branch: 796-claim fact check, author cuts recorded, a revert | `ai_game@ac8fe26`, `@648333e` (branch `blackrock-aladdin-research`) | E |
| 10-21 21:11Z | Reusable 351-line research prompt extracted, with an **explicit lessons list**: "errors that survived longest were conceptual, not factual"; "Agents' hand-back summaries miss things"; leave the heavier review rounds out unless a document goes outside | `ai_game@6698994:pmm-research-kit/PROMPT.md`, `ai_game@fb0038c:pmm-research-kit/README.md` | E (articulated lesson) |
| 10-21 21:19Z | The same prompt (byte-identical) used as the input for a new company run | `airops@c1ba3ba:00-inputs/PROMPT.md` | E (transfer) |
| 10-22 03:56Z | Agents mistook the user's status question for their task. Every brief now opens with "TASK TYPE … WORK, NOT A STATUS QUESTION" | `airops@8581d67` | E |
| 10-22 04:13–04:30Z | Verification narrowed to cited facts for cost reasons; audits time-boxed | `airops@1e2e6f5`, `@353addc`, `@7bf38f3` | E |
| 10-22 | Jacob rewrites the 3,399-line prompt in the README and appends §19 "Execution integrity and machine-enforced completion": the orchestrator "is not the authority for declaring … complete" | `airops@0398294:README.md`, `airops@0d21793:README.md` | E |
| 10-23 10:47–11:25 | Codex branches turn the prompt into a constitution, failure registry (68), requirement inventory (1,732), control plane, and CI | `airops@fd5e029` (branch `codex/research-agent-refactor`) | E/[N] (Codex) |
| 10-23 11:28→15:07 | The refactor is published as its own tool (identical README md5) and grows through stacked `codex/*` branches: CLI runner, SQLite scheduler, saturation discovery, diagrams, brand guide, cache, then lean | `research_prompt@5fab799`→`@1a4d35c`; 45 tests OK (synthesis re-run) | E |
| 10-23→10-24 | Live run of the tool. Real failures (robots, DNS blocks, share-link pollution) fixed with tests, on the branch only. Run stops mid-capture; brand guide produced | `genesis@d073470`, `@7c9d11d`, `@3ee0288`, `genesis@7c2fff2:WORKFLOW_STATE.md` | E (abandoned or paused) |

**Characteristics.** This is the only phase where lessons are written down as lessons and then carried into later work: the kit README feeds airops, then §19, then the control plane. The move from prose rules to code-enforced gates repeats the chip pattern from 06-28, now generalized. The tooling shift to Codex and `gpt-5` workers [N] coincides with the move toward code, so part of the "control plane" capability may reflect the new tool.

## Cross-cutting patterns over the 7 months

**Recurring habits** (seen in 3 or more phases):
- Spec or PRD first: etta_app, r_app, ashby, marketplace, the research prompts.
- Audit or adversarial review loops: etta_app → etta_app_update → marketplace → airops reviewers.
- Provenance discipline: study guide → chip quotes → pmm line tokens → airops receipts → control plane.
- Handoff and state docs: Moondream HANDOFF, airops WORKFLOW_STATE, genesis WORKFLOW_STATE.

**Plateaus** (no visible improvement):
- Doc drift after pivots: stale READMEs in etta_app, liquid-ai-prep-course, slider, Moondream, marketplace, ashby, billboard, OEM, and research_prompt's default branch.
- PR merges in seconds without visible review: etta_app_update in June, marketplace in July.
- Unmerged or stranded branches every month from March to October: etta_app audit, prototype_Jules, billboard, Clearly-Rated tour, ai_game research, airops codex, genesis fixes.

**Regressions:**
- `TextAdventures-Content@03afa34` playtest fails on re-run.
- June etta "green" gates vs the `be2d460` defects.
- `OEM@52648ce` drops the quote gates the same night it built them.

**Abandoned directions** (abandonment is not counted as failure):
- TextAdventures family (06-15).
- token-budget-liquid (07-03).
- home_security steps 3–5.
- prototype_Jules triage.
- Moondream write-up.
- genesis run, mid-capture.

**Inconsistent adoption.** Gates and negative controls appear on 06-28 but not in ashby in September (tests not committed) or in the billboard-map tuning in July. Fail-closed design arrives in October, but its fixes stay off `main`.
