MANIFEST | billboard | private | research workflow + data pipeline + interactive map + agent-run vendor research (mixed) | complete | `main` is only an empty initial commit; all work lives on two unmerged `claude/*` branches; no PRs/issues; the handoff brief that drives everything is not committed; the agent session transcripts (claude.ai links in trailers) were not accessible; the vendor web-research workflow was not re-run (it needs agent/web runtime)

DISCLOSURE: No credentials found. A Census API key is *mentioned* ("with the Census key", kdevbw `PRESSURE_TEST.md`), but a search of the scripts, docs and workflow history for key-shaped strings found nothing committed. `.gitignore` (added in `billboard@13e07cc`) excludes `output/*subscriber*` and `output/*customer*`. Its commit message describes "the zero-subscriber expansion target list built from the uploaded customer address CSV" and calls it "private BI". No such file appears anywhere in the history (checked with `git log --all --name-only`). So the repo implies a real business with customers or subscribers, and a "client" (see "client-directed calibration" in `output/Billboard_Targeting_Report.md`), but it never names one. **Ownership/disclosure: partly ambiguous.** The repo contains no customer data, but the business beneficiary is unidentified, so the lead should confirm the context before this is shared or described as fully independent work. Third-party data committed: public Census/RCMS/election mirrors, about 140k precinct-level 2024 results (`data/raw/precincts_std/`), and public business contact details (phone, email, address) for billboard vendors in `output/vendors/*.csv`. Subject sensitivity: this is ad targeting by political lean, religious adherence and women aged 40–64. That is a reputational consideration if shared. The public counterpart repo `billboard-map` (named only) receives a redacted map. **Suitability to share:** possible after review. Keep the internal map (`output/billboard_map.html`) and full-factor CSV private as the repo itself intends, confirm the client context, and consider how the targeting subject reads.

# billboard — investigation report

## 1. Identity
- **Context:** A personal repository under the NYCandrun account. It is private, not a fork, and has no description. It was created 2026-07-19T17:32Z and last pushed 2026-07-22T03:43Z (from `gh api` / repos.json).
- **Type:** Mixed. It is an analytical research workflow (pressure-testing a "Swarm Handoff Prompt: Billboard ZCTA Ranking" spec), a reproducible Python data pipeline, two self-contained d3/canvas HTML maps, and an agent-orchestrated vendor web-research workflow.
- **Purpose:** It ranks every populated US ZCTA (ZIP-code area; 33,642 rows) for billboard placement. The intended audience profile (ICP) is "women 40–65, Christian and/or conservative, in middle-to-high-income ZIPs". The original strategy favoured conservative pockets inside liberal contexts. It then produces outreach lists of billboard vendors for the top areas.
- **Intended user:** A marketer or media buyer (called "the user"/"client" in the commits).
- **Maturity:** The pipeline works and reproduces exactly (verified, §4). Deliverables are versioned. The work was never merged to `main`, and the method was left in a reversed state (§8).

## 2. Dates and attributable contributions
- **First commit:** `99b9c35`, 2026-07-19 13:32 -0400. "Initial commit" by **NYCandrun <jacobnikolau767@…>**, committed through GitHub's web UI. It is the only commit Jacob authored, and contains a README with just a title.
- **Latest commit:** `71231d0`, 2026-07-22 03:43 UTC, on `claude/markdown-pressure-test-fb34h9`.
- **All 35 other commits** have author and committer "Claude <noreply@anthropic.com>". Most carry the trailer `Co-Authored-By: Claude Fable 5` or `Claude Opus 4.8`, plus `Claude-Session:` links to two distinct Claude Code sessions (`session_016iA4…` and `session_01NAyF…`). The last five vendor commits (`b308a51`…`71231d0`) have no trailers but the same Claude author. No other humans or bots appear.
- **Jacob's direction is visible only indirectly**, through agent-written commit text:
  - "Per user direction" (`57b9ce4`, 2026-07-20)
  - "client-directed calibration" (report, around `ed5ede4`)
  - "Not yet run pending scope confirmation" (`164b6a8`)
  - an "uploaded customer address CSV" (`13e07cc`)
- **Activity periods:**
  - 2026-07-19, 18:02–20:56 UTC: an intense build, about 30 commits.
  - 2026-07-20, 15:07–16:32: the second session's v0/rework, plus the `.gitignore`.
  - Pause of about 33 hours.
  - 2026-07-22, 01:19–03:43: vendor research.
- No inherited history, squashes or forks.

## 3. Branch and history coverage
- **Default branch:** `main`, containing only `99b9c35`.
- **Remote branches** (both forked from `99b9c35` and never merged; no PRs or issues per `gh pr list` / `gh issue list --state all`):
  - `origin/claude/markdown-pressure-test-fb34h9`: 32 commits (Fable 5 session). Contains the full pipeline, maps, Pages workflow, precinct data, methodology comparison and vendor research.
  - `origin/claude/markdown-pressure-test-kdevbw`: 3 commits (Opus 4.8 session): `f80ad2c`, `3647596` and `57b9ce4`. A separate pressure test of the same brief, a "v0" screen and a conservatism×reach filter CLI (`pipeline/`).
- **The two branches are parallel, independent agent runs on one brief.** They are not a feature split. Both reached the same finding (all Census/ARDA/Dataverse hosts blocked by egress) and then diverged:
  - fb34h9 hunted for GitHub mirrors and built the full model.
  - kdevbw built only the reachable half, documented three data paths, and stopped.
- **Files present in history but removed at tip:** `scripts/build_map.py`, `scripts/build_public_map.py` (superseded in `801a198`) and `output/vendors/_master_raw.json` (added in `b308a51`, dropped in `7ef8ebd`).
- **Inaccessible:** the brief itself (`Swarm_Handoff_Prompt___Billboard_ZCTA_Ranking.md`, referenced but not committed), the session transcripts, the "two OKComputer builds" being compared, and the GitHub Pages deployment state.

## 4. Actual functionality (inspected and executed)
**fb34h9 pipeline.** `scripts/fetch_data.sh` → `convert_rda.py` → `build_rankings.py` (about 25 KB) → `validate_and_charts.py`, plus `build_precinct_zcta.py` and `build_maps.py`.

The score combines four factors:
- **demo_fit:** share of women aged 40–64 (ACS 2022 B01001)
- **affluence:** median household income (S1903)
- **faith:** RCMS 2020 adherence, weighted 0.5/0.3/0.2
- **politics:** two-party share from precinct votes aggregated to ZCTAs where at least 200 votes exist, otherwise county share

These feed a weighted receptivity term. The total score is `0.50·receptivity + 0.30·tension·politics_damp + 0.20·exposure`. Eight precomputed variants (income-free, population-neutral and deep-red, in combinations) drive toggles on the maps.

**Maps.** `build_maps.py` emits two maps:
- the internal full-tooltip map, `output/billboard_map.html` (about 9.9 MB)
- a redacted public `index.html` whose gzip payload holds only location, score, rank and population. Grep of the tip `index.html` found no `gop24`, `faith` or `med_hh` strings.

A Pages workflow (`.github/workflows/pages.yml`) deploys only `index.html`, and only from the agent branch.

**Vendor workflow.** `scripts/vendor_research.workflow.js` defines one workflow per area. Three parallel web-research agents (national OOH operators / regional and local independents / marketplaces and programmatic platforms) return results in a JSON schema, which are then deduplicated by normalised name. The prompt says "Do NOT invent vendors, phone numbers, or URLs". `_runs.json` records 10 runs with run IDs and 222 vendor rows. `build_vendor_csvs.py` produces per-area CSVs, a local-only CSV (69 operators) and a "best-pick" call sheet.

**kdevbw.**
- `pipeline/build_screen.py` computes `screen_score = 100·(0.60·pr(gop24)+0.40·reach)`, with income, age and faith columns present but NaN.
- `pipeline/filter.py` is a CLI that slices by state, region, trifecta, `rel_redness` and similar.

**Executed (offline, on `git archive` copies in /tmp; nothing was pushed):**
- `build_rankings.py` reproduced `output/billboard_zcta_rankings.csv` exactly: 33,642×77, and the maximum absolute difference was 0.0 on `score`, `national_rank`, `score_deepred`, `score_noincome` and `score_popadj`. The top 10 is South Orange County and Staten Island.
- `validate_and_charts.py` passed its gates: 100% vote-join coverage; 90210 medHH $172,285; Bible-Belt median rank 15,300.
- kdevbw's `build_screen.py` reproduced `billboard_zcta_ranked.csv` byte-identically, and `filter.py` ran correctly.

**Not executed:** `fetch_data.sh` (network), `build_precinct_zcta.py` (needs shapely and ZCTA geometry), the agent vendor workflow, and the maps in a browser. Vendor contact accuracy was not verified.

## 5. How Jacob uses or builds with AI
- **AI is used to build and to research.** The product itself contains no AI. The vendor stage is an AI research product: an orchestrated multi-agent web-research workflow with structured output.
- **Delegation pattern:** Jacob appears to have:
  - written or obtained a detailed spec (the "swarm handoff prompt", originally for another sandbox, evidently the OKComputer environment the comparison references);
  - handed it to Claude Code with an instruction to *pressure-test* it (the branch name is "markdown-pressure-test");
  - run **two sessions with different models in parallel** on the same task (strongly inferred from the two branches, models and session IDs);
  - steered iteratively through short directives visible in the commit text.
- **Cross-system comparison:** He also had the agent benchmark its output against two other AI builds of the same problem. `output/METHODOLOGY_COMPARISON.md` reports Spearman 0.845 and 0.490 and top-2000 overlap, and lists what to adopt from each. This is deliberate multi-agent triangulation, and the strongest direct evidence of a verification mindset.
- **Judgment visible in direction:**
  - map label naming and polarity fixes (`e1a3fdc`, `c60f747`)
  - a requirement to redact the public map (`167f97e`)
  - weight calibrations (`edd59dd`, `33b6ce7`, `ed5ede4`)
  - a directive to let deep-red areas dominate (`57b9ce4`, `33340f7`)
  - a scope gate before the vendor runs (`164b6a8`, "pending scope confirmation")
  - data-privacy hygiene (`13e07cc`)
- **Agent-level verification and debugging, as documented by the agent:**
  - the §6.5 sanity-geography gate caught a fractions-vs-counts bug and a border-ZCTA bug (`PRESSURE_TEST.md` §4);
  - a scout subagent's wrong B01001 column mapping was caught "by checking the file's own label row";
  - a workflow bug where `args` arrived as a string, so agents searched for "undefined", was found, fixed and fully re-run (`b308a51` → `7ef8ebd`).
- **Caveat:** whether Jacob or the agent noticed these bugs cannot be determined from the repo.

## 6. Subjective quality assessment
**Strong (high confidence):**
- **Reproducibility:** the outputs regenerate exactly from committed raw data.
- **Provenance:** every substitution, its vintage and its cost is tabulated, and quality flags are kept as columns (`politics_data`, `income_imputed`, `demo_source`).
- **Real validation gates and falsification:** kdevbw showed that dropping the tension term recreates the brief's "Bible-Belt failure pattern".
- **Candid scoping:** kdevbw's v0 README states the screen over-weights population.
- **Methodology critique** (kdevbw Part A): tension double-counts state partisanship, faith weights favour the Northeast, ecological fallacy, `diversity_adj` has no adjacency term, and ZCTA is not the buyable media unit. The critique is substantive.
- **Respecting the egress policy:** it explicitly refused to bypass the egress controls.
- **Extending past the spec:** precinct-level politics for 73% of ZCTAs.

**Weaknesses and defects:**
- **The method was reversed without the docs being reconciled.** The report's mission still says "explicitly *not* prioritizing saturated deep-red regions", while the final vendor work targets the top-10 *deep-red* areas (Magnolia TX, Brentwood TN…). The deep-red mode simply drops tension. Many intermediate calibrations became moot.
- **Stale figures in the docs:** commit text and docs give Bible-Belt figures such as "9 of 2,383" and "15 of 2,383" in the top-2000, while the current run gives 49.
- **The public redaction intent eroded.** `f9f210d` deliberately kept income hidden on the public map, and `ce1b9e1` used a neutral "Economic adjustment" label. `e1a3fdc` then renamed it to "Income adjustment", and the tip `index.html` contains that label, which reveals income as an input. This may have been user-directed, but it is undocumented.
- **No tests beyond print-based gates.**
- **A local patch to the `rdata` library is required** (`scripts/rdata_raw_patch.md`).
- **About 100 MB of data is committed.**
- **The kdevbw critique's recommended fixes (Problems 1, 2, 4) were never applied** on either branch.
- **Vendor link accuracy is unverified:** the call sheet says "vendor sites block automated fetch but are live", and links were resolved via search.

**Overall (medium-high confidence):** a strong, well-documented analytical build with exemplary provenance and reproducibility. The strategy changed late, and the docs and stated validation targets were not reconciled with it.

## 7. Developmental milestones
1. **2026-07-19 18:02 (`4c92436`) and 18:07 (`f80ad2c`):** two parallel pressure tests plus a first build on mirrors.
2. **18:11–18:26 (`08de7c9`, `1d31c47`):** one integrated dataset; a mirror hunt replaces every fallback (ACS 2022, RCMS 2020); first interactive map.
3. **18:31–18:43 (`7998342`, `440c9e2`, `167f97e`):** contrast modes, Pages publishing, redacted public map.
4. **18:53–19:11 (`08a133a`, `801a198`):** precinct aggregation script; switch from county to ZCTA-polygon choropleth (with a ring-winding fix).
5. **19:21–19:39 (`f9f210d`, `ce1b9e1`, `edd59dd`):** score variants; politics damping.
6. **19:45–19:51 (`811888a`…`fbe57f7`):** an 8-agent precinct extraction "fleet" (about 140k precincts); politics now from precinct data.
7. **19:54 (`486ddd0`):** comparison with the OKComputer builds.
8. **19:59–20:56:** population-neutral variant, toggle UX fixes, damping recalibrated twice, then Deep-red mode (`33340f7`).
9. **2026-07-20 (`3647596`, `57b9ce4`):** kdevbw v0 screen, then a conservatism×reach rework "per user direction".
10. **2026-07-22 (`164b6a8`…`71231d0`):** vendor-research workflow, bug fix and re-run, local-only filter, call sheet.

## 8. Changes in working method and possible lessons
- **Spec execution → spec pressure-testing and adaptation (07-19).**
  - Before: the brief prescribed a 6-agent fetch swarm with a paste-back protocol.
  - After: one deterministic pipeline using mirrors (`PRESSURE_TEST.md` §1).
  - Trigger: egress blocks were documented.
  - Lesson: environment playbooks don't carry over between sandboxes, so redesign for the actual runtime.
  - Evidence: **explicitly documented**.
- **County → precinct politics (07-19, `811888a`/`fbe57f7`).**
  - Trigger: the brief's own expectations (DuPage, Anoka) were "inconsistent with the §5 formula" at county level (§4).
  - Evidence: **explicitly documented**.
- **"Contested relative-red" strategy → absolute deep red (07-19 20:56 `33340f7`; 07-20 `57b9ce4`; vendor stage 07-22).**
  - Trigger: user direction. The motive is not stated, though one is suggested by the "zero-subscriber expansion" analysis using customer addresses (`13e07cc`).
  - Inferred lesson: real customer data may have contradicted the brief's thesis.
  - Evidence: the direction change is **explicitly documented**; the reason is **speculative**.
  - Alternative explanation: a business preference for simplicity, or an A/B comparison.
- **Single-run trust → cross-build triangulation (`486ddd0`).** Evidence: **explicitly documented**. A lesson recorded there: adopt OKC-2's independent audit agent ("stronger than our spot-check-based validation"). It was never adopted afterwards.
- **Vendor research: gated scoping → run → fix → full re-run (`164b6a8`→`7ef8ebd`).**
  - The run→area mapping was tracked (`_runs.json`) so the outputs could be audited.
  - Lesson: verify agent inputs, since agents silently searched for "undefined".
  - Evidence: **explicitly documented**.
- **Earlier process:** this is the snapshot of three days; the brief's own earlier evolution cannot be reconstructed.

## 9. Demonstrated capabilities, limitations, uncertainties
**Demonstrated:**
- specifying and delegating a complex analytics brief to coding agents;
- running parallel agent attempts and comparing them quantitatively;
- steering scoring and UX through iterative directives;
- an awareness of public/private data exposure;
- gating costly agent fan-out on a scope confirmation;
- an agent-built pipeline with strong provenance and exact reproducibility.

**Uncertainties:**
- the identity of the "client" and the source of the customer CSV;
- whether Jacob personally caught any of the bugs;
- the content of the brief;
- vendor data accuracy;
- whether `billboard-map` (public) mirrors the redacted `index.html`.

## 10. Evidence references and verification limits
- `billboard@99b9c35:README.md`; `@4c92436` (initial build, 21 files); `@f80ad2c`/`@3647596`/`@57b9ce4` (kdevbw `PRESSURE_TEST.md`, `pipeline/build_screen.py`, `pipeline/filter.py`, `output/README.md`).
- `@71231d0` tip of fb34h9: `PRESSURE_TEST.md` §§1–5, `output/Billboard_Targeting_Report.md` §3, `output/METHODOLOGY_COMPARISON.md`, `scripts/build_rankings.py`, `scripts/vendor_research.workflow.js`, `output/vendors/_runs.json`, `output/vendors/top10_best_picks_callsheet.csv`, `.github/workflows/pages.yml`, `.gitignore`.
- Key diffs: `b308a51` (args JSON.parse fix), `167f97e` (redaction), `f9f210d`/`ce1b9e1`/`e1a3fdc` (public label sequence), `edd59dd`/`33b6ce7`/`ed5ede4`/`33340f7` (damping → deep red), `13e07cc` (customer-data gitignore).
- PRs/issues: none.
- **Verification limits:** offline re-runs only. Fetch, precinct aggregation, browser rendering of the maps, the Pages deployment and the agent vendor runs were not executed. Session transcripts, the brief and the OKComputer builds were unavailable.
