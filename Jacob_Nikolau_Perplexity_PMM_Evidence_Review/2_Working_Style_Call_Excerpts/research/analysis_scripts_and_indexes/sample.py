import json
d=json.load(open('work/index_classified.json'));L=open('calls.txt').read().split('\n')
from collections import defaultdict
bym=defaultdict(list)
for c in d:
    if c['n_statements']>=10: bym[c['month']].append(c)
plan=[]
for m in sorted(bym):
    seen=set()
    for c in sorted(bym[m],key=lambda c:-c['n_statements']):
        if c['category'] in seen: continue
        seen.add(c['category']); plan.append(c)
        if len(seen)==3: break
WIN=14
out=[]
for c in plan:
    s=c['line']+1+int((c['end_line']-c['line'])*0.4); e=min(s+WIN-1,c['end_line'])
    out.append({'call_id':c['call_id'],'start':s,'end':e})
json.dump(out,open('work/sample_plan.json','w'))
print(len(plan), sum(o['end']-o['start']+1 for o in out))
for c in plan: print(c['month'],c['call_id'],c['category'],c['title'][:40])
