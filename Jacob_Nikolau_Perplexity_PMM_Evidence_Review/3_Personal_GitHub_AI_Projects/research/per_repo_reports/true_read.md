MANIFEST | true_read | PUBLIC | small app (single-page static marketing/landing site for a personal consulting offer) | complete | Single-file site, 8 commits in one day; no PRs/issues; no AI-process artifacts; not rendered in a browser (no headless browser available), only static/structural checks

DISCLOSURE: No credentials, API keys or tokens found. Contains Jacob's own business contact (jacob@trueread.co, CNAME trueread.co) and a public Google Calendar appointment-schedule embed URL (`index.html`, booking iframe) — this is a public booking link by design, not a secret. The page text names prior employers (Mosaic, NovoEd, Mursion) only as self-described résumé-style credentials ("Designed, fielded, and wrote *The State of AI in A&E 2026*… at Mosaic", "30%+ inbound growth… at NovoEd", "AI pipeline on Gong and Claude"). These are marketing claims written by Jacob about his own experience; no employer data, code or customer data is present. The repo itself is clearly a personal venture (own brand/domain). Claims are unverified by this repo. Already public; suitable to share as-is (it is a live-site source).

## 1 Identity
- Personal repository `NYCandrun/true_read`, visibility PUBLIC, not a fork, not archived, default branch `main`, created 2026-06-22T06:22:51Z, last push 2026-06-22T23:43:44Z (repos.json).
- Type: static single-page website (one `index.html`, ~50 KB / 566 lines, plus `CNAME` = `trueread.co`) — almost certainly served via GitHub Pages given the CNAME file (inferred; Pages settings not inspected).
- Purpose: landing/sales page for "TrueRead", a B2B consulting offer selling original survey-based research as a demand-gen asset. Intended user: B2B marketing/sales leaders. Problem framed: AI answer engines and AI-written outreach erode SEO, paid search and cold email; primary research is positioned as "the one thing AI can't fake."
- Maturity: deployable, content-complete marketing site with pricing, process explanation, mailto CTAs and an embedded Google Calendar booking page. No backend, no build, no analytics, no forms.

## 2 Dates & attribution
- All 8 commits: 2026-06-22 06:25 UTC (`735fa4b`, "Add TrueRead site as index.html") → 2026-06-22 23:43 UTC (`b72a49c`). One-day project.
- Single author/committer for every commit: `Jacob Nikolau <jacobnikolau767@gmail.com>`. No bots, no Co-authored-by trailers, no other identities, no commit bodies.
- Activity: burst 06:25–07:50 UTC (6 commits: initial, big restructure, CNAME, layout/booking/wording fixes), pause ~15.5 h, then 23:31 and 23:43 (major copy rewrite + process-page trimming). No imported history or squash evidence beyond the first commit already containing a 390-line finished page (authored elsewhere, then committed).

## 3 Branch & history coverage
- Branches: `main` only (`origin/main`, `origin/HEAD -> origin/main`). No other branches, so no unmerged work.
- PRs: none. Issues: none (`gh pr list`/`gh issue list --state all` returned empty).
- All 8 commits inspected with `git show --stat` and diffs; all commit messages are generic ("Update TrueRead site") except the first and the CNAME commit, so intent must be inferred from diffs.
- Inaccessible: how the HTML was produced before the first commit; Pages/DNS configuration.

## 4 Actual functionality
Inspected the full final `index.html` and each historical version (text extracted with CSS/JS stripped). Static checks performed: all `data-goto` targets (`book`, `pricing`) exist as IDs; hash router logic read. Not rendered in a browser.
- Two "views" in one file (`#view-home`, `#view-process`) toggled by a small vanilla-JS hash router (`showView`, `route`), with `data-goto` buttons that switch to the process view and smooth-scroll to `#book`/`#pricing`; IntersectionObserver reveal animations honoring `prefers-reduced-motion`; accessible hamburger menu (`aria-expanded`, `aria-controls`, label toggling); safe-area insets for notched phones.
- Content: problem (three channels breaking), thesis, "one report, three jobs", week-one deliverables, credentials, inputs (outside-in study, buyer survey, optional sandboxed first-party CRM/call data "under a clear data agreement"), cadence (marquee + cross-cuts), four pricing tiers (Trial $10K once; Research only $15K/report; Growth $15K/report + $3K/mo; Done-for-you $15K/report + $6K/mo; panel costs passed through), engine/LinkedIn/paid sections, payoff, booking iframe.
- Statistics are attributed in text (G2/Forrester 2026, Semrush/SparkToro 2025, Semrush 2025, Forrester) but not linked to sources.

## 5 How Jacob uses or builds with AI
- No direct evidence of AI-assisted authorship in this repo: no agent instruction files, prompts, trailers, bot authors or agent branches. Per brief, none is inferred from style or speed.
- AI appears as the site's subject matter (positioning research against AI-generated content and AI answer engines; GEO/AEO) and in a self-described credential ("Built an AI pipeline on Gong and Claude that mines every sales call…").

## 6 Quality assessment (purpose: small business landing page)
Strengths (moderate–high confidence):
- Communicates a single, coherent thesis; copy sharpened over iterations toward plain language and a problem-first narrative.
- Commercially concrete: explicit prices, scope boundaries ("We are not your general paid or social agency"), risk reversal (money-back on the 30-day date), panel costs at cost — evidence of offer design thinking, not just page design.
- Clean, dependency-free implementation; reasonable accessibility and mobile handling; robust routing for two views in one file.
Weaknesses (high confidence, observed):
- Voice inconsistency: `6435016` deliberately changed "if I miss the date"/"I find and manage" to "we", but `b1495ce` reintroduced "I" (final has "money-back if I miss the date" x3 and "I'm not a press agent") while the rest says "we". A reversal, likely unintentional.
- Leftover/unused CSS (`.proofrow`, `.trust`, `.step`, `.num` no longer used); four `<style>` blocks, including small appended patch blocks (e.g. `.gp2` override with `!important`) added in `b1495ce` — patch-style editing rather than consolidation.
- Booking iframe height hard-coded (1500/1180/980 px breakpoints in `55554b8`) — pragmatic fix for Google's embed, fragile.
- Third-party statistics cited without links; employer-attributed results are unverifiable from the repo.
- Generic commit messages make the history hard to read.
These are typical, acceptable shortcuts for a one-day personal landing page.

## 7 Developmental milestones
1. `735fa4b` (06:25) single long page, title "Research the field hasn't published", pricing included "$3K / quarter" options and list fees.
2. `98d945e` (07:06) +311/−155: split into Home and "Our process" views with hash routing; new home hero "Own the data your category doesn't have yet"; Google Calendar booking iframe added; meta title reframed "Original B2B research, built for demand gen".
3. `57d5988` (07:18) CNAME → trueread.co (custom-domain launch).
4. `acb4e6f`, `55554b8` (07:38–07:46) padding fix; booking iframe height fix.
5. `6435016` (07:50) "I" → "we" voice change.
6. `b1495ce` (23:31) +132/−77: home rewritten problem-first ("The channels you use to reach buyers are breaking"); stats moved to sourced strip; "fast start" moved to home; pricing restructured to monthly retainers ($3K/mo, $6K/mo), $15K "unit" logic, Growth/Done-for-you scope details; credential stat "30%+ inbound growth" removed from hero.
7. `b72a49c` (23:43) −48: removed duplicated problem/thesis sections from the process page; process hero changed to "How one report becomes a year-round motion" with "You've seen why…" bridging copy; "Two jobs" → "Three jobs".

## 8 Changes in working method & possible lessons
- Single long page → two-view structure (06:25 → 07:06). Trigger undocumented. Inferred lesson: separate the short persuasive pitch from detailed process/pricing. Evidence: strongly inferred from diff. Alternative: aesthetic preference.
- Credential-led hero → problem-led hero (07:06 → 23:31). Earlier hero leaned on "Built by the founding marketer…" and a "30%+" stat; later leads with buyer pain and third-party stats. Inferred lesson: lead with the customer's problem, put credentials later. Evidence: strongly inferred. Alternative: outside feedback (not documented).
- De-duplication (23:31 → 23:43): problem/thesis existed on both views; removed from process page and replaced with a bridge sentence. Inferred lesson: avoid repeating the argument across views. Evidence: strongly inferred.
- Pricing: quarterly add-ons/list fees → per-report unit plus monthly retainers with minimum report counts (06:25 → 23:31). Inferred: business-model clarification toward recurring revenue. Evidence: explicit in diff; motive speculative.
- Voice "I" → "we" → partially "I" (07:50 → 23:31). Speculative: the later rewrite was produced from a source that predated the voice change (e.g. edits done outside the repo and pasted in), consistent with each commit replacing large blocks. Evidence: speculative.
- No prompts, plans or AI instructions exist, so AI working method cannot be reconstructed from this repo.

## 9 Demonstrated capabilities, limitations, uncertainties
- Demonstrated: shipping a polished, deployable single-file site with custom domain in one day; offer/pricing design and positioning copy; iterative copy refinement visible in diffs; basic accessible front-end JS.
- Uncertainties: whether the site is live (not checked); who/what authored the HTML before commit; reasons behind changes (no messages/PRs).

## 10 Evidence references & verification limits
- `true_read@b72a49c:index.html` (final; router script at end of file; pricing `#pricing`; booking `#book`), `true_read@57d5988:CNAME`.
- Diffs: `true_read@98d945e` (views + iframe), `@55554b8` (iframe height), `@6435016` (I→we), `@b1495ce` (home rewrite, pricing restructure, extra `<style>` blocks), `@b72a49c` (process page de-dup).
- Metadata: `/home/user/workspace/research/repos.json` entry `true_read`.
- Limits: no browser render; GitHub Pages settings and live site not inspected; no PRs/issues exist; external claims (stats, employer outcomes) not verified.
