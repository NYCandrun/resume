import json,sys
d={c['call_id']:c for c in json.load(open('work/index_classified.json'))};L=open('calls.txt').read().split('\n')
P=json.load(open('work/sample_plan.json'))
a,b=int(sys.argv[1]),int(sys.argv[2])
for o in P[a:b]:
    c=d[o['call_id']]; print(f"### c{c['call_id']} {c['date']} {c['title'][:40]} [{c['category']}]")
    for n in range(o['start'],o['end']+1): print(f"L{n}: {L[n-1][:300]}")
