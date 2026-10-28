MANIFEST | liquid-ai-study-guide | PRIVATE | research workflow → single-file HTML field guide (content synthesis + small static app) | complete (git) / partial (PR metadata) | `gh` unauthenticated in sandbox, so PR bodies/reviews/issues not fetched (PR titles/numbers recovered from merge commits only); upstream research inputs (`REPLACEMENT_LANGUAGE.md`, `_WORLD_BRIEF`, fact-check reports, "unit citation source files", 14 source briefs) referenced but not in repo; not rendered in a browser (no headless browser available)

DISCLOSURE: No credentials, tokens, or personal data found (searched for key/token/password/secret patterns; only hits are prose). Content is an analysis of a named third-party company (Liquid AI) and its competitors, built from public sources: 249 citation entries link to liquid.ai, arXiv, Hugging Face, Bloomberg, TechCrunch, vendor blogs, etc. The earliest PRD (`@789d729:README.md`) framed the material as compressing "a 90-day Liquid AI onboarding", listed "internal briefs" as source material and said a flat HTML file "survives leaving the company"; commit `b7050eb` rewrote the README source line from "internal briefs and external coverage" to "AI-generated research reports and external coverage". I found no material in the current file that looks internal or proprietary. All verified claims point to public URLs. The wording does leave **ownership/disclosure context ambiguous**, though, so the lead should confirm what the "briefs" were before sharing. The file contains candid "vulnerabilities" and competitive-critique sections about a real company, and many figures are dated June 2026 and will go stale. Suitability to share: **plausibly shareable after review**, provided the source-brief question is resolved and the reader understands it as a point-in-time personal study artifact.

---

## 1. Identity
- Personal repository on the NYCandrun account. Visibility is PRIVATE. Description (repos.json): "Long-form HTML field guide for ramping into Liquid AI in ~2 weeks: 8 Units, ~92-term Lexicon, six recurring lenses, six reading paths."
- **Type:** a research-synthesis artifact delivered as a self-contained static web document: one `index.html`, about 309 KB, 1,823 lines, with inline CSS/JS. The only other file is `README.md`.
- **Purpose / intended user:** self-study to become a "credible interlocutor" on the company in about two weeks. The PRD personas are new technical hire, GTM hire, investor prep, partner engineer, and comms. It covers technology (LFM2, STAR, liquid-NN lineage), market, company, competition (five "rings", ten deployment environments), vulnerabilities, narrative/comms, and six skeptical "lenses".
- **Maturity:** finished and polished for its purpose. It went through 15 merged PRs in about 7 hours, all doing fact-checking, calibration, citations, and tone work. It is a point-in-time artifact (June 2026) with no refresh mechanism.
- **Related:** the README links `NYCandrun/liquid-ai-prep-course` as an "independent rendering of the same source synthesis" (gated lesson app). I mention it by name only and did not inspect it.

## 2. Dates & attribution
- First commit: `ab5386c` on 2026-06-11 03:13 UTC. Latest: `f1697c9` on 2026-06-11 10:03 UTC (06:03 −0400). Every commit falls inside **one ~7-hour session**. The 2026-06-10 dates in the log are just the −0400 local timestamps of the same night.
- Authors: "Jacob Nikolau" and "NYCandrun" both use the same email. Jacob Nikolau has 9 commits (`ab5386c`→`7612da4`, the first content and the fact_check waves). NYCandrun has 25, including the 15 GitHub web merges (committer "GitHub") and the later citation/tone commits. There are no bot authors and no Co-authored-by or "Generated with" trailers.
- No inherited history, fork, or squash. The initial commit already contains a 1,455-line `index.html`, so the guide was built elsewhere and imported. Its creation process **cannot be reconstructed** from this repo.

## 3. Branch & history coverage
- Default branch `main`. There are 15 remote feature branches: readme_update, mobile_ux_update, readme_correction, fact_check, fact_check_2…5, fact_check_5b, citation_audit, research_gap_fill, link_fix_pass2, tone_fix, tone_fix_lens1.
- **Every branch is 0 commits ahead of main** (`git rev-list --count main..origin/X`). Each branch maps to exactly one merged PR (#1–#15). I found no unmerged or abandoned work.
- Exception: `b7050eb` (the citation layer, +667/−364 lines) was committed directly to main with no PR, between PR #10 and #11.
- There is one reversal: `53f1a57` (mobile fix pushed straight to main) was reverted by `55c154e` ("will reapply via PR") and re-landed as `e0039b0` / PR #2. That reads as a deliberate return to the PR-per-change discipline.
- PR/issue metadata through `gh` was unavailable (unauthenticated). PR titles come from the merge-commit messages.

## 4. Actual functionality / research workflow
**Inspected:** the full commit log with bodies and stats, the README at `ab5386c`, `789d729` and HEAD, the structure of `index.html`, and representative diffs (`ba9abbb`, the `b7050eb` README change).

**Executed (offline, with node; script at /tmp/chk_lsg.js):**
- The single inline `<script>` parses without errors.
- `GLOSSARY` has 92 entries, which matches the README's "~92".
- `CITATIONS` has 249 entries and there are 252 `data-c` markers (242 unique). Every marker resolves to an entry. Seven entries are never used, and one entry has no URL. These counts match the commit message of `9dc48ed` ("252 markers, 249 entries").
- All 53 inline `data-t` term references resolve to glossary keys.
- All five non-linear `PATHS` (product 10, competitor 10, environment 8, mental 9, vulnerability 8) point to section IDs that exist.
- No fetch/XHR/beacon calls and no external script or CSS, which supports the README's "no network, no telemetry" claim.

**Not verified:** visual rendering, mobile layout, localStorage notes/export, keyboard shortcuts, and whether the cited URLs are live or support their claims. Spot-checking claims against sources was out of scope and offline.

**Citation entries are structured** as `{t, v, n, s:[[label,url]]}`. The verification labels break down as:

| Label | Count |
|---|---|
| Verified | 162 |
| Partially verified | 41 |
| Verified · vendor-reported | 26 |
| Vendor claim | 11 |
| Unverified | 5 |
| Editorial framing / arithmetic / estimate | 4 |

Inline prose also carries 7 "(unverified)", 17 "vendor claim" and 3 "Liquid-reported" tags.

**The workflow visible in history** (the inputs live outside the repo):
1. Imported guide.
2. Fact-check waves 1–4, applying corrections from external reports (`REPLACEMENT_LANGUAGE.md`, "fact-check report §2.3").
3. Readability rewrite.
4. Calibration sweeps 5 and 5b.
5. Citation layer.
6. Dual citation audit.
7. Gap-fill via web research.
8. Conservative link-fix pass.
9. Tone passes.

## 5. How Jacob works with AI
**Direct evidence (explicitly documented):**
- `1c4a924` says the work was "executed by 22 parallel Opus 4.8 agents each owning one isolated chunk". It states a mandate and reader floor ("technical generalist (PM, founder, GTM lead)"), and lists about 17 "Wave-4 fact decisions preserved verbatim" as locked constraints. Post-checks: "178 lines modified in place; total line count unchanged at 1505. HTML structure validated; <span class="t"> wrapper count unchanged."
- `7612da4`: "Five Opus 4.8 sweep agents each read the full file + _WORLD_BRIEF + sweep brief, then applied minimal surgical edits within isolated line ranges. No grep, no audits, judgment-led." It notes one edit "resolves internal contradiction flagged by C2", i.e. an agent-raised issue that was resolved at the parent level.
- `b3ca947` mentions chunk labels C1–C5, edits "evidence-grounded against _WORLD_BRIEF and prior audits", and a verification line ("HTML parses 0 errors… 38 span.t wrappers preserved, all locked facts untouched").
- The README (HEAD) says the source material is "AI-generated research reports".

**Mode:** using AI to do research and editorial work, then directing and verifying it. It is not an AI-powered product.

**Practices demonstrated:**
- Partitioning a large document among parallel agents with isolated line ranges.
- A shared context brief (`_WORLD_BRIEF`).
- Explicit locked-fact lists so later waves don't undo earlier corrections.
- Mechanical invariants (line count, wrapper counts, parse) as cheap regression checks.
- A policy-level instruction ("understate over overstate").
- Deliberately switching between a grep/audit-driven pass and a "judgment-led, full-doc context" pass.

Whether Jacob personally reviewed each diff can't be confirmed, because PR review data is inaccessible. The detailed, line-numbered commit bodies may themselves be agent-written; there is no direct evidence either way.

## 6. Quality assessment
**Strengths (high confidence):**
- **Provenance and claim calibration.** The work goes past a bibliography: claim-level markers carry graded verification labels, and vendor claims are kept distinct from verified ones.
- **Iterative, auditable correction**, with concrete corrections stated in commit bodies, for example:
  - IFEval reversal (LFM2-2.6B trails Qwen3-4B), in `68652f6`
  - employee count ~80–90 rather than ~121
  - Cartesia funding corrected from "$27M" to "~$191M", in `541a19a`
  - Insilico "1,000+ benchmarks" corrected to "200+ tasks", in `b3ca947` and harmonized in `7612da4`
  - Mercedes reframed from "shipping" to "production targeted H2 2026"
- **Correctly identified recurring overstatement patterns**: "proven in production", "only", "first", "no competitor ships".
- **Static integrity holds**: no dangling citations, terms, or path IDs.
- A sensible zero-dependency architecture for a personal reading tool.

**Weaknesses and limits:**
- **Incomplete cleanup.** Missed instances needed follow-up passes (`c691a80` catches "the missed line 571 instance"; Insilico was fixed in the body before the glossary). The pattern is visible in the history and handled, but it shows that chunked edits can leave inconsistencies.
- **One inconsistency is known and deliberately kept.** "SG-internal Gartner 2028 (body) vs 2030 (glossary) NOT harmonized" (`1c4a924`). `ba9abbb` later removed the "outside the US" qualifier, but I did not verify whether the 2028/2030 split remains.
- **The research inputs are not in the repo**, so whether the reports were sound, and how they were checked, is not reproducible here.
- **README drift.** The first PRD (`789d729`) described a different artifact (14 modules / 97 lessons, password gate, a differently named file). PR #3 fixed it about 20 minutes later. Medium-confidence reading: the PRD was a generated or copied description from the sibling app.
- **Staleness.** Explicitly a June 2026 snapshot. The PRD's open question about refresh cadence is never answered.
- **AI-heavy authorship.** By its own description, the prose comes from AI-generated research and AI rewrite waves. The original contribution visible here is orchestration, fact-check policy, and editorial judgment, not first-hand domain analysis.

## 7. Developmental milestones (all 2026-06-11, UTC)
| Time | Commit | Milestone |
|---|---|---|
| 03:13 | `ab5386c` | Import of the guide |
| 03:33 | `789d729` | PRD |
| 03:42–03:45 | `53f1a57`, `55c154e`, `e0039b0` | Mobile UX, with revert and re-land via PR |
| 03:50 | `a819ef6` | README corrected to match the artifact |
| 04:50–05:45 | `68652f6`, `c691a80`, `541a19a`, `e522156` | Fact-check waves 1–4 |
| 06:23 | `1c4a924` | 22-agent readability rewrite |
| 06:44 / 06:54 | `b3ca947` / `7612da4` | Calibration and overstatement sweeps |
| 08:15 | `b7050eb` | Hoverable citation layer (227 claims, 234 entries); README source line reframed |
| 08:41 / 08:54 | `8911cad` / `9dc48ed` | Dual audit, then web-research gap fill (249 entries) |
| 09:42 | `ba9abbb` | Conservative fix of 52 flagged citations |
| 09:53 / 10:03 | `dfde5b8` / `12c57a0` | Tone passes |

## 8. Changes in working method & possible lessons
1. **Direct-to-main → PR-per-change.** Earlier (03:42) the mobile fix went straight to main; at 03:45 it was reverted and re-landed via PR, and every later change used a branch and PR except `b7050eb`. Trigger: none documented. Lesson: keep each change isolated and reviewable. Evidence: explicitly documented (revert message). Alternative explanation: the user just wanted a tidy PR history for display.
2. **Applying an external corrections list → graded hedging.** Waves 1–2 (04:50–05:05) applied "40 corrections from REPLACEMENT_LANGUAGE.md". Waves 3–4 (05:35–05:45) added "(unverified)" prefixes and "vendor claim" tags, and "verified unhedges". Lesson: binary correct/incorrect isn't enough, so uncertainty is now labeled. Evidence: strongly inferred from the commit bodies.
3. **Fact work → readability, with fact locks.** At 06:23 the 22-agent rewrite came with an explicit preservation list. Possible trigger: risk that rewrites reintroduce errors. Evidence: explicitly documented (the locked list). Alternative explanation: standard caution, not prompted by an observed regression.
4. **Grep/audit-driven → judgment-led sweep.** Wave 5 (06:44) was "evidence-grounded against… prior audits". Wave 5b (06:54) was "No grep, no audits, judgment-led, full-doc context", and agents read the whole file. Possible trigger: chunk-isolated edits missing cross-document contradictions; 5b fixed a contradiction flagged by C2 and harmonized glossary with body. Evidence: strongly inferred. Alternative explanation: the two passes were planned as complementary from the start.
5. **Inline hedges → structured citation layer with audits.** After 08:15, claims were backed by per-claim sources and verification labels. Then came a "dual audit", web-research gap fill, and a "conservative" pass that removed unsourced claims instead of keeping them. Lesson: provenance as a first-class feature, and trimming preferred over unsupported assertion. Evidence: explicitly documented. Note: the README's reframing from "internal briefs" to "AI-generated research reports" happened in the same commit; the reason isn't documented.
6. **Accuracy → voice.** The final passes (09:53, 10:03) recast "auditor-voice" copy as "strategist pressure-testing" while preserving facts and markers. Trigger: not documented (possibly reader feedback, or a self-read after the critique-heavy waves). Evidence: speculative as to trigger.

## 9. Demonstrated capabilities, limitations, uncertainties
- **Demonstrated in this personal repository:**
  - orchestrating many parallel LLM agents over a partitioned document, with shared briefs and locked constraints
  - multi-wave fact-checking with explicit calibration policy
  - claim-level provenance with graded verification
  - lightweight regression invariants
  - PR-per-change hygiene
  - a usable zero-dependency static reading tool (glossary drawer, reading paths, local notes/export, responsive degradation)
- **Uncertainties:**
  - how far Jacob personally reviewed agent edits
  - what the "internal briefs" / "AI-generated research reports" were
  - whether the cited sources actually support their claims (not spot-checked)
  - rendering and behavior in a browser (not run)

## 10. Evidence references & verification limits
- Commit-pinned references:
  - `liquid-ai-study-guide@789d729:README.md` (PRD, "internal briefs", onboarding framing)
  - `@a819ef6:README.md` (corrected README)
  - `@b7050eb:README.md` (source line reframed; citation layer)
  - `@1c4a924` (22 Opus 4.8 agents, locked facts)
  - `@b3ca947` and `@7612da4` (sweep agents, `_WORLD_BRIEF`)
  - `@68652f6` (REPLACEMENT_LANGUAGE.md corrections)
  - `@541a19a` and `@e522156` (hedging tags)
  - `@8911cad`, `@9dc48ed`, `@ba9abbb` (citation audits)
  - `@dfde5b8` and `@12c57a0` (tone)
  - `@53f1a57` / `@55c154e` / `@e0039b0` (revert and re-land)
- HEAD `f1697c9:index.html` (`GLOSSARY` near line 1148, `CITATIONS` near line 1325, `PATHS` near line 1759, store key `liquid-edge-curriculum-v2`).
- PRs #1–#15 (titles from merge commits); one-to-one with the branches listed in §3.
- **Limits:**
  - `gh` was unauthenticated, so no PR bodies, reviews, or issues.
  - Only the static checks listed in §4 were run, with no browser rendering.
  - External URLs were not fetched.
  - Upstream research files were not in the repo.
