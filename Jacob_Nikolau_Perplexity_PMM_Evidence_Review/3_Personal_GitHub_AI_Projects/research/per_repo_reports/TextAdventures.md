MANIFEST | TextAdventures | PRIVATE | mixed: product spec + iOS app (SwiftUI) + LLM content pipeline + Cloudflare Worker + 3 games | complete | Swift/iOS not built or run (no Xcode in sandbox); OpenRouter/Apple/Cloudflare paths not executed; no PRs/issues exist; single-session history (~87 min)

DISCLOSURE: No credentials found. Secrets are referenced only by name (`OPENROUTER_API_KEY`, `APPLE_SHARED_SECRET`, `COMPILE_MODEL`) in `.github/workflows/compile-games.yml` and `worker/wrangler.toml`. KV IDs and the worker URL are placeholders (`REPLACE_WITH_…`, `textadventures-worker.example.workers.dev`). There is no third-party personal data. The only personal data is the author email in commit metadata. Nothing looks employer-owned. Third-party material: `data/vocab.json` is derived from the Inform 6 standard library 6.12.8 (Artistic License 2.0), with attribution in `data/vocab-notes.md`. Code comments mention a "LiquidZork" web prototype (8 references, for example "_template.html line 586"); this looks like reuse of the user's own pattern, but I did not check it because the brief limits evidence to this repo. The repo looks suitable to share after review, but the README overstates the build status (see §6), and that should be fixed or explained first.

# TextAdventures — repository report

## 1. Identity
- Personal project on the NYCandrun account. Visibility is PRIVATE. Not a fork. Created 2026-06-15T04:08:38Z; last push 2026-06-15T05:35:35Z (`repos.json`).
- Description: "Native iOS messenger-UI app for publishing interactive text adventures. JSON game format, Inform 6 parser, LLM coach."
- Type: mixed product prototype. It includes (a) a product spec (README), (b) a JSON game format with a JSON Schema and docs, (c) an LLM "compiler" that turns author markdown briefs into game JSON, plus static playtest and GitHub Action scripts, (d) a SwiftUI iOS app (interpreter, parser, chat UI, StoreKit, Game Center, AI coach), (e) a Cloudflare Worker (LLM proxy, Apple receipt check, catalog cache), and (f) three launch games.
- Intended user: iPhone players who get a free parser game with an optional paid AI tier, and authors who write games in plain-English markdown.
- Maturity: a broad first-pass prototype that has never been deployed. Several layers do not yet work together (§6).

## 2. Dates and attributable contributions
- All branches: first commit `1034a02` on 2026-06-15 04:08:39 UTC ("Initial commit", author NYCandrun, committer GitHub, made by the web UI with LICENSE and .gitignore). Latest commit `64d955a` at 05:35:33 UTC the same day.
- Identities: `NYCandrun <jacobnikolau767@gmail.com>` (1 commit) and `Jacob Nikolau <jacobnikolau767@gmail.com>` (5 commits). Both use the same email, so all commits are attributable to Jacob. There are no bot authors and no other contributors.
- Jacob's contributions run from 04:08 to 05:35 UTC on 2026-06-15, all in one session:
  - 04:09 spec (`1bf6603`)
  - 05:22 bulk build (`4cc5000`, 77 files, +17,070 lines)
  - 05:33 AI-features branch (`06c0100`) and merge (`0a6b51b`)
  - 05:35 README status correction (`64d955a`)
- There were no pauses and no later activity. The history is not inherited or imported, and nothing looks squashed. The 17k-line initial commit means the build process inside that hour cannot be reconstructed.

## 3. Branch and history coverage
- Default branch is `main` = `64d955a`. Remote branches are `origin/main` and `origin/feature/ai-features-pass` (= `06c0100`).
- `git log main..origin/feature/ai-features-pass` is empty: the branch is fully merged. The merge `0a6b51b` has parents `4cc5000` and `06c0100`, so it was a non-fast-forward merge even though main had not moved. The branch changed 5 files (+364/−15): `AICoachService.swift`, `ChipRow.swift`, `MapSheet.swift` (new), `ThreadView.swift`, and `README.md`.
- There is no unmerged work and no abandoned branches.
- `gh pr list` and `gh issue list` (state all) both returned nothing.
- All history was accessible, and no large blobs were missing.

## 4. What it actually does
I inspected all of the top-level areas and read the main code paths. I ran only the offline scripts and tests below.

**Content pipeline**
- `prompts/compile-markdown.md` (535 lines) is a system prompt that asks for raw JSON. It contains:
  - a compact schema reference;
  - 15 validation rules to enforce before output;
  - 7 mechanic patterns (key/door, container, dark room/light source, NPC give, multiple endings, scoring, Echo Chamber `on_any_command`);
  - `__compile_error` and `__author_note` escape hatches;
  - a rule not to invent content.
- `scripts/compile.py` posts to OpenRouter (`temperature` 0.2) and strips code fences if present. It checks that the output is valid JSON. If the model returns `__compile_error`, the script prints it but still writes the file and exits 0. The workflow's next step catches it.
- `.github/workflows/compile-games.yml` triggers on PRs that touch `submissions/**`. It compiles, checks for `__compile_error`, runs `check-jsonschema`, runs `playtest.py`, updates the manifest, and auto-commits. This repo has no `submissions/` directory, so the workflow is meant for the separate `TextAdventures-Content` repo. I did not run it.
- `scripts/playtest.py` is a static checker:
  - BFS reachability, both with default flags and ignoring blockers;
  - reference integrity checks;
  - win-condition satisfiability.

  The README describes "an automated 50-turn playtest with a simple AI player." No AI player exists; the checker is purely static.

**Executed and verified**
- JSON Schema (draft 2020-12, using pip `jsonschema` in the sandbox): all three launch games and `examples/example-game.json` are valid.
- `playtest.py`:
  - locked-garden: passes.
  - echo-chamber: passes.
  - example-game: passes.
  - **concierge: FAILS (exit 1)** with "Structural disconnect: … unreachable even ignoring all blockers: ['room-13']". I confirmed this by hand:
    - The elevator's exits are only w/u/d. No exit and no `move_player` leads to `room-13`.
    - The `photograph` item exists only in `room-13`.
    - The "Truth" ending and the roof route's `blocked_message` both depend on the photograph.

    So that game's main ending path cannot be completed as shipped. The elevator's dynamic description even says "You can now go to floor 13," but no exit is defined. This contradicts the `4cc5000` commit message, which says "All three launch games validate against the schema and pass playtest."
- Bundled games under `ios/.../bundled-games/` are byte-identical to `content/launch/*/game.json`, so the iOS copy has the same defect.
- Worker tests: I copied `worker/` to `/tmp`, installed vitest 1.6.0, and ran the suite: **18/18 tests pass.** The tests use mocked fetch and KV. They cover receipt caching, the sandbox fallback on Apple status 21007, the model allowlist, rate limits, CORS, and 404 handling.

**Worker** (`worker/worker.js`, 617 lines)
- Routes: `/health`, `/catalog` (5-minute KV cache), `/llm`, and `/validate-receipt` (legacy `verifyReceipt`, with sandbox fallback).
- `/llm` expects the header `X-Receipt-Token` and a body of `{task: hint|translate|coach, game_context, user_input, level}`. It builds the system prompts server-side. The default model is `liquid/lfm-7b`, with an allowlist that includes anthropic/claude models.

**iOS app** (39 Swift files, about 6,960 lines; 56 XCTest functions across Parser, Interpreter, and ActionDSL tests)
- Four tabs, a JSON interpreter (`Engine/Interpreter.swift`, 796 lines), a parser using reduced vocabulary (`Resources/vocab.json`, 80 lines, against 98 verbs in `data/vocab.json`), StoreKit 2, Game Center, and a catalog fetched from `raw.githubusercontent.com/NYCandrun/TextAdventures-Content/main/manifest.json`.
- `AICoachService` builds a WORLD DATA ground-truth block from the current room's exits, items, and flags. Each system prompt repeats the line "Never invent items, rooms, or exits…".
- I did not compile or run the app, because there is no Swift or Xcode toolchain in the sandbox.

**Implemented vs claimed**
- Hint, translate, coach, examine, and map have their own prompts.
- "Describe" and "Recap" are listed as separate features in the README (`ThreadView.swift:136–216`), but in code both simply call `hint(level: .vague)` and `hint(level: .normal)` under new labels.
- Still pending (README): app icon, `.storekit` file, worker deploy, multiplayer.

## 5. How Jacob uses or builds with AI
- **Building AI-powered products: directly evidenced.** AI shows up in two product roles:
  - an LLM used as a build-time compiler, with a validator chain after it (schema check, then static playtest, then human PR review);
  - an LLM used at runtime as a grounded coach, kept in line by a ground-truth block assembled on the client.

  Key decisions:
  - deterministic engine first, with AI only as a paid add-on;
  - one JSON format that serves both the engine and as LLM context;
  - explicit anti-hallucination prompting;
  - a model allowlist and rate limits on the proxy;
  - `__compile_error` / `__author_note` channels so the compiler can refuse or flag assumptions instead of guessing quietly.
- **Using AI to write this code: not directly evidenced.** There are no Co-authored-by or "Generated with" trailers, no agent instruction files, no agent branch names, and no PRs. Per the brief, I am not inferring authorship from the size or speed of `4cc5000`.
- **Verification behaviour:**
  - The repo includes static checks and unit tests, and the worker tests do pass.
  - `64d955a` ("Update README build status to reflect actual repo state") shows an attempt to reconcile the docs with reality. It added notes, listed the remaining gaps, and moved Game Center to done. However, it did not catch these mismatches.

## 6. Quality assessment
**Strengths** (confidence: high)
- Clear, coherent product thesis and architecture: messenger UI, free deterministic parser, paid grounded AI.
- A careful, well-specified schema and compiler prompt, with validation rules, patterns, and error channels.
- Thoughtful Echo Chamber mechanic (cooldown, `first_match` escalation).
- Correct Inform 6 provenance and licence notes.
- The worker is well organised, with tests that pass.
- The static playtest checker is useful: it actually finds a real bug in the repo's own content.

**Defects and integration gaps**
1. **Client and worker API contracts do not match** (high confidence, from reading the code):
   - iOS POSTs `{system, user, receiptToken, model}` in the body, with no `X-Receipt-Token` header (`AICoachService.swift:19–24, 423–447`).
   - The worker requires that header and a `{task, game_context,…}` body (`worker.js:373–400`).

   Every AI call would therefore return 401. The ownership of prompts also conflicts: iOS assembles system prompts itself, while the worker ignores them and builds its own. The README's "generic passthrough" claim describes neither side.
2. **Receipt semantics do not match** (high confidence): the client sends a StoreKit 2 `transaction.id` (`SubscriptionService.swift:116–124`), while the worker validates legacy base64 receipts through `verifyReceipt`.
3. **`MapSheet.swift` is missing from `project.pbxproj`** (strongly inferred; not built): it was added in `06c0100`, but the project file was never updated (objectVersion 56, explicit file references, 0 matches). The project likely would not compile, because `ThreadView` uses `MapSheet`.
4. **The concierge game cannot be completed** through its main ending (verified by running the playtest).
5. **The catalog URL points at a private repo's raw URL**, which an unauthenticated app cannot fetch (high confidence). The worker's `/catalog` endpoint exists, but iOS does not use it.
7. `compile.py` exits 0 on `__compile_error` (minor; the workflow catches it).

**Intentional shortcuts** (acceptable for this stage): placeholder URL and KV IDs, a placeholder icon, and multiplayer deferred.

**Overall:** strong on design and specification. The individual components are plausible (the worker and checker are verified to work). The end-to-end integration is unverified, and in places demonstrably broken.

## 7. Developmental milestones (all on 2026-06-15 UTC)
| Time | Commit | Milestone |
|---|---|---|
| 04:08 | `1034a02` | Repo created |
| 04:09 | `1bf6603` | One-page product spec (README, 171 lines); most components marked "in progress/next" |
| 05:22 | `4cc5000` | Full build: schema, vocab, compiler prompt and scripts, Action, worker and tests, iOS app and tests, three games |
| 05:33 | `06c0100` | Branch `feature/ai-features-pass`: Examine and Map AI features plus MapSheet |
| 05:33 | `0a6b51b` | Branch merged |
| 05:35 | `64d955a` | README build status revised "to reflect actual repo state" |

## 8. Changes in working method and possible lessons
There is only one session, so the method can be reconstructed only partly.
- **Spec first, then build.** At 04:09 the README was a plan with status markers (🔨 / ⏳). By 05:22 the build matched almost every section of the spec. This suggests a document-first decomposition. Evidence: explicitly documented by the README diffs.
- **Feature-branch pass for an add-on.** The AI features were developed on a named branch and merged with `--no-ff`. This possibly reflects a deliberate wish to isolate a scoped feature pass. Evidence: strongly inferred from the history. Alternative explanation: habit or tooling default.
- **Status correction.** `64d955a`'s message says it corrects the README to the "actual repo state." It added a Notes column with file locations and explicit lists of gaps. Possible trigger: the status table in `06c0100` was coarse and still showed Game Center as "next." Possible lesson: tie status claims to concrete artifacts. Evidence: explicitly documented. However, the correction did not include running the playtest or checking the client/worker contract, so the lesson was only partly applied. Alternative explanation: tidying up the docs only.
- **Prompt evolution.** There are no earlier versions of the compiler or coach prompts; each exists in one version only. Their history cannot be reconstructed.

## 9. Capabilities, limitations, uncertainties
**Demonstrated in this repo**
- Product framing.
- Data-format and schema design.
- Prompt design for grounded and structured LLM output.
- Designing an LLM-plus-validator pipeline.
- Serverless proxy design with tests.
- Breadth across Swift, JS, and Python.

- A working end-to-end integration of the app, worker, and catalog.
- A deployed service.
- An actual LLM compile run or its outputs.
- An executed iOS build or test run.
- Any evaluation of the coach's grounding quality.
- Iteration in response to user or playtest feedback.

**Uncertainties**
- Whether `MapSheet` would break the build depends on Xcode, which I could not run.
- How the code was authored (AI-assisted or not) is unknown from direct evidence.
- The relationship to the "LiquidZork" prototype is known by name only.

## 10. Evidence references and verification limits
- Commits: `TextAdventures@1034a02`, `@1bf6603`, `@4cc5000`, `@06c0100`, `@0a6b51b`, `@64d955a`. Branches: `main`, `origin/feature/ai-features-pass`. PRs and issues: none.
- Key files (at `@64d955a`):
  - `README.md`
  - `prompts/compile-markdown.md`
  - `schema/game.schema.json`
  - `docs/game-schema.md`
  - `docs/author-template.md`
  - `scripts/{compile,playtest,update_manifest}.py`
  - `.github/workflows/compile-games.yml`
  - `worker/worker.js:373–486`
  - `worker/test/worker.test.js`
  - `worker/wrangler.toml`
  - `ios/TextAdventures/Services/AICoachService.swift:19–58, 340–470`
  - `ios/TextAdventures/Services/SubscriptionService.swift:116–124`
  - `ios/TextAdventures/Services/CatalogService.swift:15`
  - `ios/TextAdventures/Views/Threads/ThreadView.swift:136–216`
  - `ios/TextAdventures.xcodeproj/project.pbxproj` (no MapSheet)
  - `content/launch/concierge/game.json` (room-13, photograph)
  - `data/vocab-notes.md`
- Executed:
  - `playtest.py` on 4 games (3 pass, concierge fails);
  - jsonschema validation (4/4 valid);
  - worker vitest in a `/tmp` copy (18/18 pass);
  - byte comparison of bundled and launch games (identical).
- Not executed: the Swift build and tests, `compile.py` and the GitHub Action (they need a paid API key), and the live worker, Apple, and OpenRouter calls.
