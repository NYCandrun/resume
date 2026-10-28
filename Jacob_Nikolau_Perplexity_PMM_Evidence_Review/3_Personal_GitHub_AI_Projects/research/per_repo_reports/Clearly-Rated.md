MANIFEST | Clearly-Rated | PRIVATE | research workflow (agent-run public-web archive + multi-analyst product reconstruction) + small static demo (HTML product tour) | complete | Every commit was made by the Claude identity; none of Jacob's prompts or session transcripts are in the repo, so his direction can only be inferred. The tour generator and the analyst scratch notes are not committed. The repo's GitHub permalinks point to a different repo (`NYCandrun/pmm`, by name only), which I did not check. No PRs or issues. I ran no network fetches.

DISCLOSURE: No credentials found. A regex scan for common key/token patterns came back empty, and the only hits on `token|secret|password` in the code are variable names. The repo holds **bulk copies of a third party's public content**: about 437 knowledge-base pages with 521 kept screenshots (`clearlyrated-kb/`, ~87 MB), 575 marketing-site pages (`clearlyrated-com/`), converted PDFs, and 55 transcripts made from YouTube captions or local Whisper runs on the company's webinars and podcasts. That copied content includes real names and some work email addresses of ClearlyRated staff and customer contacts (public case studies, webinars). The fetchers send a desktop-browser User-Agent string (`scraper/recrawl.py:18`, `site/site_crawl.py:19`). The YouTube caption fetch uses a player-client workaround described as "the only route that worked from a datacenter IP" (`scraper/README.md`). Nothing here looks like employer-internal or proprietary material. Everything came from public pages of a company that is the *subject* of the research, and nothing in the repo ties it to Jacob's employment. **Sharing:** the method docs, briefs, scripts and analysis chapters could be shared after review. The mirrored archives, screenshots and transcripts raise copyright and personal-data concerns and should not be published. The repo already marks itself do-not-index/no-AI (`robots.txt` on the tour branch).

# Clearly-Rated — investigation report

## 1. Identity
- **Owner/context:** a personal repository under NYCandrun. Visibility is PRIVATE. It was created 2026-09-24T07:54Z and last pushed 2026-09-24T18:38Z (repos.json).
- **Type:** an agent-orchestrated research workflow. The pipeline goes: public-web archive → 15–24 parallel "analyst" agents → generated reference chapters → synthesis → contradiction hunt → a KB-vs-website diff. The `claude/` branch adds a static HTML product-tour demo.
- **Purpose (from README):** build a "text-first archive of the public ClearlyRated knowledge base … built for reading by an LLM one file at a time". From that archive it produces a "granular reconstruction of what the product is and does" (screens, controls, packaging, awards, messaging) for someone "who has never seen the product". It then extends to the marketing site (www.clearlyrated.ai) and compares the two sources. The working directory in the briefs is `/home/user/pmm/`.
- **Maturity:** finished as a research deliverable. Each stage has a final commit ("all 7 synthesis chapters complete", "complete 15-chapter … diff"). The scripts are one-off: they keep absolute session paths, and the README tells you to adjust them before re-running.

## 2. Dates and contributions
- **First commit:** `cf13473`, 2026-09-23 18:51 UTC. **Latest on main:** `2a9c9d0`, 2026-09-24 07:49 UTC. **Latest on any branch:** `7fd6870`, 2026-09-24 18:38 UTC, on `origin/claude/product-information-vmr3h7`.
- **Authors/committers:** all 26 commits are authored and committed by `Claude <noreply@anthropic.com>`. Trailers name three models: `Co-Authored-By: Claude Opus 4.8` (13), `Claude Fable 5.1` (12) and `Claude Opus 5.5` (1). Two `Claude-Session:` IDs appear: session `…DbkXvgk…` covers the 19 main commits and session `…VBr8VdX…` covers the 7 tour-branch commits. No human author identity appears anywhere.
- **Jacob's attributable contributions:** none at the commit level. He is the repo owner, and he presumably started both sessions and created the repo. The repo was created about 13 hours after the first commit and right after the last main commit (07:54 vs 07:49), which suggests the history was built elsewhere and pushed here. This is inferred.
- **Activity periods:**
  - 09-23 18:51–21:34: KB archive, pass 2, KB analysis, cross-check, site archive.
  - A gap of about 3.5 hours.
  - 09-24 01:14–01:24: website-edition reference chapters.
  - About 6 hours.
  - 07:39–07:49: synthesis and diff.
  - About 1.5 hours.
  - 09:23–09:28: tour.
  - About 8 hours.
  - 17:25–18:38: tour revisions.
  
  The gaps fit long-running parallel agent work or user downtime. The commits are interim checkpoints ("interim; customer-proof part 1 of 5").
- **Imported history:** the first commit already contains 762 files, so collection happened before any commit. The permalinks point at `NYCandrun/pmm` branch `claude/clearlyrated-kb-scraper-5dhel6` (6,670 links, branch-based rather than SHA-pinned), which strongly suggests the work was first done in a repo named `pmm` and pushed here. No squash or fork markers (`isFork: false`).

## 3. Branch and history coverage
- **Default branch:** `main` (19 commits). The remote branches are `origin/main` and `origin/claude/product-information-vmr3h7`.
- `git log main..origin/claude/product-information-vmr3h7` shows 7 commits that were never merged, and the branch contains all of main. `git diff --stat main...branch` shows 4 files and +3,527 lines: `product-tour.html`, `product-tour-artifact.html`, `product-tour-review.md`, `robots.txt`.
- **PRs/issues:** `gh pr list` and `gh issue list --state all` both return nothing.
- **Inaccessible:** the prompts, the agent transcripts behind the session links, the scratchpad digests (`/tmp/claude-0/.../scratchpad/...`, referenced in `scraper/analysis-site/SYNTHESIS.md`), the per-analyst notes and JSON, the raw HTML corpus (`work2/`), and the tour generator script. The tour commit says "Generated deterministically from product-analysis/reference/*.md", but no generator is committed.

## 4. What it actually does
**Pipeline (code in `scraper/`, about 15 Python/shell files):**
- `extract.py` turns HTML into Markdown. It picks the main container by text density because the site went through three page builders, keeps `rel=canonical`/noindex metadata, and replaces images with placeholders.
- `paths.py` maps URLs to archive paths deterministically.
- `fetch_and_extract.py`, `recrawl.py`, `reextract.py` and `plan_images2.py` handle pass 1 and pass 2. `plan_images2.py` reuses earlier image decisions where it can.
- `assemble.py` builds front matter, a per-folder `_index.md`, long-page splitting, `manifest.json` and `image-log.md`. Its inputs and outputs are set by env vars (`bf4e4f4`).
- `site/` adapts the pipeline to the Webflow marketing site.
- `videos/` covers caption fetch, VTT→MD conversion and faster-whisper `small.en`.
- `gen_reference2.py` merges analyst notes into chapters and links each cited path to the archive and the live URL.
- `diff_links.py` resolves `[[kb:path#Lnn]]` tokens.
- `cross-check/build_xlsx.py` merges the contradiction rows.

Images went through vision-agent review: 1,093 reviewed, 521 kept, 7 uncertain, 565 discarded, with every decision logged in `clearlyrated-kb/image-log.md`.

**Outputs:**
- `product-analysis/`: 9 chapters plus 15 reference chapters (~152k words, 297 screens with control tables).
- `product-analysis-site/`: the website-only twin (~246k words, 24 analysts).
- `cross-check/contradictions.{xlsx,csv}`: 285 rows.
- `product-analysis-diff/`: 158 conflicts.
- On the branch, `product-tour.html`: 181 steps, about 59 MB with images embedded. `product-tour-artifact.html` is about 750 KB and references the images instead.

**What I inspected and ran (offline only):**
- Read README, `scraper/README.md`, all 6 agent briefs, one package list, the diff summary, the tour review, and all commit messages.
- `py_compile` on every `.py` file: all pass.
- Resolved all relative Markdown links in `product-analysis*/`: **17,515 links, 0 broken.**
- Checked the 285-row CSV: for 570 quotes, the opening fragment appears within ±2 lines of the cited line in **533 cases**. Another 25 appear elsewhere in the same file and 12 were not found by my simple normalisation (ellipses or markup could explain these). That is a high but imperfect citation accuracy.
- Spot-checked two headline conflicts against source lines; both are accurate:
  - Rackspace at `clearlyrated-kb/client-services/data-privacy/02-gdpr-and-ccpa-compliance-statement.md:30` vs GCP/SOC 2 at `clearlyrated-com/ai-instructions/02-…md:42`.
  - User quotas "Unlimited | 50 | 10" at `clearlyrated-kb/client-services/accounting/full-feature-list.md:20` vs 5/15/30 at `clearlyrated-com/pricing.md` around L89.
- The tour's 181 `class="step"` blocks: every image `src` resolves to a file in `clearlyrated-kb/`.

I did **not** re-run any fetch, transcription or vision step, and I did not check the external `pmm` permalinks.

## 5. How Jacob uses AI
This repo shows **AI agents doing research**, with Jacob most likely acting as the commissioner and director. It is not an AI-powered product. The direct evidence:
- Claude authorship and trailers on every commit.
- A `claude/` branch name.
- Committed **worker briefs written for sub-agents**: `scraper/analysis/INSTRUCTIONS.md` ("You are one of 15 analysts…"), `analysis-site/INSTRUCTIONS.md`, `SYNTHESIS.md`, `DIFF_INSTRUCTIONS.md`, `cross-check/INSTRUCTIONS*.md`.
- The tour review, which describes a "five-reviewer panel".

The briefs appear to have been written by the orchestrating agent; whether Jacob wrote or edited them is not evidenced. They show careful task design:
- Non-negotiables: "Read every page in full… Do not skim"; "View every product image"; tell "what the text says" apart from "visible: …"; "Never invent behaviour".
- A fixed 9-section template so outputs can be merged.
- Source isolation for the website edition: "Do NOT open … clearlyrated-kb … do not use outside knowledge".
- A machine-checkable citation-token format with line numbers.
- Instructions to validate JSON.
- Context management: the archive is laid out for an LLM to read "one file at a time", with index files in every folder and digests for synthesis agents.

Verification appears as a deterministic link resolver ("6,100 citations, 0 broken"), the line re-location step in `build_xlsx.py`, and a review panel that audits before anything changes.

Signs that Jacob steered the work are **speculative** and come only from commit content:
- The second-pass fix "Address two gaps" (`4fa1943`).
- The turn to make the tour "self-guided" and to put a plain-language purpose line first in every step (`95f034d`, `54acf58`).
- The do-not-index/no-AI-training layer (`594a702`).
- The rebuild to fit under the "16 MB Claude-artifact cap" for private publishing (`7fd6870`).

These read like responses to user requests, but the prompts aren't available.

## 6. Quality assessment
**Strengths (high confidence):**
- **Provenance:** every claim links to the archive file, the line and the live URL, and links resolve.
- **Uncertainty:** "visible only" vs "per docs", "the website does not state…", both values given on conflicts, an open-questions chapter, and severity and staleness labels on contradictions.
- **Design for independence:** the KB and website editions were written separately and then compared, which avoids contaminating one source with the other.
- **Completeness:** it recognised that the sitemaps were incomplete and recovered 101 pages by walking the link graph with canonical de-duplication.
- **Reproducibility notes:** limitations are stated honestly (Vimeo returned 403, private videos are noted, absolute paths are flagged).
- **Consistent with source:** the diff summary's synthesis (plan repackaging, Rackspace→GCP, Privacy Shield→DPF) matches the cited source lines I checked.

**Weaknesses:**
- It **cannot be reproduced from this repo**: absolute `/home/user/pmm` and `/tmp/claude-0` paths in about 20 files, no raw HTML, no analyst notes, no tour generator. Re-running needs network access and vision agents.
- The **GitHub permalinks point to another repo and a mutable branch**, so the "0 broken" claim only held in the original repo. Here, only the relative and live links can be relied on.
- About 6% of spreadsheet quotes are not at the cited line ±2. That is minor.
- No dependency manifest beyond the README.
- The "analyst" outputs are themselves LLM paraphrase. The design deals with this by telling the diff analysts to "Quote the source, not the chapter".
- Scope is large and intentional. It is a one-off research artifact, not a maintained tool, which fits its purpose.
- The tour's `robots.txt` has no effect in a private GitHub repo. It only matters if the tree is ever served.

## 7. Developmental milestones
1. `cf13473` (09-23): KB archive with 336 pages from the sitemaps.
2. `4fa1943`: pass 2, a link-graph walk taking it to 437 pages and a text-density extractor.
3. `3df36d8`: a KB product analysis by 15 analysts.
4. `db6e0b8`/`bf4e4f4`: tooling parameterised by env vars so it can be reused for a second archive.
5. `6387545` then `0081ff3`: contradictions spreadsheet, first preliminary (180 rows) and then final (285 rows).
6. `c04df27`: marketing-site archive plus transcripts.
7. `531ba81`: `gen_reference2.py` (edition-aware, live links), replacing `gen_reference.py`.
8. `8064e57` to `e7adad0` (09-24): website edition.
9. `2a9c9d0`: KB-vs-site diff with 158 conflicts.
10. Branch `0340a1f` to `7fd6870`: product tour, then embedded images, then self-guided, then purpose lines, then panel review, then noindex, then the lightweight artifact build.

## 8. Changes in working method and possible lessons
- **Sitemap seeding → link-graph walk (`cf13473` → `4fa1943`, 09-23 18:51 → 19:36).** The trigger is stated: "The site's sitemaps turned out to be incomplete". The lesson is not to trust sitemaps for completeness. Evidence: *explicitly documented*.
- **Single-template extraction → text-density container picking (same commits).** The trigger was that the "KB was rebuilt across several page builders". Evidence: explicit.
- **Hard-coded paths → env-configurable assembler and generator (`db6e0b8`, `bf4e4f4`, 09-23 20:12–20:32).** The trigger was reusing the pipeline for the website archive. Evidence: strongly inferred from timing and the "so the same assembler builds other archives" wording.
- **Archive-path citations → archive + live link (`531ba81`), then line-pinned `[[kb:…#Lnn]]` tokens for the diff.** The earlier chapters cited paths without lines, and the diff brief says "the chapters cite paths but not lines, and the chapter text is an analyst's paraphrase, not the source". The lesson is to verify against the primary text at line level. Evidence: explicitly documented in `DIFF_INSTRUCTIONS.md`.
- **Single-source analysis → twin independent editions plus diff (09-23 KB edition → 09-24 site edition).** The site brief forbids opening the KB. Evidence: explicit design. The trigger is not stated.
- **Tour grouped by source chapter → grouped by screen type (`e8989a0`, 09-24 18:21).** The panel found the cause: "screens were routed by source chapter". It produced 66 findings and cut the tour from 199 to 181 steps. Evidence: explicitly documented in `product-tour-review.md`.
- **Embedded 59 MB tour → 750 KB referenced build (`8854a86` → `7fd6870`).** The trigger was the 16 MB artifact cap. Evidence: explicit. An alternative explanation is that self-contained sharing was wanted first and private-artifact publishing came later.
- **Prompt evolution beyond what is committed cannot be reconstructed.** The briefs exist only in their final form, each committed once.

## 9. Demonstrated capabilities, limitations, uncertainties
- **Demonstrated (through agents he directed):**
  - Large multi-agent research decomposition with merge-ready templates.
  - Citation discipline and deterministic verification.
  - Iterating on completeness gaps.
  - Separating sources to get an independent comparison.
  - A review-then-fix loop on a deliverable.
  - Awareness of artifact and publishing limits and of not wanting the content indexed or used for AI training.
- **Uncertainties:** how much Jacob specified vs what the agents decided themselves (*high uncertainty*), and the final purpose of the analysis (not stated in the repo).

## 10. Evidence references and verification limits
- **Commits:**
  - `Clearly-Rated@cf13473`, `@4fa1943:scraper/README.md`, `@3df36d8:scraper/analysis/INSTRUCTIONS.md`, `@531ba81:scraper/gen_reference2.py`, `@0081ff3:cross-check/contradictions.csv`, `@2a9c9d0:product-analysis-diff/00-summary.md`.
  - `@2a9c9d0:scraper/analysis-site/{INSTRUCTIONS,SYNTHESIS,DIFF_INSTRUCTIONS}.md`.
  - Branch `origin/claude/product-information-vmr3h7`: `@e8989a0:product-tour-review.md`, `@594a702:robots.txt`, `@7fd6870:product-tour-artifact.html`.
- **Spot-checked lines:** `clearlyrated-kb/client-services/data-privacy/02-gdpr-and-ccpa-compliance-statement.md:30`, `clearlyrated-com/ai-instructions/02-where-clearlyrated-is-not-the-right-fit.md:42`, `clearlyrated-kb/client-services/accounting/full-feature-list.md:20`, `clearlyrated-com/pricing.md:85-95`.
- **Limits:**
  - No network re-runs.
  - `NYCandrun/pmm` permalinks not checked.
  - Session transcripts are not available.
  - The citation-accuracy check was a heuristic fragment match.
  - The HTML tour was checked structurally (step count, image paths), not rendered in a browser.
