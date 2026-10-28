MANIFEST | OEM | PRIVATE | research workflow (agent-orchestrated data-verification pipeline + dataset) | complete | Single branch, 3 commits in ~10 h; history before the first commit was imported as one snapshot and can't be recovered; agent run artefacts (rows.jsonl, telemetry, results, citation-validation batches) are gitignored and missing; no live/agent runs done (read-only, no paid APIs)

DISCLOSURE: **Ownership/disclosure is unclear. Lead should confirm before any substantive use.** (a) The profile schema includes a field named `liquid_relevance`, defined as "could an OUTSIDE model realistically win this decision?" (`cache/profile_instructions.md`, `pipeline/profile.py`). That makes the edge-AI profile output look like go-to-market or market-sizing analysis for one specific edge-AI model vendor. (b) All three commits use the author/committer email `jacobn@mosaicapp.com`. That is an identity fact only and is not used for attribution. (c) The data is compiled from public company disclosures (annual reports, 10-Ks, IR releases) plus model-generated categorical judgements. I found no internal, proprietary, customer or personal data. No credentials: `pipeline/fetch_extract.py` uses the placeholder `contact@oem-verify.example` and an env override. Following the brief, I describe the profile dataset's business content only at a high level. The pipeline engineering assessment below is generic and does not depend on who owns it. Sharing: the pipeline code and agent specs look shareable after review. The `profiles.json` content and the `liquid_relevance` framing should not be shared until ownership is confirmed.

# OEM — NYCandrun/OEM

## 1 Identity
- Personal-account repo (NYCandrun), **PRIVATE** (visibility only). Not a fork. Default branch `main`. Created 2026-06-28T20:32Z, last pushed 2026-06-29T06:23Z (`repos.json`).
- **Type:** research/data workflow. A Claude Code multi-agent pipeline plus a deterministic Python engine that fills and verifies a spreadsheet of non-China OEMs. Columns cover revenue, units shipped, analyst estimates, guidance and edge-AI classification. The README calls it "OEM units verification pipeline (rebuilt)".
- **Intended user:** an operator running Claude Code one "wave" at a time (`/oem-increment`, `/oem-audit`, `/oem-status`).
- **Purpose/problem:** the README says it was rebuilt because "an elegant tiered design was documented but never wired up, so every increment actually ran on expensive general-purpose agents". The goal is cheap model tiers handling the bulk, with deterministic gates enforcing that figures have sources.
- **Maturity:** the engine is substantial and tested. The dataset itself is only partly filled (see §4). The final commit changed the main output to categorical edge-AI profiles.

## 2 Dates and contributions
| Commit | Date (−0400) | Author = committer | Trailer |
|---|---|---|---|
| `8392da1` Import oem-verify-pipeline | 2026-06-28 16:47 | NYCandrun `<jacobn@mosaicapp.com>` | none |
| `52648ce` Harden pipeline, add verify-existing + native-currency revenue, re-shape to edge-AI profiles | 2026-06-28 23:24 | same | `Co-Authored-By: Claude Opus 4.8` |
| `b4a98af` Add edge-AI model-decision profiles + segment-evidence pass | 2026-06-29 02:23 | same | `Co-Authored-By: Claude Opus 4.8` |

- There is one identity. There are no bot authors, no `codex/*` or `jules/*` branches, no PRs and no issues (`gh pr list` and `gh issue list` both returned empty).
- All activity falls in one ~10-hour session. The earliest attributable work is 2026-06-28 16:47 and the latest is 2026-06-29 02:23.
- **Inherited history:** `8392da1` imports 38 files and 2,551 lines in one go, already mature. README, golden set and tests all claim "32 tests, all green". Development happened elsewhere first: the name `oem-verify-pipeline` and the mention of a "previous project" whose data is "untrusted" both point to that. That history is not in this repo. `seed_candidates.py` also mentions earlier workbook exports ("v2(2)", "v10") that aren't here.

## 3 Branch and history coverage
- Branches: `main` and `origin/main` only (plus `origin/HEAD`). Nothing to diff between branches and no unmerged work.
- Linear history of 3 commits. The full stat for every commit was read, along with diffs of `.claude/agents/*`, `PIPELINE.md`, `.gitignore` and `pipeline/profile.py`.
- Not accessible: development before the import; run artefacts that are gitignored (`cache/rows.jsonl`, `telemetry.jsonl`, `results/`, `batches/`, `url_cache.json`, `seg_*`, `val_*`); the citation-validation script or prompt (`val_batches/` is gitignored and I found no script for it); and the "memory: edge-ai-profile-reshape" note that `pipeline/profile.py` refers to, which lives outside the repo.

## 4 What it actually does
**Design** (`PIPELINE.md`, `MASTER_PROMPT.md`, `CLAUDE.md`):
- Deterministic code handles fetching, arithmetic and gating. Models only make semantic judgements.
- A rule-based router (`pipeline/difficulty.py`) sends each row to a Haiku batch or a Sonnet batch. A Sonnet QA router gives PASS / RETRY / CONFIRMED-ABSENT. Opus handles single-row escalations only, after at most 2 rounds.
- Extractors return a "typed evidence record": the figure as written, scale, currency, period basis, metric, scope, geography and precision. They are explicitly forbidden from computing the final integer; `checks.normalize()` does that.
- Gates G1–G8 include G7 (the quote must appear in the cached source text) and G8 (a first-party URL must be on the company's own domain). Absent and estimate rows have their own gates (A1–A5, E1–E6). Triangulation T1–T3 adds group-sum, ±40% YoY and cross-source checks.
- Each version is written as a new file (`vN+1`). A regression gate (`pipeline/regression.py`) blocks nulled or changed verified integers.
- `pipeline/golden.py` checks 7 cases against hash-pinned snapshots in `golden/snapshots/`. These cover Hyundai, Mercedes, Ford (US-only trap), JLR (March fiscal year), Honda (table), Apple (revenue-only) and Nintendo (cumulative, rejected).

**Agent roles:** 5 subagent specs (`.claude/agents/oem-discover|extractor-haiku|extractor-sonnet|qa-router|escalation-opus.md`) and 3 slash commands.

**What I ran** (offline, on a copy at `/tmp/OEMcopy`):
- `pytest`: **55 passed**, matching the commit message.
- `python -m pipeline.golden`: **7/7, accuracy 1.0**.
- `python -m pipeline.run_wave status` on v6: 1,064 rows; revenue (col 7) filled on **27**; col 10 units **0**; cols 14–24 all 0; next pass = revenue.
- I opened all 6 workbooks with openpyxl. Revenue fills by version: v1 0 → v2 14 → v3 14 (universe 831 → 1,064) → v4 19 → v5 22 → v6 27.
- `cache/profiles.json`: 1,102 profiles across 1,064 companies. 940 have segment_revenue, 190 have units_shipped, 1,002 have an evidence_url. `citation_status`: 248 valid, 25 mismatch, 27 inaccessible, 802 unset. This matches the `b4a98af` message: "remainder pending weekly-limit reset".
- **Not run:** any agent wave, live fetch or discovery. These need Claude or the network.

**Implemented vs. claimed:**
- The deterministic half is real and tested.
- The waved verification was used for only ~27 revenue rows. Units, third-party, guidance and edge-ai passes never ran in the committed workbooks.
- Token telemetry is empty (`python -m pipeline.telemetry` → `{}`), so the README's claim that "telemetry proves the cheap tier carries the bulk" is not verifiable here.

## 5 How Jacob works with AI
Direct evidence: `Co-Authored-By: Claude Opus 4.8` trailers on 2 of 3 commits, the `.claude/agents` and `.claude/commands` files, `MASTER_PROMPT.md`, `HANDOFF_TEMPLATE.md` and `cache/profile_instructions.md`. The repo shows all three modes:
- **Using AI to build:** Claude co-authored the hardening and profile code.
- **Agents doing research:** subagent extractors and discover agents, plus a "swarm" for segment evidence (`b4a98af`).
- **Directing and verifying AI output:** the strongest signal is that every control assumes model output is untrusted:
  - prior data is treated as candidates only ("Ctrl-F hint");
  - models never write the integer;
  - quote-in-source (G7) and domain (G8) gates;
  - escalation is explicitly bounded;
  - "trust the workbook, not the note" handoffs, to manage context across sessions;
  - one wave per session, then stop.
- **Cost-aware delegation:** a model-tier routing design with Opus reserved for the hardest rows, and per-tier token telemetry hooks.
- **Learning from failures:** `PIPELINE.md` "Why decomposed" ties each evidence field to a named past failure (Daihatsu geography/metric, a thousands-scale bug, FY2024 leftovers, GoPro "~2,000,000"). The `52648ce` prompt edits add specific guards, e.g. "NEVER 'millions' for a billions value", "EUR value carried as USD", and "copy the CONTIGUOUS line … A composed/restated quote fails G7".
- **A deliberate trade-off between rigour and speed:** the profile pass tells agents to use "your own product/industry knowledge — NO deep research … Coarse-but-right beats precise-but-slow". It then adds a separate partial citation-validation pass.

Who wrote which lines (human vs. Claude) can't be separated beyond the trailers.

## 6 Quality assessment (all confidence ratings are qualitative)
**Strengths** (high confidence):
- The verification design is careful and well reasoned. It separates deterministic from model work, uses typed decomposition, and has falsifiable "absent" outcomes.
- The golden set is hash-pinned so it can't decay when sources move. The rationale is written down.
- Versions are never overwritten. Tests pin historical bug classes (55 tests). Docs mostly match the code.
- Recording citation status (`valid`/`mismatch`/`inaccessible`) instead of hiding mismatches is good provenance practice.

**Weaknesses and defects:**
- **Revenue pass writes into units columns** (high confidence, from reading the code plus the v6 state):
  - `workbook.WRITE_MAP` maps the generic `quote` → col 12 (Units Quote) and `basis` → col 13 (Units Basis).
  - In v6, all 27 revenue rows show the revenue quote in col 12 and "First-party disclosed" in col 13, while col 10 (units) is blank.
  - `run_wave.select_targets` picks first-party targets where basis is blank, and guidance targets where basis == First-party. So these rows would be **skipped by the units pass and wrongly picked for guidance**, and `status` shows 27 "First-party disclosed" units rows that don't exist.
  - No test covers this.
- **Revenue units and header don't match** (medium confidence): col 7 is still headed "Qualifying Segment Revenue (USD B)", but it stores native-currency *millions* (VW 321900 EUR; Toyota 48036700 JPY). The currency is in col 25. This is easy to misread.
- **Stale or contradicted docs:**
  - README and CLAUDE.md say 32 tests; there are 55.
  - MASTER_PROMPT says 831 rows and "do not expand the universe", yet `52648ce` grew it to 1,064. The rule wasn't updated.
  - The profile pass has "NO verbatim-quote gates", which undercuts the rebuild's own premise. This looks like a conscious scope trade-off, but the docs were not revised to match.
- **Coverage is low against the defined "done"**: 27/1,064 revenue rows, 0 units.
- **The categorical profiles are model-judgement output** with light enum validation only. The 300-row citation sample showed ~17% mismatch or inaccessible, and 73% of rows were never validated.

**Intentional shortcuts vs. defects:**
- Intentional: the profile reshape and the deferred validation are documented as choices.
- Defects: the column-mapping problem and the stale docs.

## 7 Developmental milestones
1. **2026-06-28 16:47 — rebuilt pipeline imported.** Tiered agents, gates G1–G8, golden set, a blank v1 seed.
2. **2026-06-28 23:24 — hardening:**
   - fetch improvements: browser and SEC user agents, retries, WAF-cookie and JS-render fallback, shell-page detection, content cache;
   - "verify-existing" mode that seeds candidates from a prior workbook, joined by company and not by rank, guarded by `tests/test_seed_join.py`;
   - native-currency revenue with no FX, plus `gates_revenue`;
   - opportunistic segment capture;
   - universe expanded to 1,064;
   - workbooks v2–v6 produced;
   - **reshape** to company × device-category edge-AI profiles (1,102).
3. **2026-06-29 02:23** — evidence fields (segment revenue/units, quote, URL, citation_status) merged into the profiles; partial citation validation.

## 8 Method changes and possible lessons
| Change | Earlier (dated) | Later (dated) | Possible trigger | Inferred lesson | Evidence | Alternative explanation |
|---|---|---|---|---|---|---|
| Tiering made real | "Previous version" ran everything on general-purpose agents (before 06-28, from README) | Deterministic Haiku/Sonnet batch routing, Opus as exception handler (06-28 16:47) | README says the old tiering was "never wired up" | Model tiering has to happen at batch/spawn time, not inside an agent | Explicitly documented | n/a |
| Trust model | Old filled data was trusted (before 06-28) | Everything re-derived; old fills become "candidates" (06-28 16:47 → 23:24) | Named bugs listed in "Why decomposed" | Treat AI-filled data as hints that must be confirmed against the source | Explicitly documented | n/a |
| Extractor prompts | `scale` = units/tens/thousands/millions; no currency (16:47) | Adds billions/trillions, required native currency, rules for contiguous table quotes, candidate-trap rules (23:24) | Revenue pass hit billion headlines, EUR-as-USD and composed quotes failing G7 | Prompt fixes aimed at observed failure classes | Strongly inferred (the specific examples in the diff) | Written ahead of time while designing the revenue pass |
| Seed join | Join by rank (implied) | Join by company, idempotent, with a test (23:24) | Commit message: "join prior workbook BY COMPANY (not rank)" | Never key on unstable rank | Explicitly documented (commit + test) | n/a |
| Main output | Precise verified per-row figures, quote-gated (16:47) | Fast categorical profiles "from own knowledge", no quote gates, then later evidence fields and sampled citation checks (23:24 → 02:23) | Throughput: 27 rows verified across 5 waves; the "weekly-limit" cap | Strict verification at this scale was too slow or costly for what was needed, so precision was traded for coverage plus after-the-fact sampled validation | Strongly inferred (commit says "re-shape … (primary output)"; v2–v6 fill counts) | A change in the downstream question, not a lesson from failure |

## 9 Capabilities, limitations, uncertainties
**Demonstrated in this repo:**
- designing multi-agent research workflows with model-tier cost routing;
- explicit task contracts and definitions of done for agents;
- deterministic verification gates around LLM extraction;
- golden-set regression testing against frozen snapshots;
- context handoffs across sessions;
- prompt revisions aimed at specific failures;
- recording validation outcomes honestly.

**Uncertainties:**
- the pre-import history and how much of the original design came from human versus AI;
- how the citation validation was done;
- whether the profiles were reviewed by a human;
- ownership context (see DISCLOSURE).

## 10 Evidence references and verification limits
**Files and commits:**
- `OEM@8392da1:README.md`, `PIPELINE.md`, `MASTER_PROMPT.md`, `CLAUDE.md`, `HANDOFF_TEMPLATE.md`, `.claude/agents/*.md`, `.claude/commands/*.md`, `golden/golden_cases.jsonl`, `golden/snapshots/*.txt`
- `OEM@52648ce:.claude/agents/oem-extractor-haiku.md` (diff), `pipeline/seed_candidates.py`, `pipeline/profile.py`, `cache/profile_instructions.md`, `tests/test_seed_join.py`, `Top_OEMs_exChina_Universe_2025_v2–v6.xlsx`
- `OEM@b4a98af:pipeline/profile.py` (`merge_evidence`), `cache/profiles.json`, `.gitignore`
- Column-mapping defect: `OEM@b4a98af:pipeline/workbook.py` (`COL`, `WRITE_MAP`) and `pipeline/run_wave.py` (`select_targets`); seen in v6 cols 12–13.

**Executed:** pytest (55 pass), golden gate (7/7), `run_wave status`, `telemetry` (empty), openpyxl inspection of v1–v6, and counts over `profiles.json`. All ran offline on a copy.

**Limits:**
- no agent or network runs;
- live source URLs and quotes not re-checked;
- gitignored artefacts and pre-import history unavailable;
- no PRs or issues exist.
