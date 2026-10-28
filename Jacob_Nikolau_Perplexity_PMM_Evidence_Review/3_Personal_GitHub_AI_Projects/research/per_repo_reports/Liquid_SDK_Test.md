MANIFEST | Liquid_SDK_Test | public | small app / AI-powered game demo (mixed with imported archival source) | complete | No agent transcripts or AI-attribution trailers; LLM features not executed (would need paid OpenRouter key); no browser available, so UI checked only by code reading plus a headless Node run of the game engine

DISCLOSURE: No credentials found. The only key-related strings are an `sk-or-v1-…` input placeholder and `Authorization: Bearer ' + key` code (`web/_template.html:142,531`); the user's key is read from `localStorage`. Third-party material: (a) `zork1.z5` (root and `web/`) and its base64 copy embedded in `index.html`/`web/index.html`/`web/zork-chat.html` is the commercial Infocom Zork I Release 88 story file (the banner prints "Copyright (c) 1981, 1982, 1983 Infocom"). `web/README.md` says this openly and notes that a clean-room build would compile from the MIT-licensed ZIL source. In a **public** repo this is a licensing/redistribution question to check before sharing more widely. (b) `zork-src/` is an import of the MIT DDC 1977 Zork MDL source, with its own LICENSE.md/codemeta.json. (c) `web/jszm.js` is the public-domain JSZM interpreter by zzo38. Personal data: the author email appears in commit metadata (normal). Nothing in the repo looks employer-owned. "Liquid" refers to Liquid AI's LFM models as a third-party API vendor reached through OpenRouter. There is no proprietary SDK, internal data or customer data. Suitable to share after review, with the story-file licensing caveat.

# Liquid_SDK_Test (app name: "LiquidZork")

## 1. Identity
- Personal repo, owner NYCandrun, **public**, not a fork, default branch `main`. Created 2026-06-12T06:22Z, last pushed 2026-06-15T03:51Z (repos.json). GitHub description is empty, and the root `README.md` contains only the title `# Liquid_SDK_Test`.
- **Purpose** (`web/README.md`): a single-file, mobile-first web app that plays Zork I in a chat-style UI ("styled to match the Computer iOS UI", per the commit message of `56e8d6e`). It adds optional LLM features (hint, vague hint, spoiler hint, describe, recap, inventory and examine flavor) that call Liquid AI LFM models through OpenRouter with the user's own key. The intended user is a player on an iPhone, via Safari "Add to Home Screen".
- **Type:** small AI-powered game demo / experiment. Despite the repo name, no "SDK" is used. Calls go straight to the OpenRouter REST endpoint.
- **Maturity:** working v0 prototype ("v0 ready for Pages"), with three small iterations after it. There are no tests, no CI and no docs beyond `web/README.md`.

## 2. Dates and attribution
- First commit: `a7dced5` "Initial commit", 2026-06-12 06:22:15Z (author NYCandrun, committer GitHub, i.e. made in the web UI).
- Latest commit: `10b1689` merge, 2026-06-15 03:51:54Z. The same holds across all branches, since every branch is merged into `main`.
- Authors/committers: `NYCandrun <jacobnikolau767@gmail.com>` (1 commit), `Jacob Nikolau <jacobnikolau767@gmail.com>` (11 commits), and `GitHub` (committer of the initial commit only). No bots, no `Co-authored-by`, no "Generated with" trailers.
- **Jacob's attributable contributions:** all 12 commits, from 2026-06-12 06:22Z to 2026-06-15 03:51Z.
- **Activity periods:**
  - Jun 12, 06:22–07:00Z: initial commit, source import and v0, all within about 40 minutes.
  - Jun 14, 03:22–03:25Z: Pages entry point and the 10-turn context change.
  - Jun 14, 06:42–06:44Z: world-data grounding and the root `index.html`.
  - Jun 15, 03:51Z: autocorrect.
  - Nothing after that. The repo looks finished as a short experiment, not stalled mid-feature.
- **Inherited history:** `489e764` imports the MITDDC/zork 1977 source as a flat snapshot, without its upstream history. `web/jszm.js` and `zork1.z5` are vendored third-party files. There are no squashes and no fork relationship.

## 3. Branch and history coverage
- Remote branches: `main` (default), `feature/web-app`, `feature/ten-turn-context`, `feature/world-json-grounding`, `feature/autocorrect-suggestions`.
- `git log main..origin/X` is empty for every feature branch, so **all work is merged and nothing is left unmerged**. Each branch holds one feature commit followed by an explicit merge commit on `main`:

| Branch | Feature commit | Merge commit |
|---|---|---|
| feature/web-app | `de52357` (adds `web/index.html`) | `b4980fb` |
| feature/ten-turn-context | `d2d00e3` | `ebccd5a` |
| feature/world-json-grounding | `a3c3294` | `adcd03c` |
| feature/autocorrect-suggestions | `17abacd` | `10b1689` |

- The v0 commit `56e8d6e` and the root `index.html` commit `bda7c3f` were made directly on `main`.
- PRs and issues: `gh pr list` and `gh issue list --state all` both return none. Merges were done locally, without PRs.
- History is fully accessible. `index.html`, `web/index.html` and `web/zork-chat.html` are byte-identical build outputs; `zork1.z5`/`web/zork1.z5` and `jszm.js`/`web/jszm.js` are duplicates (checked with `cmp`).

## 4. Actual functionality
Inspected: `web/_template.html` (about 29 KB of real source), `build_html.py`, `web/README.md`, `web/zork-world.json` structure, and the diffs of every commit.

- **Build:** `build_html.py` inlines `jszm.js`, the base64 story file and `zork-world.json` into the template, and writes `web/zork-chat.html` plus `web/index.html`. It escapes `</` in the JSON to avoid breaking the `<script>` tag. Paths are hard-coded to `/home/user/workspace/Liquid_SDK_Test/Liquid_SDK_Test` with `/tmp` fallbacks, so it is not portable without editing.
  - **Verified:** with ROOT pointed at a temp copy, the rebuild produced output **byte-identical** to the committed `index.html`. The root `index.html` (`bda7c3f`) was copied by hand; the script does not write it.
- **Game engine:** JSZM generator wiring (`bootZmachine`, `stepZmachine`, `drainSubGen`). Input from `read()` goes through a Promise; save/restore use `localStorage`.
  - **Verified:** a headless Node harness using the same hook pattern ran the README walkthrough (open mailbox → take leaflet → read leaflet → n → look → inventory) plus e → open window → w → w → take lamp, with correct game output.
- **LLM layer:** `callLLM()` POSTs to `https://openrouter.ai/api/v1/chat/completions` (temperature 0.7, max_tokens 220). Model choices are `liquid/lfm-7b` (default), `lfm-40b` and `lfm-3b`. Errors appear in the chat as status messages.
  - `gameContext()` sends the status line, the last output chunk, world "ground truth" and the last 10 turns.
  - There are five task-specific system prompts, each restricted to the scene or turn log ("no invented objects, exits, or NPCs").
  - **Not executed:** a real call would need a paid key and incur charges. Whether these model IDs are still served was not checked.
- **World grounding (`a3c3294`):** `zork-world.json` (110 rooms, 120 objects; `source` field: "MITDDC/Microsoft ZIL release (1dungeon.zil + 1actions.zil), parsed"). `worldLookup()` matches the status-line room name and lists exits, blocked or conditional exits and items for the LLM.
  - **Verified:** every room visited in the Node run resolved (West of House, North of House, Behind House, Kitchen, Living Room).
- **Autocorrect (`17abacd`):** turns mobile autocorrect back on and adds a `<datalist>` of Zork verbs plus room and object names and their tokens, so the keyboard stops "correcting" game words.

## 5. How Jacob uses or builds with AI
- **Building an AI-powered product:** this is clearly shown. The app is an LLM wrapper whose main design issue is keeping hallucination in check: grounding in game state, then in parsed world data, plus prompt constraints.
- **Using AI to build it:** there is no direct evidence. There are no agent instruction files, no trailers and no agent branches (the branches are named `feature/*`).
  - Indirect and inconclusive: `build_html.py` hard-codes a `/home/user/workspace/...` path and `/tmp` scratch files (`/tmp/jszm.js`, `/tmp/zork1.b64`). That points to building in a hosted sandbox workspace, but it does not show who or what wrote the code. Under the brief's rules, AI authorship is **not established**.
- **Verification:** the `56e8d6e` message records a manual end-to-end check ("West of House -> open mailbox -> ... inventory all work correctly"). No automated verification exists.

## 6. Quality assessment (confidence: moderate-high for code, low for LLM output quality)
**Strengths**
- Shipping a single file that needs no server suits the goal (open it on an iPhone, host on Pages).
- The Z-machine integration is correct and short.
- Having the user bring their own key, kept in `localStorage`, avoids hosting a secret, and the README states the privacy model.
- The grounding change is the most thoughtful decision in the repo. Instead of tightening the prompt alone, it adds structured ground truth from the game's source data.
- Commit messages are specific and explain the reason behind each change (e.g. the autocorrect rationale).

**Weaknesses and defects**
- Duplicate room names are keyed with suffixes (`"Forest (FOREST-2)"`), but the status line shows just "Forest". Every forest room therefore resolves to the first "Forest" entry, which feeds the LLM wrong exits. Maze rooms are likely affected the same way (inferred from the key format, not run).
- The JSON parser and the ZIL source it read are **not in the repo**. The imported `zork-src/` is the 1977 MDL version, not the ZIL that `zork-world.json` claims as its source, so the world data cannot be regenerated from the repo.
- `CURRENT SCENE` is the last output chunk (e.g. "Taken."), not the room description. Grounding relies on the world data to make up for it.
- Output capture relies on `setTimeout` (50 ms / 300 ms) instead of an event.
- Command-name mismatch: the README and datalist say "vague hint"/"spoiler hint", but the typed-command handler only accepts "hint vague"/"hint spoiler" (the chips work).
- Built HTML is committed in triplicate, so every change touches 3–4 files of about 300 KB.
- The empty root README and the misleading repo name hurt discoverability.
- Treat these as prototype-level shortcuts, apart from the forest/maze lookup bug and the missing parser, which are real defects.

## 7. Developmental milestones
1. `489e764` (Jun 12): imports historical Zork source as reference. The app never uses it.
2. `56e8d6e` (Jun 12): working v0 with six AI features, verified manually.
3. `de52357`/`bda7c3f` (Jun 14): deployment entry points for GitHub Pages (`web/` first, then the root).
4. `d2d00e3` (Jun 14): context window raised from 5 to 10 turns, buffer from 12 to 15.
5. `a3c3294` (Jun 14): grounding in structured world data, with a hardened hint prompt.
6. `17abacd` (Jun 15): mobile typing usability.

## 8. Changes in working method and possible lessons
- **Context size, 5 → 10 turns** (`56e8d6e` Jun 12 → `d2d00e3` Jun 14).
  - Trigger: not documented (the commit has no body).
  - Inferred lesson: hints and recaps lacked enough history.
  - Evidence strength: speculative.
  - Alternative explanation: a pre-emptive tweak.
- **Hallucination control: prompt-only → prompt plus structured ground truth** (Jun 12 → Jun 14 06:42).
  - Earlier hint prompt: "Do NOT invent items or rooms not in the scene".
  - Later: "CRITICAL: When a WORLD DATA section is provided, treat it as ground truth…", plus injected exits and items.
  - Trigger: the commit says "hint sys prompt hardened against invention". That suggests invented content was seen, but no failure example is recorded.
  - Inferred lesson: prompt instructions alone were not enough with small LFM models, so grounding moved into data.
  - Evidence strength: strongly inferred.
  - Alternative explanation: planned from the start. The `zork-src` import in the first hour suggests source-grounding was intended early.
- **UX: autocorrect off → on with a domain dictionary** (Jun 15).
  - Trigger explicitly documented: "Mobile autocorrect was disabled, making typing unfriendly". It points to real phone use.
  - Evidence strength: explicitly documented.
- **Workflow: direct commits to `main` → one `feature/*` branch per change with local merge commits** (from Jun 14). This shows a consistent branching habit within the repo.
- No prompt-iteration logs, evals or plans exist, so prompt development beyond these diffs cannot be reconstructed.

## 9. Demonstrated capabilities, limitations, uncertainties
- **Demonstrated:** fast delivery of a self-contained, mobile-targeted LLM feature on top of a third-party engine; grounding LLM output in structured, source-derived data; small, well-described, purpose-driven iterations; awareness of privacy and licensing in the docs.
- **Uncertainties:**
  - Whether the LLM features produce good results (not run).
  - Whether the GitHub Pages deployment is live (not checked; read-only, offline).
  - Who or what generated `zork-world.json`.

## 10. Evidence references and verification limits
- **Code and data:**
  - `Liquid_SDK_Test@10b1689:web/_template.html` (lines ~140–147 model selector, 207–278 suggestions and world lookup, 372–465 VM wiring, 515–610 LLM calls and prompts)
  - `@10b1689:build_html.py`
  - `@10b1689:web/README.md`
  - `@a3c3294:web/zork-world.json`
  - `@489e764:zork-src/README.md`
- **Diffs:** `git diff 56e8d6e a3c3294 -- web/_template.html` (prompt and grounding change); `git diff b4980fb d2d00e3` (turn window); `git show 56e8d6e:build_html.py` (original `/tmp`-based build).
- **Branches:** all four `origin/feature/*` branches are fully merged. There are no PRs or issues.
- **Executed (offline):**
  - Node harness for JSZM plus `zork1.z5` with the world lookup: passed.
  - Rebuild via `build_html.py` with a redirected ROOT, into `/tmp/lzt`: output byte-identical.
  - `cmp` checks for duplicated files.
- **Not executed:** browser UI (no browser available), OpenRouter calls (paid/credentialed), GitHub Pages URL.
