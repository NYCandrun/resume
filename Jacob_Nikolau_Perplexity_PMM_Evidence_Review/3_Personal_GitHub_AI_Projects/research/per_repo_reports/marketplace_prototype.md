MANIFEST | marketplace_prototype | PRIVATE | mixed: small app (two-sided payments marketplace prototype) on `main` + strategy/market-research documents on 10 unmerged `claude/*` branches | complete | PR/issue data from lead's pre-fetched JSON (gh unauthenticated); no real Stripe/Google run; research-branch facts not re-verified; earlier PRD drafts (v1–v7) and the uploaded "v0.40" source drafts are not in the repo

**DISCLOSURE.** No credentials found: `git grep` across all 14 refs for live/test Stripe keys, webhook secrets, AWS/GitHub/Resend tokens, and private keys found nothing. `.env.example` has placeholders only, and the CI/test secrets are dummy strings (`sk_test_ci`, `sk_test_stubbed`). The demo seed data is fictional (e.g., "Hartwell Fabrication, Toledo"). The research branches hold dossiers on about 517 real companies, built from public sources (TechCrunch, company docs, etc.). These dossiers are third-party but public, and they contain no personal data beyond named founders. **Ownership/disclosure ambiguous (flag for lead):** the founding-charter branches describe a venture with plural "founders". They state "Payment stays separate…; Bitcoin Computer, which we built, must win a written comparison" (`origin/claude/version-comparison-3cps2t@84a0810:docs/FOUNDING-THESIS-AND-VALIDATION-CHARTER.md`). That is company-strategy material and may involve other parties. I describe those branches only at a high level and do not attribute them to any organization. **Suitable to share after review:** `main` (code, PRDs, runbook) looks suitable. The charter, research and dossier branches should be held until the lead confirms ownership.

## 1 Identity
- A personal repository owned by NYCandrun. It is private (visibility only), not a fork, and was created 2026-07-07T01:08Z (`repos.json`).
- **Purpose (main):** "Compute Marketplace", formerly "Patient Compute". It is a high-latency marketplace for AI compute jobs. A buyer posts an AI task at a fixed price with a deadline of 12h–14 days. A vendor claims it first-come, and at that moment the platform charges the buyer's saved card through Stripe Connect and holds the money. The vendor delivers, the buyer accepts (or the review window auto-accepts), and the vendor is paid. Intended users are buyers who don't want to run batch infrastructure themselves, and vendors who want to profit from cheap or batch capacity (`docs/COMPUTE-MARKETPLACE-PRD-PHASED-PLAIN-ENGLISH.md` §1–2).
- **Type:** a working prototype app (Phases 1–2 of a 3-phase spec), plus strategy and research documents on side branches.
- **Stack:** Next.js 15 App Router/TypeScript, raw `pg` with hand-written SQL migrations, Auth.js v5 (Google, plus Resend magic links), Stripe Connect Express, Zod, Tailwind v4, Vitest against a real Postgres.
- **Maturity:** a polished, well-tested prototype. The README says it has "not met real Stripe yet". Pre-launch items are listed in `README.md` under "What's left before launch". Phase 3 (disputes, order book) is specified but not built.

## 2 Dates and attribution
- **First commit:** `3105bd1` 2026-07-06 21:08 -0400, "Initial commit" (a 1-line README, NYCandrun via GitHub web).
- **Latest commit on main:** `a270425` 2026-07-16. **Latest commit on any branch:** `c1f7e16` 2026-07-20 (`claude/dossier-searchable*`). `pushedAt` is 2026-07-30, which suggests a later push or branch operation that left no newer commits.
- **Author identities (all branches):** `NYCandrun <jacobnikolau767@gmail.com>` wrote 5 commits plus 5 PR merge commits (committer GitHub). `Claude <noreply@anthropic.com>` wrote all other commits. No other humans or bots appear.
- Every non-merge commit carries `Co-Authored-By: Claude Fable 5` (29) or `Claude Opus 4.8` (14), plus `Claude-Session:` URLs (10 distinct sessions). That includes the four NYCandrun-authored Phase 1 commits on 2026-07-07 (`16f93c7`, `b1444df`, `3475ce8`, `b660d77`).
- **Commits attributable to Jacob alone:** only `3105bd1` and the merges of PRs #1–#5 (2026-07-07 to 2026-07-08).
- **Jacob's documented direction elsewhere:** the PRDs list "Owner: Jacob". `84a0810` says "By founder instruction, remove all quantitative threshold tables…". `research/v2/09-how-we-did-this-research.md` on the jm8sor branch records "The pivot (your call): focus entirely on GitHub".
- **Activity periods:**
  - (a) 2026-07-07 to 07-08: code build. Intense; about 2 days, 23 commits.
  - (b) 2026-07-16: README handoff doc, then founding-charter iteration v0.50 → v0.55 within about 19 hours.
  - (c) 2026-07-17: market-research corpora.
  - (d) 2026-07-20: competitor dossiers.
  - The direction moved from building the product to validating the business. No commits after 07-20.

## 3 Branch and history coverage
- **Default branch:** `main`. There are 13 `claude/*` remote branches. All history is local; nothing was inaccessible apart from PR review threads (none appear to exist).
- **Merged:**
  - `claude/new-prototype-repo-5n2sjr` → PRs #1 (07-07 15:25Z) and #2 (07-07 22:13Z), both with empty bodies.
  - `claude/codebase-quality-review-9incd1` → PRs #3, #4, #5 (07-08). The bodies were agent-written and include test plans; #4 states "89/89" and the "Tailwind v4 token repair".
  - **Every PR was merged 6–13 seconds after it was opened** (from the PR JSON). The GitHub record shows no review comments or issues (issues JSON = `[]`).
- **Unmerged (`git log main..X`, `git diff --stat main...X`). All are docs-only; no code changes:**
  - `document-versions-comparison-8q1t21` (base `365bc8d`): `0fb2685`, `4d52cb0`. v0.40 comparison and charter v0.50 (+722 lines).
  - `document-versions-compare-nxecb5` (base `8055824`): charter v0.51 (+654).
  - `version-comparison-3cps2t`: v0.52 → v0.55 (4 commits; the canonical file ends at 370 lines).
  - `verified-work-market-research-jm8sor`: 6 commits, 31 files, a GitHub-only research corpus plus plain-English "V2" versions.
  - `read-confirm-p4dv89`: 3 commits, 37 files. A 12-workstream landscape study with a 477-entity CSV, red-team remediation, and an audit trail.
  - `opus-research-agreement-analysis-8qup3u`: a report reconciling five research corpora (383 lines).
  - `ignore-the-repo-60q7k9`: a 251-company dossier (3,804 lines). The branch name suggests the repo was used only as a workspace.
  - `full-dossier-517`: a 517-company dossier (7,924 lines).
  - `dossier-searchable` and `dossier-searchable-c3ajtf`: the same commit `c1f7e16` (no diff between them). 520 per-company files plus a CSV/JSONL index.
- The charter branches fork off each other's bases instead of building one linear history. This is consistent with several parallel sessions whose drafts were later merged by hand in v0.52 ("Merge the three competing v0.51 drafts").

## 4 Actual functionality
- **What I inspected:** the README (375 lines), both PRDs (828 and 327 lines), `RUNBOOK.md`, `src/lib/claims.ts` (666 lines; claim race and charge), `email.ts`, the migrations, the tests/stripe-stub, the CI workflow, and commit bodies on every branch.
- **What I ran, in a /tmp clone with no repo writes:**
  - `npm ci`, then `tsc --noEmit`: clean.
  - **`vitest run` against a local Postgres 18: 89/89 pass.** The first run used a database that defaulted to SQL_ASCII encoding and gave 88/89; the failure was `input_chars` code-point counting. This is an environment requirement, not a defect, since CI uses `postgres:16` with UTF-8. It is undocumented, though.
  - `npm run build` (production): succeeds.
  - `npm run demo`: boots with zero config. `GET /` returned 200. I fetched the feed with a vendor token, claimed a seeded job with its version (it went to `claimed`, version 2, mock charge), and **re-sent the same claim, which got `{"error":"job_changed"}`**. That confirms the optimistic version-check race end to end.
- **Implemented:**
  - Posting with client-supplied `group_id`/`chunk_index` idempotency.
  - A version-checked claim (`claims.ts:131` `where … status='open' and version=$3 and buyer_id <> $1`).
  - One PaymentIntent per buyer per claim action, taken under a session-level advisory lock, with the PI id recorded before confirm.
  - Webhook reconciliation, claim expiry with exact partial refunds, and auto-accept.
  - A new-vendor payout hold, dollar and concurrency caps, and two-strike suspension.
  - Scoped, hashed bearer tokens, plus `/api/cron/sweep`, which runs every runbook branch.
  - A `job_events` audit trigger, and a reference vendor bot and buyer client.
  - Demo mode with a mock Stripe, dashboards, and CI (typecheck + Postgres tests + build).
- **Not implemented or stubbed:**
  - Phase 3 rejection/disputes (the `rejected` status exists but nothing sets it).
  - The order book.
  - Real Stripe or 3DS testing.
  - `selectBackend` in `clients/vendor-bot/adapters.ts`, which the README itself calls dead code.
  - The vendor bot uses a `MockAdapter`; it does no real model calls.

## 5 How Jacob uses or builds with AI
This is **using AI agents to build**. The product has no runtime AI features; the "AI" is the commodity being traded. Direct evidence:
- **Spec-first delegation.** A long, decision-ID'd PRD with "Owner: Jacob". It is "Draft v8, consolidated" and replaces "two parallel revision lines (line A's v6; line B's v6 and v7)". The agent built against it, with code comments citing D/P IDs (`16f93c7` message: "Implements the Phase 1 build from docs/COMPUTE-MARKETPLACE-PRD-*"). How the PRD itself was authored isn't visible in the repo.
- **Structured verification loops, likely set up by the user but executed by agents:**
  - "adversarial spec review" → 25 findings fixed (`b660d77`)
  - "usability audit" → 17 (`3e55290`)
  - "adversarial QC wave" (`10a312e`)
  - "QC wave 2 … 40 confirmed findings, 0 refuted" (`c2e6050`)
  - "multi-agent audit against a 'billion dollar product' bar … 39 findings" (PR #5)
  - a red-team plus remediation step on the research (`d8e1c3d`)
  - an "adversarial loss audit" on condensing (`84a0810`)
  - The "confirmed / refuted" wording points to a find-then-verify pattern.
- **Multi-model comparison.** These are strongly inferred from document content:
  - Charter v0.40 drafts labelled CV1/CGPT/C2 are compared in `0fb2685` ("Four uploaded files").
  - Five research corpora are reconciled in `4519611` (labelled "VAWI, OKComputer, GPT Research, Plain-English v2, Landscape").
  - This suggests Jacob ran the same task across several tools or sessions and had an agent compare and adjudicate the results.
- **Human judgment calls:**
  - Instructing cuts to the charter ("By founder instruction").
  - The GitHub-only pivot when web access failed ("your call").
  - Requesting plain-language rewrites (v0.54 "readability audit"; research "V2 plain-English").
- **Limits of the evidence:**
  - PRs were merged within seconds with no review comments, so **no review-in-GitHub is visible**. Any review happened outside the repo, and I can't determine it.
  - The four NYCandrun-authored commits carry Claude co-author trailers, so they are not evidence of hand-written code.

## 6 Quality assessment
**Strong:**
- **Money-path design.** The core rule, "every state that holds captured money has an automatic exit", is documented and enforced.
- **Concrete Stripe edge-case fixes.** For example: `off_session` with `confirm=false` rejected (so no claim could ever charge before `b660d77`), and a 'processing' PI orphaning risk. This shows real failure-mode reasoning, not just generated boilerplate.
- **The test stub enforces real API rules.** In `b660d77` it "now enforces the real API rules that hid the off_session bug". That is a good lesson about test fidelity.
- **Real Postgres in tests and CI** instead of mocking the database.
- **An honest README.** It has a "Known rough edges" section that separates safe deletions from load-bearing code, and it admits a weak test (`tests/qc-fixes.test.ts:70-82` hand-copies production SQL).
- Confidence: high, from code reading plus test and demo runs.

**Weaknesses:**
- Copy-pasted cap formulas between enforcement and dashboard code (acknowledged in the README).
- Unused component variants and dead routes.
- No real-Stripe dress rehearsal.
- Undocumented UTF-8 database requirement.
- **An unacknowledged deviation from the spec:**
  - PRD D11 explicitly rejects a "Postgres trigger on the jobs table" for event capture.
  - Yet `50337c6` implements `job_events` "written by a database trigger".
  - The README calls the PRD authoritative ("Where the two disagree, the PRD wins").
- **A README contradiction:**
  - "What's left" lists a human delivery-notification email as not done.
  - But `src/lib/email.ts` `sendDeliveredNotice` is wired into `result/route.ts:96` (it only sends when `RESEND_API_KEY` is set).
- These are minor documentation drift, not functional defects. Confidence: high.

**Research branches:**
- Strong method: FACT/INFERENCE/FORECAST tagging, a saturation stop rule, and an audit trail that candidly records degraded workstreams. For example, "ws09 … executed zero live web searches" (`read-confirm-p4dv89:…/10-research-audit-trail.md` §1), and the red team was re-run after "agents hit session limit" (`e56bf12`).
- Weaknesses: much of the content is training-era or secondhand. Several overlapping corpora were never merged into `main`, and there is no evident final decision record. Confidence that they are self-consistent: medium. I verified none of their facts.

## 7 Developmental milestones (dates are 2026)
- 07-07 `16f93c7`: Phase 1 scaffold.
- `b1444df`: 34-test harness.
- `b660d77`: 25 spec-review fixes; 44 tests.
- `50337c6`: demo mode, audit trail, dark UI; 47 tests plus a Playwright pass.
- `4cf6385`: Headless V0; 61 tests.
- 07-08 `8b3fb3c`: Phase 2; 78 tests.
- `10a312e`: QC fixes (self-dealing, NUL crash).
- `caf84e6`–`d14e6f9`: design "Elevation" M1–M5 and a copy pass.
- `c2e6050`: QC wave 2.
- `48e1a8c`: CI; 89 tests.
- `5ce7ec3`/`480d3dd`/`1616f9a`: rebrand to a light theme, then a11y/brand audit fixes.
- 07-16 `8055824`: README rewritten as an architecture/handoff doc.
- 07-16 → 07-20: charter v0.50→v0.55, research corpora, dossiers.

## 8 Changes in working method and possible lessons
1. **Build → adversarial audit → batch fix.** This started 07-07, after the first build (`b1444df`) and continued with `b660d77`. It then repeated for usability, QC, UI and brand.
   - Trigger: none documented. Inferred lesson: agent output needs independent adversarial passes.
   - Evidence: explicitly documented as a practice, but its motivation is speculative. Alternative: it was planned from the start.
2. **Manual checks → CI.**
   - Earlier: gates verified "by hand" on every change (07-07/08).
   - Later: CI on 07-08 15:52.
   - Trigger, documented in `48e1a8c`: "The one recommendation from the original quality review that never got done", and the build gate "caught the dead Tailwind token layer" (`c2e6050`: Tailwind v4 bracket syntax had silently voided the design tokens).
   - Lesson: silent visual regressions need automated gates. Evidence: explicitly documented.
3. **Test stub made stricter after a hidden bug.** In `b660d77`, the stub was changed to reject invalid Stripe parameter pairs.
   - Trigger: the off_session bug passed the permissive stub. Evidence: explicitly documented.
4. **In-document revision notes → version history in git.** v0.51 had revision notes; `b5e23bf` removed one; `df91432` (v0.53) "version history now lives in git". Evidence: explicitly documented.
5. **Exhaustive charter → condensed prose.**
   - v0.52–0.53: threshold tables, owners, stop conditions.
   - v0.54: plain-language rewrite (160 findings).
   - v0.55: a 59% cut "by founder instruction".
   - Possible lesson: readability over bookkeeping for an outside audience. The doc says Part I is "for outside review". Evidence: documented change; the motivation is strongly inferred.
6. **Research: open web → GitHub-only after quota exhaustion and 403s.**
   - Recorded lessons: "one level of delegation only, with a budget per topic" and "verify environment claims first-hand" (jm8sor `research/v2/09-…`). Evidence: explicitly documented.
7. **Several parallel drafts/corpora, then agent adjudication** (v0.40 → v0.50; v0.51 ×3 → v0.52; the five-corpus report). Evidence: explicitly documented. The motivation (reducing single-model bias) is speculative.

## 9 Capabilities, limitations, uncertainties
- **Demonstrated:**
  - Writing a detailed build spec with explicit rejected alternatives.
  - Directing agents through phased implementation with recurring adversarial review.
  - Shipping a tested, runnable payments-marketplace prototype.
  - Iterating strategy documents through comparison and condensation.
  - Running multi-agent research with provenance tagging and candid failure accounting.
- **Uncertain:**
  - How much of the PRD Jacob wrote himself; earlier drafts are absent.
  - What review happened in the Claude sessions.
  - Why the research branches were never merged.

## 10 Evidence references and verification limits
- **Code:** `marketplace_prototype@a270425:src/lib/claims.ts` (L124–131, L171), `:src/lib/email.ts`, `:src/app/api/jobs/[id]/result/route.ts` L96, `:migrations/002_job_events.sql`, `:tests/stripe-stub.ts`, `:.github/workflows/ci.yml`.
- **Docs:** `:README.md` ("Known rough edges", "What's left before launch") and `:docs/COMPUTE-MARKETPLACE-PRD-JOBBOARD-TO-ORDERBOOK.md` §1 (D11, D21, D30).
- **Commits:** `16f93c7`, `b660d77`, `50337c6`, `4cf6385`, `8b3fb3c`, `10a312e`, `c2e6050`, `48e1a8c`, `5ce7ec3`, `8055824`, `0fb2685`, `17f9dc0`, `df91432`, `84a0810`, `e56bf12`, `d8e1c3d`, `4519611`, `c1f7e16`.
- **PRs:** #1–#5 (from `research/github/prs/marketplace_prototype.prs.json`). Issues: none.
- **Verification limits:**
  - gh CLI unauthenticated (I used the lead's JSON instead).
  - No real Stripe, Google OAuth or Resend calls.
  - UI not visually inspected in a browser.
  - Research facts not re-verified.
  - Session URLs in trailers not opened.
