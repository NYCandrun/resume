MANIFEST | prototype_Jules | PRIVATE | small app (Phase 1 marketplace prototype) + product spec; agent-delegation experiment | complete | Jules task prompts/sessions not visible (only PR bodies/commits); PRD drafting history pre-dates repo (only the documented changelog inside the PRD); no live Postgres/Stripe run

DISCLOSURE: No real credentials found. `.env.example` (added in `d96127f`) holds only placeholders (`sk_test_...`, `your_auth_secret`). No third-party or customer data; no employer-looking material. The PRDs name "Owner: Jacob" and the commits carry a personal email (`jacobnikolau767@gmail.com`) on the merge commits. Content is the owner's own product concept. It looks suitable to share after review. Before sharing, note that the default branch is a `jules-*` branch and that 25 bot PRs are still open.

# prototype_Jules: report

## 1. Identity
- **Context:** Personal repo `NYCandrun/prototype_Jules`. Private. Not a fork. Created 2026-07-07T04:29Z; last push 2026-07-20 (repos.json). The default branch is `jules-compute-marketplace-init-8268856299554605176`. No `main` exists.
- **Purpose:** Phase 1 of a "High-Latency Compute Job Marketplace". Buyers post AI jobs at a fixed price with a deadline of at least 12h. Vendors who hold cheap batch, off-peak or spare model capacity claim jobs, and the first claim wins. Stripe Connect charges the buyer when a job is claimed and pays the vendor when the buyer accepts. The aim is to test whether buyers will pay a premium over raw batch-API cost (`COMPUTE-MARKETPLACE-PRD-PHASED-PLAIN-ENGLISH.md` §1–2).
- **Type:** Small full-stack app prototype built from a detailed spec. It is also an experiment in delegating to Google's Jules coding agent (the repo name, and every commit is by the Jules bot).
- **Technologies:** Next.js 16.2.10 App Router (the README says "Next.js 14", which is wrong), React 19, TypeScript, Tailwind 4, `pg` with raw SQL migrations, NextAuth v5 (Google), Stripe Connect (SetupIntents, unconfirmed PaymentIntents, webhooks, transfers), zod, jest/ts-jest.
- **Maturity:** Early prototype. The code compiles and builds. It has never been run against a real database or Stripe in any evidence I saw. Phase 2 sits unmerged in PR #1.

## 2. Dates and attributable contributions
- **First commit:** `f912077`, 2026-07-07 05:33Z. **Latest across all branches:** `512b118`, 2026-07-20 13:07Z (branch `jules-4261477942089108757-89318dae`). The latest commit on the default branch is merge `572ca2d`, 2026-07-08 19:29Z.
- **Authors and committers:**
  - `google-labs-jules[bot]` authored and committed every non-merge commit (33 commits across branches).
  - `NYCandrun` <jacobnikolau767@gmail.com> authored the 4 merge commits (PRs #3–#6, 2026-07-08 19:28–19:29Z, committer GitHub).
  - Every bot commit carries `Co-authored-by: NYCandrun <196604778+...>`. This is Jules's standard attribution to the user who started the task, not proof that Jacob wrote that code.
- **Jacob's attributable contributions:**
  - He started every Jules task. Each PR body ends "PR created automatically by Jules for task … started by @NYCandrun".
  - He made the four merges on 2026-07-08.
  - He owns the PRD. Both docs say "Owner: Jacob" and arrived fully formed as "Draft v8" in the first commit. Who typed the PRD text, and whether AI helped draft it, cannot be determined from this repo.
  - No commits written by hand are present.
- **Activity periods:**
  - 07-07: scaffold, Phase 1 build and fix pass.
  - 07-08 18:09–19:43Z: Phase 2 PR, then about 20 maintenance PRs within roughly 35 minutes.
  - 07-09 to 07-20: one PR per day, mostly around 12:1x–12:3x UTC. That regular pattern strongly suggests scheduled or recurring Jules tasks, but this is inference.
  - Nothing after 07-20. No imported history and no squashes beyond the PR merges.

## 3. Branch and history coverage
There are 31 remote branches (all fetched) and 29 PRs (all read via `gh` and the lead's `prs/prototype_Jules.prs.json`). There are 0 issues, 0 review comments and 0 reviews. The only comment on each PR is Jules's "reporting for duty" boilerplate.

**Merged (4), all on 07-08 within 55 seconds:**
- #3: remove webhook console.logs
- #4: jest tests for POST /api/jobs
- #5: bound `limit`/`offset` on `/api/jobs/mine`
- #6: split the POST handler into helpers

**Open and unmerged (25).** Substantial work and real defect fixes were never merged:
- **#1 Phase 2 endpoints.** `phase-2-endpoints-…`, +787/−16 across 13 files: cron auto-accept and sweep, price edit, cancel, resume, token management, vendor onboard routes, magic-link auth. Never merged.
- **Duplicate fixes for the same real bug.** On payment failure the code leaves `claimed_by` set, so the failed claimer keeps full-payload access (`src/app/api/jobs/[id]/route.ts:61`). The fix was proposed three times: #7 (07-08), #24 (07-09, adds a test), #29 (07-20). None was merged. The default branch's webhook (`src/app/api/stripe/webhook/route.ts`) still has the bug.
- **Duplicate vendor claim-limit race fixes.** #8 and #19 (07-08) both add `pg_advisory_xact_lock` per vendor. Neither was merged. The default branch locks only on the buyer, so concurrent claims by one vendor against different buyers can exceed `claim_limit_cents`.
- **Four overlapping N+1 bulk-insert rewrites.** #15 (multi-row VALUES), #22, #25 and #26 (`unnest`). These are 07-08 to 07-15, all open, and they conflict with each other.
- **Pagination.** #27 and #28 cover GET /api/jobs (07-18, 07-19). This duplicates the intent of merged #5 but for a different route.
- **Tests and cleanup:** #10–#14, #16–#18, #21 (tests); #2 (duplicate of merged #3); #9; #20; #23.
- Several test branches show diffs of 6–11k lines, mostly `package-lock.json` churn from adding test dependencies.

**Inaccessible:** Jules task conversations (`jules.google.com/task/<id>`), so the actual task prompts cannot be seen. Also the earlier PRD drafts (v1–v7), which are described only inside the PRD's §15.

## 4. Actual functionality (inspected and executed)
**What I ran** (on a throwaway clone in /tmp, offline after `npm ci --ignore-scripts`):
- `npx jest`: 1 suite, 3/3 pass. These are mocked-DB insert tests.
- `npx tsc --noEmit`: clean.
- `next build`: succeeds and lists 20 routes.
- There is no `test` script in `package.json`.
- Not run: anything needing Postgres, Google OAuth or Stripe.

**Implemented on the default branch, read in code:**
- **Schema.** Migrations 001, 002 and 003 (`src/db/migrations/`) mirror the PRD.
- **Job posting** (`src/app/api/jobs/route.ts`):
  - single jobs and groups with `chunk_index`, where retries are de-duplicated by skipping unique-constraint violations
  - deadline floor and ceiling validation
  - a buyer exposure cap
  - an excerpt-only open feed of 200 chars (the PRD proposes 500)
- **Claim** (`[id]/claim/route.ts`) and **claim-batch:**
  - bearer token stored as a sha256 hash with vendor scope and expiry/revocation checks
  - buyer advisory lock, `FOR UPDATE`, and a version-checked UPDATE
  - an unconfirmed PaymentIntent created inside the transaction, cancelled if the claim race is lost, and confirmed `off_session` after commit
  - this follows PRD D21 (one charge per claim action)
- **Webhook.** Handles `payment_intent.succeeded` and `payment_failed`. A second failure suspends the job (D28). The PRD specifies four webhooks and only two are handled.
- **Accept** (`[id]/accept/route.ts`):
  - session-only, as D29 requires
  - transfers with `source_transaction`
  - a new-vendor hold for vendors with fewer than 10 accepted jobs. Held payouts are never transferred later on this branch; the release would need the Phase 2 cron.
- **Other:**
  - result delivery
  - pages for posting with Stripe Elements, buyer dashboard, job detail, vendor feed, operator-only vendor onboarding, accept-terms, ToS and vendor agreement
  - `scripts/mint-token.ts` for operator-issued tokens
  - `src/lib/pricing.ts`: a cost-floor pure function with hand-set model price constants (D15)

**Planned or stubbed only:**
- claim expiry with refund (P1-15/D30; on this branch it exists only as the PRD runbook)
- all of Phase 2 (in PR #1)
- Phase 3 event log and order book
- Appendix A reference vendor bot and buyer client
- Appendix B local validation harness

## 5. How Jacob works with AI
The direct evidence is bot authorship, Jules PR footers, task IDs and branch names.
- **Using AI to build.** He did not build an AI product inside this repo; the marketplace sells AI work but contains no model calls.
- **Spec-driven delegation.** The first commit includes about 1,150 lines of PRD: decision table D1–D31, exact schemas, state machine and build order. Jules's commit messages cite PRD IDs (D21, D24, D28, D29), and the code comments quote them. The PRD was clearly the main tool for steering the agent. Evidence: strong.
- **Agent context file.** `AGENTS.md` (with `CLAUDE.md` → `@AGENTS.md`) is the stock create-next-app agent block ("This is NOT the Next.js you know…"). It is template text, not a custom instruction.
- **Iteration within the build.** `d96127f`, "Fix Phase 1 … implementation issues", lists concrete corrections:
  - SetupIntent not persisting the payment method
  - `off_session` moved to confirm
  - Stripe build-time fallback
  - removal of synchronous mock interfaces from PRD Appendix A
  
  This reads as a reviewed second pass, but who found the issues is not recorded. Evidence: moderate.
- **The agent edited the spec.** `55b3396` and `322e0fe` changed the PRD (batch adapter lifecycle, token-drift notes) inside code commits. The PRD stayed the source of truth while the agent also wrote to it.
- **Review and verification were thin.** There are no review comments on any PR. Four PRs were merged in under a minute. 25 agent PRs, many duplicates, piled up unmerged. Real security and correctness fixes (#7/#24/#29, #8/#19) were proposed repeatedly and never merged. This shows high-volume agent output without triage. It does not show Jacob correcting agent output inside the repo.

## 6. Quality assessment
**Strong:**
- **The PRD itself.** For each decision it states the choice, the rejected alternatives and the rationale, plus a non-goals list, a "deliberately not building" list, exit criteria, a money-exit invariant and fee arithmetic (D21's 30-cent fee reasoning).
- **The money paths** follow the spec carefully: version-checked claims, Stripe calls placed outside the DB commit, session-only accept, hashed scoped tokens.
- The code builds and type-checks. Confidence: high for these points.

**Weaknesses and defects:**
- **Stale-claimer data exposure.** Still present on the default branch, despite three fix PRs.
- **Vendor claim-limit race.** Unfixed on the default branch.
- **Payout holds with no release path.**
- **Webhook coverage.** Two of the four specified events are handled.
- **Spec drift.** The excerpt is 200 chars against the PRD's 500, and the README says Next 14.
- **Testing.** Three mocked tests, no test script, no integration or "lose-a-race" test (which the PRD's build order requires).
- **Stripe call inside a held transaction.** The PaymentIntent is created while DB locks are held, which adds latency under contention. This is probably acceptable for a prototype.

**Intentional shortcuts vs defects:** The manual runbook for claim expiry is an intentional Phase 1 shortcut per the PRD. The unmerged security fixes are defects.

**Overall:** A well-specified prototype that agents largely implemented, with an unfinished integration and triage loop. Confidence: medium-high.

## 7. Developmental milestones
1. 07-07 05:33: scaffold, migrations and PRD v8 (`f912077`).
2. 07-07 07:49: Phase 1 routes and pages (`322e0fe`, +1,321 lines).
3. 07-07 16:53: fix pass, buyer and vendor pages, pricing, mint-token (`d96127f`).
4. 07-08 18:09: Phase 2 PR #1 (unmerged).
5. 07-08 19:25–19:43: burst of about 20 categorized Jules PRs; 4 merged.
6. 07-09 to 07-20: about one PR per day, unmerged; then activity stops.

## 8. Changes in working method and possible lessons
- **The PRD's evolution before the repo, v1 to v8.** Explicitly documented in PRD §15.
  - Earlier approach: a two-phase job board then order book, with an in-app dispute flow, per-chunk charging and one revision line.
  - Later approach: three gated phases; email disputes; charge aggregation, because the "30-cent fixed fee … a third of small-chunk volume" was a named flaw; a fork into lines A and B "each responding to a different critique", then a v8 consolidation "from the comparative review".
  - Lesson the document itself states: every change is "traceable to a named flaw", and v7's 12h batch-window claim was "arithmetically wrong".
  - Evidence: explicitly documented. The dates and the identity of the critics or reviewers (human or AI) are not recorded, so whether AI took part cannot be determined.
- **Inside the repo: from one large spec-driven build task (07-07) to many small categorized agent tasks (07-08 onward).** The emoji categories 🧹, 🔒, ⚡ and 🧪 follow Jules's suggested-task style.
  - Possible trigger: wanting to harden the Phase 1 code.
  - Result: duplicated, conflicting PRs that were mostly not merged.
  - Inferred lesson: unclear. The repo shows no response, such as closing duplicates or merging fixes.
  - Evidence: strongly inferred for the shift itself; speculative for intent.
  - Alternative explanation: the user switched to other repos and let the scheduled tasks run on.
- **No dated versions of agent instructions exist.** `AGENTS.md` is unchanged boilerplate, so prompt evolution cannot be reconstructed.

## 9. Demonstrated capabilities, limitations, uncertainties
**Demonstrated:**
- writing detailed product and technical specs: payments, concurrency, unit economics, phase gating, non-goals
- using such a spec to drive an autonomous coding agent to a building Phase 1 app
- running agent tasks in parallel or on a schedule

**Uncertain:**
- how the PRD was authored (by hand or with AI assistance)
- the content of the Jules task prompts
- whether the 07-07 fix pass reflects Jacob's own testing

## 10. Evidence references and verification limits
- **Spec:** `prototype_Jules@f912077:COMPUTE-MARKETPLACE-PRD-PHASED-PLAIN-ENGLISH.md`, `…-JOBBOARD-TO-ORDERBOOK.md` (§1 decisions, §14 build order, §15 changelog, Appendices A and B). PRD edits: `@55b3396`, `@d96127f`.
- **Code:** `@572ca2d:src/app/api/jobs/[id]/claim/route.ts`, `src/app/api/jobs/claim-batch/route.ts`, `src/app/api/stripe/webhook/route.ts`, `src/app/api/jobs/[id]/accept/route.ts`, `src/app/api/jobs/route.ts`, `src/app/api/jobs/[id]/route.ts:61`, `src/lib/pricing.ts`, `scripts/mint-token.ts`, `src/db/migrations/00{1,2,3}_*.sql`, `AGENTS.md`, `CLAUDE.md`, `.env.example`.
- **Branches and PRs:**
  - `origin/phase-2-endpoints-16042141057267710755` (`cf95c7b`, PR #1)
  - claimed_by fixes: `9d2bb02` (#7), `6205006` (#24), `512b118` (#29)
  - vendor lock: `92f33f8` (#8), `a83e904` (#19)
  - bulk insert: `01ca192` (#15), `1be4432` (#22), `c01c209` (#25), `04136b2` (#26)
  - pagination: `3ea8b22` (#27), `03ed7a7` (#28)
  - merges: `9d128e2`, `e8959aa`, `3a449dc`, `572ca2d`
- **Verification limits:**
  - jest, tsc and next build were run offline on the default branch only. Open-PR branches were inspected by diff only.
  - No DB or Stripe runtime.
  - Jules task logs are not accessible.
  - PR data came from `gh` and from `research/github/prs/prototype_Jules.prs.json` (29 PRs). There are 0 issues.
