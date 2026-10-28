PRIVATE — internal research synthesis. Not for distribution without disclosure review.

# Jacob Nikolau: Personal AI Projects, Current Capabilities, and Evolution

**Evidence basis.** This synthesis uses only the 28 personal repositories owned by the GitHub account NYCandrun, their branches and history, and PR/issue metadata. It draws on 28 per-repo investigator reports, re-checked by the synthesis agent with git history inspection and offline test re-runs on read-only copies. No résumé, call, Drive or memory material was used.

**Scope rulings.** All repos are personal projects. Companies that appear as research subjects are not employers. BTCsecrets and the strategy/charter branches of marketplace_prototype are withheld and are not used for capability claims. billboard is assessed for method only.

**Window.** The portfolio spans 2026-03-10 to 2026-10-24, about 7 months, with no personal repos before 2026 and no commits in April–May or August.

Companion files: `coverage_manifest.md`, `comparison_table.md`, `evolution_timeline.md`.

---

## A. Where he currently stands

*Question: Based specifically on Jacob's personal GitHub projects, where does his practice of building and researching with AI currently stand?*

The practice does not fit one label. It is uneven across six areas.

| Area | Current standing (as of Oct 2026) | Representative evidence |
|---|---|---|
| **Research orchestration** | The most developed area. He designs multi-agent research runs with source grading, verbatim receipts, separate reviewer contexts, recorded live steering, and cost and context controls. In October he turned this into a reusable method, then a fail-closed control plane | `airops@c1ba3ba:00-inputs/PROMPT.md`; `airops@8581d67`; `airops@0d21793:README.md` §19; `research_prompt@1a4d35c` (45 tests OK, re-run); `pmm@2071a24` |
| **Prototyping** | Fast and broad. He directs coding agents from a PRD to a working prototype in hours to days, with tests and build passing in the stronger cases. Depth and hardening vary a lot | `marketplace_prototype@48e1a8c` (vitest 89/89, CI vs Postgres); `etta_app_update@be2d460`; weak: `TextAdventures`, `r_app` (not buildable) |
| **Experience design** | Clear attention to the reader or player: plain-language rewrites for a generalist reader, removing answer cues in a game, reader-facing reframes after real outputs. These are mostly product-thinking decisions, not visual craft | `liquid-ai-study-guide@1c4a924`; `ashby@cbcb985`; `liquid-token-budget-slider@90927bc` |
| **Integration** | Moderate. LLM APIs (BYO key), VLM serving on Modal, Stripe Connect, Cloudflare worker, Tauri. Integration bugs and contract mismatches recur | `Liquid_SDK_Test@a3c3294`; `liquid-token-budget-slider@18bcd91`; iOS/worker mismatch in `TextAdventures` |
| **Evaluation** | Strong when evaluation is the point of the project: pinned benchmarks, a referee lane, golden sets with negative controls, planted-error tests, documented negative findings. Weak when evaluation is a side task: eval judges stubbed, tests left uncommitted | Strong: `Liquid-Moondream-450M-Benchmark` (198 tests, re-run), `chip` golden 16/16, `airops` citation planted-error test. Weak: `TextAdventures-Content@03afa34` (concierge fails, re-run), `ashby` tests not committed |

**Personal experimentation vs production constraints.** Almost everything here is self-directed, single-user, and short-lived. Repos are typically built in one burst of hours to a few days. Merges happen in seconds. Branches are often left unconsolidated. These are normal traits of exploratory personal work. They are not evidence about behavior under team review, uptime, or customer constraints, and the repos say nothing either way about how he works in those settings.

**Summary.** As of October 2026 his practice is most mature at directing and governing AI agents for evidence-grounded research. He treats agent output as untrusted until it is checked by code, and he writes down why. Prototyping is fast but uneven in rigor. Evaluation rigor is high when it is the focus, inconsistent when it is not.

---

## B. Evolution over time (Mar–Oct 2026, ~7 months)

Full dated chronology: `evolution_timeline.md`.

1. **March: spec-first delegation with AI self-audit.** Jacob writes a PRD. Claude Code web sessions build the app, and he merges PRs (`etta_app@2848342`; 68 agent commits). Verification is agent-on-agent audit (`etta_app@97a382e`, `@ce7308b`), with self-reported status, no CI, and overclaims (`r_app@2b87df2`). His own visible correction is restoring fixes an agent had overwritten (`r_app@27de0ed`).
2. **June: parallel partitioning, provenance, and the first code gates.** Study material is rewritten by "22 parallel Opus 4.8 agents each owning one isolated chunk" (`liquid-ai-study-guide@1c4a924`). Sourcing is restated honestly as "AI-generated research reports" (`liquid-ai-prep-course@603753d`). On 06-28 agents bypassed a prose instruction, and he responded with a structural boundary (`chip@75d4fa1:AGENT_BRIEF.md`) and deterministic gates with negative controls. Two weeks earlier (06-15) the same habits were missing, and a false "all pass" claim was committed (`TextAdventures-Content@03afa34`, re-run fails).
3. **July: independent instruments and paired comparison.** A pinned benchmark with a referee lane and a numbered change log (`Liquid-Moondream-450M-Benchmark`). The same PRD went to Claude and to Jules (identical md5; `marketplace_prototype@16f93c7` vs `prototype_Jules@f912077`). Cross-build methodology comparison (`billboard@486ddd0`). A cost/security self-catch (`liquid-token-budget-slider@18bcd91`). A regression surfaced: the June etta rebuild's green gates had passed a 100% crash and an onboarding loop (`etta_app_update@be2d460`).
4. **September: scale and line-pinned provenance.** 24-analyst KB research with `[[kb:path#Lnn]]` citations and a line-by-line live check (`pmm@2071a24`). Jacob's visible role shifts further to direction; the `Claude` identity authors the commits.
5. **October: articulated lessons and reusable, code-enforced method.** A research kit with an explicit lessons list (`ai_game@fb0038c:pmm-research-kit/README.md`), carried byte-for-byte into the next run (`airops@c1ba3ba`). Run-time failures became prompt rules (`airops@8581d67`). Jacob's own §19 states that the orchestrator cannot declare completion (`airops@0d21793`). This was then implemented as a fail-closed control plane through Codex (`research_prompt@5fab799`→`@1a4d35c`) and run live (`genesis@7c2fff2`), where it stopped mid-capture.

**What did not evolve (plateaus).**
- Documentation drift after pivots, in roughly ten repos.
- Seconds-long merges without visible review.
- Work stranded on unmerged branches, every month, including October's genesis fixes.
- Reproducibility gaps from uncommitted briefs and session paths (pmm).

**Caveat on attribution of change.** Model and tool labels change throughout: Opus 4.7, 4.8, 5, 5.5; Fable 5 and 5.1; Sonnet 5; Jules; Codex; `gpt-5` workers. Some apparent progress, especially the scale of the October control plane, may reflect newer tools rather than learned practice. Section C marks where the two can be separated.

---

## C. Learning arcs

Evidence-type codes:
- **[T1]** technique tried once
- **[RH]** recurring habit
- **[EL]** explicitly articulated lesson
- **[IL]** inferred lesson
- **[NT]** capability plausibly from newer tools

| Earlier evidence | Later evidence | Inferred lesson | Evidence of transfer | Confidence and alternatives |
|---|---|---|---|---|
| **1. Prose instructions → code-enforced boundaries.** `chip@75d4fa1`: "some batch-1 agents bypassed it", then an `AGENT_BRIEF.md` hard boundary and single-writer re-ingest (06-28) | `airops@0d21793` §19: orchestrator "is not the authority for declaring a phase … complete" (10-22). `research_prompt@5fab799` fail-closed UNKNOWN gates, F001 "Agent messages are never execution evidence" | Agents do not reliably obey prose. Put the checkable parts in code and make missing evidence block [EL in Oct; IL linking June to Oct] | Strong. Same pattern in chip and OEM (June), the Moondream referee lane (July), the airops planted-error tests, and the October control plane [RH] | **High** that the habit recurs. **Medium** that June directly taught October: no document links them. The October scale of code is partly [NT] (Codex). Alternative: general agent-engineering practice adopted from outside sources |
| **2. Self-reported verification → independent re-check.** Mar: agent audits of agent work (`etta_app@97a382e`). Jun: `TextAdventures-Content@03afa34` playtest re-run fails. June etta gates green | July: `etta_app_update@be2d460` "154 findings, adversarially verified" finds a 100% crash. Referee lane in Moondream. Cross-build comparison `billboard@486ddd0`. Oct kit: "Agents' hand-back summaries miss things. Reading the full reports found fixes the summaries left out" (`ai_game@fb0038c`) | Agent claims of success need an independent check [EL in Oct; IL before] | Partial. Adopted in research and benchmark work, not consistently in apps or games. Ashby (Sep) did not commit tests | **Medium**. The July adversarial pass coincides with a new model trailer (`Sonnet 5`) [NT]. Alternative: an ad hoc response to visible breakage |
| **3. Provenance as a first-class design object.** 06-11: honest source labels (`liquid-ai-prep-course@603753d`) and a citation layer (`liquid-ai-study-guide@b7050eb`) | 06-28 quote-in-cache gates (`chip`, all 361 quotes found). 09-24 line-pinned tokens and live check (`pmm@2071a24`). 10-21 P/S/T/I grades and receipts (`airops@c1ba3ba`). 10-23 citation/quote validators (`research_prompt`) | Claims must be traceable to captured evidence, and the evidence class must be labeled [RH; IL] | Strong. Appears in every research project from June to October | **High**. Weakness that persists: ellipsis-stitched quotes (chip); 5,673 of 9,179 airops facts checked by script only (stated openly) |
| **4. Spend model judgment where it reaches the reader.** Earlier: verify everything with layered audits (airops prompt v1, 10-21). `OEM@52648ce` trades precision for coverage under budget | `airops@1e2e6f5`/`@353addc`: scripts on all facts, one Opus pass on cited facts only. `@7bf38f3` time-boxes audits. Kit README: leave out the heavier rounds for onboarding. `home_security_benchmark@61eb1cb` budget-aware planner. `etta_app@d4b9bb2` token budgets (March) | Proportionate verification and cost awareness [EL in Oct] | Medium. Cost reasoning appears in March, July and October. The October rule is explicit and reused in research_prompt (model-tier routing, `@717440a`) | **Medium**. Alternative: time pressure rather than principle. The airops run still used ~1.67B tokens (self-reported) |
| **5. Delegation briefs robust to context contamination.** Oct 22 03:53Z: agents read the user's status question as their task (RUN_HISTORY) | `airops@8581d67` TASK TYPE line. `research_prompt`/`genesis` `AGENTS.md`: packets carry "no inherited status conversation" | Isolate worker context; briefs must state the task type [EL] | Yes: airops → research_prompt → genesis within 2 days | **High** for the lesson; **low** for durability, since it is only 2 days old |
| **6. Choosing and comparing agents.** Mar–Jun: Claude Code only | 07-07: same PRD to Claude and Jules (`marketplace_prototype` vs `prototype_Jules`). Oct: Codex for the refactor, `gpt-5` workers (`genesis` ledger), adapters for both (`AGENTS.md`, `CLAUDE.md`) | Treat agents as interchangeable executors behind a host-neutral spec [IL] | Partial. The Jules experiment was not written up and its PRs were left untriaged. October adapters show host-neutrality by design | **Low–medium**. Alternative: curiosity or tool trials rather than deliberate selection |

**One-off techniques [T1]:**
- Prompt mode-slicing (`etta_app@d4b9bb2`)
- LLM-as-compiler with a playtest gate (TextAdventures)
- Gemini synthetic benchmark (home_security_benchmark)
- Product tour from KB screenshots (Clearly-Rated branch)

---

## D. Current operating approach

**Demonstrated (seen in October repos and earlier):**
- Writes a long, first-person specification before agents start (`airops@c1ba3ba`, 351 lines), and later edits it himself (`airops@0398294`, `@0d21793`).
- Runs agents in parallel, with one orchestrator owning shared state, workers on non-overlapping slices, and reviewers in separate contexts (airops `WORKFLOW_STATE.md`; `research_prompt` reducers).
- Steers live and records decisions with timestamps: cut Wayback, do not bypass bot challenges, a 10–15 page brief, a currency wording rule (airops `WORKFLOW_STATE.md` §5).
- Requires receipts and grades for facts, and keeps vendor claims apart from independent evidence.
- Turns observed failures into rules, then into code with tests (`airops@8581d67` → `research_prompt`; `genesis@d073470`/`@7c9d11d`/`@3ee0288`).
- Uses multiple agent hosts: Claude Code, Codex, earlier Jules.
- Keeps editorial control over outputs: author cuts and decisions on the ai_game research branch; the "company brief" reframing (airops `prompt/CHANGES.md`).

**Inferred intent (not proven):**
- To build a repeatable, host-neutral "one URL → cited company brief" capability for his own onboarding into new domains. The scope says "Point of view: product marketing" (`genesis@7c2fff2:00-scope.md`).
- To prefer completeness before synthesis, accepting high token and time cost.
- To keep the repos as working notebooks rather than maintained products. This would explain the unconsolidated branches and stale READMEs.

---

## E. Strengths, limitations, and next steps

**Strengths (grounded):**
1. **Verification design for agent work.** Golden sets with negative controls (`chip`), a referee instruments lane (Moondream; 198 tests re-run), planted-error tests (airops), and fail-closed gates (`research_prompt`, 45 tests re-run).
2. **Provenance discipline**, applied consistently across research work from June to October.
3. **Candor about limits.** Negative findings recorded (`home_security_benchmark@068e7e6`), "least sure of" sections, refusal to "retroactively certify" (`research_prompt@5fab799:REFACTOR_REPORT.md`), and the honest source relabeling (`603753d`).
4. **Learning from failures within a project**, sometimes generalized across projects (Section C, arcs 1 and 5).
5. **Cost and security awareness at key points** (`18bcd91`, `8581d67`, budget planner).
6. **Breadth.** Desktop, iOS, web, VLM serving, benchmarks, data pipelines and research runs, all directed through agents.

**Limitations (observed gaps):**
1. **Green gates that missed defects.** Examples: `TextAdventures-Content@03afa34` (concierge playtest fails on re-run), June `etta_app_update` (fixed in `be2d460`).
2. **Doc drift** after pivots in roughly ten repos. It did not improve over the window.
3. **Follow-through and consolidation.**
   - 25 Jules PRs left open, including security fixes.
   - Two billboard sessions unmerged.
   - genesis run fixes stranded off `main`.
   - research_prompt's default branch is the oldest version.
   - Several write-ups unfinished: Moondream, home_security steps 3–5.
4. **Review visibility.** PRs are merged within seconds, and there is no evidence of line-level human review of agent code.
5. **Reproducibility.** pmm depends on session paths. Briefs and pre-repo runs are uncommitted (home_security `LESSONS_LEARNED` refers to a run not in the repo). Large binaries and caches are committed.
6. **Process cost relative to output.** The genesis run produced only the capture stage and a brand guide. airops used ~1.67B tokens (self-reported) for one brief.
7. **Hygiene and disclosure.** Commercial assets in public repos (`zork1.z5`, fonts), personal material in public repos (ai_game branch), a trivial password in history.

**Next steps suggested by the gaps (personal practice):**
- Make "re-run every claimed check before committing the claim" a committed pre-commit or CI step in app and game repos, as in the research repos.
- After pivots, add a README/PRD reconciliation step, and a "consolidate or close" pass for branches and bot PRs.
- Finish one end-to-end live run of the October control plane through release, merge its fixes to `main`, and publish the cost profile.
- Commit the briefs and prompts that drive runs, so they can be reproduced.
- Run a disclosure sweep on public repos.

**Further evidence that would help this assessment:**
- PR review comments or local review notes.
- Session transcripts, to separate Jacob's edits from agent output.
- A completed genesis or research_prompt run.
- Any personal project operated over time with users.
- Repos from before March 2026, if any exist outside this account.

As noted above, absence of evidence here is not evidence of absent professional ability.

---

## F. Optional: potential implications for the PMM role

*Labeled exception requested by the task. These are potential implications drawn from personal work only.*

- The October research method has the explicit aim of getting "up to speed fast" on a company's products, packaging, positioning, customers and competitors (`airops@c1ba3ba:00-inputs/PROMPT.md`). It suggests a personal habit of evidence-graded competitive and product research that could transfer to market-intelligence tasks.
- Separating vendor claims from independent evidence (142 vendor-only citations flagged in `liquid-ai-prep-course`; P/S/T/I grades) and surfacing conflicts rather than resolving them (158 conflicts in `pmm`) are relevant to positioning and claims-review work.
- Reader-first reframes (`liquid-ai-study-guide@1c4a924`; the "company brief" reframe in airops `prompt/CHANGES.md`) suggest attention to audience.

---

## Limitations of this synthesis

- **Short window.** The evidence covers ~7 months, with 3 of those months empty, so "evolution" means short-term change. Most repos are one-burst sessions.
- **Attribution.** Agent authorship is credited only from trailers, bot accounts, agent files and branch names. Commits with no trailers (research_prompt, genesis, Liquid_SDK_Test, TextAdventures) are unattributed, not assumed hand-written. Jacob's edits within agent sessions are invisible.
- **Coverage of runs.** Networked and paid model runs were not repeated. Investigators and synthesis re-ran only offline tests: OEM 55, Moondream 198, research_prompt 45, TextAdventures-Content playtest. Factual accuracy of research outputs was sampled, not audited.
- **Withheld material.** BTCsecrets and the strategy branches of marketplace_prototype were excluded from capability claims. billboard was assessed for method only.
- **Family counting.** pmm and Clearly-Rated were counted once. The research-prompt lineage (ai_game kit → airops → research_prompt → genesis) was treated as one body of work. Synthesis verified it byte for byte and corrected two reports that called its early history unrecoverable.
- **Ratings are subjective** and calibrated within project type. Small investigator disagreements were resolved toward later, verifiable commits.
- **Confounds.** Tool and model changes confound learning claims (Section C, [NT]).

---

## Shortlist: examples potentially suitable for sharing after disclosure review

| Example | Why it is representative | Must be removed or checked first |
|---|---|---|
| `Liquid-Moondream-450M-Benchmark` (METHODOLOGY.md, RESULTS.md, change log, HANDOFF.md) | Best single evaluation example: pinning, referee lane, self-correction; tests pass | Confirm no Modal account identifiers or tokens in history; finish or label the write-up as unfinished |
| `chip` method (AGENT_BRIEF.md, gates, golden set; commit `75d4fa1` narrative) | Clearest "agents bypassed → structural fix" story with negative controls | Remove the 534 MB third-party document cache; note the `mosaicapp.com` email in metadata |
| `research_prompt` at `1a4d35c` (already public) | Fail-closed control plane, 45 tests | The legacy prompt in history reveals personal job-search context and names AirOps. Decide whether to rewrite history or accept it; set the default branch to the latest version |
| `ai_game@fb0038c:pmm-research-kit/README.md` + PROMPT.md | Explicit lessons list, generic and reusable | Extract it alone. The surrounding public branch contains personal interview material and BlackRock research that should be reviewed and probably removed or made private |
| `marketplace_prototype` main vs `prototype_Jules` (same PRD) | Paired comparison of two agents | Exclude the withheld charter/strategy/research/dossier branches entirely; check Stripe test keys and env files |
| `liquid-token-budget-slider@18bcd91` | Concise security and cost self-catch | The old endpoint URL is in history. Confirm the endpoint is decommissioned |
| `airops` method docs (prompt v2 CHANGES, WORKFLOW_STATE decisions, citation checker test) | Live steering and lessons-to-rules evidence | Remove the non-public fact about a named person (IN-004/ORG-475), the personal job-search framing, third-party captures, and commercial fonts |

Not recommended for sharing without major review:
- BTCsecrets (third-party legal package).
- billboard and billboard-map (unnamed client, sensitive targeting).
- pmm/Clearly-Rated (copyrighted mirror).
- true_read (names prior employers).
- Liquid_SDK_Test (commercial game file).
