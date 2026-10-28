# Liquid-Moondream-450M-Benchmark: repository report

MANIFEST | Liquid-Moondream-450M-Benchmark | PRIVATE | research workflow (reproducible ML benchmark / evaluation harness + results) | complete | GPU runs (Modal) not re-executable offline; Modal-volume-only artifacts (full referee RefCOCO-M CSVs) not in repo; Phase 4 write-up never done; no PRs/issues to inspect

DISCLOSURE: No credentials found. HANDOFF.md names the env-var names `MODAL_TOKEN_ID`/`MODAL_TOKEN_SECRET` and the Modal account/workspace handle `jacob-4532`, but no values. `calibration/vlmevalkit/run_log.json` logs VLMEvalKit's warning "OPENAI_API_KEY is not working properly". That is a warning only, with no key in it. Author emails (`jacobnikolau767@gmail.com` and local Mac hostnames) appear in git metadata. All data is public: Hugging Face checkpoints and public datasets (RefCOCO-M, POPE, CountBenchQA), with COCO image refs by filename only. I found no employer-internal, customer or proprietary material. The subject is a public LiquidAI checkpoint (LFM2.5-VL-450M) compared with public Moondream and other checkpoints. Per the brief, it is treated as a personal project and not attributed to any company. Some framing reads as advocacy, e.g. "the buyer has no choice" and "head-to-head is one-sided" (RESULTS.md, deployed-form table). The repo looks suitable to share after review. Before sharing, remove the account handle and finish the stale/inconsistent tables (see §6). The ~388 MB working tree includes a duplicated `consolidated_data/` copy (202 files, ~203 MB).

## 1. Identity
- **Owner/context:** personal account NYCandrun. Created 2026-07-02T23:49Z. Visibility PRIVATE (repos.json). Not a fork. Default branch `main`. The GitHub description reads "Benchmarking suite for the Liquid-Moondream-450M vision-language model", but no model by that name exists in the repo. The project's internal name is "Edge-VLM Benchmark" (README.md, HANDOFF.md).
- **Purpose:** a fair, fully pinned, provenance-strict benchmark of small "edge" vision-language models. It has two parts:
  1. **Part 1:** six models × three public benchmarks (RefCOCO-M grounding, POPE hallucination, CountBenchQA counting), bf16, greedy decoding, A100. It also has a separate CPU "deployed-form" table (Moondream 0.5B int8 vs LFM Q8_0 GGUF).
  2. **Part 2:** an image-token-budget sweep (accuracy and latency vs visual-token budget), plus an NVML energy probe and an independent "referee" lane that re-scores the same checkpoints with the community tool VLMEvalKit.
- **Intended user:** the owner, writing an evidence-backed comparison. The README also mentions a "demo-consumable lookup table".
- **Type and maturity:** research workflow with substantial original code (about 6.1k lines across `harness/`, `parsers/`, `scoring/`) plus committed raw per-item data. Execution is essentially complete. The final Phase 4 write-up is not started (HANDOFF.md §2–3), `demo_data/` contains only `.gitkeep`, and the README still says "Phase 0 … No results yet".

## 2. Dates and attributable contributions
- **Commits:** 46 on one branch. First: `ac6b30a` 2026-07-02 19:49 -0400 ("Initial commit: README and .gitignore", author NYCandrun <jacobnikolau767@gmail.com>). Latest: `e87ea76` 2026-07-05 01:26 -0400 (adds `consolidated_data/`).
- **Authors/committers:** "NYCandrun" (1 commit) and "Jacob Nikolau" (45 commits, local Mac hostnames `Jacobs-MacBook-Pro-2.local` and `macbookpro.mynetworksettings.com`). Author and committer are the same on every commit. No bot accounts.
- **AI co-authorship:** all 46 commits carry `Co-Authored-By: Claude Opus 4.8 <noreply@anthropic.com>`, the initial commit included. So Jacob's attributable contribution dates are 2026-07-02 → 2026-07-05, all co-authored with Claude.
- **Activity:**
  - The bulk of the work ran 07-02 19:00 → 07-03 18:00, about 23 hours of near-continuous commits, including 01:00–04:00 on 07-03.
  - There is a pause until 07-04 23:00. Then come handoff and doc commits, the reading of final referee scores, and data consolidation.
  - No inherited history, squashes or imports were detected.

## 3. Branch and history coverage
- **Branches:** `main` only (`origin/main`, `origin/HEAD → origin/main`). There are no other branches and no unmerged work. HANDOFF.md §4 records the rule "Commit to `main` and push (don't create side branches)".
- **PRs/issues:** `gh pr list`/`gh issue list --state all` returned none.
- **History coverage:** full. Commit messages are long and act as a lab notebook, citing change-log numbers (#1–#16).
- **Data rewrite:** raw data files were rewritten once. `0167292` added a derived `parsed` field to 38 raw records. The commit says outputs, latencies and metadata are byte-identical. I spot-checked one diff and it is consistent with that, but I did not verify every byte.
- **Superseded runs kept in place:**
  - `results/raw/sweep/` holds the crash-discovery run; `sweep_v2/` holds the corrected run.
  - `bench/` holds bare-prompt POPE; `bench_suffixed/` holds the standard-prompt POPE.
- **Not in the repo:** the full referee RefCOCO-M CSVs stayed on the Modal volume. Their scores were transcribed into HANDOFF.md (`d96e44f`) and `consolidated_data/scored/referee_grounding_full_RefCOCO-M/`.
- **Missing originating brief:** the code refers to "the brief" (`harness/adapters.py:238`, `METHODOLOGY.md:66,523`), but that task brief is not committed. The original specification cannot be read directly.

## 4. Actual functionality and research workflow
**What I inspected:** README, HANDOFF, all section headers and change logs of METHODOLOGY (610 lines), RESULTS (241 lines), prompts/PROVENANCE.md, consolidated_data/MANIFEST.md, scoring/score.py, the parser structure, and every commit message.

**What I executed (offline):**
- `pytest parsers scoring`: **198 passed, 164 subtests**.
- `python3 scoring/score.py` re-scored committed raw JSONL to /tmp, and the results match RESULTS.md exactly:

| Cell | Re-scored | RESULTS.md |
|---|---|---|
| LFM grounding Acc@0.5 | 0.76875 | 76.9% |
| moondream2 grounding | 0.7644 | 76.4% |
| LFM count | 0.7149 | 71.5% |
| LLaVA count | 0.7312 | 73.1% |
| LFM suffixed POPE acc / F1 | 0.8791 / 0.8762 | 87.9% / 0.876 |
| SmolVLM2 suffixed POPE | 0.8508 | 85.1% |

GPU inference (Modal), the CPU deployed lanes and VLMEvalKit were not run.

**Pipeline:**
- **Control plane and runs:** a local control plane launches Modal functions (`harness/run.py`, `cell_core.py`, `run_sweep_serial.py`, `run_deployed.py`, `run_power_probe.py`, `run_vlmevalkit2*.py`).
- **Configs and pins:** one YAML per cell (`configs/bench/` 18, `configs/sweep/` 8). Images and lockfiles are pinned (`envs/images.py`, `envs/locks/*`). Model revisions, remote-code file hashes, dataset revisions and the VLMEvalKit commit are all pinned (METHODOLOGY "Model pins", "Dataset pins").
- **Prompts, parsers, scoring:** verbatim prompt files with provenance (`prompts/`). Model-specific parsers live in `parsers/boxes.py` and `answers.py`; the yes/no parser is an exact port of VLMEvalKit `YOrN_Extraction`. A standard-library scorer (`scoring/`).
- **Raw data:** per-item JSONL rows (raw_output, parsed, gt, latency, error, meta including GPU UUID).
- **Staged gates:** Phase 0 (load matrix, dataset pins, knob liveness), then Gate A/B/C audits and a parser freeze, then Phase 3 full runs.

**Notable analytic results (from RESULTS.md):**
- The POPE prompt suffix moves accuracy by +1.5 to +30.1 points across models.
- The LFM token-budget curve runs 39.5% → 77.5%.
- On energy, SmolVLM2 uses about 11–13× more joules per answer than LFM at defaults.
- LFM Q8_0 performs about the same as its own bf16 version.

## 5. How Jacob builds with AI
This repo is an evaluation of AI models, built by directing an AI coding agent. It is not an AI-powered product. The direct evidence is the Claude trailer on every commit. The commit and methodology prose is the agent's voice reporting to an "owner", with decisions attributed to that owner, for example:
- "owner directive: bias toward fair comparison; never two harnesses"
- "owner amendment" making the gate audits non-blocking
- "owner-raised" deployed-form asymmetry disclosure (`1ee7eee`)
- "owner decision after brainstorm" (change #7)
- "Owner approved a corrected re-run" (#14)
- VLMEvalKit lane "descoped, then REINSTATED by the owner within minutes" (#9)
- "Owner request" for the latency column and energy probe (#10)
- "owner directive, twice-strengthened" for single-GPU sweep discipline (#5)

The pattern this shows is that Jacob set the methodology (fairness, provenance, hardware constancy), approved scope, and made the judgment calls, while the agent executed and documented. This is **strongly inferred**: the owner's words are paraphrased by the agent, and no raw prompts are committed.

**Context management:** HANDOFF.md (`b8855a5`, then four revisions) exists so "a fresh (incl. cloud) session can resume". It lists rules "you set that must not be broken", including:
- at most 4 GPU jobs at once;
- stop and ask if a safety timer kills jobs;
- no Qwen in tables;
- "Keep status updates in plain English".

`2a8e5f5` rewrote it into plain English at that request.

**Verification of AI output:**
- Functional smokes run before full runs.
- Byte-identical regression check after refactoring (change #6, 3/3 rows).
- A second, independent instrument (VLMEvalKit referee).
- Failed hypotheses are recorded. For example, #14 says "An earlier version of this change wrapped only preprocessing in the retry — falsified by the first smoke".

**One documented automation failure:** an "automated transition script misread one failed container status-check as 'cell finished'" and killed a SmolVLM cell at about 90%. The pattern was then "retired" (change #7).

## 6. Quality assessment (research rubric)
**Strengths (high confidence):**
- **Experimental design:** single-variable changes, pinned environments, a hard GPU-type assert, one physical die per sweep curve, and dedicated CPU reservation for timing.
- **Provenance:** every number is backed by a raw row. I confirmed this for six cells.
- **Disclosed patches:** both VLMEvalKit patches (moondream revision, Qwen flash-attn → sdpa) are disclosed.
- **Failures treated as findings:**
  - transformers-version sensitivity (8/20 SmolVLM2 outputs differ between 4.57.1 and 5.12.1);
  - the POPE.tsv baked-in suffix discovered through the referee;
  - the forced-budget crash, root-caused to the `ceil` upscale branch in `smart_resize` exceeding the 1024-patch cap (#12/#14) and described as upstream-reportable.
- **Self-correction:** #12 corrects a previously published wrong reading (the b256 "drop" was crashes scored as misses). The superseded data is kept.

**Weaknesses and unfinished items:**
1. **Write-up not reconciled (unfinished, not a defect):**
   - RESULTS.md still includes Qwen2.5-VL-7B in the main table, against the 07-03 drop decision.
   - The referee table's "ours" POPE column shows bare-prompt numbers (e.g. SmolVLM2 55.0) while the main table moved to suffixed numbers, a stale cross-reference.
   - The README status and repro commands are still "TBD".
   - `demo_data/` is empty.
   - The full referee RefCOCO-M results (moondream2 79.04, LFM 70.48, LLaVA 4.04, SmolVLM2 0.0) appear only in HANDOFF and consolidated data, not in RESULTS.
2. **Main open question unresolved:** LLaVA counting, ours 73.1 vs referee 31.6. My offline check strongly suggests the cause:
   - 389 of 491 LLaVA count outputs are sentences or number words ("There are four pots…", "nine"), despite the "answer with a number directly" instruction.
   - The repo's parser extracts number words from zero to twenty (`parsers/answers.py`), so it credits these answers. A stricter exact-match extraction would not.
   - This fits the repo's own hypothesis ("answer-extraction/scoring difference"). It also means the main-table Count column is lenient by design, which should be stated alongside it.
3. **Comparison scope:** the probe uses only 100 items, which the repo notes (±5 pts). Grounding prompts are model-specific by design, and two of them are "best-effort". The headline grounding zeros for SmolVLM2/LLaVA partly reflect missing native formats, and this is disclosed.
4. **Framing tilt:** some LFM-favorable phrasing in the deployed-form readings. The disclosures and caveats themselves are present.

**Overall:** unusually rigorous and self-auditing for a three-day personal project. The method is strong and the final synthesis is incomplete. Confidence: high on design and reproducibility of the scoring; medium on GPU-run claims, which I could not execute.

## 7. Developmental milestones
| Date | Commit(s) | Milestone |
|---|---|---|
| 07-02 | `05c889c` | Skeleton |
| 07-02 | `df87969` | Phase 0 and Gate A |
| 07-02 | `e2a135b` | Parsers frozen (Gates B/C) |
| 07-02 | `007ca07`–`bd7c5c7` | Changes #1–#5: InternVL tiling, GPU policy split, CPU reservation, "!" pin unsupported, single-container dual-venv SWEEPBOX |
| 07-02 | `dd8a762` | Version-sensitivity finding |
| 07-03 | `11d55ae` | All 18 bench cells complete |
| 07-03 | `dba1944`, `23f0bba` | Change #7: SmolVLM sweep re-scoped to counting. Change #6: shared CPU loop |
| 07-03 | `36b06ba`, `950d0d2` | Referee lane reinstated, then 8/8 |
| 07-03 | `4f59270` | Deployed table complete, plus change #12 |
| 07-03 | `384c59f` | Energy probe |
| 07-03 | `e157516`, `a9492d9` | Change #14: corrected sweep |
| 07-03 | `3a09d85` | Change #16: suffixed POPE headline |
| 07-03 | `0167292` | Qwen dropped |
| 07-03 → 07-05 | `b8855a5`…`d96e44f` | HANDOFF series |
| 07-05 | `e87ea76` | Consolidated data |

## 8. Changes in working method and possible lessons

**POPE prompt convention**
- Earlier: bare question (Gate A, 07-02).
- Later: standard suffix as the headline (#16, 07-03).
- Trigger: the referee revealed a +30.8-pt SmolVLM2 swing; the disposition was deferred until all six models showed a swing.
- Lesson: audit tool data files, not just code. Settle the disposition with evidence before switching.
- Evidence strength: explicitly documented.
- Alternative explanation: none needed.

**Sweep crash handling**
- Earlier: crashes scored as misses, then a dual "completed-only" view (#12).
- Later: a root-caused, opt-in pre-upscale fallback with per-row provenance (#14).
- Trigger: the probe smoke crashed, and an audit of the stored `error` fields followed.
- Lesson: inspect error fields before interpreting curves.
- Evidence strength: explicitly documented.

**Gating**
- Earlier: blocking gates (implied).
- Later: "non-blocking per owner amendment" recorded audits (07-02).
- Possible trigger: speed.
- Evidence strength: documented change. The reason is speculative.

**Automation trust**
- A silence-as-success transition script killed a cell, and the pattern was retired (#7).
- Lesson: treat a missing status as failure.
- Evidence strength: explicitly documented.

**Referee lane**
- Descoped (#9, reasoning that vendor anchors are already VLMEvalKit numbers), then reinstated within minutes.
- It later produced the most important correction (#11).
- Evidence strength: documented. The inferred lesson, that independent instruments pay off, is strongly inferred.

**Scope**
- Qwen-7B was dropped for runtime and "edge" framing (`0167292`).
- Evidence strength: explicitly documented.
- Alternative explanation: cost and time pressure.

**Session continuity**
- HANDOFF.md was introduced and then simplified to plain English (07-03 → 07-04).
- Evidence strength: documented. The trigger (handing off to a fresh or cloud session) is stated.

## 9. Demonstrated capabilities, limitations, uncertainties
**Demonstrated in this repo:**
- Specifying and enforcing an evaluation protocol (pins, fairness rules, provenance).
- Directing a coding agent over a long, multi-phase GPU workflow with gated audits and owner approvals.
- Cross-instrument validation.
- Root-causing framework bugs from source.
- Correcting published numbers transparently.
- Cost and safety controls (concurrency caps, kill timer, stop-and-ask rule).
- Context handoff between AI sessions.

**Uncertainties:**
- The owner's actual instructions are known only through the agent's paraphrase.
- The relative share of human vs agent design ideas cannot be separated.
- GPU results could not be re-executed.

## 10. Evidence references and verification limits
**Key files:**
- `Liquid-Moondream-450M-Benchmark@e87ea76`: `README.md`, `HANDOFF.md`, `METHODOLOGY.md` (Gate A/B/C/C2 records; change logs #1–#16), `RESULTS.md`, `prompts/PROVENANCE.md`, `parsers/answers.py`, `scoring/score.py`, `consolidated_data/MANIFEST.md`
- `calibration/vlmevalkit{,2}/`
- `results/raw/{bench,bench_suffixed,sweep,sweep_v2,deployed,probe}/`

**Commits cited:** `ac6b30a`, `05c889c`, `df87969`, `e2a135b`, `007ca07`, `bd7c5c7`, `dd8a762`, `11d55ae`, `1ee7eee`, `23f0bba`, `dba1944`, `8922a02`, `36b06ba`, `68d94f6`, `4f59270`, `30b76a4`, `384c59f`, `950d0d2`, `e157516`, `a9492d9`, `3a09d85`, `0167292`, `b8855a5`, `2a8e5f5`, `d96e44f`, `e87ea76`.

**Verified locally:**
- the pytest suite (198 passed);
- six re-scored cells matching RESULTS.md;
- the LLaVA count output-format analysis;
- the branch list, authors and trailers;
- the absence of PRs and issues.

**Not verified:**
- Modal GPU/CPU runs, NVML energy figures, the VLMEvalKit referee execution, and volume-only CSVs;
- byte-identity of all 38 rows rewritten in `0167292` (one spot-checked);
- the lazily fetched blobs larger than 2 MB were not individually checked.
