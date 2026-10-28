MANIFEST | liquid_LFM2.5-VL_demo | PUBLIC | demo / persuasive technical field note (static web asset + calculator + PDFs) | complete | 2 commits, single branch, no PR/issue access (gh unauthenticated); PDFs inspected via text extraction only; pages not rendered in a browser; factual claims (benchmarks, prices) not checked against external sources per repo-only rule

DISCLOSURE: No credentials, customer data, or third-party private data found. Subject is a third-party company's public model (Liquid AI LFM2.5-VL-450M); both HTML pages and both PDFs state "Independent technical … not an official Liquid AI asset" (index.html footer; onepager.html `.ft`), and all cited figures are attributed to public sources (HF model cards, Liquid blog/docs, vendor price pages). The exec one-pager is styled as a vendor sales brief ("LFM2.5-VL-450M · Liquid AI" header, "for the visual-data buying committee"), which a reader could mistake for official collateral despite the footer disclaimer — I don't think this makes ownership ambiguous, but it is worth noting. Commit author email is a company-domain address (`jacobn@…mosaicapp.com`) and is exposed in public history. That is identity metadata only and is not evidence of employer ownership. The LICENSE names "Jacob Nikolau" (MIT, 2026). Appears suitable to share after review. Before sharing, decide whether to make the "independent / unofficial" status more prominent on the one-pager header and whether to keep the work-domain email in history.

# liquid_LFM2.5-VL_demo — investigation report

## 1. Identity
- Personal repo on the NYCandrun account, **public** (repos.json: created 2026-07-01T20:26Z, pushed 2026-07-01T20:33Z, not a fork, default `main`, no description).
- Type: **demo / persuasion asset**. It is a single-page interactive "field note" (`index.html`, 460 lines) with a client-side TCO calculator, a print-styled executive one-pager (`onepager.html`, 129 lines), and two Headless-Chrome-printed PDFs of those pages. README is 12 lines and MIT LICENSE.
- Purpose: argue that LFM2.5-VL-450M (a 450M-parameter vision-language model) belongs in **data pipelines** ("corpus-scale visual triage"), not in user-facing products. The core argument is that re-processing whole image archives makes metered APIs expensive, while on-device inference has ≈$0 marginal cost. Intended audience: "data & ML platform teams" (index hero tag) and a "visual-data buying committee" at a "Fortune-2000" (one-pager).
- Maturity: finished, published snapshot. There is no model code, inference, or backend. It is a communication artifact, not software that runs the model.

## 2. Dates & attributable contributions
- All history: `a7d90e4` "Empty repository" (2026-07-01 16:30:12 −0400) → `cb10ba5` "Publish LFM2.5-VL-450M demo…" (2026-07-01 16:33:50 −0400). Both are on `main`.
- Authors/committers: only `jacobn-a11y <jacobn@mosaicapp.com>` (author = committer on both). No bot authors.
- AI co-author trailer on `cb10ba5`: `Co-Authored-By: Claude Opus 4.8 <noreply@anthropic.com>`.
- Pre-repo work: PDF metadata gives CreationDate **2026-06-29 20:13–20:15 UTC** (Creator: HeadlessChrome/149, Producer: Skia/PDF). So the content existed at least two days before the repo, and earlier iterations happened elsewhere. The repo is a **publish-only snapshot**. Jacob's attributable activity spans one ~4-minute window on 2026-07-01, plus content dated 2026-06-29 via file metadata.

## 3. Branch & history coverage
- Branches: `main` only (`origin/HEAD -> origin/main`). There are no other remote branches, so no unmerged work and no branch diffs to report.
- PRs/issues: `gh` is unauthenticated in the sandbox, so PRs and issues could not be listed. With 2 commits pushed straight to main within 4 minutes, PRs are unlikely, but this is unverified.
- No squash evidence beyond the obvious fact that the drafting history isn't in the repo. The commit message references the "pipeline, not your product" *angle* and says the README was "aligned to the pipeline angle". That wording implies other angles were considered before publishing. Those drafts are not in this repo, and the process cannot be reconstructed from it. (Sibling Liquid-themed repos exist on the account, e.g. `liquid-token-budget-slider`, created the same day. I did not inspect them, and no copy relationship is evident.)

## 4. Actual functionality
Inspected: every file, in full (HTML source; PDF text via `pdftotext`, metadata via `pdfinfo`).
Executed: `node --check` on the extracted inline scripts of both HTML files (both pass), plus an independent reimplementation of the calculator formula in Node to check its outputs. I did not render the pages in a browser because no headless browser was available.

- **index.html (interactive field note).** It is dark-themed static HTML/CSS with vanilla JS and no dependencies or network calls. Sections:
  1. Problem framing: three alternatives (frontier API, self-host 3–7B, silicon-partner on-device).
  2. The "reframe": a product reads each image once, while a pipeline re-reads the corpus.
  3. **Calculator.** Sliders for corpus size (1–300M), monthly inflow (0–60M) and full re-processes per year (0–12), a dropdown of 5 API price tiers ($0.05–$3.83 per 1k images), and 4 industry presets. It renders sorted cost bars, readouts, a verdict sentence and a visible assumptions line.
  4. Benchmark tiles against SmolVLM2-500M.
  5. An explicit "Where it is NOT the answer" callout: OCRBench 684 vs Qwen2.5-VL-7B's 864.
  6. A licence caveat: the LFM Open License v1.0 is not Apache/MIT.
  7. A competitor table.
  8. A 5-line llama.cpp deployment snippet.
  9. A falsifiable two-week pilot: 100k images, fine-tune, measure precision/recall and cost-per-million.
  10. A primary-sources list.
- **Calculator model** (`index.html` script):
  - Annual inferences = 12·monthly + corpus·reprocesses.
  - API cost = inferences/1000 × tier price.
  - On-device: devices = ceil(inferences / 130M), cost = devices × ($1500/3 yrs + $160 power).
  - The 130M figure comes from 242 ms/img on Jetson Orin running continuously. I verified 365·86400/0.242 ≈ 130.3M.
  - For the default preset (30M corpus, 3M/mo, 3×/yr), my reimplementation gives 126M inferences: $6.3k (Flash-Lite) / $18.9k / $63k / $163.8k / $482.6k (GPT-4o-mini) vs $660 on-device. These match the static bars printed in the one-pager PDF exactly ($483k, $164k, $63k, $19k, $6.3k, $660), so the HTML and PDF are internally consistent.
- **onepager.html.** A print layout (`@page Letter`) with three value cards, a bar chart, a short competitor table, the OCR/licence caveat, the pilot ask and a disclaimer footer. Its script **hardcodes** 126M inferences and the $660 on-device figure rather than sharing the calculator logic. That is acceptable for a static brief, but the two pages would drift apart if either were edited.
- **PDFs.** `LFM2.5-VL-450M_field-note_static.pdf` (9 pages, a print of index.html for email; same text, including the Mercedes-Benz claim and the disclaimer) and `LFM2.5-VL-450M_exec-onepager.pdf` (1 page).
- Not implemented: there is no actual model run, no sample images or outputs, and no benchmark reproduction. All benchmark and price numbers are quoted, not measured, in this repo.

## 5. How Jacob uses / builds with AI
- **Using AI to build** a communication asset *about* an AI model. Direct evidence: the `Co-Authored-By: Claude Opus 4.8` trailer on `cb10ba5`, the only content commit. The repo has no agent instruction files, prompt files or agent branches.
- The repo can't show how work was split between Jacob and Claude, what instructions were given, or what was corrected. The record shows only a curated final output and a deliberately chosen framing ("the pipeline angle").
- Some judgment visible in the content (this is about the artifact, not proof of who contributed what):
  - It volunteers weaknesses: OCR, the non-Apache licence, the Qwen-3B Research licence, and that "the API is not unaffordable at the cheapest tier".
  - It frames the pilot so it can fail ("designed to kill the idea fast").
  - It prints the calculator's assumptions on the page.

## 6. Quality assessment (purpose: demo/persuasive brief)
**Strengths (high confidence)**
- Clear single thesis with a strong reframing (pipeline re-processing as the cost driver). The interactive calculator makes the argument concrete, and its arithmetic is correct and transparent.
- Unusual candour for a persuasion piece: it states the limits (OCR), licence risks for both LFM and Qwen, that the cost argument doesn't hold at every API tier, and that three of the four axes are not priced. The honest competitor table concedes that Qwen2.5-VL-3B scores higher.
- Well-crafted static web: responsive grid, no dependencies, sticky nav, print-ready one-pager. The packaging works for different channels (web, email PDF, exec PDF).

**Weaknesses (medium–high confidence)**
- **The TCO model is one-sided.** On-device cost counts only amortized hardware and power. It leaves out engineering and ops labour, fine-tuning compute and labelled data for "fine-tune to your taxonomy", orchestration and storage, and redundancy. It also assumes 100% continuous utilization of a single Jetson at single-image latency. The page discloses some of this, but the big multiples ("~700× less") depend on it.
- API pricing is given as $/1k images with no stated tokens-per-image derivation in the repo. The "~33× image-token multiplier" for GPT-4o-mini is asserted, not shown.
- Self-hosted Qwen appears in the table as "≈$0 marginal" but not in the calculator, even though it's the "real self-host rival". So the calculator compares mainly against APIs, which is the easiest comparison to win.
- Sources 5–7 (Business Wire, vendor pricing pages, competitor cards) have no URLs, despite the claim that "every figure on this page is sourced to a primary document".
- The one-pager hardcodes its figures, so it can drift from the calculator.
- Small UX issue: dragging a slider leaves a preset highlighted as active.

**Unverified**: whether the benchmark numbers, prices, release date and the Mercedes-Benz claim are accurate. The brief scopes this report to repo evidence, so I did not check them.

## 7. Developmental milestones
- 2026-06-29 (PDF metadata): both PDFs printed from HTML with Headless Chrome, so the content was essentially final by then.
- 2026-07-01 16:30: repo initialized empty.
- 2026-07-01 16:33: all content published in one commit with an AI co-author trailer. There was no further activity.

## 8. Changes in working method & possible lessons
Only a final snapshot exists, so **the process cannot be reconstructed** from this repo. One weak signal: the commit message's "Ships the 'pipeline, not your product' data-pipeline angle" and "README aligned to the pipeline angle" suggest that one framing was chosen from several. *Evidence strength: speculative.* Alternative explanation: this is just descriptive language for the single angle that was ever drafted.

## 9. Demonstrated capabilities, limitations, uncertainties
- Demonstrated: technical-marketing synthesis of a model's positioning (use-case selection, competitor framing, licence and limit disclosure); building a dependency-free interactive cost calculator with correct arithmetic; multi-format packaging (web, print PDFs); declaring AI co-authorship in the commit.
- Uncertainties: who authored which parts (shared with Claude per the trailer); whether the external claims are accurate; PR/issue state (gh unauthenticated); how the pages render visually (not rendered).

## 10. Evidence references & verification limits
- `liquid_LFM2.5-VL_demo@a7d90e4` (empty init); `@cb10ba5` (all content; `Co-Authored-By: Claude Opus 4.8` trailer).
- `@cb10ba5:index.html`: hero "Every figure… sourced"; calculator script constants `OD_PER_DEVICE_YR = 130e6`, `OD_HW = 1500, OD_AMORT = 3, OD_POWER = 160`; "Where it is NOT the answer" callout; footer "Not an official Liquid AI asset"; sources list.
- `@cb10ba5:onepager.html`: hardcoded `inf=126e6` and `660`; footer disclaimer.
- `@cb10ba5:LFM2.5-VL-450M_exec-onepager.pdf` (1 p., created 2026-06-29T20:15:42Z) and `@cb10ba5:LFM2.5-VL-450M_field-note_static.pdf` (9 pp., created 2026-06-29T20:13:48Z).
- `@cb10ba5:LICENSE` (MIT, Jacob Nikolau 2026); `@cb10ba5:README.md`.
- Branches: `main` / `origin/main` only.
- Verification limits: no PR/issue listing (gh auth missing); no browser rendering; JS syntax checked and calculator outputs reproduced in Node; external factual claims not checked.
