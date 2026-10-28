MANIFEST | ashby | public | small app / interactive persuasion mini-game (single-file HTML) + brand-reference page | complete | No PRs/issues readable (gh unauthenticated); human prompts/Claude session transcript not in repo; tests and screenshots cited in commits are not committed; GitHub Pages deployment not checked live

DISCLOSURE: No credentials found (pattern search over README.md, index.html, decoded-stripped brand guide). No employer material: the repo is about Ashby (a third-party recruiting-software vendor) and says so plainly. `index.html` footer reads "An independent experiment. Not affiliated with Ashby." (added in 87d47e9). Third-party IP concern: `ashby-brand-guide.html` embeds Ashby's wordmark SVG and base64 copies of the commercial fonts TT Norms Pro and Signifier (Klim). The page says it was "assembled from ashbyhq.com production CSS tokens, embedded site fonts, and full-page captures of thirty pages" and calls itself "Unofficial; for internal reference". Even so, it sits in a PUBLIC repo. `index.html` also embeds a subset of TT Norms Pro and the wordmark. Redistributing those fonts and the trademark publicly may raise licensing or trademark questions. The game also makes competitive claims ("capabilities Ashby sells against Greenhouse and Lever"). All people and company data are fictional ("Meridian"). Suitability: the game itself looks fine to share after review. Review the embedded font binaries and the brand guide's public status before pointing anyone to the repo.

# ashby: Investigation report

## 1. Identity
- **Context:** a personal repository under the NYCandrun account, PUBLIC (`repos.json`: created 2026-09-15T05:16:22Z, not a fork, no description). It is not employer work. Its subject is a third-party vendor (Ashby), and the work is explicitly unaffiliated.
- **Type:** a small interactive web app, "Blind Briefing". It is a 3–5 minute browser mini-game that argues through play: "AI in recruiting is only as good as the data underneath it" (README PRD). There is also a separate brand-reference HTML page.
- **Intended user:** a recruiting or talent leader. The player acts as Head of Talent at the fictional company "Meridian". The PRD says the file "can be sent as an attachment or hosted anywhere", so it is meant as a shareable persuasion or demo piece.
- **Maturity:** a finished, polished v1 built in a single day. It is deployed through GitHub Pages (`.nojekyll`, `index.html` at the root). There is no ongoing development.

## 2. Dates and attributable contributions
- **First commit:** 7143a0a, "Initial commit", 2026-09-15 01:16 EDT (05:16 UTC). Author NYCandrun <jacobnikolau767@gmail.com>, committer GitHub (web UI). README is a 1-line placeholder.
- **Latest commit:** f8d33bf, 2026-09-15 10:18 UTC.
- **Authors and committers:** NYCandrun (1 commit, the initial one only). "Claude <noreply@anthropic.com>" is author and committer of the other 15 commits. Every Claude commit carries `Co-Authored-By: Claude Opus 5` and the same `Claude-Session: https://claude.ai/code/session_0128whJsPf7GaAX2vXTTEQcY`. No other bots or identities appear.
- **Jacob's attributable contribution:** directly, only the repo creation (2026-09-15 05:16 UTC). Everything else was produced in one Claude Code (web) session over about 5 hours (05:50–10:18 UTC). Jacob's direction inside that session is not recorded in the repo.
- **Activity:** a single burst on one day with no pauses. Phases: setup (05:50–06:16), then content redesign (07:27–08:11), then fact and copy polish (09:03–09:22), then bug and QA fixes (10:07–10:18).

## 3. Branch and history coverage
- **Default branch:** `main`. Remote branches: `origin/main` and `origin/claude/push-merge-main-mxz8bh`. Both point at f8d33bf, so there is no diff and no unmerged work. History is linear (0 merge commits).
- **Imported history:** the brand guide arrived whole in 77265eb (511 lines). The PRD arrived whole in 65f4e0e (129 lines). Both were authored before or outside the commit sequence, so how they were made cannot be reconstructed.
- **PRs/issues:** not accessible (`gh` unauthenticated). The branch name suggests a Claude Code push branch fast-forwarded to main.
- **Files added then removed:** 324253e committed 6 Playwright screenshots (`shot-*.png`); 38e8bd2 removed them ("picked up by a broad git add"). e95a3f7 added `.github/workflows/pages.yml`; f8d33bf removed it.

## 4. Actual functionality (inspected and executed)
**Inspected:** README (the PRD), all of `index.html` with base64 blobs stripped, the text of `ashby-brand-guide.html`, every commit message, and the diffs for 6af0445, f8d33bf and the round content at 75f442e.

**Implemented** in `index.html`, about 62KB in a single file:
- Three screens: intro, rounds and reveal.
- 7 rounds of pre-written answer pairs ("unified" vs "fragmented"), stored in one commented `ROUNDS` constant. There are no live LLM calls.
- Card order is randomised from a seed stored with the save, so it stays the same after a reload.
- Voting is two steps: select a card, then press Lock in. Pressing Lock in with nothing selected shows "Pick an answer first."
- Progress saves to `localStorage` under `blindBriefing.v4`, with a silent in-memory fallback. A save with a different schema version is discarded, and the v1–v3 keys are dropped.
- The reveal shows the tally in three bands, a "turn" panel, lists of the two stacks, and the closing line "Same AI. Same confidence. One of them fails silently."
- An expandable round-by-round debrief shows both labelled answers, the player's pick, a "blindspot" consequence narrative and the mapped capability.
- Accessibility: answer cards use `aria-pressed`, there is an `aria-live` announcer, focus moves to the content, transitions are disabled under reduced motion, and dark mode is supported.

**Executed:** I served a copy offline (python http.server) and drove it with headless Chromium through an iframe harness. The repo was not modified. Results for HEAD f8d33bf:
- Intro shows "Start".
- An empty lock-in shows the hint.
- A double-tap on Lock in records 1 vote.
- A full playthrough reaches `completed:true`, `lastResult {unifiedPicks:4, of:7}`, `playCount:1`.
- The reveal says "You split your votes."; the debrief has 7 items; focus lands on `tally-headline`.
- The file makes 0 external http(s) src/href references.

**Regression check:** the same harness on e0f7090 (before the fix) recorded **2 votes from a double-tap and 8 votes total**. That reproduces the bug described in f8d33bf and confirms the fix.

**Not verified:** iOS/Safari behaviour, WCAG contrast, layout across 320–1440px, the live Pages site, and playtest success criteria. Those are claimed in commits or the PRD only.

**PRD drift:** the README PRD was never updated after the redesign. It still says rounds 1–2 are unscored and the tally runs out of 5, gives the old reveal copy and closing line, lists the old round order, and specifies a "system font stack". The code now scores all 7 rounds, uses new bands and copy, reorders the rounds and uses the embedded brand font.

## 5. How Jacob works with AI
- **Mode:** using an AI coding agent (Claude Code, web) to build a non-AI artifact *about* AI. The product does not call any AI.
- **Direct evidence:** the Co-Authored-By trailers, the Claude-Session URL, the claude/* branch, and Claude as author of 15 of 16 commits.
- **Inferred, not proven:** the sequence shows a spec-first workflow. A full PRD (65f4e0e) and a brand reference (77265eb) were committed before any code, then implemented "to the PRD". The later commits are substantive redirections of the design, not bug fixes. Rewriting all rounds, "rebuild the reveal around silent failure", and "break the surface correlations" look like human critique of the first build. The commit messages, however, are written in the agent's voice, and the prompts are absent. So I cannot separate Jacob's judgment from the agent's own.
- **Verification evidence (agent-reported):** 75f442e lists a Chromium test matrix. 324253e says "full suite passes". f8d33bf says the bug was "Found by QC in a headless browser". e0f7090 says "a test now asserts the two match". **No test files are committed**, so the suite cannot be reproduced from the repo. My own run confirmed the double-tap fix independently.
- **Fact discipline:** 6af0445 narrows two capability claims to "what is actually native" (for example, budget reconciliation "generally rides on an integration"). This is deliberate correction of overclaiming, but the source behind the correction isn't documented. Confidence: medium.

## 6. Subjective quality assessment
**Strengths** (confidence high, based on code reading and execution):
- It is a clear, purpose-fit single-file artifact with no dependencies and no external requests.
- Careful state handling: seeded order, schema-versioned saves, legacy-key cleanup, and a storage fallback.
- Defensive guards with explanatory comments.
- Good accessibility intent.

**The strongest design decision** is cbcb985. The first build let surface cues give away the answer: in the v1 content, the fragmented answers were vague ("usually at the onsite... most companies") and the unified ones were specific. That made the blind test easy to game. The rewrite makes both sides cite sources and splits contrarian stance and action-bias across both assistants. The game's thesis then shifts to "silent failure" (84289de) instead of "you picked right".

**Weaknesses:**
- The PRD is stale relative to the code, so the documentation is misleading.
- Tests are referenced but not committed.
- The persuasive content is fully scripted, so the "blind" result shows what the game argues, not anything measured.
- Public redistribution of commercial fonts and the wordmark (see DISCLOSURE).
- The workflow file was added and then removed because of a deploy race. That was a small misstep, fixed quickly and documented.

Overall, for its purpose: a well-executed demo piece. Confidence: medium-high.

## 7. Developmental milestones
- 77265eb: brand guide imported.
- 65f4e0e: PRD.
- 75f442e: full v1 implementation, about 54KB, saved as `blindBriefing.v1`.
- 324253e / e95a3f7: Pages deployment.
- 2b562c2: all 7 rounds rewritten, reordered and scored.
- 84289de: reveal rebuilt (v2).
- cbcb985: surface-correlation removal (v3).
- 6af0445 / ea462f4 / 87d47e9: claim accuracy, copy consistency, unaffiliated disclaimer.
- e0f7090: round reorder (v4).
- f8d33bf: double-tap fix, focus management, workflow removed.

## 8. Changes in working method and possible lessons
1. **Scoring design.**
   - Earlier (75f442e, 06:06 UTC on 09-15): rounds 1–2 were unscored "both answers equally good" calibration rounds, tallied out of 5.
   - Later (2b562c2, 07:27 UTC): every round turns on a data gap and is scored out of 7.
   - Trigger: not stated beyond the content rewrite.
   - Possible lesson: every round must carry the argument.
   - Evidence: explicitly documented change, speculative motive.
2. **What "fragmented" looks like.**
   - Earlier: generic, unsourced answers.
   - Later (cbcb985): equally specific and sourced answers, with stance decorrelated.
   - Trigger, as documented: "nothing visible on the card predicts which assistant could see the data".
   - Possible lesson: a blind test must not leak through style. This also changed the thesis to "you can't tell, and at work you'd never find out".
   - Evidence: explicitly documented change, strongly inferred lesson.
   - Alternative explanation: the agent self-critiqued without human prompting. That cannot be ruled out.
3. **Save versioning as a principle.**
   - Each content change bumped the schema version, and the reason ties back to the thesis ("resuming into reordered content is exactly the failure this game is about", 84289de).
   - Evidence: explicitly documented.
4. **Claim accuracy pass** (6af0445).
   - Overstated vendor capabilities were narrowed.
   - Evidence: documented change; the research source is not documented.
5. **Deployment.**
   - An Actions workflow was added (e95a3f7), then removed (f8d33bf) after it raced the branch build: "due to in progress deployment".
   - Lesson: one deploy path only.
   - Evidence: explicitly documented.

How the PRD and brand guide were created, and the human prompts throughout, cannot be reconstructed.

## 9. Demonstrated capabilities, limitations, uncertainties
- **Demonstrated:**
  - Writing or directing a detailed product spec before building.
  - Directing an AI agent through iterative design critique on a persuasion artifact.
  - Insisting on content accuracy and on not overclaiming.
  - Shipping a small, robust, accessible static web app with deployment, within one session.
- **Uncertainties:**
  - How much of the redesign was Jacob's judgment versus the agent's. The prompts are absent.
  - Who made the brand guide, and how.
  - The licensing status of the embedded fonts.

## 10. Evidence references and verification limits
- **Commit-pinned references:**
  - `ashby@7143a0a:README.md`
  - `ashby@77265eb:ashby-brand-guide.html` (provenance lines in the hero meta and footer)
  - `ashby@65f4e0e:README.md` (PRD)
  - `ashby@75f442e:blind-briefing.html` (v1 rounds; scored:false rounds 1–2; vague fragmented answers)
  - `ashby@e95a3f7:.github/workflows/pages.yml`
  - `ashby@f8d33bf:index.html` (`lockIn` guard, `ROUNDS`, `KEY = "blindBriefing.v4"`, disclaimer)
- **Diffs and messages:** the 6af0445 diff (capability lines), and the messages of 2b562c2, 84289de, cbcb985, e0f7090 and f8d33bf.
- **Branches:** `origin/main` and `origin/claude/push-merge-main-mxz8bh`, both at f8d33bf.
- **Limits:**
  - No PR or issue data (gh not authenticated).
  - The Claude session URL was not opened (it is outside the repo).
  - Base64 font and logo blobs were not decoded or inspected.
  - The live Pages URL was not visited.
  - My execution covered logic and flow only. Visual, contrast and cross-browser claims are unverified.
  - Test harness and outputs are in /tmp/ashbytest (outside the repo).
