# Investigation 2 — Working style & character through Jacob Nikolau's own words (independent)

## Source (local only)
- Plain text: /home/user/workspace/research/calls/calls.txt (8,015 lines, ~148K words). Line-numbered copy: calls_numbered.txt.
- Index: /home/user/workspace/research/calls/call_index.json — 140 call sections, each {call_id, line, end_line, date, title, n_statements, words}. Headers are lines `YYYY-MM-DD — Title`. Dates span 2025-06-10 to 2026-06-25.
- The doc ("Jacob_Nikolau_Meeting_Contributions_Edited.docx", uploaded 2026-10-26) contains ONLY Jacob's side, extracted from transcripts via grep, possibly edited ("Edited" in filename). Extraction method undocumented → completeness cannot be verified.

## Mandatory processing rules
- NEVER read the whole file into context. Use rg/grep/sed -n/python scripts to search, count, sample and extract bounded passages (≤ ~40 lines at a time). Build your own index/notes in /home/user/workspace/research/calls/work/.
- Inspect small samples first. Cite every quote as `[call_id | date | title | L<line>]` using stable line numbers from calls.txt.
- Adjacent lines are NOT necessarily a continuous exchange. Never reconstruct others' speech, reactions, agreement, tone, or outcomes. Jacob's description of others' positions = his characterization only.
- Distinguish: observable language / self-reported actions / stated intentions (commitments ≠ follow-through) / interpretations needing missing context.
- Do not use any other evidence (Drive, résumé, GitHub, memory). Do not diagnose personality or infer sensitive characteristics. Flag apparent transcription errors. Quotes are "exact to the supplied document, not verified against audio".
- Omit unnecessary identifying info (colleague/customer names → roles where possible) and confidential business details in the brief.

## Research questions (questions, not presumed strengths; find counterexamples)
How he: defines problems/clarifies ambiguity; translates technical capability → customer/business value; uses evidence/examples/analogies/reasoning; expresses uncertainty/limits; questions assumptions/considers alternatives; states disagreement & trade-offs; proposes decisions/owners/next steps; expresses customer curiosity & formulates questions; gives credit/offers help/acknowledges others; uses humor/directness/detail/brevity; explicitly reconsiders a position. Also less effective tendencies, and change over time (2025 H2 vs 2026).

## Method
Combine (a) targeted lexical searches (e.g. "I think", "I don't know", "not sure", "I could be wrong", "let me push back", "disagree", "trade-off", "the reason", "for example", "imagine", "what if", "why", "?", "I'll", "can you", "great job", "thank", "actually", "you're right", "changed my mind") with (b) systematic stratified sampling: read a fixed sample from every month and every call category (internal team/ops, 1:1s, sales/customer, agency/vendor, exec/leadership, partner — classify from titles; flag unclassifiable). Count frequencies per call to show spread (pattern across many independent calls > repeated project discussion). Deduplicate near-identical excerpts. Record how much was substantively read vs only searched.

## Deliverables
1. Evidence ledger: /home/user/workspace/research/calls/ledger.jsonl — fields: id, call_id, date, title, line_start, line_end, quote (exact), observable_behavior, interpretation, confidence, missing_context, alternative_explanation, counterexample_refs, pattern_tag.
2. Brief: /home/user/workspace/research/calls/Jacob_Nikolau_Working_Style_Brief.md titled exactly "Jacob Nikolau: Working Style and Character Through His Own Words". Open with the limitation (only extracted statements; no full conversations, audio, or colleague feedback). Sections: 1 Overall portrait (calibrated confidence); 2 Five–eight demonstrated patterns (observation vs interpretation, cross-call support counts, counterexamples); 3 Revealing passages (3–5, no reconstruction of missing exchange); 4 Strengths and possible friction (label hypothetical effects); 5 Collaboration hypotheses (explicitly inferences); 6 What remains unknown; 7 Source appendix & methodology (coverage, identifiable calls/categories, passages read, sampling design, search terms, extraction limitations, distinction between searching full corpus vs reading every passage). Mark "PRIVATE — not for external sharing".
