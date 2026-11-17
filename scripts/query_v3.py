import os
RAW = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'data', 'raw')
META = os.path.join(RAW, '..', 'metadata')  # place ACL Anthology data/xml here as acl_xml/, paperlists venue folders as paperlists/
# 확장 질의(v3): 보안 개념군에 안전·정책 용어 추가. v2와 동일 모집단.
import json,re,collections,xml.etree.ElementTree as ET
A = re.compile(r'\b(agent\w*|multi-agent|tool-augmented|tool-integrated|llm-integrated|mcp)\b', re.I)
B = re.compile(r'\b(llms?|language models?|lmms?|mllms?|vlms?|vision-language|multimodal|foundation models?|gpt\S*|chatgpt|ai agents?|web agents?|gui agents?|computer-use|agentic)\b', re.I)
C2 = re.compile(r'\b(attack\w*|secur\w*|inject\w*|privacy|defen[cs]\w*|defend\w*|adversar\w*|poison\w*|backdoor\w*|hijack\w*|exfiltrat\w*|authori[sz]\w*|access control|threat\w*)\b', re.I)
C3 = re.compile(r'\b(safe\w*|harm\w*|risk\w*|jailbreak\w*|vulnerab\w*|malicious\w*|leak\w*|permission\w*|guard\w*|polic(y|ies))\b', re.I)
def hit2(s): return bool(A.search(s) and B.search(s) and C2.search(s))
def hit3(s): return bool(A.search(s) and B.search(s) and (C2.search(s) or C3.search(s)))
out=[];stat=collections.OrderedDict();pop=0;noabs=0
SCOPE={'2022.emnlp':['main'],'2022.findings':['emnlp'],'2023.acl':['long','short'],'2023.findings':['acl','emnlp'],'2023.emnlp':['main'],
 '2024.acl':['long','short'],'2024.findings':['naacl','acl','emnlp'],'2024.emnlp':['main'],'2024.naacl':['long','short'],
 '2025.acl':['long','short'],'2025.findings':['naacl','acl','emnlp'],'2025.emnlp':['main'],'2025.naacl':['long','short'],
 '2026.acl':['long','short'],'2026.findings':['acl']}
def txt(e): return re.sub(r'\s+',' ',''.join(e.itertext())).strip() if e is not None else ''
for f,vols in SCOPE.items():
    r=ET.parse(os.path.join(META, 'acl_xml', f+'.xml')).getroot()
    for v in r.findall('volume'):
        if v.get('id') not in vols: continue
        yr=v.find('meta').findtext('year'); mon=v.find('meta').findtext('month')
        for p in v.findall('paper'):
            t=txt(p.find('title')); a=txt(p.find('abstract')); pop+=1; noabs+= (a=='')
            s=t+' '+a
            if hit3(s):
                out.append(dict(venue=f"{f}.{v.get('id')}",title=t,abstract=a,site=p.findtext('url') or '',doi=p.findtext('doi') or '',yr=yr,mon=mon,v2=hit2(s)))
ACC={'Poster','Spotlight','Oral','Top-25%','Top-5%','Technical','ICLR 2026 ConditionalPoster','ICLR 2026 ConditionalOral'}
TRK={'main','Datasets & Benchmarks','aaai special track'}
for f in ['iclr/iclr2023','iclr/iclr2024','iclr/iclr2025','iclr/iclr2026','icml/icml2023','icml/icml2024','icml/icml2025','icml/icml2026','nips/nips2023','nips/nips2024','nips/nips2025','aaai/aaai2023','aaai/aaai2024','aaai/aaai2025','ijcai/ijcai2023','ijcai/ijcai2024']:
    for x in json.load(open(os.path.join(META, 'paperlists', f+'.json'))):
        if x.get('status') not in ACC or x.get('track') not in TRK: continue
        pop+=1; a=(x.get('abstract') or '').strip(); noabs+=(a=='')
        s=(x.get('title') or '')+' '+a
        if hit3(s):
            out.append(dict(venue=f.split('/')[1],track=x['track'],title=x['title'].strip(),abstract=a,site=x.get('site') or '',v2=hit2(s)))
print('population',pop,'no-abstract',noabs,'v3 hits',len(out),'of which v2',sum(o['v2'] for o in out),'new',sum(not o['v2'] for o in out))
json.dump(out,open(os.path.join(RAW, 'hits_v3.json'),'w'),ensure_ascii=False,indent=1)
