import csv,json,collections,re
remap={'C3':'S02','S2':'S07','S3':'S05','S1':'Q078'}
F1={}
for f in ['FT_1.tsv','FT_2.tsv','FT_3.tsv','FT_4.tsv','FT_5.tsv','FT_6a.tsv','FT_6b.tsv','pb/FT_new.tsv']:
    for r in csv.DictReader(open(f),delimiter='\t'):
        rid=remap.get(r['rid'],r['rid']); r['rid']=rid; F1[rid]=dict(r)
# adjudication of full-text disagreements (overlap subset)
ADJ={
 '10.18653/v1/2026.findings-acl.240':{},
 'M026':{'public_bench':'N'},
 'M031':{'stage':'P;A','public_bench':'N','fpr':'Y'},
 'M052':{'stage':'I','public_bench':'N'},
 'M067':{'stage':'M;C','public_bench':'Y'},
 'M101':{'stage':'A;O','judge':'SEP','policy_src':'-'},
 'M109':{'judge':'ML;SEP;RULE','utility':'N','overhead':'Y:latency'},
 'M113':{'stage':'I','judge_exposed':'Y'},
 'M144':{'stage':'I','adversarial':'N','adaptive':'NA'},
 'N046':{'judge':'SEP;RULE'},
 'Q502':{'judge_exposed':'Y'},
 'Q557':{'utility':'Y'},
 'S04':{'stage':'P;A'},
}
for k,v in ADJ.items(): F1[k].update(v)
final=json.load(open('final_codes.json'))
fin={f['id']:f for f in json.load(open('final_includes_pre.json'))}
rows=[]
for i,c in final.items():
    if c['decision']!='INC': continue
    m=fin[i]; r=dict(id=i,title=m['title'],venue=m['venue'],year=m['year'],route=m['route'],site=m.get('site',''),arxiv_id=m.get('arxiv_id','-'))
    for k in ['type','actor','T','T5sub','viol','multistage','embodied','D']: r[k]=c[k]
    r['coding_source']=c['source']
    if i in F1:
        for k in ['src','arxiv_id','arxiv_v1','stage','A_mode','judge','policy_src','judge_exposed','granularity','decisions','adversarial','adaptive','bench','public_bench','n_models','utility','overhead','fpr','hitl_burden','evidence']:
            r['ft_'+k]=F1[i].get(k,'')
    rows.append(r)
json.dump(rows,open('FINAL_CORPUS.json','w'),ensure_ascii=False,indent=1)
print(len(rows))
# ---- v10: judge input exposure level (dual full-text recoding + adjudication) ----
import csv as _csv
_A={};_B={};_ADJ={}
for f in ['pb/expo_1_A.tsv','pb/expo_2_A.tsv']:
    for r in _csv.DictReader(open(f),delimiter='\t'): _A[r['id']]=r
for f in ['pb/expo_1_B.tsv','pb/expo_2_B.tsv']:
    for r in _csv.DictReader(open(f),delimiter='\t'): _B[r['id']]=r
for r in _csv.DictReader(open('pb/expo_adj.tsv'),delimiter='\t'): _ADJ[r['id']]=r['final']
for r in rows:
    if r['id'] in _A:
        a,b=_A[r['id']]['judge_input'],_B[r['id']]['judge_input']
        r['ft_judge_input_A']=a; r['ft_judge_input_B']=b
        r['ft_judge_input']=_ADJ.get(r['id'], a if a==b else '?')
json.dump(rows,open('FINAL_CORPUS.json','w'),ensure_ascii=False,indent=1)
print('judge_input merged',sum('ft_judge_input' in r for r in rows))
