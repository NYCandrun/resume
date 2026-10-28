MANIFEST | home_security_benchmark | PRIVATE | research workflow / dataset-generation pipeline (synthetic VLM benchmark) | complete (PR/issue listing blocked: gh CLI unauthenticated in sandbox) | single-day history (2026-07-02→03); pre-repo experimentation (24-agent "swarm v1", lever A/B, "breadth v2") not in git; QA reviewer workflow ("hsg-qa-review") not committed; no paid API calls made, so generation not re-executed

DISCLOSURE: No credentials found. `.keyenv` (Gemini keys) is gitignored and never appears in history (searched all commits for `AIza`/key files; `scripts/gen.py` only reads the file). All 356+24 images are AI-generated synthetic scenes (Gemini), not real camera footage; no third-party personal data observed. Minor personal info: every `.meta.json` sidecar and `scripts/stop_at_500.sh` embed the absolute local path `/Users/jacobnikolau/Desktop/hsg-grounding-bench/...`; author email is a local hostname address. Low-level context note: `BENCHMARK_SPEC.md` refers to "the docs' headline promise", "buyers", and a "sibling repo" with a RefCOCO-M grounding lane and `scoring/metrics.py`; README frames it as what "a company" needs before shipping. Nothing in the repo is identifiably employer data or proprietary code, so I did not flag it as ownership-ambiguous, but the lead may want to confirm the "docs" being referenced. Repo is ~319 MB (images committed). Looks suitable to share after scrubbing local paths from sidecars.

## 1. Identity
- Personal repo of NYCandrun, private, default branch `main`, not a fork (repos.json: created 2026-07-03T02:00:18Z, pushed 04:37:25Z).
- Purpose: build a contamination-resistant, single-frame **home-security VLM benchmark** for grounding, counting, and scene description (incl. negatives / false-alarm suppression), using Gemini-generated images whose ground truth is known by construction (README.md, BENCHMARK_SPEC.md). Intended users: whoever evaluates small on-device VLMs for security cameras.
- Type: research workflow / data-generation pipeline. Python stdlib scripts + JSON/Markdown catalog and prompt library; Gemini image API (`gemini-3.1-flash-image` @1K).
- Maturity: **step 2 of 5 partly done**. Catalog (106→118 events), prompt library (1,054→1,174 stems), generator, metadata sidecars, and a 356-image v0 set exist. Annotation (step 3), metrics/scoring (step 4) and difficulty reporting (step 5) are **spec-only**: all 356 sidecars have `annotation_status: auto_tagged` with null bbox/count/caption fields.

## 2. Dates & contributions
- First commit `1653cc2` 2026-07-02 22:00 −0400; latest `e3cf4b8` 2026-07-03 00:37 −0400. 15 commits in ~2.6 hours; one branch.
- Single author/committer identity: `Jacob Nikolau <jacobnikolau@Jacobs-MacBook-Pro-2.local>` (14 commits on 07-02, 1 on 07-03). No bots, no other humans.
- 7/15 commits carry `Co-Authored-By: Claude Opus 4.8 <noreply@anthropic.com>` (1653cc2, d3e5b9c, 9ec4b92, e09c98b, 3accbd2, 3fa5711, d0a83c1); the other 8 have no trailer.
- Imported history: the initial commit already contains a 106-event catalog, 1,054-stem library, `LESSONS_LEARNED.md` "distilled from ~100 single-image tests (v1 swarm, lever A/B, breadth v2)", 24 agent QA reports, and a working generator. The working directory was `hsg-grounding-bench` (paths in sidecars/scripts). That earlier iteration is not reconstructable from git.

## 3. Branch & history coverage
- Branches: `main` only (`origin/HEAD -> origin/main`). Nothing unmerged, no experimental branches.
- PRs/issues: `gh pr list` / `gh issue list` failed (CLI not authenticated in sandbox). With one branch and direct commits, PRs are unlikely, but this is **unverified**.
- History is linear with no squashes visible. The large data commit `d0a83c1` adds 746 files (356 images + sidecars, plus `data/raw/` 24 swarm images).

## 4. Actual functionality / research workflow
Inspected: every Markdown doc, all scripts, catalog/prompt JSON, sample sidecars, one image. Executed offline on a /tmp copy (not the clone): `batch_generate.py --dry-run --target 600` and `counting_plan.py --dry-run --n 400`. No API calls made.
- **Pipeline**: `catalog/events.json` (events × category × task_type) → `prompts/prompt_library.json` (content-only stems, ~10/event, lint-checked per PROMPT_DESIGN_REPORT.md) → `scripts/compose.py` (stem + variant {positive, false_alarm, empty, obstruction} + condition {day/night/inclement or day/dim/IR} + device profile {aspect, lens, mount}) → `scripts/gen.py` (REST call, multi-key rotation, advance key on "credits are depleted" 429, backoff on 429/5xx, no-image refusals don't burn keys) → `scripts/batch_generate.py` (threaded, resumable, breadth-first coverage-aware planner, 1/50 random QA queue to `logs/qa_queue.jsonl`, 12-min pacing every 500) → `scripts/metadata.py` sidecars with task applicability, difficulty, provenance (`prompt_sha`).
- **QA loop**: adversarial sub-agent image review (results in `QA_REPORT.md`, two batches of 12, keep-rate 0.167 each, per-lens/per-device breakdown). The reviewer prompt/workflow itself is not in the repo.
- **Verified**: 356 images, 106/106 events covered (docs); files are JPEG bytes (`FF D8 FF E0`) despite `.png` extension. A sampled image (`child_in_garage__false_alarm_dim__indoor_pan__st02_s0`) visibly shows the fisheye barrel look and what looks like a ceiling device, matching the documented failure modes.
- **Dry-run output (HEAD)**: 1,174 stems, 118 events; 244 new jobs for target 600, skewed to obstruction (117) and empty (74), as intended to fill thin slots.
- **Counting plan (`e3cf4b8`)**: `counting_plan.py` only plans and prints. It has no generation call, and its outputs would go to `pictures/`, not `data/scale/`. The dry run reproduced the 43/42/15% split.

## 5. How Jacob uses / builds with AI
- **Using AI to build** (Claude co-authored commits) **and orchestrating agents for research/QA**. Direct evidence: Claude trailers; `master_style.md` "calibrated from 24-agent swarm v1"; `agent_reports/*.md` (per-image structured reviews: query, groundable objects, realism 1–5, keep yes/no); `agent_reports/refine_*.json` (agent-authored stems); `genc.py` "for refinement agents"; "adversarial sub-agent review"; PROMPT_DESIGN_REPORT "lessons-informed design pass (reads LESSONS_LEARNED.md)".
- **Directing**: `counting_plan.py` docstring records "User directive (2026-07-03)" with the exact target distribution. Commit `3fa5711` records "Chosen path: fix now, keep 356, regen later (budget depleted)", which reads as a human choice between options (strongly inferred). Commit `50b226c` reverses an agent design choice (per-device QA guarantee dropped for pure random).
- **Context management**: `LESSONS_LEARNED.md` is written as context for later agents ("Read this BEFORE authoring stems… don't make the model re-learn them at scale"). `HANDOFF.md` is a "restart entry point for the next session". README rewritten "in plain English" for non-technical readers.
- **Verification**: lint gate on stems; adversarial QA with a numeric haywire threshold; confirming the lens finding on a second scene-diverse sample to rule out a pool-scene artifact (`068e7e6`); an explicit regen gate (keep-rate ≥0.7) before the fixes are trusted.

## 6. Quality assessment (confidence: moderate-high for the pipeline, high for the docs)
Strengths:
- Strong experimental hygiene around generator failure. The lens failure was caught by sampled QA, confirmed on a second diverse sample, and root-caused per lens class. Fixes were labeled **UNVALIDATED**, sidecars were stamped `lens_reliable=false`, and a gate was set. Honest status reporting throughout (README "What went wrong", DATASET_v0_356.md "Known issues").
- Benchmark design is careful: dimensions kept separate, hallucination/negatives built in (~31% absent), referring expressions authored post-hoc (a documented lesson), and `must_mention`/`must_not_hallucinate` caption checklists planned.
- Budget-aware engineering, with fixes driven by real problems: a breadth-first planner (`61eb1cb`), key rotation, a resumable design, and the filename-collision fix (`9ec4b92`, which documents a ~636 unique-image cap).
Weaknesses / defects:
- **Stale or inconsistent docs after the last commit**. README/HANDOFF still say 106 events / 1,054 stems, but HEAD has 118 / 1,174. The `counting_plan.py` docstring says the general planner "EXCLUDES counting events", but `build_jobs` has no such filter: the dry run schedules `people_count_*` / `packages_count_*` jobs. That contradicts the intended count distribution (verified defect). The `compose.py` header docstring still lists fisheye/telephoto. Docs say JPEG while files use the `.png` extension.
- **Provenance gap**: sidecars store `prompt_sha` but not the stem/full prompt. `compose.py` changed after generation, so v0 prompts can't be regenerated from HEAD.
- The QA reviewer workflow is not versioned, so the key validation step is not reproducible from the repo. QA sample size is small (n=12×2).
- Counting buckets ("1-2" group built from `count_1` + `count_2_3`) don't line up with the spec's 1–3/4–7/8–15/15+ density buckets. The 8+ range is absent.
- Known data issues are acknowledged, not defects of honesty: `child_in_pool_area` 58× over-sampled; obstruction/empty/inclement thin; ~20% may show an in-scene camera.
- Intentional shortcuts: committing images to git (for handoff), stdlib-only HTTP, no tests.

## 7. Developmental milestones
1. `1653cc2` (07-02 22:00): import of a pre-built pipeline + lessons + agent reports.
2. `d3e5b9c`: lessons-informed library (1,054 stems, 0 lint).
3. `9ec4b92`: collision fix.
4. `e09c98b`: device/lens/aspect axis + live QA sampling.
5. `50b226c` / `61eb1cb`: QA simplification; breadth-first budget planner.
6. `3accbd2` / `6d67249`: pacing, plus a 500-cap watcher (budget control).
7. `19419f1` / `068e7e6`: lens-axis negative finding, confirmed.
8. `3fa5711`: prompt fixes (unvalidated) + labeling of unreliable data.
9. `d0a83c1` / `94a3bee` / `bc22094`: dataset commit, handoff, plain-English README.
10. `e3cf4b8` (07-03 00:37): controlled counting distribution (plan only).

## 8. Changes in working method & possible lessons
| Earlier approach (date) | Later approach (date) | Trigger | Inferred lesson | Evidence |
|---|---|---|---|---|
| gemini-2.5-flash + negative "NOT fisheye" prompt (pre-repo, per master_style.md) | 3.1-flash + rectilinear lens wording, camera not named (≤07-02 22:00) | ~20/24 swarm reports complained of fisheye; 4-way lever A/B (`lever_test.py`) | Fix at the model layer; negative prompts don't override priors | Explicitly documented |
| Stems control camera, lighting, referents (v1/v2, pre-repo) | Content-only stems; style/condition added at compose time; referents post-hoc (`d3e5b9c`) | Superlatives not honored, cameras drawn, text leaked | Separate content from rendering controls; annotate what actually rendered | Explicitly documented |
| Depth-first generation (10 stems × 6 variants per event) | Breadth-first round-robin (`61eb1cb`, 22:33) | 59 images covered only 2 events; `child_in_pool_area` 58× | Under a fixed budget, ensure coverage before depth | Explicitly documented |
| Per-device QA guarantee + 1/60 (`e09c98b`) | Pure 1/50 random (`50b226c`) | Not stated | Simpler unbiased sampling | Speculative (no rationale given) |
| Lens as a labeled difficulty axis with fisheye/telephoto (`e09c98b`, 22:16) | Rectilinear/wide/ultrawide, vantage-only mounts, regen gate ≥0.7 (`3fa5711`, 23:05) | QA keep-rate 0.167 twice | Validate controllability of every generated axis before scaling; don't trust labels you can't render | Explicitly documented |
| Uniform round-robin incl. counting events | Dedicated count-bucket plan (`e3cf4b8`, 07-03) | "User directive" on distribution | Benchmark composition should be set deliberately | Documented directive; integration with batch planner incomplete |

## 9. Demonstrated capabilities, limitations, uncertainties
- Demonstrated: designing a multi-axis eval/benchmark spec; building a budgeted, resumable generation pipeline; using adversarial agent QA to catch systematic generator failure; recording negative results and data caveats honestly; keeping cross-session agent context (LESSONS_LEARNED, HANDOFF).
- Uncertainties: how much of the design came from Jacob vs. Claude (only the trailers, the "User directive" note and decision records indicate direction); what happened in the pre-repo phase; PR/issue state.

## 10. Evidence references & verification limits
- Docs: `home_security_benchmark@bc22094:README.md`, `@94a3bee:HANDOFF.md`, `@3fa5711:FINDINGS_lens_axis.md`, `QA_REPORT.md`, `DATASET_v0_356.md`, `BENCHMARK_SPEC.md`, `PROMPT_DESIGN_REPORT.md`, `prompts/LESSONS_LEARNED.md`, `prompts/master_style.md`.
- Code: `scripts/gen.py`, `scripts/batch_generate.py` (`build_jobs`, `SLOTS`, pacing), `scripts/compose.py` (`LENS_DESC`, `VARIANTS`), `@e3cf4b8:scripts/counting_plan.py`, `scripts/lever_test.py`, `scripts/poll_until_funded.py`, `scripts/stop_at_500.sh`.
- Data: `data/scale/**` (356 JPEG-in-.png + sidecars), `data/raw/` (24), `agent_reports/`.
- Limits: no PR/issue access; no live generation (paid API); QA reviewer workflow absent; I viewed one image only. Image-quality claims rest mainly on the repo's own QA reports.
