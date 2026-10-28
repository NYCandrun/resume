MANIFEST | liquid-token-budget-slider | PUBLIC | demo (browser app + local model server + eval scaffold) | complete | single branch, 9 commits in ~10h; no PRs/issues; UI not visually rendered (no browser in sandbox); real model not run (would download ~900 MB weights, no Apple-Silicon GPU)

DISCLOSURE: No API keys, tokens or passwords found in any commit (searched full `git log --all -p`). Commits 90927bc through 0c64d13 put a hard-coded public Modal endpoint URL in `web/index.html` (`MODEL_ENDPOINT`). The URL contains a personal account handle. I have not copied it here. The URL is still in public history, but the 18bcd91 message says the app was stopped (`modal app stop`). Commit author email is a company-domain address (`jacobn@…mosaicapp.com`). That is an identity only; nothing in the content suggests the work belongs to that company. The repo targets a public third-party model (LiquidAI/LFM2.5-VL-450M) and is reskinned to that vendor's brand ("Liquid brand guide's canonical token block", 64e6c33). It contains no internal or proprietary material from that vendor: all model facts cite public HF/blog URLs, and the images are CC0. Because it carries the vendor's logo and brand styling, a reader might take it for an official vendor demo; the repo has no disclaimer. Third-party data: 3 CC0 Roboflow images, provenance documented. No personal data. **Suitability to share:** suitable after review. Consider adding an "unofficial / personal project" note, and be aware the old endpoint URL is still visible in history.

# liquid-token-budget-slider: report

## 1 Identity
- Personal repo under NYCandrun, **public** (repos.json: created 2026-07-01T20:45Z, pushed 2026-07-02T06:32Z, not a fork, no description). It is published as a GitHub Pages site (README "Try it"; `.nojekyll` and the root `index.html` redirect were added in fb490a6).
- **Type:** an interactive product/tech demo with a real local inference backend and an evaluation scaffold.
- **Purpose:** to show that LFM2.5-VL-450M's runtime vision-token budget (`max_image_tokens`) is a dial for per-frame cost on edge cameras. A doorbell frame is turned into a structured event `{event, where, conf}`, and a slider sets the budget.
- **Intended user** (PRD §0, §5): a "technically sophisticated evaluator", e.g. an engineering lead choosing a model for a home-camera product. Secondary users are a presenter and the evaluator's engineer.
- **Maturity:** a polished demo. The simulated mode is complete. The local live mode is implemented and described as verified. The accuracy/detail evaluation is a stub (`_judge` returns `None`).
- The README calls it a "Companion to the 'cameras as a sensor' control-loop one-pager". That one-pager is not in this repo.
- A sibling repo, `liquid_LFM2.5-VL_demo`, was created about 20 minutes earlier. I note it by name only; I did not inspect it.

## 2 Dates and attributable contributions
- All 9 commits are on `main`. Author and committer are both `jacobn-a11y` for every commit. There are no other authors and no bot accounts.
- First commit: 23ff718, 2026-07-01 16:45 -0400 (a GitHub-generated "Initial commit" with a 1-line README). Last commit: 18bcd91, 2026-07-02 02:32 -0400.
- Activity came in two bursts:
  - 17:50–18:26 on Jul 1: the build and the reskin.
  - 23:56 on Jul 1 to 02:32 on Jul 2: the README, the reframe, UI polish and the security fix.
- **Every commit after the initial one has the trailer `Co-Authored-By: Claude Opus 4.8 <noreply@anthropic.com>`.** The work was done jointly with Claude under Jacob's identity.
- No imported history or squashes are visible. However, dbc12d7 lands 1,546 lines in one commit, so the development before it was not committed and cannot be reconstructed.

## 3 Branch and history coverage
- Branches: `main` (default) and `origin/main`. There are no other remote branches, so nothing was left unmerged.
- `gh pr list --state all` and `gh issue list --state all` both returned nothing.
- Commit sizes (from `git show --stat`):
  - dbc12d7: +1,546 lines across 10 files (initial build)
  - fb490a6: index.html +145/−91 (reskin)
  - 9fdd31a: README +20
  - 90927bc: 11 files, +531/−336, plus 3 JPGs (reframe)
  - 64e6c33: +43/−39
  - 19de33e: +4/−27
  - 0c64d13: +9/−2
  - 18bcd91: 6 files, +37/−53
- History coverage is complete for what was pushed.

## 4 Actual functionality (inspected and executed)
**Front end** (`web/index.html`, 571 lines, one self-contained file):
- Data is embedded so the page works from `file://`. It has a slider over 8 stops (64–512 tokens) and 3 scenes using real CC0 frames.
- It shows an event JSON card, a cost-per-frame panel and an inline-SVG chart of event confidence vs cost. The scene image is blurred with a CSS filter as a visual metaphor for fewer tokens.
- In simulated mode, latency comes from an illustrative formula (`base + per_token*t + quad*t²`, with deterministic jitter). Cost % is `100*(40+t)/(40+512)`. Confidence and captions are hand-authored per stop, and the page labels them "illustrative".
- **Live mode:** `initMode()` probes `location.origin/health` and switches to live only when a same-origin server answers. `runInfer()` debounces for 160 ms, uses a sequence counter to drop stale responses, and posts the frame as base64 with `DATA.eventPrompt`. `renderEventReal` parses the model's JSON and flags it "not yet reliable — fine-tune…". If the server fails, the page falls back to simulated mode.

**Back end** (`server.py`, 362 lines, FastAPI):
- The model loads lazily with double-checked locking. Device choice is MPS/CUDA in fp16, or CPU in fp32.
- Image splitting is turned off (`do_image_splitting = False`) so the budget controls the token count. The comment says that with splitting on, caps of 64/128/256 all gave about 1,600 tokens on transformers 5.12.
- The budget is set directly on `image_processor.max_image_tokens`, because passing it through `apply_chat_template` is "silently ignored" in 5.x.
- Vision tokens are counted as occurrences of `image_token_id`. Latency is timed around `generate()` with a device synchronize. Requests are serialized by `INFER_LOCK`, and the schema floor is `ge=64`.

**Eval** (`data/eval_sweep.py`):
- Sweeps every budget × scene through the same `/infer` endpoint and writes `sweep_results.json`.
- Scoring is an explicit stub: "Do not fabricate an accuracy number."

**`modal_app.py`:** an optional cloud recipe that is not deployed, with a security warning.

**What I executed:**
- `py_compile` on all 3 Python files: OK. `node --check` on the extracted page script: OK.
- FastAPI `TestClient` against `server.py` with no model loaded:
  - `/health` returned `{'status':'ok','model_loaded':False,'device':'cpu'}`.
  - `/` returned 200 and served the page.
  - `/data/scenes/package.jpg` returned 200.
  - `/infer` with `max_image_tokens=10` returned 422, so schema validation works.

**What I did not run:** real inference, and rendering of the UI in a browser.

**What is claimed but not verified by me:**
- The 64/128/256/512 → 60/112/240/476 token mapping (dbc12d7 message).
- "Verified in-browser… console clean" (several commits).
- The raw model returning "valid JSON but noisy event/conf" (90927bc).

## 5 How Jacob works with AI
- **Both building and directing.** He builds a demo of an AI model (a VLM inference server plus an evaluation design), and he builds it together with Claude, as the co-author trailer on all 8 substantive commits shows.
- **Task specification:** `token-budget-slider-PRD.md` ("Draft v1 · 2026-07-01") is a structured spec. It has background written to be read "with no prior context", goals and non-goals, MoSCoW requirements, runtime tiers, an honesty section, success criteria, phasing and open questions. This reads like context prepared for delegation. Authorship split between Jacob and Claude cannot be determined (strongly inferred from the trailer, not proven).
- **Verification:** commit messages record specific checks:
  - "Verified end-to-end on Apple Silicon… 60/112/240/476 real vision tokens (monotonic)" (dbc12d7)
  - "no duplicate IDs, no control overflow… console clean" (64e6c33)
  - "latency still renders (279→735)" (19de33e)
  - "verified on Modal — the model hallucinates otherwise" (90927bc)
- **Debugging against the real library:** the server comments record two empirical findings on transformers 5.x. Tiling swamps the budget, and the `apply_chat_template` kwarg is ignored. Both workarounds are in the code.
- **Judgment and correction:**
  - The demo was reframed after real-model results showed detection, counting and OCR were "too noisy… to fake a clean 'it breaks at low budget' story" (rubric, README).
  - The deployed endpoint was withdrawn after a "denial-of-wallet" analysis (18bcd91).
  - The hardware-rescale feature was cut (19de33e).
- **No agent instruction files** (AGENTS.md, CLAUDE.md) or prompt files are present. The only prompts are the product prompts `caption_prompt` and `event_prompt`.

## 6 Quality assessment
**Strengths** (high confidence):
- **Honesty is designed in.** Real, modeled and illustrative values are kept separate in the UI, the README, `scenes.json` `_note`s and the PRD §9–10. Latency is caveated as "shape, not a device number", and the custom-NPU path is scoped out explicitly (Tier 2).
- **The server is careful for its size:** lazy load, a correct critical section, synchronized timing, a token count read from config, and a schema floor matching the processor minimum.
- **The pivot was driven by evidence.** When real outputs undercut the "accuracy breaks" story, the claim was changed to cost and detail rather than faked.
- **Security catch:** the public cost exposure was recognized and the endpoint removed. Still, the URL shipped publicly for about 40 minutes of commits (01:55–02:32).
- **Provenance:** model facts cite public URLs, and the image source, licence and processing are documented.

**Weaknesses and defects** (medium-high confidence):
1. **The README is partly stale after the reframe.** "How to use the demo" still describes 4 scenes (person, two people, empty porch), an "accuracy curve" and "Different scenes break down". "Scenes show placeholders — you haven't added footage" is also outdated. The PRD still describes accuracy-vs-budget and hardware presets.
2. **`data/scenes.json` is out of sync with the UI.** It still has `device_presets` and the latency `device factor` after 19de33e removed them from the UI. The "canonical data" file is not kept in sync automatically with the copy embedded in the HTML.
3. **The eval scaffold no longer matches the new rubric.** `eval_sweep.py` uses the caption prompt and a boolean `passed`. The rewritten `rubric.md` scores a detail fraction, and the live UI uses the event prompt, so the sweep would not measure what the demo shows. No measured curve was ever produced.
4. In live mode, the "what the model saw" caption field shows the raw event-JSON output, because only one prompt is sent per call.
5. **No tests.**
6. **Brand reskin without a disclaimer**; see DISCLOSURE.

Items 1–3 look like consequences of a fast pivot rather than deliberate shortcuts. The eval stub itself is an intentional, documented shortcut.

## 7 Developmental milestones
- **dbc12d7 (Jul 1 17:50):** full v1. Accuracy-vs-budget story, 4 synthetic-label scenes (no images; drop-in placeholders), device-rescale presets, PRD, FastAPI server, eval scaffold.
- **fb490a6 (18:26):** reskinned to the vendor brand; GitHub Pages wired up.
- **9fdd31a (23:56):** "Try it" section added to the README.
- **90927bc (Jul 2 01:55):** reframe to "camera → structured event, on a budget". Added the cost panel, a confidence-vs-cost curve, 3 real CC0 frames and a Modal GPU endpoint for the public live mode.
- **64e6c33, 19de33e, 0c64d13 (02:08–02:15):** layout regroup and brand-token fidelity, removal of the device selector, tighter footer.
- **18bcd91 (02:32):** live mode made local-only; Modal endpoint removed and stopped.

## 8 Changes in working method and possible lessons
1. **From accuracy to cost and detail.**
   - Earlier (dbc12d7): a pass/fail rubric with presence, count and no-contradiction checks across person, two-people and empty-branch scenes, where the "hard part" was counting and false positives.
   - Later (90927bc): a detail-completeness rubric on package frames, plus an event-confidence/cost framing.
   - Trigger: real-model runs on 450M showed detection, counting and OCR were too noisy (rubric.md, README).
   - Lesson: anchor the demo claim to behaviour actually observed.
   - Evidence: **explicitly documented**. Alternative explanation: real frames with people were not available under CC0.
2. **Hosted live model to local-only.**
   - Earlier (90927bc): a public Modal endpoint with open CORS ("opt-in, scales to zero").
   - Later (18bcd91): no live endpoint at all.
   - Trigger: recognizing that an unauthenticated public GPU endpoint invites denial-of-wallet, and that a token cannot be hidden in client JS.
   - Lesson: public no-signup demos should not call paid compute.
   - Evidence: **explicitly documented**. It is unknown whether an incident or a review prompted this.
3. **Pruning scope.**
   - Earlier: the device rescale was a PRD "Should have" (dbc12d7).
   - Later: removed (19de33e).
   - No stated reason. Possibly to reduce speculative numbers ("est./projected") or clutter.
   - Evidence: **speculative** as to motive.
4. **Synthetic placeholders to real sourced data.**
   - Earlier: the PRD said "staged/public images are not shipped" (dbc12d7).
   - Later: 3 CC0 frames with SOURCES.md (90927bc).
   - Evidence: strongly inferred. It enabled real-model verification on shipped frames.

The process before dbc12d7, including how the PRD came about, cannot be reconstructed.

## 9 Demonstrated capabilities, limitations, uncertainties
**Demonstrated:**
- Writing a clear product spec aimed at a skeptical technical audience.
- Building an end-to-end VLM demo (static front end plus a local inference server) with Claude.
- Debugging empirically against library behaviour and recording the findings in code comments.
- A deliberate honesty and labeling discipline.
- Changing the claim when the evidence contradicts it.
- Spotting and fixing a cost-exposure security risk.
- Documenting data provenance.

**Uncertainties:**
- How much of the code and text was written by Jacob versus Claude (the trailer says co-authored, nothing more).
- Whether the claimed in-browser and Apple-Silicon verifications happened as described (I have the commit messages only).
- The repo's relationship to the "one-pager" and to the sibling repo.

## 10 Evidence references and verification limits
**Code and data (commit-pinned):**
- `liquid-token-budget-slider@18bcd91:server.py`: `do_image_splitting=False`, the budget set on the image processor, `INFER_LOCK`
- `@18bcd91:web/index.html` (`initMode`, `runInfer`, `renderEventReal`)
- `@18bcd91:data/eval_sweep.py` (`_judge` stub)
- `@18bcd91:data/rubric.md` vs `@dbc12d7:data/rubric.md` (accuracy → detail)
- `@dbc12d7:data/scenes.json` (4 scenes, `correct`/`accuracy`) vs `@18bcd91:data/scenes.json` (3 scenes, `conf`, stale `device_presets`)
- `@18bcd91:modal_app.py` (security warning)
- `@18bcd91:token-budget-slider-PRD.md`
- `@90927bc:data/scenes/SOURCES.md`

**History and disclosure:**
- Endpoint URL present at `web/index.html@90927bc..0c64d13`, removed in 18bcd91.
- All commit messages, with Co-Authored-By trailers, are listed in §2 and §7.
- No PRs or issues.

**Verification limits:**
- The UI was not rendered.
- The real model was not loaded and no inference was performed.
- The live Pages site and the Modal app state were not checked.
- Claims about verification in commit messages are taken as the author's statements.
