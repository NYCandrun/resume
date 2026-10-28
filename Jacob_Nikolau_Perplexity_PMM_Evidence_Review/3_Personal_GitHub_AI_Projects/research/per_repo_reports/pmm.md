MANIFEST | pmm | private | research workflow (agent-run web archive + multi-analyst document analysis + spreadsheet deliverable) | complete | 100% of commits authored by "Claude" via Claude Code; Jacob's prompts and the session transcript are not in the repo; intermediate analyst notes/scratchpad are not committed; the network pipeline was not re-run; the "one-pager" the workbook feeds is not in the repo

DISCLOSURE: No credentials found (regex sweep of non-archive files; scripts read only path env vars). The repo is about ClearlyRated, a third-party company, and holds a bulk copy of its **public** knowledge base (knowledge.clearlyrated.com, 437 pages, about 87 MB including 500+ screenshots and 40 converted PDFs) and its marketing site (www.clearlyrated.ai, 575 pages, about 1.2M words), plus video/podcast transcripts. Nothing in the repo looks like internal, customer-confidential or employer-owned data. Every source is a public URL, and the documents themselves call the material "public content". There is no evidence of any employment relationship with ClearlyRated, so none is inferred. The repo does contain third-party copyrighted text and images, plus names (and at least one email address the analysis decoded from a press release) of ClearlyRated staff and customer firms, all taken from public pages. **Sharing:** the method and the analysis layers (scraper/, analyst briefs, product-analysis*/, cross-check, deliverable workbook) could be shared after review. The raw mirrored archives (clearlyrated-kb/, clearlyrated-com/) should not be redistributed publicly because of copyright and personal names. Keep the repo private or share it without those folders.

# pmm — investigation report

## 1. Identity
- **Owner/context:** NYCandrun personal account. Private repo, not a fork, created 2026-06-30 (repos.json), with an empty description. The only branch and the default branch is `claude/clearlyrated-kb-scraper-5dhel6`. There is no `main`.
- **Type:** an agent-run research workflow. Step one builds an LLM-readable archive of a company's public documentation. Next comes a reconstruction of the product ("what it is, screen by screen, button by button", plus packaging and messaging) from each source on its own, then a comparison of the two sources and a list of factual contradictions. The output is an Excel workbook of "content conflicts" meant to feed a "one-pager" (workbook column `On the one-pager`; commit 2718b66).
- **Intended reader:** someone who needs a complete, sourced picture of ClearlyRated's product, packaging and positioning, and of where its public content is inconsistent. The README says the archive is "built for reading by an LLM one file at a time". Why Jacob wanted this is not stated in the repo and is not inferred here.
- **Maturity:** finished for its purpose. Each phase was carried through to a final deliverable, and the deliverable was then live-checked and de-duplicated. It is a one-off study, not a maintained tool.

## 2. Dates and attributable contributions
- First commit `cf13473` 2026-09-23 18:51 UTC. Last commit `a907067` 2026-09-24 18:17 UTC. That is 22 commits in about 23.5 hours, all on one branch. The repo was created three months before the first commit, and nothing in the history explains the gap.
- **Authors/committers:** every commit's author and committer is `Claude <noreply@anthropic.com>`. Every commit carries the same trailer, `Claude-Session: https://claude.ai/code/session_01DbkXvgkokbX79bjMyukDuM`, so all the work came from one Claude Code session. Co-Authored-By model labels change over time: "Claude Opus 4.8" (cf13473, 4fa1943, 6920084–2a9c9d0, 2071a24, a907067), "Claude Fable 5.1" (3df36d8 through ed16c2c) and "Claude Opus 5.5" (2718b66).
- **Jacob:** none of the commits are authored by NYCandrun, jacobn-a11y or any other human identity. His contribution is indirect: he owns the repo and the agent session that pushed the work. His instructions are not in the repo. All dates for his work are inferred from the session's activity, 2026-09-23 to 2026-09-24.
- Activity: an intense day (09-23, about 18:51–21:34), work again 09-24 from 01:14 to 07:49 (site edition and diff), and a final round 09-24 09:23–18:17 (workbook, live-check, de-duplication). There are no PRs and no issues. No history is imported, squashed or forked.

## 3. Branch and history coverage
- Only `origin/claude/clearlyrated-kb-scraper-5dhel6` exists (also HEAD), so there are no unmerged branches or diffs between branches. Every commit was reviewed (`git log --all`, all commit bodies, `--shortstat`).
- The volume of change sits in the data drops: cf13473 (762 files, about 36k lines), 4fa1943 (355 files), c04df27 (1,039 files, about 230k lines, the site archive) and 531ba81 (relinking every citation, 1,629 deletions). The three deliverable commits change only the binary xlsx.
- **History that cannot be seen:** the Claude Code session transcript and Jacob's prompts; the 15/24 per-analyst notes and contradiction JSON (they lived under `/tmp/claude-0/.../scratchpad`, which the hard-coded paths in `scraper/assemble.py` L14 and `scraper/cross-check/build_xlsx.py` reference); the generator for the final `deliverable/` workbook (no script in the repo writes "Live check" or "content-conflicts"); and the one-pager.

## 4. What it does
Pipeline as recorded in the commits, `scraper/README.md` and the analyst briefs:
1. **Knowledge-base archive** (cf13473). Reads robots.txt, then the sitemap index, then 6 sub-sitemaps (336 URLs) split into 30 batches for parallel workers. HTML is converted to Markdown with front matter and an `_index.md` per folder. Pages over 3,000 words are split, linked PDFs are converted, and `manifest.json` and `image-log.md` are written. Agents reviewed images and kept only product screenshots; every decision is logged.
2. **Completeness pass** (4fa1943). The commit records that the sitemaps were incomplete. `recrawl.py` walks the internal link graph (206 candidates) and collapses duplicates by `rel=canonical`, recovering 101 real pages (336 → 437). The extractor moves from one assumed template to picking the container by text density, because the site was built with Beaver Builder, Elementor and classic WordPress. Earlier image decisions are reused, and only about 327 new images go to "15 vision workers".
3. **KB product analysis** (3df36d8). The 437 pages are split into 15 package files (`scraper/analysis/packages/*.txt`). Each package goes to one "analyst" sub-agent under `scraper/analysis/INSTRUCTIONS.md`, which sets a 9-section template and rules: read every page and every screenshot, separate "per docs" from "visible only", never invent behaviour, cite KB paths. `gen_reference.py` merges the notes into 15 reference chapters (about 152k words, 297 screens with control tables) and builds the glossary and open questions. Synthesis chapters 01–07 follow.
4. **Website archive and transcripts** (c04df27). 575 marketing pages, 255 redirects and 17 404s recorded. YouTube captions plus local Whisper transcription. Vimeo refusals and private videos are noted, not hidden.
5. **Contradiction hunt** (6387545, then 0081ff3). Analysts get verbatim-quote, file+line and severity rules and must validate their JSON (`scraper/cross-check/INSTRUCTIONS*.md`). `build_xlsx.py` merges 285 rows and re-locates line numbers by searching for the quote text.
6. **Website-only edition** (8064e57–e7adad0). 24 analysts with an explicit rule: do not open the KB edition, so that the two analyses stay independent and can be compared (`scraper/analysis-site/INSTRUCTIONS.md`, `SYNTHESIS.md`).
7. **KB-vs-site diff** (6920084, 2a9c9d0). Per-area briefs require quoting the archive, not the chapter, with `[[kb:path#Lnn]]` tokens. `diff_links.py` resolves each token to three links: archive file, GitHub line and live URL. 158 conflicts are recorded with "6,100 citations, 0 broken", and `00-summary.md` synthesises the patterns (plan repackaging, acquisition, hosting/SOC 2 vs Rackspace/Privacy Shield, LLC vs Inc., benchmark drift, award-rule inconsistencies).
8. **Deliverable workbook** (2718b66, 2071a24, a907067). Four tabs: Site vs KB, KB vs Itself, Ambiguities, Key. Severity has a formula-driven score. After that: a "line-by-line live-check" by four agents (one row dropped as resolved, 8 explanations and 3 severities corrected), then de-duplication (7 rows merged, 284 → 277).

**What I inspected and verified (offline):**
- All commit messages and the instruction files. I read README, scraper/README, product-analysis/_index.md, 00-summary.md and cross-check/README.
- `py_compile` on all scraper scripts: passes.
- I opened the workbook with openpyxl. The tabs and headers match the commits: 73 Site vs KB, 92 KB vs KB and 112 Ambiguities data rows, plus Key.
- I checked row S-02's quotes and the S-01 "20%" quote word for word against the archives (`clearlyrated-com/blog/best-staffing-firms-for-women-2026-winners.md:113`, `clearlyrated-kb/blog/clearlyrated-to-publish-its-inaugural-list-of-best-staffing-firms-for-women.md:40`, `clearlyrated-com/blog/reputation-management-for-recruiting-firms/02-…md:109`).
- Random sample of 300 of the 2,524 quote+line citations in product-analysis-diff: 243 matched by plain substring within ±2 lines. I read four of the 57 misses by hand and all four were formatting differences only (curly vs straight apostrophes, line wraps, a heading split from its text), not wrong quotes.

**Not done:** I did not re-run any fetch, transcription or vision step (network or paid services), did not check live pages, and did not verify individual screenshot descriptions.

## 5. How Jacob works with AI
This is **directing agents to do research**, not building an AI product. The direct evidence:
- Commit trailers name Claude models and a single Claude Code session.
- The branch name is `claude/*`.
- The repo has six agent brief files.
- Commits describe fan-out to parallel workers ("30 batches", "15 vision workers", "20 analysts", "24 analysts", "Four agents re-checked all 285 rows").

The orchestrator's choices for task design and context management show in the artifacts:
- Fixed note templates with verbatim headings so the notes can be merged mechanically.
- Strict source isolation between the KB edition and the site edition, so the comparison means something.
- Citation-token formats resolved by scripts rather than by models.
- An archive designed around LLM context limits: `_index.md` files, summaries, page splitting.
- Reuse of earlier image decisions so work is not repeated.
- Validation steps: "Validate your JSON", "0 broken" link checks, re-locating quotes by text, a live recheck ("570 of 570 found").

Whether Jacob wrote these briefs, or the orchestrating Claude wrote them from his higher-level requests, **cannot be determined**: everything is committed under the Claude identity. The late rounds suggest human steering: a "consolidated workbook for the one-pager", then a live recheck, then de-duplication. Each looks like a reaction to a review of the previous output, but that is **strongly inferred, not documented**. There is no direct evidence of Jacob reviewing or correcting specific AI output.

## 6. Quality assessment
**Strengths (confidence: high):**
- The research design fits the question: two independently built analyses, a structured diff, and both "likely-stale" and "contradiction" categories with defined severity rules.
- Provenance is strong. Quotes are verbatim, with file+line, GitHub line link and live URL, and my sample held up.
- Coverage problems were found and documented rather than hidden: sitemap gaps, template variance, Vimeo refusals, private videos, a mislabelled-title CMS artefact.
- Uncertainty is stated explicitly: "per docs" vs "visible only", "the website does not state…", open-questions chapters, and chart figures in images flagged "need a human eye".
- The final workbook was validated against the live sites and corrected in a recorded commit (2071a24).

**Weaknesses:**
- **Reproducibility is partial.** The scripts hard-code session paths (`/home/user/pmm`, `/tmp/claude-0/...scratchpad`), which the README admits. The analyst notes and contradiction JSON are not committed, and the final workbook's generator is missing, so the deliverable cannot be rebuilt from the repo.
- GitHub links point at the branch, not a commit, so they will drift if files change. The xlsx line re-location reduces this only inside `build_xlsx.py`.
- There are small stale docs. `product-analysis/_index.md` (last changed 3df36d8) still says "Embedded videos … were not transcribed", although transcripts were added in c04df27. The top README title still describes only the KB archive.
- Model-written claims of exhaustive reading ("Read every page in full") cannot be checked from the repo.
- The bulk of the repo is a raw third-party mirror (about 100 MB), which drives the disclosure concern.
- Severity ratings are the model's judgement, corrected in 2071a24. I did not test them independently.

## 7. Developmental milestones
- **09-23:** KB archive (cf13473) → completeness/robustness pass (4fa1943) → KB product analysis (3df36d8) → reusable assembler/env config (db6e0b8, bf4e4f4) → preliminary contradictions (6387545) → site archive and transcripts (c04df27) → 285-row contradictions (0081ff3) → every citation linked to the live page (531ba81).
- **09-24:** website-only edition (8064e57–e7adad0) → 15-area diff and summary (2a9c9d0) → consolidated workbook (2718b66) → live-check (2071a24) → de-duplication (a907067).

## 8. Changes in working method and possible lessons
1. **Sitemap-only discovery (cf13473, 09-23 18:51) → crawling the link graph with canonical de-duplication (4fa1943, 19:36).** Trigger documented: "the sitemaps proved incomplete". Lesson: don't trust the seed list; check coverage. *Explicitly documented.*
2. **One assumed page template → container chosen by text density (4fa1943).** Trigger documented: inconsistent containers across page builders. *Explicitly documented.*
3. **One KB-only analysis (3df36d8) → a parallel website-only edition with a no-cross-reading rule, then a formal diff (8064e57–2a9c9d0).** Possible trigger: early site-vs-KB contradiction rows (0081ff3) showed the two sources disagree, so separate reconstructions became necessary. *Strongly inferred.* Alternative explanation: the plan from the start.
4. **Citations as bare KB paths (`gen_reference.py`) → archive+live links (531ba81) → line-level tokens with three resolved links (`diff_links.py`).** Lesson: claims need line-level, checkable provenance. *Strongly inferred* from the commit messages and brief wording ("Quote the source, not the chapter").
5. **Archive-only checking (0081ff3, 2a9c9d0) → live recheck of all rows (2718b66, then 2071a24), which found one resolved item and 11 wrong explanations or severities → de-duplication (a907067).** Lesson: a snapshot goes stale, and agent output needs a second verification pass before it goes to a reader. *Documented as actions; the motive is inferred.*
6. **Analyst roles/models:** the trailers change from Opus 4.8 to Fable 5.1 to Opus 4.8 to Opus 5.5 to Opus 4.8. The reason is not documented. *Speculative* (model choice per phase, or session defaults).

## 9. Capabilities, limitations, uncertainties
**Demonstrated in this personal repository:**
- Large-scale multi-agent research orchestration through Claude Code: decomposition into packages, fixed templates, isolated parallel analyses, scripted merging and link resolution.
- Source-provenance discipline and validation loops: quote re-location, link checks, live recheck, de-duplication.
- Turning a raw corpus into a reader-facing deliverable (a severity-scored workbook) and iterating on it.

**Uncertainties:**
- Who wrote the briefs.
- Why the project exists and what the one-pager is.
- Whether per-image descriptions and exhaustive-read claims are accurate.
- The three-month gap between repo creation and the first commit.

## 10. Evidence references and verification limits
- **Commits:**
  - `pmm@cf13473`, `pmm@4fa1943`: scraper/README.md, extract.py, recrawl.py
  - `pmm@3df36d8`: scraper/analysis/INSTRUCTIONS.md, packages/*.txt, product-analysis/_index.md
  - `pmm@c04df27`: scraper/site/, scraper/videos/whisper_batch.py
  - `pmm@0081ff3`: scraper/cross-check/INSTRUCTIONS.md, INSTRUCTIONS_SITE.md, build_xlsx.py (L13–16 hard-coded scratchpad/branch)
  - `pmm@531ba81`: scraper/gen_reference2.py, diff_links.py
  - `pmm@8064e57`: scraper/analysis-site/INSTRUCTIONS.md
  - `pmm@6920084`: scraper/analysis-site/SYNTHESIS.md, DIFF_INSTRUCTIONS.md
  - `pmm@2a9c9d0`: product-analysis-diff/00-summary.md
  - `pmm@2718b66`, `pmm@2071a24`, `pmm@a907067`: deliverable/ClearlyRated-content-conflicts.xlsx
- **Other paths:** `scraper/assemble.py` L14–15 (session paths); `cross-check/README.md`; `clearlyrated-com/redirects.json`.
- **Other evidence:** session trailer `session_01DbkXvgkokbX79bjMyukDuM` on all 22 commits. PRs: none. Issues: none.
- **Verification limits:** offline only. No scraping, transcription or vision re-runs, and no live-site checks. The citation check was a crude 300-sample substring test plus manual review of 4 misses. I did not read the analysis chapters in full (about 400k words across the editions).
