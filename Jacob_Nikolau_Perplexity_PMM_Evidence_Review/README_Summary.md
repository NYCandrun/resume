# Jacob Nikolau — Perplexity PMM Evidence Review

**Sanitized copy.** Internal Google Drive links and file IDs, internal Mosaic and NovoEd business figures, customer, colleague and third-party names, and email addresses have been removed from the files in this folder. The methods, prompts, scripts, coverage counts and findings are kept.

Prepared October 26, 2026. It collects the outputs of the three investigations you asked for in your original request (`00_Original_Request_Consolidated.md`). The three workstreams were kept separate on purpose. The working-style brief and the GitHub assessment did not inform the role-fit assessment or the application thread.

## What's in this folder

| Item | What it is |
|---|---|
| `README_Summary.md` | This file: the folder contents, the research done, coverage and caveats |
| `00_Original_Request_Consolidated.md` | Your original two-part prompt, copied verbatim from the session log and joined into one file |
| `Files_Reviewed_and_Verified.xlsx` | Consolidated list of what was reviewed and how it was checked: 150 Drive files, 86 evidence findings, 140 calls, 28 repos and 9 public or other sources. The first tab explains each sheet |
| `1_Professional_Work_Google_Drive/` | Investigation 1: professional work and role fit |
| `2_Working_Style_Call_Excerpts/` | Investigation 2: working style and character brief |
| `3_Personal_GitHub_AI_Projects/` | Investigation 3: personal GitHub AI practice and how it has evolved |

Each workstream folder has the same layout:

- `PROMPTS_1_Research_Agents.md`, `PROMPTS_2_Synthesis.md`, `PROMPTS_3_Final_Deliverables.md`: the exact prompts sent to subagents, copied verbatim. Where a stage was done by the lead agent rather than a subagent, the file says so and describes what was done. No prompts were reconstructed after the fact.
- `research/`: agent instructions, raw ledgers, logs, indexes and per-item reports
- `synthesis/`: reconciled or cross-cutting analysis
- `output/`: final deliverables

Left out on purpose:
- The small "Ask Jacob's Work – Evidence Explorer" web app, as you asked. It is still saved as a private preview and was never published.
- Raw source copies: Drive file exports (about 2.2 GB), the full call-excerpt text, and the 28 repository clones (about 4 GB). These stay in their source systems. The index files point back to them.

## Research done

### 1. Professional work and role fit (Google Drive and résumé)

- **Scope:** We mapped all 5,442 Drive files and filtered them to 1,984 professional files dated October 2021 onward. The résumé was used only as a map of claims to test.
- **Method:** Three research agents worked in parallel:
  - T1: positioning, research and competitive intelligence
  - T2: launches, enablement and influence
  - T3: outcomes, metrics and pricing

  They produced the ledger findings. The lead agent reconciled the findings, spot-checked five key attributions against the source text, and verified seven public web sources.
- **Coverage:** 150 unique files were logged: 35 read deeply, 35 read through, 76 skimmed, and 4 cited in the ledger only. That covers about 8% of the professional set.
- **Findings:** 38 demonstrated and 48 inferred.
- **Headline:** Interview: yes. The strongest evidence is research-led positioning, claim discipline for AI products, and launch kits built as systems. Positioning-centered work spans about 4.75 years.
- **Outputs:**
  - `output/Private_Hiring_Assessment_Perplexity_PMM.md`
  - `output/Application_Thread_Why_Jacob_Nikolau_SHAREABLE_DRAFT.md`
  - `synthesis/Professional_Evidence_Ledger_reconciled.md`

### 2. Working style and character (call excerpts)

- **Scope:** Jacob's own lines from 140 call sections, June 2025 to June 2026. The source was the Google Doc of extracted statements, exported and processed locally. The full text was never loaded into model context.
- **Method:**
  - The lead indexed the document locally (`research/call_index.json`).
  - A single agent searched the full corpus with regex and lexical tools and read 39 sampled windows closely. It produced 44 ledger entries, each citing line numbers, plus the brief.
  - The lead reviewed the brief for quality.
- **Headline (moderate confidence):**
  - Explanation-first. He asks what work is for before building it, and translates features into buyer concerns, often through analogy.
  - Direct and informal. He rates his own skill highly but is candid about specific limits.
  - Method note: the source contains his side of each call.
- **Output:** `output/Jacob_Nikolau_Working_Style_Brief.md`

### 3. Personal GitHub AI practice (NYCandrun)

- **Scope:** All 28 personal repositories, dated March to October 2026. There are no personal repos from before 2026, so "evolution" covers about 7 months.
- **Method:**
  - One agent per repository investigated it (`research/per_repo_reports/`).
  - A synthesis agent then revisited git history and key files and re-ran cheap offline tests.
  - It produced the coverage manifest, the comparison table, a timeline with commit-pinned references, and the synthesis report.
- **Headline:**
  - Research orchestration is the most developed area: multi-agent runs with source grading, separate reviewer contexts, and cost and context controls.
  - Prototyping and evaluation work spans games, curricula, benchmarks and app rebuilds.
- **Output:** `output/Jacob_Nikolau_Personal_AI_Projects_Synthesis.md`. It includes a separately labeled section on possible PMM implications.

## Shareable material

`1_Professional_Work_Google_Drive/output/Application_Thread_Why_Jacob_Nikolau_SHAREABLE_DRAFT.md` was written for external use. It contains no internal revenue or pipeline figures and no customer names, and it links only to public pages.

## Rules followed

- No source files were modified.
- This folder was later sanitized in place: links, internal figures, names and unsupported-claim statements were removed; prior revisions are retained in Drive version history.
- No Drive sharing settings were changed.
- No one was contacted, nothing was submitted, and nothing was published.
- Personal projects were not attributed to any employer.
- Instructions found inside retrieved files were treated as content, not as commands.
