import json
d={c['call_id']:c for c in json.load(open('work/index_classified.json'))};L=open('calls.txt').read().split('\n')
E=[]
def add(cid,ls,le,sub,obs,interp,conf,miss,alt,tag,cx=None):
    txt=' / '.join(L[n-1].strip() for n in range(ls,le+1))
    if sub:
        assert sub in txt,(cid,ls,sub); q=sub
    else: q=txt
    c=d[cid]; assert c['line']<=ls<=le<=c['end_line'],(cid,ls)
    E.append(dict(id=f"E{len(E)+1:02d}",call_id=cid,date=c['date'],title=c['title'],line_start=ls,line_end=le,quote=q,
      observable_behavior=obs,interpretation=interp,confidence=conf,missing_context=miss,alternative_explanation=alt,counterexample_refs=cx or [],pattern_tag=tag))
NC="Other speakers' turns absent; cannot see what prompted the line or the response."
# P1 clarifying problem / purpose
add(41,2430,2431,None,"Asks the purpose and success metric of a newsletter in consecutive lines.","Tends to anchor work requests in goal and success criteria before execution.","medium",NC,"Could be a scripted agency-review question rather than a habit.","clarify_goal")
add(113,6856,6856,None,"Asks a string of questions about what a one-pager is meant to fix.","Interrogates purpose of a deliverable before producing it.","medium",NC,"Could be skepticism about the specific request rather than general method.","clarify_goal")
add(26,1324,1325,None,"Apologises for repeated questions and states he wants to avoid being 'conceptually weak' about product relationships.","Persists in clarifying technical concepts before writing about them; self-aware that it may feel repetitive.","medium",NC,"Politeness formula; listener's view unknown.","clarify_goal")
add(26,1275,1275,"in order to build an AI page, I need to understand what the AI does. Otherwise, the AI page is junk nonsense.","States that understanding the capability must precede writing a page about it.","Values substantive product understanding over surface messaging.","high",NC,"None strong; statement is explicit.","clarify_goal")
# P2 customer curiosity
add(6,298,300,None,"Explains to a customer why he wants to know whether value was over/undersold and asks them to talk through why they bought.","Customer interviews framed around calibrating marketing promises to real value.","medium","Whether this was a formal research interview is inferred from title only.","Standard customer-interview script.","customer_curiosity")
add(6,306,308,None,"Bundles three questions; asks for an obsolete spreadsheet to study the 'pre-state'; admits he has never worked in ops at such a firm.","Seeks artefacts to understand prior customer workflow; acknowledges domain limits.","medium",NC,"Could reflect time pressure rather than curiosity.","customer_curiosity")
add(5,226,227,None,"Hypothesises how a customer's standup meeting runs, then hedges 'I don't know'.","Probes workflow with concrete scenarios while marking uncertainty.","low","Adjacent lines may include paraphrase of the customer; attribution not verifiable.","Could be summarising what the customer said.","customer_curiosity")
# P3 value translation
add(28,1391,1393,None,"Describes the fear of an agency CEO not knowing who is staffed on which project (profanity masked in source).","Translates resource-management capability into an executive's business anxiety.","medium",NC,"Could be rehearsed pitch language.","value_translation")
add(8,361,362,None,"Frames partner messaging as 'you can sell lots and lots of services against us' vs a six-week direct implementation.","Distinguishes value story by audience (partner vs direct buyer).","medium","Business context of the partner program not visible.","None strong.","value_translation")
add(68,3738,3739,None,"Explains 'push rather than pull' workforce mobility with a concrete unstaffed-ticket example.","Converts product positioning into a concrete scenario for a non-technical listener.","medium",NC,"Could be rehearsed positioning.","value_translation")
# P4 analogy/examples
add(87,5191,5193,None,"Uses the subway-map analogy to explain relative vs absolute positioning in a visual.","Reaches for everyday analogies to explain abstract design/product ideas.","high","What the visual was is not visible.","None strong.","analogy_example")
add(55,3084,3085,None,"Uses a burger-chain example to explain core value vs added value.","Same analogical habit, separate call/month.","high",NC,"None strong.","analogy_example")
add(19,884,885,None,"Says his core competency is explaining complicated technology (e.g. to a child) rather than creative/design work; 'underperform' appears ungrammatical.","Self-identifies as an explainer; acknowledges a design limit.","medium","'underperform' likely an editing substitution (see E42).","Self-presentation in a vendor context.","analogy_example")
# P5 reasoning / evidence
add(19,852,852,None,"States the reason a topic is raised: it affects paid-spend economics.","Explicitly links agenda items to economic rationale.","medium",NC,"None strong.","reasoning_evidence")
add(115,6925,6926,"As an example, two weeks ago, randomly, a bunch of inbound leads were overwritten because they were converted to contacts.","Supports claim that the CRM can't be relied on with a dated, specific incident.","Uses concrete incidents as evidence when defending workload.","medium","Whether the incident is accurate is not verifiable; colleagues named in neighbouring lines are his characterization only.","Defensive context may select favourable examples.","reasoning_evidence")
add(27,1365,1365,None,"Cites a mentor (former consulting partner) as validating that utilization is the most important thing.","Uses authority/anecdote as validation alongside reasoning.","low",NC,"Conversational storytelling rather than evidence.","reasoning_evidence")
# P6 uncertainty / limits
add(28,1458,1458,"So you need to know your skill set and this isn't mine.","States a task is outside his skill set.","Acknowledges limits openly.","medium",NC,"Could be deflection of a task.","uncertainty_limits",["E30","E31"])
add(23,1050,1050,None,"Apologises and says he is 'not really such a multitasker'.","Names a personal working limit.","low",NC,"Social nicety.","uncertainty_limits")
# P7 reconsider / own mistakes
add(101,6125,6126,None,"Says he misunderstood the other person's direction and apologises.","Explicitly revises his interpretation when it proves wrong.","medium","What the other person said is absent.","Could be face-saving.","reconsider_ownership")
add(121,7277,7277,None,"Says he 'should have surfaced more' while explaining he saw the work as planning- not deliverable-oriented.","Accepts partial fault while offering his reasoning.","medium",NC,"Mixed apology/justification.","reconsider_ownership")
add(64,3459,3459,None,"Takes 'complete ownership' of getting a process right for a colleague.","Stated intention; follow-through not observable.","medium","No outcome data.","Formulaic reassurance.","reconsider_ownership")
add(64,3466,3466,"I want to make sure that the way that I communicate with you works for you","States intent to adapt communication to the listener.","Attends to communication fit with a senior colleague.","medium",NC,"Formula after feedback.","reconsider_ownership")
add(29,1614,1614,None,"Flags a misordering in a deck and calls it his fault.","Small, spontaneous ownership of errors.","medium",NC,"None strong.","reconsider_ownership")
# P8 disagreement / directness
add(80,4468,4469,None,"Names a disagreement on prioritization, then 'That's true. I hear that.'","States disagreement plainly, then acknowledges the other view.","low","The other view and resolution are absent.","Could be conceding rather than integrating.","disagreement_directness")
add(102,6233,6233,"I don't I don't care what [name] wants. I don't care. it's driving me crazy. we need to get into Salesforce.","Blunt rejection of a colleague's preference in a vendor call.","Directness can become dismissive under frustration.","medium",NC,"Possibly justified by system urgency.","disagreement_directness")
add(43,2539,2539,"you want to have a provocative editorial position.","Advocates contestable editorial positions.","Values disagreement as a content strategy.","medium",NC,"Content advice, not interpersonal style.","disagreement_directness")
add(100,6053,6053,"I don't think it would make sense for you to resell.","Advises a partner against a heavier arrangement, with a reason.","Willing to steer partners toward the simpler option.","medium","Business terms omitted here.","Could reflect internal policy.","disagreement_directness")
# P9 sweeping/overconfident generalisations
add(45,2662,2662,None,"Claims everyone in marketing services is terrible ('underperform' substitution visible).","Uses sweeping generalisations; possible friction with agencies/vendors.","medium","Tone unknown; may be joking.","Hyperbole as humor.","sweeping_claims")
add(16,716,716,None,"'who cares what a thousand people think'.","Dismissive of a sample-size point (context missing).","low",NC,"Could be a reasoned point about audience fit.","sweeping_claims")
add(115,6897,6898,None,"Says he can 'eyeball the time intensity and quality' of work fast because he has only ever done B2B vertical SaaS marketing.","High confidence in own judgment drawn from experience.","medium",NC,"Defending workload under pressure.","self_assessment")
add(136,7755,7755,"I pride myself on my ability to turn these things out.","Self-praise about producing large content pieces.","Confident self-assessment, repeated across calls (E13, E30).","medium",NC,"Reassurance to manager.","self_assessment")
# P10 management stance & change over time
add(27,1363,1363,None,"Says that if he is not 'breathing down the necks' of direct reports they stop working.","Close-oversight management belief in 2025.","medium",NC,"Hyperbole while selling a time-tracking concept.","management_stance")
add(52,2914,2918,None,"Says AI use by his reports lowers quality; describes asking them to read text aloud and explain it.","2025 skepticism of team AI use; intensive review style.","medium","Reports' perspective absent.","Could be a vivid story for a vendor.","management_stance",["E34"])
add(121,7282,7282,None,"Says he now has the team run call recordings through 'your AI of choice' to extract priorities and action items.","2026 shift toward structured team AI use.","medium",NC,"Context-specific use, not a general change.","change_over_time",["E33"])
add(136,7756,7756,None,"Outlines first because 'the AI goes off the rails' if underspecified.","Specification-first approach to AI tools.","medium",NC,"None strong.","change_over_time")
# credit / help
add(1,6,7,None,"Opens by telling someone they did a great job and why documentation matters.","Gives specific credit linked to a reason.","medium",NC,"Opening pleasantry.","credit_help")
add(12,472,472,None,"Reassures a colleague who seems frustrated that they are doing well.","Notices others' emotional state and encourages.","medium","Colleague's actual state not visible.","Could be managing a sales call.","credit_help")
add(40,2369,2369,None,"Defends a colleague by noting they do unseen ops work.","Acknowledges invisible contributions.","medium",NC,"None strong.","credit_help")
add(46,2695,2695,None,"Invites questions so he does not have to 'middleware every single piece of WebDev'.","Pushes clarity up front to reduce his own gatekeeping load.","medium",NC,"None strong.","next_steps")
add(115,6900,6901,None,"Promises not to put more time into a project.","Stated commitment in response to (unseen) pushback; follow-through unknown.","medium",NC,"Concession under pressure.","next_steps")
add(26,1308,1308,None,"Jokes about 'thingify' and fancy buzzwords.","Self-deprecating humor about jargon.","medium",NC,"None strong.","humor")
# data quality
add(19,884,884,"Man, I underperform at creatives","Ungrammatical 'underperform' (26 hits/20 calls) in slots where another word fits.","Likely systematic editing substitution in the 'Edited' doc; tone evidence altered.","high","Original audio/transcript.","Transcriber artefact.","data_quality")
add(83,4840,4840,"she [name] Bediliated it","Transcription of an idiom ('[name] Bedelia-ed').","ASR artefact; also an example of characterizing a colleague's mistake.","high",NC,"None.","data_quality")
add(38,2217,2217,None,"Identical line appears at L3149 (c57); c38/c57, c127/c138, c15/c21 share duplicated text.","Duplicate call sections in source; counts slightly inflated.","high","Extraction method.","Repeated rehearsal script could produce same words (unlikely for 16 identical lines).","data_quality")
with open('ledger.jsonl','w') as f:
    for e in E: f.write(json.dumps(e,ensure_ascii=False)+'\n')
print(len(E))
for e in E: print(e['id'],e['call_id'],e['pattern_tag'])
