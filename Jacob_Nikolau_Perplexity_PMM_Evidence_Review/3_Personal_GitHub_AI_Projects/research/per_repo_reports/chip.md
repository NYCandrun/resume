MANIFEST | chip | PRIVATE | research workflow (agent-orchestrated evidence-collection pipeline + dataset) | partial | Ownership/disclosure ambiguous (see DISCLOSURE): methodology and AI-practice evidence assessed; downstream framework/deck content described only at a high level. One-night history (~10h). Prior "original project" not in repo. No PRs/issues. 534 MB third-party page cache not reviewed row-by-row. Network fetch/render not executed.

DISCLOSURE:
- **Ownership/disclosure ambiguous. The lead needs to confirm.** Every commit author email uses an employer-looking domain: `jacob.nikolau@…mosaicapp.com` (2 commits) and `jacobn@…mosaicapp.com` (33 commits). The repo also calls itself "the chip-side evidence layer for the *Inferring Edge AI Demand* framework" and mentions "Liquid relevance" (`README.md:114`, `PIPELINE.md:200`), "deck Slide 7" (`AGENT_BRIEF.md`), "the deck's signal-decay logic", and a "Liquid workbook" that receives new sheets (commit `fd7cfb4` message). That workbook is not in the repo. This suggests the work feeds a third-party or employer-related framework. Per the brief, I attribute nothing to any company. I describe the framework/deck only at this level, and I assess only the pipeline engineering and the AI working method, which come from code and commits in this repo.
- Credentials: none found. I pattern-searched for sk-/ghp_/AKIA/Bearer outside `data/cache`. Hits for the word "token" refer to LLM tokens or TOPS.
- Third-party content: `data/cache/` holds 3,752 files (534 MB) of fetched vendor web pages and PDFs, which are public but copyrighted. `data/evidence.csv` holds verbatim vendor quotes.
- Personal data: local paths `/Users/jacobnikolau/Downloads/chip-market-map` (`AGENT_BRIEF.md`, `scripts/render.py:12`) and work-domain email addresses in commit metadata.
- Suitability to share: **not as-is.** Before sharing, someone would need to confirm ownership, strip or justify the vendor-page cache, and remove the framework/deck references.

---

## 1. Identity
- Personal account NYCandrun. Visibility PRIVATE (`repos.json`). Not a fork. Default branch `main`. GitHub repo created 2026-06-28T20:20Z.
- **Type:** an agent-run research workflow. A deterministic Python "integrity engine" checks the output of Claude Code sessions and subagents that research edge-AI chip vendors (43-OEM universe in `data/chip-universe.csv`) from first-party sources only. The output is a typed, quote-verified evidence dataset (`data/evidence.csv`), a chip→OEM edge table, and an .xlsx deliverable.
- **Intended user:** the author, as the operator of Claude Code (`README.md`: "one Claude Code session = one OEM… You type `/chip-increment`"). The repo states its scope as the "chip evidence layer only". OEM-side inference is a separate pipeline.
- **Maturity:** working and populated. 361 evidence rows across 42 OEMs, 138 parked rows, and 705 edges. Golden set and selftests pass. It is a one-night build with no later passes, so the "time series" design goal is untested.

## 2. Dates and attributable contributions
- First commit `64d9c8f` at 2026-06-28 16:14:51 -0400. Latest commit `fd7cfb4` at 2026-06-29 02:34:45 -0400. Total of 35 commits in about 10h20m, all on `main`.
- Author identities (author and committer are the same on every commit):
  - `chip-market-map <jacob.nikolau@…>`: `64d9c8f`, `fb40322`.
  - `jacobn-a11y <jacobn@…>`: the other 33.
  - Both look like Jacob from the name and local path. No bot authors.
- AI trailers: `Co-Authored-By: Claude Opus 4.8` on 28 commits and `Claude Sonnet 4.6` on 4 (`07cf1dd`, `ac715d0`, `34b71f7`, `498ab2d`, the single-session `/chip-increment` runs). The 3 commits without a trailer are `64d9c8f`, `fb40322` and `895d892`. All 361 evidence rows record `model_tier=claude-sonnet-4-6` (the `ingest_inbox.py` default).
- **Inherited history:** the initial commit lands 2,169 lines fully formed: 4 design docs, 10 scripts, a 10-case golden set and a 44-row universe. The text describes itself as "rebuilt", and says "the original pipeline spent its tokens on ~40 autonomous research agents" and "the manually-produced first-party workbook (245 lines)" (`b6f9c30`). That earlier project and workbook are not in this repo, so the design's prehistory cannot be reconstructed.

## 3. Branch and history coverage
- Branches: `main` and `origin/main` only (HEAD → `origin/main`). No other branches, so nothing exists that was never merged.
- `gh pr list` and `gh issue list` (state all) are both empty.
- History is linear and readable, with descriptive commit bodies that often give the trigger and the before/after counts. One deliberate reset: `6c5662b` "reset to hardened v1" removed earlier rows from evidence, ledger and parked.

## 4. Actual functionality
**Inspected:** README, PIPELINE, SCHEMA, AGENT_BRIEF, `.claude/commands/chip-increment.md`, and the scripts `common`, `checks`, `autofix`, `ingest_inbox`, `render`, `build_edges` and `build_workbook`. I also read representative diffs (`6c5662b`, `fa14273`) and dataset statistics.

**Executed offline:**
- `checks.py --selftest`: ALL SELFTESTS PASSED.
- `verify.py`: 16/16 golden cases, GREEN.
- Independent re-check of all 361 evidence rows with `common.quote_in_source` against `data/cache/<url_hash>.txt`: 361 found, 0 missing, 0 without a cache file.

**Not executed:** `fetch_source.py`, `render.py` and the agent workflow, because they make network calls or need Claude.

**Architecture:**
- **Two operating modes.**
  - (a) `/chip-increment` slash command: one session does one OEM through reconcile → fetch → extract → gate → write → guard → commit → handoff, then stops.
  - (b) Parallel subagents (from `a9ecbb9`) bound by `AGENT_BRIEF.md`. Each writes only `data/inbox/<oem>.json`. The main thread serializes writes through `ingest_inbox.py` (autofix, then gates, then `write_rows.py`).
- **Division of labour.** The model does "judgment": choosing sources and grading evidence. Scripts do the mechanical work: fetching and caching by hash, pdftotext/pdfplumber extraction, windowed candidate snippets, all arithmetic, and CSV writing ("You never do arithmetic").
- **Gates.** There are 13+ deterministic gates in `checks.py`, including:
  - `quote_in_source`
  - `specs_in_source` (every number in a spec field must appear in the cached source)
  - `first_party_domain` with denylist
  - `source_is_deeplink`
  - `scale_matches_quote`
  - `signal_class_supported` (keyword evidence)
  - `stage_consistent`
  - `quality_not_overstated`
  - `design_win_partner` (named partner grounded in the source)

  The routing distinguishes RETRY from CONFIRMED_ABSENT and has a 2-round escalation cap before a row is PARKED with `needs_human`.
- **Guards.**
  - `regress_diff.py`: flags a figure that moved more than 40% versus the prior pass.
  - `corroborate.py`: recomputes `corroboration_count`.
  - Golden set of frozen fixtures with inline `_source_text` and a freeze guard. It includes synthetic negative controls (hallucinated quote, homepage URL, GOPS→TOPS, and others).
- **Outputs.**
  - `evidence.csv`: 361 rows, 347 PASS and 14 CONFIRMED_ABSENT. Signal classes: 35 design_win (0 without a partner), 25 certification, 20 production_backlog, 11 devkit, 270 blank. Compute filled on 125 rows.
  - `chip_oem_edges.csv`: 705 edges, 80 Tier-1 named design wins and 625 Tier-3 rows from a keyword device-class map.
  - `Edge_AI_Chip_Market_Map_Hardened.xlsx`.
  - `parked.csv`: 138 rows, all `needs_human`.
- **Implemented vs described.** PIPELINE.md explicitly says it describes "no machinery … that doesn't exist" and lists render/OCR as an external hook. Two described items are not built: "token telemetry" in the ledger, and the golden set at its planned "~20–30" size (it has 16). The "Liquid workbook" sheets from `fd7cfb4` are produced outside this repo.

## 5. How Jacob uses or builds with AI
Direct evidence shows Jacob using AI agents for research and coding while designing a control system around them:
- **Task specification.**
  - A 168-line slash command and a 126-line subagent brief.
  - Exact enums and a return contract.
  - Keyword rules for passing gates.
  - A ⛔ hard boundary saying subagents never write the dataset or run git. It was added in `75d4fa1` after "some batch-1 agents bypassed it" (explicitly documented).
- **Context and cost management.** "Token-adaptive, not token-maximal". Bounded sessions. Snippets instead of whole PDFs. Escalation only on failure. A stated reaction to "~40 autonomous research agents" in the earlier version.
- **Delegation topology.** Parallel research agents and a serialized single writer. The design moved from one session per OEM to parallel batches within about 3 hours (`a9ecbb9` at 17:07).
- **Verification as the main lever.** Code-enforced quote and spec grounding, golden negative controls, and re-ingest of all inboxes after each engine change (`131ed6e`, `f210055`, `75d4fa1`).
- **Debugging and judgment visible in commit bodies.**
  - `b6f9c30`: the bot User-Agent caused silent timeouts that were "misread as 'unreachable / not disclosed'", which was the root cause of thin rows.
  - `ce9119c`: a regex captured a trailing period ('70.' vs '70') and wrongly dropped grounded specs.
  - `fa14273`: the `first_party_domain` gate "was bypassed" because ingest fed in the source's own domain.
  - `24358dd`: a whole-page availability scan mislabeled "Sampling Rate ADC" as sampling, so precision was tightened from 147 to 75 rows ("Honest blanks over wrong labels").
- **Model comparison.** In `91cd7ab`, "single-session and tiered-subagent AMD runs independently flagged" an under-inclusive gate. That is a deliberate A/B of two agent modes.
- **Unclear.** The trailers mark Claude as co-author of the engine commits, so how much code Jacob wrote versus reviewed cannot be separated. The initial 2,169-line commit has no trailer, but it is a Claude Code project from the start (`.claude/commands`).

## 6. Quality assessment (methodology only; confidence moderate-high for code, low for data correctness)
**Strengths:**
- Treating agent output as untrusted and enforcing truth in code is well matched to the problem.
- The CONFIRMED_ABSENT vs RETRY vs PARKED distinction, and the parked backlog that waits for a human, are thoughtful choices.
- Negative controls in the golden set address the "all-PASS set can't catch a gate that passes everything" problem, and the repo says so explicitly.
- Commit messages report measured effects (row counts, recoveries, rejections).
- Fixes generally make the data more conservative rather than inflating it.

**Weaknesses and risks:**
- `quote_in_source` accepts quotes stitched with "..." from fragments anywhere later in the page. For example, `'NPU TOPS ... Up to 55 TOPS'` is the quote on four different Ryzen rows, so the binding between a value and its SKU is not verified. `specs_in_source` only checks that the digits occur somewhere on the page.
- `autofix` rewrites agent output: it trims quotes, blanks invalid enums, and clears unsupported classes. This is honest by design, but it hides how often agents are wrong unless someone reads the logs. It is a stated, intentional shortcut (`f210055`: "one sloppy agent can't nuke an OEM").
- Of the 270 rows with a blank `signal_class`, 157 still carry strong or very_strong `evidence_quality`, so the grading semantics are unclear.
- Tier-3 edges come from a keyword map (`build_edges.py`), which is coarse even though it is auditable.
- `openpyxl` (used by `build_workbook.py`) is missing from `requirements.txt`.
- The hard-coded `/Users/...` paths and `--pass-date 2026-06-28` default reduce reproducibility.
- The docs still describe the sequential single-session model while the practice moved to parallel subagents.

**Not verified:** whether the vendor facts are true today, how well candidate snippets recall the source, and whether the parked rows were handled correctly.

## 7. Developmental milestones (all 2026-06-28/29)
1. **16:14** Full pipeline scaffold, then the Playwright render hook at 16:18.
2. **16:41** First single-session OEM (AMD 3 rows, 2 parked), followed by a gate fix.
3. **17:07** Moved to parallel subagents (AGENT_BRIEF and inbox ingest).
4. **17:14–17:21** Hardening of the User-Agent, render and `specs_in_source`, then a reset to "hardened v1".
5. **18:05** AMD deep pass (9/9 PASS).
6. **18:42–18:50** Confirming batch, then the `design_win_partner` field and gate, then a finer row_id (42→62 rows).
7. **19:05–19:19** Four Sonnet single-session increments, then batches 1–5 and the final batch, covering all 43 OEMs by 21:21.
8. **22:14–22:43** Pass-2 recovery with a hardened render, reaching 340 rows.
9. **23:24** Cleanup: first-party purity and golden set 10→16, reaching 361 rows.
10. **23:49–02:00** Launch-year and availability enrichment (scan, then a tightened scan, then an agent pass).
11. **02:34** Edge table (linkage "0+1").

## 8. Changes in working method and possible lessons
| Change | Earlier → later (dated) | Trigger | Lesson | Strength | Alternative |
|---|---|---|---|---|---|
| Orchestration | One session per OEM, explicitly "not a wall of research agents" (`64d9c8f`, 16:14) → parallel subagents with serialized writes (`a9ecbb9`, 17:07) | Not stated. Likely speed of coverage | Parallel throughput is acceptable if the writes stay single-threaded | Strongly inferred | Time pressure for one night |
| Agent boundary | Soft rules → hard "no dataset writes / no git" (`75d4fa1`) | "some batch-1 agents bypassed it" | Agents don't reliably follow scope; enforce by structure | Explicitly documented | — |
| Portfolio scope | "Pick 1–4 lines… Don't pad" → "Enumerate the FULL current portfolio" (`6c5662b`) | Thin rows compared with the 245-line manual workbook (`b6f9c30`) | Under-coverage came from the fetcher, not the method | Explicitly documented | — |
| Grounding | Quote-only check → `specs_in_source` for every spec value (`6c5662b`) | "fabricated/inferred specs (the failure mode that made the manual workbook unreliable)" | Verify each field, not just the quote | Explicitly documented | — |
| Row identity | `oem::product_line` → plus sku/source hash (`e53f619`), then plus partner (`ce9119c`) | Ambarella 18→10 collapse; NVIDIA Toyota/Volvo/BYD collapse | Dedup keys silently lose data | Explicitly documented | — |
| Repair vs reject | Reject on any gate fail → deterministic autofix (`e53f619`, `f210055`) | Synaptics lost all 11 rows to invalid enums | Make repairs conservative so one bad agent can't wipe out an OEM | Explicitly documented | It may hide agent error rates |
| Enrichment precision | Whole-page scan → only high-precision phrases (`24358dd`, 4 min later) | Mislabels such as "Sampling Rate ADC" | Prefer blanks over wrong labels | Explicitly documented | — |

## 9. Demonstrated capabilities, limitations, uncertainties
- **Demonstrated:**
  - Designing instruction and gate systems around LLM research agents.
  - Parallel-agent orchestration with a single writer.
  - Iterative root-cause debugging with measured before/after counts.
  - Building evals with negative controls.
  - Source-provenance discipline.
- **Uncertainties:**
  - How much of the code Jacob wrote, given the Claude co-author trailers on most commits.
  - What existed in the prior "original project".
  - Ownership context (see DISCLOSURE).

## 10. Evidence references and verification limits
- **Code and docs:**
  - `chip@64d9c8f:PIPELINE.md`
  - `chip@64d9c8f:.claude/commands/chip-increment.md`
  - `chip@a9ecbb9:AGENT_BRIEF.md`
  - `chip@6c5662b:scripts/checks.py` (gate_specs_in_source)
  - `chip@e53f619:scripts/autofix.py`
  - `chip@fd7cfb4:scripts/build_edges.py`
  - `scripts/common.py:172` (quote_in_source with ellipsis splitting)
  - `scripts/render.py`
  - `data/golden/golden.json` (16 cases)
- **Commits with diagnostic bodies:** `91cd7ab`, `b6f9c30`, `6060ec0`, `96f5c87`, `e53f619`, `75d4fa1`, `131ed6e`, `f210055`, `ce9119c`, `fa14273`, `991bf91`, `24358dd`, `21d34aa`, `4f98051`, `fd7cfb4`.
- **PRs and issues:** none.
- **Limits:**
  - No network fetch or render was run.
  - The cache was not audited for freshness or accuracy.
  - The xlsx was not opened.
  - The quote-verification re-check uses the repo's own lenient matcher.
  - The "Liquid workbook" and the earlier manual workbook are outside the repo.
