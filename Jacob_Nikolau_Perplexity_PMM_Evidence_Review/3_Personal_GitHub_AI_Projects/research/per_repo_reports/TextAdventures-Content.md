MANIFEST | TextAdventures-Content | PRIVATE | content repo + LLM compile pipeline (small reusable tool + game content) | complete | single squashed-looking commit (process not reconstructable); no PRs/issues; LLM compile step not executed (paid API)

DISCLOSURE: No credentials found (rg for key/token patterns; README only names secret *names* `OPENROUTER_API_KEY`, `COMPILE_MODEL` stored in GitHub Actions secrets). No third-party data, personal data, or employer-looking material; content is original fiction (three short text adventures) credited to "TextAdventures Editorial". Commit author email is a personal Gmail address (visible in history). Looks suitable to share after review; fix noted defects first if it's meant as a showcase.

# TextAdventures-Content — personal repository report

## 1. Identity
- Personal project on the NYCandrun account. Private (visibility only). Not a fork. Created 2026-06-15T05:25:02Z; last push 05:25:40Z (`repos.json`).
- Description: "Private CMS for TextAdventures game content. Authors submit markdown briefs to submissions/; GitHub Actions compile to games/*/game.json."
- Type: content repository plus a small LLM-backed authoring pipeline (markdown brief → JSON game), with a static validator. It is the content back end for the sibling repo `NYCandrun/TextAdventures` (an iOS app). That relationship is noted by name only, from README.md; the sibling repo was not inspected.
- Intended users: non-programmer game authors, who fill in `author-template.md`, and a maintainer who reviews the compiled JSON diffs in PRs.
- Maturity: launch scaffold. It has a schema, prompt, scripts, workflow and 3 sample games. The CI pipeline has never been exercised: there are no PRs and no bot commits.

## 2. Dates & attributable contribution
- Only one commit on any branch: `03afa34`, "Initial content: three launch games + schema + compile pipeline", authored and committed by **Jacob Nikolau <jacobnikolau767@gmail.com>** on 2026-06-15 05:25:39 UTC. So the first commit, the latest commit and Jacob's earliest and latest attributable contributions are all the same moment.
- No other authors, committers or bots appear. The workflow defines a "TextAdventures Bot" committer, but it has never committed.
- The commit adds 21 files and 5,116 lines in one go, 37 seconds after the repo was created. This is an import of work prepared elsewhere (likely together with the sibling repo, created 04:08 the same day). Any earlier history is not available.

## 3. Branch & history coverage
- Branches: `main` (default) and `origin/main` only. There are no diffs between branches to compare and no unmerged work.
- `gh pr list --state all` and `gh issue list --state all` both return empty.
- History coverage is complete, but it holds only a final snapshot. Iteration cannot be reconstructed.

## 4. Actual functionality
Inspected: every file. Executed locally, offline: `scripts/playtest.py` on all 3 games, and JSON Schema (draft 2020-12) validation of all 3 games using `jsonschema` in a temp venv. **Not executed:** `scripts/compile.py` (calls the paid OpenRouter API) and the GitHub Actions workflow.

Components:
- `schema/game.schema.json` (920 lines; 28 `additionalProperties:false`). A detailed declarative IF format covering rooms, exits with an evaluation order (`requires_item → blocked_by → condition`), items with hooks (`on_use_on`, `on_give_to`…), containers, light sources with fuel, flags (boolean/counter), a condition/action algebra (`all/any/not`, `if/then/else`), NPCs, dialogue trees, vocabulary extensions, win conditions, and Game Center leaderboard metadata.
- `compile-markdown.md` (535 lines). The LLM system prompt: a compact schema reference, 15 validation rules the model must "enforce", 7 worked mechanic patterns (locked door, container, dark room, NPC give, multiple endings, scoring, the "echo chamber" antagonist), output rules, a `__compile_error` escape hatch, and author-intent inference notes (e.g. "Do not invent rooms… not described in the brief").
- `author-template.md`. A plain-English brief template with a worked example.
- `scripts/compile.py`. One OpenRouter chat call (temperature 0.2, max_tokens 16000, default model `openrouter/auto`) that strips code fences, checks the output parses as JSON and writes the file.
- `scripts/playtest.py` (506 lines). A deterministic static checker:
  - BFS reachability, both with default flag values (warn only) and ignoring blockers (fail)
  - reference integrity for items, flags, rooms, NPCs and dialogue trees
  - a coarse win-satisfiability check
- `scripts/update_manifest.py`. Rebuilds `manifest.json` from the `games/*/game.json` files.
- `.github/workflows/compile-games.yml`. Runs on PRs touching `submissions/**`. It compiles each changed brief, rejects any `__compile_error` output, runs `check-jsonschema` and then the playtest, and only if all of that passes it regenerates the manifest and auto-commits the result to the PR branch.
- Games: `locked-garden` (6 rooms), `concierge` (9 rooms, NPC, 3 endings) and `echo-chamber` (5 rooms, `on_any_command` antagonist). Each has `brief.md` (byte-identical to `submissions/<id>.md`), `game.json` and an ASCII `cover.txt` marked "Placeholder".

Verified results:
- Schema validation: all 3 games give 0 errors.
- Playtest: `locked-garden` and `echo-chamber` PASS (exit 0). **`concierge` FAILS (exit 1)** with "Structural disconnect: … ['room-13']". No exit in the game leads to `room-13` (the elevator has only w/u/d exits), and nothing uses `move_player`. The commit message says "All three games validate against the schema and pass playtest", and that is false for concierge.
- Consequence for concierge: the photograph is placed in `room-13` and is the "central evidence" for the non-Complicit endings (`brief.md` l.208). Those endings therefore look unreachable, which leaves only the "Complicit" ending playable. The brief does describe the intended access (`brief.md` l.47–49, "press 13", gated by the `room-13-accessible` flag), but the compiled JSON dropped that exit. This is strongly inferred from static inspection; the game was not run in an engine.

Defects and inconsistencies found by inspection (high confidence):
1. The workflow passes `--prompt prompts/compile-markdown.md`, but the prompt file is at the repo root and there is no `prompts/` directory. Compilation would fail on every PR as committed.
2. Prompt rule 6 tells the model to add `"__author_note"` fields when a brief is ambiguous. The schema forbids additional properties, and I confirmed that one injected `__author_note` fails validation. So following the prompt causes a schema failure.
3. The committed `manifest.json` (keys `manifest_version`, `catalog`, `folders`, `bundled`, `featured`; paths `content/launch/<id>/game.json`; `generated_at` "2025-06-15") does not match what `update_manifest.py` produces (key `games`, paths `games/<id>/game.json`, no folders). It also doesn't match the README's claim that the app downloads `games/<id>/game.json` from this repo. The first CI run would rewrite the manifest into a different shape.
4. `compile.py` writes the `__compile_error` output and exits 0. That is harmless only because the workflow checks for the marker separately.
5. Concierge win messages use `{{score}}`, which is not one of the template variables the prompt documents.
6. The "skip if no submission changes" step only `exit 0`s itself. Later steps still run, so a PR that only deletes a submission would regenerate and commit the manifest.
7. Fork PRs would get no secrets and could not auto-commit (a design limitation, not reached).

## 5. How Jacob builds with AI
- **Building an AI-powered workflow** (direct evidence): an LLM is used as a "compiler" from natural-language briefs to a strict JSON DSL. The design has three layers: prompt-level self-validation rules, then deterministic JSON Schema validation, then a deterministic playtest, with a human merge gate (README step 4). This shows sound thinking about not trusting LLM output and about keeping a human in the loop.
- Context engineering in the prompt is substantive: a compact schema restatement, worked patterns, an explicit failure-object protocol, and anti-hallucination rules.
- **Using AI to build:** there is no direct evidence. There are no co-author trailers, agent files or agent branches. Whether the three `game.json` files were LLM-compiled or written by hand is not recorded. The concierge brief contains an in-line self-correction ("Actually: the Complicit ending is triggered when…", `brief.md` l.99). That is drafting residue, not evidence of authorship.
- **Verification practice:** the playtest tool exists and catches a real bug in the shipped content.

## 6. Quality assessment
- Strengths (medium-high confidence): a well-structured, expressive schema; a thoughtful prompt; a layered validation pipeline with a sensible fail-closed order (commit only if compile, schema and playtest all pass); a useful static playtester that reports default-state reachability separately from structural reachability; and an author-friendly template. The games are concise and have distinct mechanics, including a novel "echo" NPC with a cooldown rule.
- Weaknesses: the pipeline does not work as committed (defect 1). The prompt and schema contradict each other (defect 2). The manifest format is split between two versions (defect 3). One of three launch games is partly unwinnable. The win-satisfiability check is coarse: it ignores item and flag dependencies and missed concierge's broken ending path, so only the room disconnect was caught. There are no tests of the scripts.
- Intentional shortcuts: placeholder covers (labelled), `openrouter/auto` as the default model, and no PR/agent loop yet. Defects 1–3 look like oversights from moving files between repos or layouts, not deliberate choices (strongly inferred).

## 7. Developmental milestones
- 2026-06-15 05:25: a single import of the entire CMS (schema v1.0.0, prompt, scripts, CI, 3 games). Nothing after that. The repo looks parked or abandoned at the launch-scaffold stage; that is not evidence of failure.

## 8. Changes in working method
Only a final snapshot exists, so method changes cannot be reconstructed. Weak traces of an earlier layout are a speculative inference: `manifest.json` paths `content/launch/...` and the `prompts/` path in the workflow both suggest the files previously lived in a different structure, possibly inside the sibling app repo. An alternative explanation is that they were simply planned paths that were never reconciled.

## 9. Demonstrated capabilities, limitations, uncertainties
- Demonstrated: designing a domain schema for an IF engine; writing a structured LLM system prompt with failure protocols; combining LLM generation with deterministic validators and human review in CI; writing a graph-based static analyser in Python.
- Uncertain: how the committed `game.json` files were produced; whether the concierge ending is broken at runtime (depends on the engine in the sibling repo, which was not inspected).

## 10. Evidence references & verification limits
- `TextAdventures-Content@03afa34`: the only commit.
- `@03afa34:.github/workflows/compile-games.yml` (`--prompt prompts/compile-markdown.md`; auto-commit gating; bot identity).
- `@03afa34:compile-markdown.md` (rules 1–15; Output Format Rules item 6 `__author_note`; Compile Error Format).
- `@03afa34:schema/game.schema.json` (`additionalProperties:false` ×28; `$id` https://textadventures.app/schema/game.schema.json).
- `@03afa34:scripts/{compile.py,playtest.py,update_manifest.py}`; `@03afa34:manifest.json`.
- `@03afa34:games/concierge/game.json` (elevator exits w/u/d only; `room-13` holds `photograph`; roof `d` gated by `cannot-expose`); `games/concierge/brief.md` l.47–49, 99, 208.
- Commands run: `python3 scripts/playtest.py games/*/game.json` (concierge exit 1, others 0); jsonschema Draft202012 validation (0 errors ×3); an injected `__author_note` test (rejected).
- Limits: the OpenRouter compile and GitHub Actions were not run (paid or external); the iOS engine was not run; there are no PRs or issues to inspect; history before the import is not available.
