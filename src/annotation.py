"""Sample annotation schema, label quality checks, and rater agreement."""
from collections import Counter
import json
from pathlib import Path
VALID={'factuality':{'supported','unsupported','not_verifiable'},'tone':{'professional','casual','inappropriate'},'safety':{'safe','review','unsafe'}}

def validate(item):
    errors=[]
    if not item.get('id'):errors.append('missing id')
    if not item.get('text'):errors.append('missing text')
    labels=item.get('labels',{})
    for key,allowed in VALID.items():
        if labels.get(key) not in allowed:errors.append(f'invalid {key}: {labels.get(key)!r}')
    if not item.get('rationale'): errors.append('missing rationale')
    return errors

def agreement(items,label='factuality'):
    """Percent exact agreement for pairs of independent annotations (not kappa)."""
    pairs=[x for x in items if 'rater_a' in x and 'rater_b' in x]
    if not pairs:return {'pairs':0,'agreement':None}
    matches=sum(x['rater_a'][label]==x['rater_b'][label] for x in pairs)
    return {'pairs':len(pairs),'agreements':matches,'agreement':round(matches/len(pairs),3)}

def adjudicate(item):
    if item.get('rater_a')==item.get('rater_b'):return 'agree'
    return 'needs_adjudication'

if __name__=='__main__':
    items=json.loads(Path('data/annotations.json').read_text())
    print(json.dumps({'schema_errors':{i['id']:validate(i) for i in items if validate(i)},'agreement':agreement(items),'adjudications':{i['id']:adjudicate(i) for i in items}},indent=2))
