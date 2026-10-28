MANIFEST | ai_game | PUBLIC | mixed: small browser game (main) + agent-run company research workflow (unmerged branch `blackrock-aladdin-research`) | complete | Game history is web uploads with no messages/PR bodies, so the iteration process cannot be reconstructed. Research branch: one Claude Code session; checked through docs, logs, and samples of files, not by re-running it. Large PDFs were not opened. The cherry-picked source commit 63e54d2 is not accessible.

DISCLOSURE: No credentials found (pattern scan of `origin/blackrock-aladdin-research`, excluding PDFs). The repo is **PUBLIC** (repos.json). The research branch holds: (a) third-party material copied in bulk: 54 Swagger specs taken from public AladdinSDK packages, about 130 machine transcripts of BlackRock/partner videos and podcasts, product-page text, and a copy of BlackRock's web brand guide (`07-design-references/`). (b) YouTube audio that an agent fetched through third-party Invidious proxies after YouTube blocked it (`08-review-rounds/2026-10-19_0601_media-crawl-and-audio-fetch/1_youtube_audio_via_invidious_report.md`). (c) Personal job-search material: Jacob's own "Briefing and Interview Guide" (Oct 8 original), a "post-interview follow-up" leave-behind addressed to a named company's GTM head, and review personas such as "hiring manager" and "recruiter". (d) Named public speakers. A timeline note says a "client engineer" was removed as an identifiable person. Nothing here looks like employer-internal data. All sources are described as public, and BlackRock is the *subject* of outside-in research, not the owner. The game (main) says it is "inspired by Liquid AI" and borrows that company's look ("Liquid gradient" CSS). It is a fan/explainer piece, not company work. **Sharing:** main (the game) looks fine to share. The research branch needs review before anyone points to it: it is already public, it contains interview material, and it holds copyright/terms-of-service-sensitive transcripts and proxied media.

---

## 1. Identity
- **Owner/context:** personal repo of NYCandrun. Created 2026-06-09. Default branch `main`. Not a fork. Pushed 2026-10-21.
- **Type:** mixed. Two unrelated projects share the repo:
  1. **"Edge Rush"** (`main`): a single-file HTML/CSS/JS teaching game, "You are the AI chip." The player sends incoming requests to FAST (on-device), ATTENTION, NANO (specialist) or CLOUD blocks while keeping battery, RAM/KV-cache and accuracy in check. There are six lessons that each add one concept: device vs cloud, KV-cache growth, power budget, losing signal in a tunnel, specialists, and a final "design your chip" hybrid-build level (`ai_game@7216070:README.md`, `index.html`, 875 lines). The audience is non-experts ("No experience needed"). Maturity: small, finished, playable.
  2. **Aladdin Studio research pack** (`origin/blackrock-aladdin-research`, 121 commits ahead of main, never merged): outside-in research on BlackRock Aladdin/Aladdin Studio, built from public sources by Claude Code agents. Outputs: research briefings, an API catalog, an interactive HTML field guide (v1 to v3), a transcript corpus, fact-check reports, a compendium, and a 19-page "GTM leave-behind" plus a 3-page brief. It also ships a reusable `pmm-research-kit/PROMPT.md` (351 lines). Maturity: heavily iterated deliverable plus a generalized prompt.

## 2. Dates & attributable contributions
- **First commit:** 2026-06-09 11:52 -0400 (`6bd5752` Initial commit). **Latest:** 2026-10-21 22:16 UTC (`0598c4c`, research branch).
- **Main:** 16 commits, all on 2026-06-09 between 11:52 and 15:23. Author: NYCandrun <jacobnikolau767@gmail.com>. Committer: GitHub (web "Add files via upload").
- **Research branch:** 120 commits authored by `Claude <noreply@anthropic.com>`, between 2026-10-19 03:27 and 2026-10-21 22:16 UTC. Trailers: `Co-Authored-By: Claude Fable 5.1` (68) and `Claude Opus 5.5` (52). All 120 carry the same `Claude-Session: https://claude.ai/code/session_018CJaDFDWHFPiBoZoUKeuXo`. One commit (`34ad215`, 2026-10-19) is authored by NYCandrun and committed by Claude: "Remove game overview and instructions from README", cherry-picked from `63e54d2`. That source commit is not present in any fetched ref, so it is inaccessible history.
- **Authors seen:** NYCandrun (17 authored), Claude (120), GitHub web committer. No other humans. No bot accounts besides Claude.
- **Activity:** one afternoon on the game (Jun 9). Then a 4-month gap. Then about 3 days of agent-run research (Oct 19 to 21). The research is a change of direction that reuses the repo, not an evolution of the game.

## 3. Branch & history coverage
Remote branches: `main` (default), `reskin`, `root`, `ui_bugfix_1`, `improved-instructions`, `usability_bugfix_1`, `mobile_compatibility`, `ui_bugfix_2`, `blackrock-aladdin-research`.
- All game branches are fully merged: `git log main..origin/X` is empty for each. They map to PRs #1 to #6 (pre-fetched `prs/ai_game.prs.json`). Every PR is titled "Add files via upload", has an empty body, and was merged within about 10 s by NYCandrun:
  - #1 `reskin` 16:38Z: `62d0be6`, +354/−267
  - #2 `ui_bugfix_1` 17:47Z: +67/−39
  - #3 `improved-instructions` 17:49Z: +15/−2
  - #4 `usability_bugfix_1` 18:03Z: +73/−17
  - #5 `mobile_compatibility` 19:02Z: +35/−3
  - #6 `ui_bugfix_2` 19:23Z: +124/−23
  - `root` holds the pre-PR commits `37e6b47` (459-line first index.html) and `d30c4c9` (+305/−105).
- No issues (`ai_game.issues.json` empty).
- **Unmerged:** `blackrock-aladdin-research`, branched from `7216070`. `git diff --stat main...origin/blackrock-aladdin-research`: 1,188 files, +254,849/−57. It also empties README.md (1 byte).
- Branch names are descriptive feature/bugfix labels. None are agent-named (no codex/* or jules/*).

## 4. Actual functionality / research workflow
**Game (inspected and run).** I loaded `index.html` in headless Chromium (Playwright) at 1280×800 and 390×844, clicked Start → Begin lesson, and pressed keys 1/4 about 40 times. There were no page or console errors, and Lesson 1 reached "LESSON 01 · COMPLETE". Screenshots and the script are in `reports/ai_game_artifacts/`.

Implementation:
- Stage table (`STAGES`) with per-stage flags.
- Request generator with LONG/COMPLEX/SPEC tags; `route()` scoring; `tick()` loop with RAM/battery meters.
- Tunnel/no-signal stage, rotating specialist, architecture choice (`ARCHS`), end-of-run routing summary.
- Progress saved in localStorage, with a difficulty multiplier based on play count.
- Help overlay that pauses the game; keyboard plus buttons; a screen-reader live region (`srSay`).

Only Google Fonts is external. Later levels were checked by code reading only, not played to the end.

**Research branch (inspected, not re-run; it needs network, proxies and transcription).** The pipeline is documented in `blackrock-aladdin/00-timeline.md` and folder READMEs:
1. Pull 11 public `asdk_plugin_*` packages → 54 specs, `api_digest.txt`, `apis.json`.
2. Write briefings.
3. Build field guide v1, run a four-reviewer "expert panel" with before/after screenshots, then build v2.
4. Collect the BlackRock media CDN, podcast feeds and site pages; transcribe about 95 items (`04-transcripts/tools/transcribe*.py`, `vtt2txt.py`).
5. Fact-check the guide against the transcripts → v3 with 31 corrections.
6. Fact-check Jacob's own Oct 8 Briefing and "What It Does V7" (originals in `05-fact-check/originals/`) → revised Briefing and V8.
7. Compendium written by three agent "writers", then reviewed by nine reviewers, one per requested recording.
8. GTM leave-behind iterated to v24, then a 3-page brief.

Verification artifacts include:
- A 796-claim fact check with a 274-claim web re-check (`review-rounds/fact-check/`, `results.tsv`, `compile.py`).
- A link check, a citation-placement check (227 superscripts), an adversarial audit, and meaning checks before and after each rewrite pass.
- A 72-entry source register graded P/S/T with minute:second timestamps.
- Edit passes stored as replayable scripts that "assert each replaced string occurs exactly once" (`review-rounds/README.md`).

## 5. How Jacob works with AI
- **Game:** the repo has no direct evidence that AI was used. There are no trailers, prompt files or agent branches. Even though the subject is AI, the AI concepts are taught content, not features (it is not an AI-powered product). Iteration was through named branches and PRs (reskin → UI fixes → instructions → usability → mobile).
- **Research branch:** clear, directly evidenced delegation to Claude Code. Agents gathered, transcribed, wrote, reviewed and fact-checked, with many parallel "panel"/"reviewer" sub-agents (e.g. the `<!-- agent a64df60f9de0e8f3f -->` header in the media report).
- **Jacob's role as director/editor, explicitly documented:**
  - "the author's 63 highlighted passages removed", extracted from an annotated PDF (`author-cuts/highlighted_passages.txt`, `apply_cuts.py`), then a second round of 20 cuts
  - "Part 3 rebuilt with the author's copy" (`fa4556b`); "author copy for summary, Part 3 and Exhibit 15" (`8eae466`)
  - "records author decisions on extra-detail items" (`db2a9a3`); "redraw updated with author decisions" (`619bcb8`)
  - a reverted change, "restore the previous v24 review version" (`648333e`)
  - many "(not applied)" / "(preview only)" / "(read-only)" check commits that ran ahead of an applied commit, which indicates a propose → human-decide → apply loop.
- He also turned the work into a reusable specification (`pmm-research-kit/PROMPT.md`): phases, evidence grades P/S/T/I, receipt rules, inference labelling, re-derivable counts, file naming and writing rules.

## 6. Subjective quality assessment
- **Game: works and gets its idea across** (high confidence for Lesson 1 and the code structure, medium for later levels).
  - Strengths: one new concept per level, meters and buttons that appear only once introduced, explanations shown the first time a tag appears (`chipSeen`), pause-on-help, accessibility hooks, and a mobile layout.
  - Weaknesses: no tests, no commit messages, one large file, and a fixed hint that the balanced build wins (a teaching simplification).
- **Research: well-designed for provenance and verification** (medium-high confidence, from the artifacts).
  - Strengths: primary-source-first approach (API specs, proxy statements, tender records); timestamped receipts; graded source register; repeated fact checks that caught real conceptual errors (e.g. "Arcesium announced an AI platform, not agents" `c21825c`; "credit the SDK to GitHub and PyPI, not the speakers" `2287973`; a Databricks claim dropped for lack of support `2c27e8d`); explicit limits section.
  - Weaknesses:
    - The review process is very heavy (dozens of sequential passes on one document); its returns appear to diminish.
    - Agent "expert panels" are simulated readers, not external validation.
    - Machine transcripts are only spot-checked.
    - Media was obtained by working around YouTube blocks.
    - The work sits in a game repo, is public, and was never merged.
    - Branch-level docs are complete, but the top-level README is emptied.
  - Reproducibility is partial: the scripts exist, but they depend on network, proxies and transcription tooling that I did not run.

## 7. Developmental milestones
- 2026-06-09 11:53: game v1 (`37e6b47`).
- 12:26: rework (`d30c4c9`).
- 12:31: README with lesson design (`1d94c98`).
- 12:38: reskin to Liquid-style design tokens (PR #1).
- 13:47 to 15:23: UI, instructions, usability, mobile and UI fixes (PRs #2 to #6).
- 2026-10-19 03:27: research begins (`e0fd95d`).
- 04:07: field guide v1. 13:48: v3 after fact check.
- 19:54: leave-behind v1 (`7b39dff`).
- 2026-10-20 07:27: 796-claim fact check (`ac8fe26`).
- 10-21 20:55: v24 with new thesis (`ddf9eea`).
- 21:11 to 21:17: research prompt generalized into a kit (`6698994`, `fa41e5d`, `fb0038c`).
- 21:50 to 22:16: 3-page brief (`1f06d5a` to `0598c4c`).

## 8. Changes in working method & possible lessons
1. **Manual uploads → agent-driven commits.**
   - Earlier (Jun 9): whole-file browser uploads through PR branches, with no messages.
   - Later (Oct 19 to 21): one Claude Code session with descriptive, timestamped commits and a timeline doc.
   - Trigger: undocumented. Lesson: not stated. Evidence: explicitly visible. The reason is speculative.
   - Alternative explanation: a different project type and different tooling access.
2. **Draft-then-check → evidence-first.**
   - Earlier (Oct 19): briefings and field guide written first, then fact-checked against transcripts (31 corrections), plus Jacob's own Oct 8 drafts corrected.
   - Later (Oct 21 `PROMPT.md`): "The facts come first. Sense-making only uses facts that are in the facts store", with a receipt rule for every fact.
   - Trigger documented in the kit README: "errors that survived longest were conceptual, not factual" (wrong arrows, shortened quotes, wrong speaker).
   - Evidence: explicitly documented.
3. **Trusting agent summaries → reading full reports.** Kit README: "Agents' hand-back summaries miss things. Reading the full reports found fixes the summaries left out." Explicitly documented.
4. **Working around blocks → hand-open lists and "Stay public".**
   - Earlier (Oct 19 06:01): an agent used Invidious proxies to get blocked YouTube audio.
   - Later prompt: "No logins, no paywall workarounds... back off when a site rate-limits you" and "Plan for a short list of pages to open by hand."
   - Evidence: strongly inferred. Proxies are not named as the trigger.
   - Alternative explanation: generic good-practice wording.
5. **Maximal review → proportionate review.** Kit README: leave out the adversarial audit, expert panel and extra-information cut for onboarding, "worth running only when a document goes to someone outside the company." Explicitly documented, and consistent with the large review effort on the leave-behind.
6. **Additive drafting → subtractive editing.** On Oct 20 the author's highlighted cuts (63, then 20) removed sections, including the original Part 3. That part was later rebuilt as one position plus a diagram. This shows a shift toward a shorter, thesis-led document (cover "the proof is the headline" `c7e752e`; 19 pages → 3-page brief). Strongly inferred.

## 9. Demonstrated capabilities, limitations, uncertainties
- **Demonstrated:**
  - turning technical AI concepts (KV-cache growth, edge vs cloud, specialist models, hybrid architectures) into a playable lesson sequence
  - fast iterative shipping of a static web game across branches and PRs
  - directing a long multi-agent research session with explicit provenance rules
  - human editorial control recorded in the repo (cuts, author copy, decisions, a revert)
  - turning lessons learned into a reusable research specification.
- **Uncertainties:**
  - Whether Jacob wrote the game code himself or generated it with AI cannot be told from the evidence.
  - How much of each "author copy" passage Jacob wrote word for word is unclear. It is labelled as author copy, but it was committed by Claude.
  - The Oct 8 originals came from before this repo, so their process is not visible.

## 10. Evidence references & verification limits
- `ai_game@7216070:index.html`, `:README.md`; `@37e6b47`, `@d30c4c9`, `@62d0be6` (reskin), `@9bd32ad` (mobile CSS), `@fda39ee`/`@5e119c7` (first-action prompt, chip explainers); PRs #1 to #6.
- `origin/blackrock-aladdin-research` files:
  - `blackrock-aladdin/00-timeline.md`
  - `11-gtm-leave-behind/README.md`, `review-rounds/README.md`, `review-rounds/author-cuts/*`, `review-rounds/panel-goal-fit/*`, `review-rounds/fact-check/*`
  - `05-fact-check/originals/*`
  - `08-review-rounds/2026-10-19_0601_media-crawl-and-audio-fetch/1_youtube_audio_via_invidious_report.md`
  - `pmm-research-kit/PROMPT.md`, `README.md`
- Research-branch commits: `e0fd95d`, `34ad215`, `5188799`, `4f0c8cd`, `fa4556b`, `648333e`, `ac8fe26`, `ddf9eea`, `6698994`, `0598c4c`.
- **Executed:** git history and branch analysis; Playwright smoke test of the game (Lesson 1, desktop and mobile; artifacts in `reports/ai_game_artifacts/`); credential pattern scan.
- **Not executed:** research tools (they need network/proxies); later game levels; PDF contents (not opened).
- **Inaccessible:** cherry-pick source `63e54d2`; the Claude session transcript (only its URL is in trailers).
