MANIFEST | liquid-ai-prep-course | PRIVATE | research-synthesis content rendered as a single-file static study app (mixed: research workflow + small app) | complete | Single-day history (2026-06-11 UTC); the 14 source research reports, FACT_CHECK_REPORT.md, and REPLACEMENT_LANGUAGE.md are referenced but not in the repo; no browser available, so only static and Node-based checks were run (no visual render)

DISCLOSURE: No API keys or tokens found. A trivial hardcoded gate password was in `liquid-ai-prep-course@0639b93:index.html` (also stated in PR #1's body). The gate was removed in 2095ce7 but is still in history. It is not a real credential. The subject is a real company (Liquid AI), and the content is framed as outside-in interview prep built from public sources (~378 citation entries; top domains liquid.ai, arxiv.org, huggingface.co, venturebeat.com). One wording point to note: the initial README (f13376d) said "compresses a 90-day Liquid AI onboarding" and "Built from 14 source briefs / internal briefs". Commit 603753d changed this to "14 AI-generated research reports" and added "nothing in this course reflects insider or internal knowledge". I found no employer-internal data, proprietary code, or customer data in the content I inspected; every sampled claim cites a public URL. The current README still says "~90 days of Liquid AI onboarding", which could be misread. It also names individual people (founders, researchers) only as public figures. Suitable to share after review, with a README refresh (see §6).

## 1 Identity
- Personal repository of NYCandrun. Visibility PRIVATE. Created 2026-06-11T02:47Z, last pushed 2026-06-11T11:15Z (repos.json).
- Purpose: a self-study curriculum for building informed, outside-in understanding of Liquid AI and the on-device/edge AI category. The repo's own framing, added in lesson 1.0 at e3ffa20 and later moved to 0.1: "an interview-prep guide for someone preparing to talk credibly about Liquid AI… you are a candidate learning to understand Liquid as a vendor."
- Type: a research synthesis (14 AI-generated reports, not bundled) turned into a single-file HTML lesson app (`index.html`, ~319 KB). README.md is the only other file.
- Maturity: finished and heavily revised in one day. The content is the main artifact; the app shell is a vehicle for it.
- Related repo, by name only: `liquid-ai-study-guide` is described as an independent rendering of the same synthesis.

## 2 Dates and attributable contributions
- First commit: f13376d, 2026-06-11 02:47:31 UTC. Latest: ec4f3e8, 2026-06-11 11:15:05 UTC. All work falls in about 8.5 hours.
- Authors: "Jacob Nikolau <jacobnikolau767@gmail.com>" (12 commits) and "NYCandrun <same email>" (8 commits plus 5 merge commits). The committer on merges is GitHub <noreply@github.com>. No bot authors, no Co-authored-by trailers, no "Generated with" trailers.
- Activity periods:
  - 02:47–05:46: initial commit plus 5 PR branches
  - 07:29–10:24: direct-to-main sourcing and UX passes, authored as NYCandrun
  - 10:41–11:15: factual fixes and editorial tightening, authored as Jacob Nikolau
- The repo has no fork parent. The initial commit already contains the full 1,938-line app, so pre-repo development (the app and the research reports) cannot be reconstructed.

## 3 Branch and history coverage
- Default branch is `main`. Remote branches: `mobile_compatibility` (0639b93), `readme_correction` (c91e691), `fact_check` (1ef7b5d), `fact_check_3` (f7948b7), `fact_check_4` (fddf1e3).
- `git log main..origin/X` is empty for every branch, so all are fully merged and no work remains unmerged.
- PRs #1–#5 were all opened by NYCandrun and merged within minutes of creation. None has comments or reviews. There are no issues.
- After PR #5, 14 commits went directly to main.
- There is no `fact_check_2` branch. "fact_check_3" may follow a pass that happened outside the repo (speculative).

## 4 Actual functionality
**What I inspected:** the full commit and PR history and bodies. I evaluated the data blocks of `index.html` in Node with `/tmp/lq_eval.js` and `/tmp/lq2.js`.

**What I verified at HEAD:**
- 14 modules and 97 lessons (Module 0 "How to use this textbook" through Module 13 "Interrogation prompts and gaps").
- 95 glossary entries, 6 mental models, and 6 reading paths (linear, product, competitor, environment, mental, vulnerability).
- All drill-chip and path references resolve to existing lessons. All `data-key` term references resolve to glossary keys; the only unmatched value is a template literal.
- Both inline scripts parse.
- `CITATIONS` has 378 entries, referenced by 356 markers (301 unique). Each entry splits sources into independent (`s`) and vendor (`v`):
  - 107 independent-only
  - 142 vendor-only
  - 129 mixed
  - source dates run from 2002 to 2026-06-10
- `GLOSS_CITES` holds the glossary citations. Tooltips show the source name, date, and URL.

**Other UX:** a search box, keyboard navigation, mark-as-read, progress via localStorage (`liquidai-curriculum-v1`), and a mobile drawer layout (PR #1).

**Changes over time:**
- The personal-notes UI is turned off with `SHOW_PERSONAL_NOTES = false`. The code comment says it was hidden "per course owner request", with the code kept.
- Since 1be4616, each module renders as one scrolling page.
- The password and captcha gate (PR #1) was removed in 2095ce7.
- The `g` shortcut was removed in 2628898.

**Not done:** I did not visually render the page or test interaction, because no headless browser was available.

## 5 How Jacob uses or builds with AI
Direct evidence in the repo:
- **AI-generated research as the source base.** This is explicitly disclosed (README; lesson 0.1 at 603753d; glossary "anchor sentence" entry).
- **AI used for fact-checking, under his direction:**
  - PR #3 body: "Audited end-to-end with Opus 4.8 — all 7 edits verified in correct context."
  - PR #4: "corrections from the 10-chunk re-audit".
  - PR #5: "Triaged all ◐ soft items across chunks 1-5 via context-aware Opus subagents; applied REWRITE / VENDOR_CLAIM / CONTRADICTED fixes only. CONFIRMED and IMMATERIAL items left untouched."
  - These PR bodies show a decomposed audit: chunking, a verdict taxonomy, and selective application of fixes.
- **Directing the AI rather than accepting its output.** Commit messages read as task specifications with scope limits, for example ec77a86: "57 phrase-level edits; facts, citations, and anchor sentence preserved". The "per course owner request" code comment implies an agent was implementing the owner's decisions (strongly inferred).

Not directly evidenced: which tool wrote the HTML and the individual commits. There are no trailers or agent files, so per the brief I do not attribute authorship of the code to AI.

## 6 Quality assessment
**Strengths**

- **Provenance discipline (high confidence).** Every external claim gets a citation (baf4083). Vendor-published and independent sources are distinguished visually (54e2e80). Interpretive constructs are explicitly labeled as products of the AI-generated research (603753d, 41577ce). In a document built from AI research, this is the most valuable design choice: the reader can tell what is sourced, what comes from the vendor, and what is interpretation.
- **Real corrections, not cosmetic ones (high confidence).** Examples:
  - The 19-neuron demo is re-attributed to the NCP paper (Lechner et al. 2020) rather than LTC (76c54e8).
  - The Belcak attribution is corrected to NVIDIA (f7948b7).
  - "Proven in production" is calibrated: literally true only for Shopify (fddf1e3, 76c54e8).
  - LFM2.5-8B-A1B KV-cache claims are narrowed (76c54e8).
  - 2095ce7 says it cuts or softens 33 unverifiable claims and fixes 27 audit-flagged discrepancies.
- **Purposeful editorial iteration (medium-high confidence).** The voice moves from insider to "outside-analyst" (ec77a86), and lesson 0.1 is trimmed repeatedly (97cad27, 79c379b, 66f94d7, ec4f3e8).
- **Data model integrity is good.** No broken internal references.

**Weaknesses and defects**

- **README is stale (defect, high confidence).** It still documents the password gate, the `g` shortcut, the notes textarea, and "~155KB". All of these were removed or changed (2095ce7, 2628898, 1be4616); the file is now ~319 KB. PR #2 had existed specifically to make the README accurate, which highlights the later drift.
- **Statistic churn on one stats tile.** At PR #3, the SLM forecast was replaced with the $2.3B valuation. At PR #4, Lesson 4.5's tile became "$7B→$57B Agentic AI (~42% CAGR)". At 76c54e8, the ~42% CAGR was dropped. This looks like successive audits disagreeing, which is caught but not documented as a decision (medium confidence).
- **Heavy reliance on vendor sources.** 142 of 378 citation entries are vendor-only. The markers make this visible, but the claim base leans heavily on what the company says about itself.
- **No verification record in the repo.** The fact-check reports and the AI research reports are not committed, so the audit cannot be reproduced from the repo. The verdict counts in commit messages (33/27/7) cannot be independently checked.
- **No review on PRs.** All five were self-merged within about a minute. This fits a solo project.
- **Time-sensitive content.** "As of June 2026" claims will age, and nothing marks staleness.

## 7 Developmental milestones
1. f13376d: full curriculum app imported in one commit.
2. PR #1 (0639b93): mobile layout plus a client-side gate.
3. PR #2: README brought in line with the app.
4. PRs #3–#5: three AI-assisted fact-check waves.
5. 603753d / 41577ce: provenance reframing ("internal briefs" changed to "AI-generated research reports").
6. baf4083 / 54e2e80: a citation system covering all claims, with vendor/independent markers.
7. 2095ce7: conservative pass plus gate removal.
8. 1be4616 / 79c3109: switch to whole-module scrolling layout.
9. 76c54e8 → ec4f3e8: final factual fixes, an anchor-sentence rewrite, tone pass, and trimming of the intro lesson.

## 8 Changes in working method and possible lessons
- **Fact handling: from batch corrections to triaged audit.**
  - Earlier (PR #3, ~05:00): apply 7 fixed replacements from a report.
  - Later (PR #4/#5, 05:36–05:46): chunked re-audit with hard/soft verdicts, an "(unverified)" prefix, and selective application.
  - Later still (baf4083, 08:57): per-claim citations.
  - Possible trigger: the first pass covered too little (inferred from the follow-up waves).
  - Lesson: verification needs structure and claim-level provenance.
  - Evidence: explicitly documented in PR bodies.
- **Uncertainty markers: from inline labels to sourcing or removal.**
  - At f7948b7, items were marked "(unverified)".
  - At 54e2e80, the unverified markers were removed, and at 2095ce7 unverifiable claims were cut or softened.
  - Inferred lesson: hedged-but-present claims were replaced with either sourcing or removal.
  - Evidence: strongly inferred.
  - Alternative explanation: purely visual decluttering.
- **Provenance framing: from "internal briefs" to "AI-generated research".**
  - Earlier: "internal briefs" (f13376d README).
  - Later: "AI-generated research reports… not insider knowledge" (603753d).
  - Inferred lesson: honest attribution, and avoiding implied insider access.
  - Evidence: explicitly documented.
  - Alternative explanation: "briefs" may only ever have meant the AI reports.
- **Access control: gate added, then removed.**
  - Added in PR #1 at 02:57; removed in 2095ce7 at 09:52.
  - The README itself had called it "friction, not security".
  - No trigger is documented (speculative: unnecessary friction for a private repo).
- **Voice: from insider to outside-in candidate.**
  - The change runs through e3ffa20, f8a7f3b, and ec77a86 ("swaggering/insider register" changed to "measured outside-analyst").
  - Evidence: explicitly documented.
- **Personal-notes UI: hidden but kept in code** (1be4616). This is documented in a code comment.

## 9 Demonstrated capabilities, limitations, uncertainties
**Demonstrated:**
- Turning a large AI-generated research corpus into a structured, cross-linked curriculum.
- Specifying scoped AI edit and audit tasks.
- Multi-wave, AI-assisted fact verification with a verdict taxonomy.
- A claim-level provenance system that separates vendor from independent sources.
- Self-correction of overclaiming and insider-sounding framing.
- Use of branch/PR hygiene early on, later dropped for direct commits.

**Uncertainties:**
- Who or what wrote the HTML and the commit text.
- The content of the uncommitted research and fact-check reports.
- Whether the fact-checkers' corrections are themselves right. I did not re-verify individual claims online, per the brief's evidence rules.

## 10 Evidence references and verification limits
- **Files:**
  - `liquid-ai-prep-course@ec4f3e8:index.html`: `GLOSSARY` (L383), `MENTAL_MODELS` (L489), `MODULES` (L502), `PATHS` (L1449), `SHOW_PERSONAL_NOTES` (L1486), `CITATIONS` (L1876), `GLOSS_CITES` (L2256)
  - `@ec4f3e8:README.md`
  - `@f13376d:README.md` (original "internal briefs"/"onboarding" wording)
  - `@0639b93:index.html` (gate)
- **PRs:** #1–#5 (bodies quoted in §5 and §8).
- **Key commits:** 603753d, 41577ce, baf4083, 54e2e80, 2095ce7, 1be4616, 76c54e8, e3ffa20, ec77a86.
- **Limits:**
  - No visual or browser rendering.
  - The research reports, FACT_CHECK_REPORT.md, and REPLACEMENT_LANGUAGE.md are not in the repo.
  - Claim accuracy was not independently re-verified.
  - Work before the first commit cannot be reconstructed.
