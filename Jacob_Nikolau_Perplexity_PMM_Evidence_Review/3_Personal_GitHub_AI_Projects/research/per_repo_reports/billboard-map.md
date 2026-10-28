# billboard-map — repository report

MANIFEST | billboard-map | PUBLIC | small app / data-visualization demo (single-file interactive map, AI-generated via Claude Code) | complete (git history); partial (PRs/issues not checked — `gh` unauthenticated in sandbox) | Scoring pipeline/methodology not in this repo (only precomputed composite scores); no prompts/session transcript in repo; PR/issue list unavailable

DISCLOSURE: No credentials found (pattern search for key/token/secret/password in `index.html` returned no hits). No personal data: payload has ZCTA code, place name, state, county, ACS population and composite score/rank per ZIP area. The footer says "Composite market scores are proprietary", and commit `d0bead1` calls the file a "public/redacted variant". Component inputs are not exposed, though the first version (`488ac87`) also had a county table with two extra numeric scores per county. Sensitive content: the score uses **political-lean data**. Commits mention "precinct-level politics" and "bottom-half progressive politics damping", and there is a "Deep red" toggle. This is public (Pages-published) and could be read as political targeting, so the owner should weigh that before pointing anyone to it. Nothing here looks like employer material. All commit messages carry a `Claude-Session:` URL to a claude.ai session. That link is harmless but reveals the tool workflow. Suitable to share after the owner reviews the politics framing; otherwise low risk.

## 1 Identity
- Personal repo of NYCandrun, **PUBLIC**, not a fork. Created 2026-07-19T18:40:29Z, last push 2026-07-19T20:56:27Z (`repos.json`). A private sibling repo named `billboard` was created about an hour earlier (17:32Z). Given the "public/redacted variant" wording, this repo looks like the published output of that one (relationship noted by name only; not inspected).
- Type: a single-page interactive data visualization (a "Billboard Market Map"). It is effectively a static deliverable plus a deploy setup, not a reusable tool.
- Purpose: show a composite "market score" for every US ZIP Code Tabulation Area (ZCTA), apparently to rank places for billboard advertising. It highlights the top-2000 areas and lets the viewer switch between scoring variants (income adjustment, population-density adjustment, "Deep red"). Intended user: whoever chooses billboard markets (inferred from the title and "priority markets" copy in `488ac87`).
- Maturity: working, deployed-style artifact built in one sitting of about 2h16m. README is just `# billboard-map`. No tests, no build, no source data pipeline.

## 2 Dates and attribution
- First commit: `5007c4f` "Initial commit" 2026-07-19 18:40:29Z. Author NYCandrun <jacobnikolau767@gmail.com>, committer GitHub (made in the GitHub web UI; adds a 15-byte README).
- Latest: `f7cbbc3` (main) and `1ec22f0` (gh-pages), 2026-07-19 20:56Z.
- Identities: **NYCandrun** (1 commit, the initial one only). **Claude <noreply@anthropic.com>** wrote all other 24 commits as author and committer, each with the trailers `Co-Authored-By: Claude Fable 5 <noreply@anthropic.com>` and `Claude-Session: https://claude.ai/code/session_016iA4pD6jkVpBSZ13KaVM7q`. That is one Claude Code session for the whole project. No other humans or bots.
- Jacob's attributable contributions: repo creation and the initial commit (18:40Z). All code and data changes were committed by Claude Code. Jacob's direction can only be inferred from the sequence of requested changes (see §5).
- Activity: one continuous burst, 18:40–20:56Z on 2026-07-19. No later activity.

## 3 Branch and history coverage
- Branches: `main` (default, 13 commits) and `origin/gh-pages` (12 commits, an **orphan** branch whose root `488ac87` has no parent). There are no other branches.
- Relationship: each gh-pages commit has a matching main "Update map copy: …" commit made 2–4 s later, with an **identical `index.html` blob**. I checked all 12 pairs, e.g. `0a49613`/`01aa465` → blob `f8c2b37`, and `f7cbbc3`/`1ec22f0` → `4745569`. The tree difference between the branches is just `.nojekyll` (gh-pages) and `README.md` (main). Nothing is left unmerged, since every gh-pages state is mirrored on main.
- Deployment reversal: `d0bead1` added `.github/workflows/pages.yml` (configure-pages with `enablement: true`, upload and deploy). `6d7cbee` (18:46Z) removed it with the stated reason: "Pages auto-enables from the gh-pages branch, which needs no admin token; the Actions enablement path is not available to workflow tokens."
- PRs/issues: not checked, because `gh pr list` / `gh issue list` failed (CLI not authenticated in this sandbox). Commit history shows direct pushes with no merge commits, so PRs are unlikely.
- History is complete for both refs. `index.html` is about 8.7 MB (inlined d3 v7.9.0, topojson-client v3.1.0, and a base64 gzip JSON payload).

## 4 Actual functionality
Inspected: the full HTML/JS with the payload removed, the decoded payload at all 12 versions, and code diffs between consecutive versions. **Executed:** `node --check` on the app script (OK). I also rendered it offline in headless Chromium, and it loads and draws the full US ZCTA choropleth with top-2000 markers (screenshot: `reports/billboard-map_render_default.png`). I did not exercise the interactions (hover, toggles) programmatically. My reading of them comes from code only.
- Data: `z` has 32,408 ZCTA records × 28 fields. Fields: score, national rank, population, city, state, county, top-2000 flag, then (score, rank, top flag) triples for 8 variants: {income adj on/off} × {pop-density adj on/off} × {normal / Deep red}. Every variant flags exactly 2000 top ZCTAs (checked). `tz` holds ZCTA 2020 TopoJSON (33,609 geometries), `tc` holds us-atlas counties/states/nation.
- Rendering: Canvas 2D with d3.geoAlbersUsa. Precomputed Path2D objects and bounding boxes give viewport culling. Hover hit-testing uses bbox prefilter then `isPointInPath`, and is throttled with rAF. ZCTA outlines appear only above k>6. Top-2000 markers are dots when zoomed out and outlines at t.k≥5. There are contrast modes (gamma 1.0/2.2/3.6) and dark-mode CSS variables. A comment-documented fix rewinds ring orientation, because spherical d3.geoPath fills the complement of rings wound the wrong way.
- Controls: Income adjustment, Population density adjustment, Deep red, Top-2000 outline, County lines, and Top 5% / Top 1% (a Turbo-ramp rank spectrum above the cutoff).
- Not present: how scores are computed, the data sources for income or politics, and any validation. All scoring logic happens outside this repo. The page only displays precomputed variants.

## 5 How Jacob works with AI
- Direct evidence: AI built the whole thing (Claude Code, a single session, every commit authored by Claude). Jacob created the repo in the GitHub UI. Claude then pushed the deliverable, set up hosting, and iterated.
- Delegation pattern, inferred from commit order: Jacob seems to have reviewed the live map and asked for changes in quick succession. Changes covered granularity (county dots → ZCTA polygons), new scoring variants, how political data feeds the score, naming and default polarity of toggles, and new filter modes. The scoring changes ("Update scores: …") changed the data itself (see §8), so the agent was also re-running a scoring model kept elsewhere. That points to orchestration across repos/sessions, which cannot be verified here.
- Verification and correction signals: `28cd5ca` "fix income-toggle default state". At `5155059` the Income button's HTML had `aria-pressed="false"` while the code set `INC=true` (I confirmed this in the diff), so the UI state contradicted the model. It was fixed 3 minutes later, which suggests someone used the page and noticed. The agent itself diagnosed the Pages/Actions permission problem and reversed course (`6d7cbee` message).
- No AI features in the product; this is "using AI to build". No prompts, AGENTS.md or specs are in the repo.

## 6 Quality assessment
- Works as a communication artifact (high confidence: rendered locally). The rendering choices are sound for 33k polygons in one file: canvas plus culling, bbox hit-test prefilter, level-of-detail outlines vs dots, precomputed variants instead of client-side scoring (which also keeps component inputs private), and a single self-contained file that is easy to host.
- Weaknesses: an 8.7 MB single HTML file whose data payload can't be diffed, so each tweak rewrites the whole blob (the repo is ~95 MB on disk across 12 versions). Variant lookup uses magic column indexes (`NORM`/`DEEP` maps). The scheme was renumbered three times (`300c733`, `da67b9e`, `5155059`), and the default-state bug came from exactly this. There is no README or methodology note, so the viewer can't tell what "politics damping" or "Deep red" mean. The ring-rewind loop mutates geometry on every load (cheap but unnecessary). Hover over 33k paths is linear per event, though mitigated.
- Intentional shortcuts: no build step, no tests, inlined libraries. These suit a one-afternoon shareable map.
- Unfinished: README, methodology and provenance for the score.

## 7 Developmental milestones (all 2026-07-19, UTC)
1. 18:40 repo created (Jacob). 18:44–18:46 v1 published: county choropleth plus ZCTA dots (`488ac87`); Actions workflow added, then removed.
2. 19:11 `01aa465` changed to a ZCTA-level polygon choropleth (`tz` ZCTA topology replaces point lat/lon; county table dropped; "34 micro-ZCTAs fall below map resolution" note added).
3. 19:26 `300c733` Economic adjustment toggle plus Top 5% mode.
4. 19:39–19:51 politics inputs revised twice (`1b350a1` bottom-quartile damping, `d49f4e3` precinct-level).
5. 19:59–20:13 population toggle added, renamed, polarity flipped, Top 1% added, toggle-state bug fixed.
6. 20:35–20:38 politics damping widened to bottom half, then a deeper floor. 20:56 Deep red variant set.

## 8 Changes in working method and possible lessons
Only commit messages and data diffs exist. No prompts or plans are available, so the reasoning behind changes can't be reconstructed beyond what follows.
- **Deployment:** Actions workflow (18:44, `d0bead1`) → orphan gh-pages branch (18:46, `6d7cbee`). Trigger documented: workflow tokens can't enable Pages. Lesson: use the deploy path that needs no extra permission. Strength: **explicitly documented**.
- **Spatial unit:** county fill plus ZCTA dots (`488ac87`) → ZCTA polygons (`01aa465`, 25 min later). Likely trigger: dots/county averages were too coarse to choose specific markets. Strength: **strongly inferred** from the subtitle change ("Every ZIP-code area… hover any area"). Alternative: a planned staged rollout.
- **Political inputs in the score:** bottom-quartile damping (19:39; 6,239 ZCTA scores changed; top-2000 overlap with previous 1,585) → precinct-level politics (19:51; 31,756 scores changed; overlap 1,497) → bottom-half damping (20:35; 13,574 changed; overlap 1,682) → deeper floor (20:38; overlap 1,797). I computed these from the decoded payloads. Pattern: repeated tuning of how strongly the most progressive areas are penalized, with each change visibly reordering the top-2000. Lesson inferred: the user was steering the ranking by judgment from looking at the map. No metric, holdout or validation is shown. Strength: changes **documented**, motive **speculative**. Alternative: matching an external client or brief requirement.
- **Toggle semantics:** "Economic adjustment" (on = adjusted) → renamed "Income adjustment / Population density adjustment" with default off (`da67b9e`) → "Default adjustment toggles ON = original formula" (`5155059`) → state-bug fix (`28cd5ca`). Lesson: aligning UI defaults with the canonical formula, then catching the UI/state mismatch. Strength: **explicitly documented** in commit messages.
- **Release discipline:** each change shipped as a paired gh-pages + main commit with identical content. This is a consistent agent-run publish routine. Strength: **documented** (verified identical blobs).

## 9 Demonstrated capabilities, limitations, uncertainties
- Demonstrated: directing a coding agent to deliver a public, self-contained geospatial visualization quickly and to iterate on it many times within one session. It covers scoring variants, UI semantics and deployment, and includes at least one caught-and-fixed state bug.
- The agent produced the technical work (canvas rendering, geometry fixes, deploy diagnosis). Whether Jacob specified or reviewed those decisions can't be determined from this repo.
- Uncertainties: PR/issue state (unchecked); what the private `billboard` repo contains; the actual prompts behind each change.

## 10 Evidence references and verification limits
- `billboard-map@5007c4f:README.md` (Jacob, initial). `@d0bead1:.github/workflows/pages.yml` (added) and `@6d7cbee` (removed, with rationale).
- `billboard-map@488ac87:index.html` (v1 county + dots, payload keys t/z/c). `@01aa465` (ZCTA polygons, keys tz/tc/z). `@300c733`, `@adab7c1`, `@da67b9e`, `@5155059`, `@28cd5ca` (toggle evolution and the bug fix). `@1b350a1`, `@d49f4e3`, `@30b4723`, `@5570f12` (score changes). `@1ec22f0` / `main@f7cbbc3` (final, 28-field records, Deep red).
- Commit trailers on all 24 Claude commits: `Co-Authored-By: Claude Fable 5`, `Claude-Session: …session_016iA4pD6jkVpBSZ13KaVM7q`.
- Executed: payload decode for every version, per-version score diff and top-2000 overlap, `node --check`, headless Chromium render (offline file URL) → `reports/billboard-map_render_default.png`.
- Limits: `gh` not authenticated, so PRs/issues were not retrieved. Interactions were not tested end-to-end. The scoring pipeline is outside this repo.
