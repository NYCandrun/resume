MANIFEST | airops | PRIVATE | research workflow (multi-agent company-research pipeline + reusable prompt; later tooling/refactor experiments) | complete | gh unauthenticated (used lead's pre-fetched PR/issue JSON); large blobs (~1.2 GB of captures) not opened individually; codex-branch evaluation artifacts not in repo; Claude/Codex session transcripts not available

DISCLOSURE: (1) Personal context is written into the repo: `00-inputs/PROMPT.md` ("I am a product marketing manager starting at a new company"), `WORKFLOW_STATE.md` §1 and `prompt/CHANGES.md` (deliverable renamed "company brief … so it can be shared with the company before an offer"). Treat as sensitive personal information. (2) One user-provided, non-public fact about a named AirOps employee (source IN-004 / fact ORG-475, grade "I"). The repo itself says to remove it before sharing outside the company (`06-checks/final-report.md`). This is the only item that may have come from the company and not from public sources. Ownership/disclosure for this item is ambiguous, so I describe it only at a high level. Everything else is public-source research about a third-party company, not employer-owned code or data. (3) AirOps' licensed fonts (Saans, Serrif, Saans Mono) are committed at `05-synthesis/design/fonts/*.woff2` and embedded in the PDFs. This goes against the prompt's own rule against redistributing proprietary fonts. (4) About 1.2 GB of captured third-party content (web pages, transcripts, competitor docs) and a roster of named people (`01-sources/people-roster.md`, `tools/lists/people-urls.tsv`). (5) Credential-like strings are present inside captured third-party HTML at `04-competitors/athenahq/01-sources/third-party/2026-10-21 ycombinator.com - Y Combinator company page.html` and `01-sources/third-party/2026-10-21 influencermarketinghub.com - …Linqia….html` (main@15ee249). They are probably public site client keys and were not copied. (6) Claude Code session URLs appear in commit trailers. Suitability to share: the reusable prompt (`README.md`/`prompt/`), `tools/`, and the `codex/research-agent-refactor` branch could be shared after review. The full repo should not be shared as-is because of items 1–5.

# airops — personal repository report

## 1 Identity
- Personal repo, owner NYCandrun, visibility PRIVATE. It is not a fork (`repos.json`). It was created 2026-10-21T20:00Z and last pushed 2026-10-23T17:53Z.
- **Type:** an AI-agent research workflow. Claude Code runs a multi-phase process to build a sourced research repository and a branded, cited "company brief" PDF about AirOps (www.airops.com). The intended user is Jacob himself, preparing to get up to speed on that company (stated in the prompt). Later work makes the method a reusable, generic prompt ("The company URL is in my chat message"). It then adds two experiments on unmerged branches: a deterministic integrity control plane, and a URL-to-brand-guide prompt with an evaluation harness.
- **Maturity:** the main run finished and was closed (`WORKFLOW_STATE.md` §0, `06-checks/final-report.md`). The prompt is on v3+ with an appended "execution integrity" amendment. The refactor and brand-guide branches are experimental and unmerged.

## 2 Dates and attributable contributions
- First commit: `7ea8d61` 2026-10-21 20:00Z, "Initial commit", NYCandrun via GitHub web. Latest commit: `c97a854` 2026-10-23 17:51Z on `codex/brand-guide-workflow`.
- Identities seen (all branches): **Claude** <noreply@anthropic.com>, 123 commits, every one with `Co-Authored-By: Claude Opus 5.5` and a `Claude-Session:` trailer. **NYCandrun** (jacobnikolau767@gmail.com, GitHub web), 6 commits. **Jacob Nikolau** (local identity `jacobnikolau@Jacobs-MacBook-Pro-2.local`), 7 commits on the `codex/*` branches with no trailers. No bot accounts.
- Activity periods:
  - **Run 1:** Claude, 2026-10-21 21:13Z to 2026-10-22 09:30Z (about 12 h). It went through four container restarts, per `WORKFLOW_STATE.md`.
  - **Jacob's README/prompt edits:** web UI, 2026-10-22 09:33Z to 16:48Z.
  - **Codex sessions (by branch name):** 2026-10-23 14:47Z to 17:51Z.
- Jacob's attributable contributions are dated 2026-10-21 to 2026-10-23. They are the initial commit, the original prompt (`00-inputs/PROMPT.md`, committed by Claude in `c1ba3ba` as a "provided file"), the README rewrites, and the user decisions recorded in `WORKFLOW_STATE.md` §5. Whether he wrote the codex-branch content or it was agent-generated is strongly inferred to be agent-generated (Codex), going only by the branch-name convention.
- There is no imported history, no squash and no fork. All of the Claude branch's work reached main through PR #1 as a merge (`490a201` also merged main into the branch).

## 3 Branch and history coverage
- Default branch `main`. Remotes: `claude/focused-cori-ndcral`, `codex/research-agent-refactor`, `codex/brand-guide-workflow`.
- `claude/focused-cori-ndcral` has 0 commits that main lacks and is 5 behind (the NYCandrun README edits). It was fully merged by **PR #1** "Add initial AirOps research sources" (author NYCandrun, created 2026-10-22 03:34Z, merged 09:31Z). The PR body is just the first commit's message with Claude trailers, so it is an agent-generated description. No issues.
- `codex/research-agent-refactor`: 6 commits, 80 files, +7,044 lines, **unmerged**. It adds `RESEARCH_CONSTITUTION.md`, `WORKFLOW.yaml`, `FAILURE_REGISTRY.md` (68 invariants), `REQUIREMENT_INVENTORY.csv` (1,732 rows), `MIGRATION_MAP.md`, `prompts/core|phases/*`, the `research_control/` package (schemas, validators, gates, reconciliation, tests), and CI in `.github/workflows/research-integrity.yml`.
- `codex/brand-guide-workflow`: 1 commit, 6 files, +1,080 lines, **unmerged**. It adds `prompt/URL_TO_BRAND_GUIDE.md` (720 lines), `prompt-tests/evaluate_brand_guides.py`, and three evaluation reports. The generated test artifacts are "intentionally excluded" and so cannot be checked.
- History on main is dominated by about 45 "Work in progress" checkpoint commits. These follow the prompt's push-after-every-step rule.

## 4 Actual functionality / research workflow
Pipeline (phases 0–6, per `prompt/PROMPT.md`, `WORKFLOW_STATE.md`, `RUN_HISTORY.md`):
- **Phase 0 (scope):** `00-scope.md`.
- **Phase 1 (capture):** 1,063 AirOps sources (952 P / 22 S / 88 T / 1 I) and 2,649 competitor sources across 8 competitors. This includes 248 transcripts made with yt-dlp captions first and Whisper as a fallback. Everything is registered in `01-sources/MANIFEST.csv`, and what could not be captured is logged in `BLOCKED.md`.
- **Phase 2/2b (facts):** a facts store of 9,179 rows, each with a verbatim quote, source ID, location, date, grade, `about` and `said by`.
- **Phase 3 (verification):** first-round verification found 2,801 confirmed, 271 corrected and 0 unsupported. Later, a "lazy" Opus pass ran only on the 443 cited facts (336 confirmed, 107 corrected).
- **Timelines:** timelines with currency and supersession flags.
- **Phase 4 (synthesis):** nine files in `05-synthesis/`.
- **Phase 5 (review):** six independent reviewers (technical, devil's advocate, two insiders, two Sonnet editors) produced 178 findings, triaged in `06-checks/review-decisions.md`.
- **Phase 6 (output):** a branded HTML/PDF brief (`07-final-report/company-brief.pdf`, 20 pages; `one-page.pdf`).
- **Citations:** superscript per-source numbers that deep-link via text fragments, plus a citation checker tested with planted errors.
- **Visual audit:** a script-based overflow check plus an agent that reviews every page image.
- `RUN_HISTORY.md` (built by `tools/build_run_history.py`) records 40 workflows and about 1.67 B total tokens.

**Verified by me:**
- `pdfinfo` shows the brief is 20 pages, and its first pages contain coherent, cited prose and exhibits.
- `python3 tools/test_check_citations.py` (offline, works on temp copies) printed "caught" for all 6 planted errors and "real files still clean: True" in about 106 s. The working tree stayed clean.
- On an extracted copy of `codex/research-agent-refactor`, `python3 -m unittest discover -s research_control/tests` ran **25 tests OK**. `check_phase_gate.py --phase capture` failed closed with "missing or empty report …", which is the designed UNKNOWN behaviour.

**Not verified:** the factual accuracy of the brief, live links, whether fact counts match the store, the brand-guide scores (92/100 etc.), and whether the refactor would pass on the real run's data.

## 5 How Jacob uses or builds with AI
This repo is mainly about **directing agents to do research and engineering the instructions that govern them**. It does not build an AI product.
- **Task specification:** an original 351-line prompt (`00-inputs/PROMPT.md`) sets the goal, a three-layer repository, receipts and phases.
- **Live steering:** this is explicitly documented as dated user decisions in `WORKFLOW_STATE.md` §5:
  - cut Wayback after it was blocked; no secondary-source search; do not bypass the Vimeo/Cloudflare challenge;
  - keep already-verified material; choose to keep cited-fact verification "as is";
  - skip the freshness pass (07:12); set a currency-wording rule (07:15);
  - token batching (about 60k words of input, at most 2 deliverables per agent, never combine independent-judgement roles; 06:05);
  - brief length 10–15 pages; American English check;
  - add a portfolio exhibit placed in one location only (08:00/08:02);
  - ignore stop-hook commit reminders; supply one fact.
- **Context management:** a checkpoint file written before compaction, compact phase briefs (`tools/briefs/*.md`) in place of the full prompt, agent returns of about 10 lines, and per-agent scratch folders.
- **Delegation design:** a single orchestrator owns shared state, workers get non-overlapping slices, Opus handles judgement and Sonnet handles mechanical editing, and reviewers work in separate contexts.
- **Verification:** planted-error tests, a script audit with an Opus sample, and machine checks before model checks.
- **Lesson capture:** the run had to fold its decisions into prompt v2 (`prompt/CHANGES.md`). Jacob then rewrote the README himself (`0398294`, +3,184/−367; `5330d4a` markdown cleanup). The pasted text uses "⸻" separators, which suggests it was drafted outside the repo, but the tool used is not determinable. He also appended §19 "Execution integrity and machine-enforced completion" (`0d21793`) and renamed the Phase 3 heading (`15ee249`).
- **Second agent family:** he then had Codex turn that prompt into a constitution/workflow/control plane, and generate and blind-test a second prompt.

## 6 Subjective quality assessment
**Strengths (high confidence):**
- Unusually rigorous provenance design. Grades P/S/T/I, verbatim receipts, publish and modified dates kept apart, competitor claims kept in competitor folders, and conflicts presented rather than resolved (`WORKFLOW_STATE.md` §7 lists e.g. Solo 20k vs 35k tasks).
- Explicit uncertainty. "Three findings I am least sure of" includes a breadth bias in the competitor rubric that favours AirOps (28/30).
- Honest blocked list and evidence limits.
- Citation checks that are deterministic and themselves tested.
- The refactor's fail-closed UNKNOWN semantics and its failure registry show strong systems judgement about agent false-success.

**Weaknesses:**
- 5,673 of 9,179 facts are only script-checked. The repo states this, and it is an intentional token tradeoff.
- Heavy process overhead: about 1.67 B tokens and 3,399-line prompt (per `REFACTOR_REPORT.md`) for one company brief. The prompt is so long that a refactor was needed to make it usable.
- Proprietary fonts and large third-party captures were committed, contrary to the prompt's own font rule.
- `tools/` has many one-off batch scripts (`site_video_batch_11.py`, `build_transcripts_video_backlog_18.py` …). That fits a run but not reuse.
- Known tool defects were left open, e.g. `tag_fact_entities.py` produced 66 false "said by" flags.
- Codex branches are unmerged, and their evaluation evidence is excluded, so the scores are self-reported (medium-low confidence in those claims).
- The refactor's own report says adapters and legacy tools are unfinished and that the README remains the source of truth.

## 7 Developmental milestones
1. 10-21 21:13Z: inputs (a brand guide and three prior AirOps reports, used as a "scoping checklist, never as receipts") and prompt v1.
2. 22:49Z: Wayback cut. 23:12Z: Phase 1 closed.
3. 10-22 01:28Z: facts and independent verification.
4. 01:53–01:55Z: competitor videos dropped, then restored (`30e6714` → `cc0752f`/`fda74a2`). This was a scope reversal.
5. 02:24Z onward: prompt v2 iterations (parallel workflows, TASK TYPE line, script-only merge, lazy verification, currency rules, token savings).
6. 03:53–03:56Z: extraction workflows aborted because agents "answered a status question" (`RUN_HISTORY.md`). They were relaunched with the TASK TYPE fix (`8581d67`).
7. 06:28Z: cited-fact verification. 06:45Z: Phase 5 review. 07:13Z: Phase 6 brief.
8. 07:38–09:27Z: deep-link citations, renamed to "company brief", a citation checker with planted errors, Ahrefs rescoring and a fact-DB correction, and a separate-agent visual audit.
9. 09:30Z: README equals the revised prompt. PR #1 merged.
10. 10-22 Jacob's rewrite of the README prompt plus §19 integrity amendment.
11. 10-23 Codex refactor into a control plane with CI, then the brand-guide prompt with a blind evaluation.

## 8 Changes in working method and possible lessons
- **Status messages derailing agents.** *Earlier* (10-22 03:53Z): extraction agents read the user's progress question as their task and stopped. *Later* (`8581d67`, 03:56Z): every brief opens with "TASK TYPE … WORK, NOT A STATUS QUESTION". *Lesson:* agents see the user's latest message, so delegation briefs must be robust to it. Evidence: explicitly documented (`RUN_HISTORY.md`, `WORKFLOW_STATE.md` §5).
- **Verification cost.** *Earlier* (v1, 10-21): verify every fact, with layered Sonnet and Opus audits. *Later* (`1e2e6f5`/`353addc`, 04:13–04:30Z): scripts on all facts and a single Opus pass on cited facts only. *Trigger:* token cost and the size of the store. *Lesson:* spend model judgement where it reaches the reader. Evidence: explicitly documented (`CHANGES.md`). *Alternative explanation:* time pressure.
- **Unbounded audits.** "Time-box the script audit" (`7bf38f3`). The checkpoint notes 40 minutes wasted tuning word rules. Explicitly documented.
- **Agent assertion vs evidence.** *Earlier:* completion was declared by the orchestrator, with self-reported gates. *Later:* Jacob's §19 (10-22 `0d21793`) says the orchestrator "is not the authority for declaring a phase or the project complete." The Codex refactor (10-23) then implements a ledger, reconciliation, gates and release hashing. Registry entries F001/F005 concern "claimed success without output" and "partly processed" work lists. *Lesson:* agent output must be machine-reconciled. Evidence: strongly inferred. The documents name these failure classes "observed or anticipated", without tying them to specific incidents in this run.
- **Audience framing.** "onboarding brief" became "company brief" so that it could be shared before an offer, with copy changed to avoid presuming the job. Explicitly documented (`CHANGES.md`).
- **Monolithic prompt to layered architecture.** The single 3,399-line README became constitution + workflow + per-role prompts + code (10-23, unmerged). Strongly inferred to be about maintainability and context limits. *Alternative explanation:* an experiment in prompt portability.
- **From one run to reusable method.** The brand-guide prompt was generalized and blind-tested on Raycast and Redgate. Documented only through self-reports.

## 9 Demonstrated capabilities, limitations, uncertainties
**Demonstrated:**
- Specifying and steering a long multi-agent research run.
- Cost and context management.
- A provenance-first research design.
- Turning failures into prompt rules and machine checks.
- Commissioning tests for agent-built tools.

**Uncertainties:**
- How much of the codex-branch content Jacob edited.
- Whether the README rewrite was drafted with another AI tool.
- The accuracy of the self-reported metrics.

## 10 Evidence references and verification limits
**Files and commits:**
- `airops@c1ba3ba:00-inputs/PROMPT.md`, `airops@15ee249:README.md`, `prompt/CHANGES.md`, `WORKFLOW_STATE.md`, `RUN_HISTORY.md`, `06-checks/final-report.md`
- `07-final-report/company-brief.pdf`, `tools/test_check_citations.py`
- Commits `8581d67`, `1e2e6f5`, `353addc`, `7bf38f3`, `30e6714`, `cc0752f`, `0398294`, `0d21793`

**Branches:**
- `origin/codex/research-agent-refactor@fd5e029`: `REFACTOR_REPORT.md`, `FAILURE_REGISTRY.md`, `research_control/tests/`
- `origin/codex/brand-guide-workflow@c97a854`: `prompt-tests/reports/*.md`

**PRs and issues:** PR #1 (merged). No issues.

**Limits:**
- gh was unauthenticated, so I relied on the lead's JSON.
- Session transcripts are unavailable.
- Captured media and binaries were not reviewed.
- The workflow was not re-run, because it needs network access and paid models.
