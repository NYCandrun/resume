import json,re,sys
d=json.load(open('work/index_classified.json'))
L=open('calls.txt').read().split('\n')
def cid(n):
    for c in d:
        if c['line']<=n<=c['end_line']: return c
pats={
'i_think':r"\bI think\b",'i_dont_know':r"\bI don'?t know\b",'not_sure':r"\bnot sure\b",'could_be_wrong':r"could be wrong|might be wrong|correct me",
'push_back':r"push back|disagree|I don'?t agree|I don'?t think (that|we|it)",'tradeoff':r"trade-?off|on the other hand|the downside|pros and cons",
'reason':r"the reason|because\b",'example':r"for example|for instance|like if|imagine|analogy|think of it",
'what_if':r"what if|what about|why (do|are|would|is|don't)",'question':r"\?\s*$",'ill':r"\bI'll\b|\bI will\b|I'm going to",
'can_you':r"can you|could you|would you",'credit':r"great job|good job|thank|nice work|appreciate|awesome work|love (that|this|it)",
'actually':r"\bactually\b",'youre_right':r"you'?re right|good point|fair point|that'?s fair|changed my mind|I stand corrected",
'customer':r"\bcustomer|\bclient|\bbuyer|\baudience|\bpersona",'value':r"\bvalue\b|\broi\b|pain point|outcome",
'data':r"\bdata\b|\bnumbers?\b|\bmetric|\bpercent|%|attribution|pipeline",'owner_next':r"next step|owner|by (monday|tuesday|wednesday|thursday|friday|end of)|deadline|action item",
'help':r"happy to help|let me know if|I can help|if you need",'humor':r"\bhaha|\blol\b|joke|kidding|funny",
'ai':r"\bAI\b|claude|chatgpt|gpt|agent",'frustration':r"frustrat|annoy|drives me|I hate|ridiculous|waste of time",
}
res={}
for k,p in pats.items():
    r=re.compile(p,re.I); hits=[i+1 for i,l in enumerate(L) if r.search(l)]
    calls=set(); h={'2025':0,'2026':0}
    for n in hits:
        c=cid(n)
        if c: calls.add(c['call_id']); h[c['half']]+=1
    res[k]={'hits':len(hits),'calls':len(calls),'by_half':h,'lines':hits}
w25=sum(c['words'] for c in d if c['half']=='2025'); w26=sum(c['words'] for c in d if c['half']=='2026')
print('words',w25,w26)
for k,v in res.items(): print(f"{k:14} hits={v['hits']:4} calls={v['calls']:3} 2025/kw={v['by_half']['2025']/w25*1000:.2f} 2026/kw={v['by_half']['2026']/w26*1000:.2f}")
json.dump({k:{**v} for k,v in res.items()},open('work/lex_hits.json','w'))
