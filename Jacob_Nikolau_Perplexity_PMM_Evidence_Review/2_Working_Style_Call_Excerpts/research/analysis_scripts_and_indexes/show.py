import json,sys
d=json.load(open('work/index_classified.json'));L=open('calls.txt').read().split('\n')
H=json.load(open('work/lex_hits.json'))
def cid(n):
    for c in d:
        if c['line']<=n<=c['end_line']: return c
key=sys.argv[1]; mx=int(sys.argv[2]) if len(sys.argv)>2 else 40; w=int(sys.argv[3]) if len(sys.argv)>3 else 260
lines=H[key]['lines'] if key in H else [int(x) for x in key.split(',')]
step=max(1,len(lines)//mx)
for n in lines[::step][:mx]:
    c=cid(n); print(f"L{n}|c{c['call_id']}|{c['date']}|{c['category'][:10]}| {L[n-1][:w]}")
