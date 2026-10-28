PRIVATE — internal research file. Not for distribution without disclosure review.

# Coverage manifest — Investigation 3 (personal GitHub AI practice)

Scope: the 28 repositories owned by the personal account NYCandrun. The lead ruled that all of them are personal projects. Companies that appear as research subjects (Liquid AI, AirOps, Ashby, ClearlyRated, BlackRock, Genesis Computing) are not employers. A `mosaicapp.com` commit email (chip, OEM, liquid-token-budget-slider, liquid_LFM2.5-VL_demo, early etta_app/r_app) is treated only as identity metadata.

Evidence base: the per-repo reports in `reports/*.md`, local clones in `repos/`, PR/issue JSON in `prs/`, and the synthesis agent's own re-checks (see "Synthesis re-verification" below). The time window is 2026-03-10 to 2026-10-24. There are no personal repos dated before 2026.

Status key: **complete** = report delivered and reviewed by synthesis. **withheld** = assessed at a high level only, pending owner confirmation.

| Repo | Context | Visibility | Project type | Assigned investigator | Status | Limitations | Disclosure flag |
|---|---|---|---|---|---|---|---|
| etta_app | Personal project | PRIVATE | macOS app (Tauri/Rust + React) AI tutor; agent-built | repo_etta_app_mvph6uhq | complete | History imported from a predecessor account; app not run end to end; no CI | Low. A built binary zip is committed |
| r_app | Personal project | PRIVATE | iOS SwiftUI language-learning app; agent-built | repo_r_app_mvph6w04 | complete | No xcodeproj, so not buildable; nothing executed | Medium. AI API key handled in the client by design (no live secret copied); client-side paywall |
| etta_app_update | Personal project | PUBLIC | Rebuild of etta_app; agent-built | repo_etta_app_update_mvph6uli | complete | Desktop UI not exercised; tests/build only | Low |
| liquid-ai-prep-course | Personal project (subject: Liquid AI) | PRIVATE | Static study course from AI research reports | repo_liquid_ai_prep_course_mvph6v12 | complete | Factual accuracy of 378 citations only sampled | Medium. Trivial gate password in history (`0639b93`); README stale |
| liquid-ai-study-guide | Personal project (subject: Liquid AI) | PRIVATE | Static study guide; multi-agent fact-check/rewrite waves | repo_liquid_ai_study_guide_mvph6v5g | complete | Citation targets resolve; claim accuracy sampled only | Low |
| Liquid_SDK_Test | Personal project | PUBLIC | AI-product prototype (Zork + LLM hints via OpenRouter, user's own key) | repo_liquid_sdk_test_mvph6t96 | complete | No AI-authorship evidence; LLM path not called (needs key) | Medium. Commercial game file `zork1.z5` in a public repo |
| TextAdventures | Personal project | PRIVATE | iOS + Cloudflare worker text-adventure platform | repo_textadventures_mvph6tif | complete | iOS not built; single ~87-minute session | Low |
| TextAdventures-Content | Personal project | PRIVATE | Content repo; LLM-as-compiler pipeline | repo_textadventures_content_mvph6tlo | complete | Single commit | Low |
| true_read | Personal project | PUBLIC | Consulting landing page (static) | repo_true_read_mvph6wcs | complete | No AI evidence | Medium. Names prior employers in self-description |
| chip | Personal project (research; identity email only) | PRIVATE | Agent-gated market-research dataset pipeline | repo_chip_mvph6ubv | complete | 534 MB vendor cache not fully reviewed; live collection not re-run | Medium. Large third-party document cache |
| OEM | Personal project (research) | PRIVATE | Tiered-model extraction pipeline for an OEM universe | repo_oem_mvph6tcr | complete | Live model runs not repeated | Low–medium. Third-party filings cached |
| liquid_LFM2.5-VL_demo | Personal project | PUBLIC | Persuasive field note + TCO calculator | repo_liquid_lfm2_5_vl_demo_mvph6vey | complete | Only arithmetic checked | Medium. Vendor-styled one-pager could read as official |
| liquid-token-budget-slider | Personal project | PUBLIC | VLM demo (FastAPI server + UI), Modal recipe | repo_liquid_token_budget_slider_mvph6vap | complete | GPU path not run | Low now. A public endpoint was removed in `18bcd91`; URL remains in history |
| token-budget-liquid | Personal project | PRIVATE | Empty repo (created 2026-07-03) | repo_token_budget_liquid_mvph6w8r | complete (nothing to assess) | No commits | None |
| Liquid-Moondream-450M-Benchmark | Personal project | PRIVATE | Pinned, provenance-strict VLM benchmark (Modal) | repo_liquid_moondream_450m_benchmark_mvph6t59 | complete | GPU runs not repeated; scoring re-run offline | Low |
| home_security_benchmark | Personal project | PRIVATE | Synthetic-image benchmark (Gemini generation) | repo_home_security_benchmark_mvph6uw8 | complete | Steps 3–5 spec-only; generation not repeated | Low |
| marketplace_prototype | Personal project | PRIVATE | Next.js + Stripe Connect marketplace prototype; agent-built | repo_marketplace_prototype_mvph6vjy | complete (main); **withheld** (charter/strategy/research/dossier branches) | Stripe live paths not exercised | **High for withheld branches**, which reference another venture. High level only |
| prototype_Jules | Personal project | PRIVATE | Same PRD built by the Google Jules bot | repo_prototype_jules_mvph6vt5 | complete | 25 open PRs not individually run | Low |
| billboard | Personal project | PRIVATE | Geographic ranking pipeline + methodology comparison | repo_billboard_mvph6u38 | complete (methodology only) | Client context unnamed; two sessions unmerged | **Flag**: unnamed client context; political/religious targeting sensitivity |
| billboard-map | Personal project | PUBLIC | Redacted public map of billboard output | repo_billboard_map_mvph6u7i | complete | Rendered offline only | Medium. Public output of client-flagged work |
| ashby | Personal project (subject: Ashby) | PUBLIC | "Blind Briefing" browser game | repo_ashby_mvph6tz4 | complete | Tests not committed; regression run by investigator | Medium. Embedded commercial fonts/wordmark |
| pmm | Personal project (subject: ClearlyRated) | PRIVATE | Orchestrated KB + site research and conflicts workbook | repo_pmm_mvph6vpa | complete — **counted once with Clearly-Rated** | Session-path dependencies; not reproducible | Medium. Third-party copyrighted mirror |
| Clearly-Rated | Personal project (subject: ClearlyRated) | PRIVATE | Same work as pmm (19 shared commits) + unmerged product-tour branch | repo_clearly_rated_mvph6t0t | complete — **counted once with pmm** | As pmm | Medium. As pmm; tour embeds third-party screenshots |
| BTCsecrets | Personal project (content is a third-party company's legal/regulatory package) | PRIVATE | Staged agent document reconciliation | repo_btcsecrets_mvph6sv9 | **withheld** | Process only; no substantive capability claims | **High**. Third-party legal material |
| ai_game | Personal project | PUBLIC | Main: browser game "Edge Rush". Unmerged branch: large BlackRock research + reusable research kit | repo_ai_game_mvph6tqk | complete | Branch research accuracy sampled (796-claim fact check is self-reported) | **High**. Public repo contains personal interview material on the research branch |
| airops | Personal project (subject: AirOps) | PRIVATE | Multi-agent company-research run + prompt engineering + Codex refactor experiments | repo_airops_mvph6tvj | complete | 1.2 GB of captures not opened; run not repeated (needs network and paid models) | **High**. Personal job-search context in the prompt; one non-public fact about a named person (`06-checks/final-report.md` says to remove it) |
| research_prompt | Personal project | PUBLIC | Reusable research control plane (Codex-driven refactor) | repo_research_prompt_mvph6w4q | complete | No live run; network commands not executed | Medium. Public legacy prompt reveals personal job-search intent and names AirOps |
| genesis | Personal project (subject: Genesis Computing) | PRIVATE | Same tool as research_prompt + live run on a branch | repo_genesis_mvph6usm | complete | Live run not repeated; captures not opened | Medium. ~1,400 third-party public web files; SQLite binaries committed |

## Family and lineage rulings applied

- **pmm = Clearly-Rated.** They share 19 commits (`cf13473`…). pmm adds 3 workbook commits (`2718b66`, `2071a24`, `a907067`). Clearly-Rated adds 7 tour commits. Counted once.
- **Research-prompt lineage (verified by synthesis, byte-level).** `ai_game@6698994:pmm-research-kit/PROMPT.md` (351 lines, 2026-10-21 21:11Z) is byte-identical to `airops@c1ba3ba:00-inputs/PROMPT.md` (21:19Z). This evolves into the 3,399-line `airops` README (`fb6bc71`, then Jacob's edits `0398294`/`0d21793`). That README is byte-identical (same md5) on `airops` main, `airops@origin/codex/research-agent-refactor`, and `research_prompt@5fab799`. `genesis` contains the same 7 commits as `research_prompt` plus a run branch. One lineage, not three independent projects.
- **etta_app → etta_app_update**: one product, rebuilt.
- **Liquid_SDK_Test → TextAdventures → TextAdventures-Content**: one game-plus-LLM family.
- **marketplace_prototype / prototype_Jules**: the same PRD (md5 `42c2c377…`, identical in both repos) given to two different agents on 2026-07-07. Treated as a paired comparison.
- **billboard / billboard-map**: share Claude session `session_016iA4…`. The map is the publication arm.
- **chip / OEM**: the same evening (2026-06-28) and the same gated-pipeline pattern.

## Synthesis re-verification (performed on /tmp copies; read-only)

| Check | Result |
|---|---|
| Commit inventory across all refs of all 28 clones (dates, identities, trailers) | Done. Dates span 2026-03-10 to 2026-10-24 |
| `TextAdventures-Content@03afa34` playtest re-run | `scripts/playtest.py games/concierge/game.json` exits 1, "room-13 unreachable". The other two games pass |
| OEM `pytest` | 55 passed |
| Liquid-Moondream-450M-Benchmark `pytest` | 198 passed, 164 subtests |
| research_prompt `@1a4d35c` unittest | 45 OK |
| Prompt lineage (ai_game → airops → research_prompt → genesis) | Confirmed by byte comparison and md5 (see above) |
| marketplace_prototype vs prototype_Jules PRD | Identical md5 |
| Key commit messages: chip@75d4fa1, etta_app_update@be2d460, airops@8581d67, liquid-token-budget-slider@18bcd91, etta_app@d4b9bb2, liquid-ai-study-guide@1c4a924, r_app@e6ea0ad | Read. Contents match the per-repo reports |

**Correction to two reports.** The research_prompt and genesis reports say the 3,399-line prompt's earlier evolution "cannot be reconstructed". It can, from airops history plus ai_game. The lineage above is the reconstruction.
