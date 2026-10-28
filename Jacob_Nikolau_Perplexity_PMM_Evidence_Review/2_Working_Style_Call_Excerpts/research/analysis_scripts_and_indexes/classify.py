import json,re
d=json.load(open('call_index.json'))
def cat(t):
    tl=t.lower()
    if re.search(r'1:1|john / jacob|jacob john|jacob : john|jacob & john|jacob <> john|margaret / jacob|maggie / jacob|sara / jacob|jacob / eunsoo',tl): return '1:1'
    if 'pufferfish' in tl or 'shaun g' in tl or 'marlon' in tl or 'modern outbound' in tl: return 'agency/vendor'
    if 'slashblue' in tl or 'egnyte' in tl or 'channel partner' in tl or 'partner deck' in tl or 'propstream' in tl or 'bqe' in tl: return 'partner'
    if 'podcast' in tl or 'lionakis' in tl or 'zweig' in tl or 'roundtable' in tl or 'webinar' in tl or 'talentmax' in tl or 'bdc prep' in tl or 'aec' in tl or 'gather stat' in tl or 'prep' in tl: return 'external-event/content prep'
    if 'alon' in tl or 'matt' in tl or 'akshaya' in tl or 'sue cho' in tl: return 'unclear (possibly leadership/hiring/onboarding)'
    if re.search(r'meeting started|gmt20|recording transcript|hold do not',tl): return 'unclassifiable'
    return 'internal team/ops'
for c in d:
    c['category']=cat(c['title']); c['half']='2025' if c['date']<'2026' else '2026'; c['month']=c['date'][:7]
json.dump(d,open('work/index_classified.json','w'),indent=1)
from collections import Counter
print(Counter(c['category'] for c in d))
for c in d: print(c['call_id'],c['category'],c['title'][:50],sep='|')
