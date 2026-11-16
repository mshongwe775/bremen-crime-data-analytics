from pathlib import Path
import re,json,hashlib,pandas as pd
root=Path(__file__).resolve().parents[2]
out=root/'outputs/member_06'
prepared=pd.read_parquet(root/'outputs/member_01/reports_prepared.parquet',columns=['report_id','title_en','description_en','url'])
ids=set(pd.read_csv(out/'age50plus_candidates.csv').report_id)|set(pd.read_csv(out/'age50plus_controls.csv').report_id)
f=prepared.loc[prepared.report_id.isin(ids)].copy()
age_pattern=r'\b\d{1,3}(?:\s*(?:,|and|to|-)\s*\d{1,3})*[\s-]+years?[\s-]+olds?\b|\b(?:aged?|ages?)\s+(?:of\s+|between\s+)?\d{1,3}(?:\s*(?:,|and|to|-)\s*\d{1,3})*\b'
older_pattern=r'\b(?:elderly|pensioners?|senior(?: citizens?)?s?)\b|\bin (?:his|her|their) (?:fifties|sixties|seventies|eighties|nineties)\b'
nouns=r'(?:man|woman|person|female|male|victim|resident|Bremen resident|senior citizen|pensioner|pedestrian|cyclist|driver|passenger|employee|worker|security (?:guard|employee)|owner|customer|tourist|couple|wife|husband|patient)'
adverbs=r'(?:(?:also|reportedly|allegedly|suddenly|seriously|critically|lightly|slightly|severely|fatally|repeatedly|brutally|sexually|initially|previously|subsequently)\s+){0,4}'
attack=r'(?:robbed|mugged|ambushed|attacked|assaulted|defrauded|scammed|stabbed|shot|beaten|hit|struck|punched|kicked|threatened|harassed|molested|abused|blackmailed|tied|locked|pushed|knocked|dragged)'
aux=r'(?:was|were|is|has been|had been|have been)\s+'
passive=re.compile(r'^\s*[^,;.!?]{0,60}?'+aux+adverbs+attack+r'\b',re.I)
active_before=re.compile(r'\b(?:'+attack+r'|mugged|grabbed|injured|hit|ran over|knocked down|defraud|targeting)\s+(?:(?:a|an|the|another|one)\s+)?$',re.I)
injury=re.compile(r'^\s*(?:'+nouns+r'\s+)?(?:'+aux+adverbs+r'(?:injured|killed)|(?:suffered|sustained)\s+(?:(?:minor|serious|severe|slight|fatal)\s+)?(?:injur|wound|burn|fractur))',re.I)
other=re.compile(r'^\s*(?:(?:man|woman|male|female)\s+)?(?:suspect|suspected|perpetrator|offender|witness|police officer|officer|investigator|spokesperson|captain|first officer|professional driver)|^\s*(?:'+nouns+r'\s+)?(?:'+aux+r'(?:provisionally |temporarily )?(?:arrested|apprehended)|(?:drove|was driving|stole|fled|resisted|attempted to steal|attacked (?:a|the)|robbed (?:a|the)))',re.I)

def assess(title,description):
 source=title+'\n'+description
 normalized=re.sub(r'[\u2010\u2011\u2012\u2013\u2014\u2212]','-',source)
 findings=[]
 for sentence in re.split(r'(?<=[.!?])\s+(?=[A-Z])|[\r\n]+',normalized):
  matches=list(re.finditer(age_pattern,sentence,re.I))
  for i,m in enumerate(matches):
   ages=[int(a) for a in re.findall(r'\d+',m.group()) if 1<=int(a)<=120]
   if not any(a>=50 for a in ages):continue
   before=sentence[max(0,m.start()-90):m.start()]
   after=sentence[m.end():matches[i+1].start() if i+1<len(matches) else len(sentence)]
   exact=len(ages)==1
   property_target=bool(re.search(r'(?:stole|stolen|snatched|taking|ripped|grabbed)[^.;]{0,75}\b(?:from|of)\s+(?:a |an |the )?$',before,re.I))
   direct=bool(property_target or passive.search(after) or active_before.search(before) or re.match(r'^\s*(?:'+nouns+r'\s+)?(?:fell victim|became (?:a |the )?victim)',after,re.I))
   direct=direct or bool(re.match(r'^\s*[^,;.!?]{0,50}?became (?:a |the )?victim',after,re.I))
   direct=direct or bool(re.match(r'^\s*[^,;.!?]{0,40}?(?:has fallen|had fallen|became the target of a (?:phone )?scam)',after,re.I))
   direct=direct or bool(re.match(r'^\s*[^,;.!?]{0,35}?had (?:his|her|their)[^.;]{0,65}(?:stolen|taken|snatched|torn|ripped)',after,re.I))
   harmed=bool(injury.search(after) or re.match(r'^\s*[^,;.!?]{0,45}?suffered (?:life-threatening |serious |severe |minor |slight )?(?:injur|wound|fractur)',after,re.I))
   role=bool(other.search(after) or re.search(r'\b(?:suspect|offender|perpetrator|witness|officer|investigator)\s+(?:aged\s+)?$',before,re.I))
   role=role or bool(re.search(r'\b(?:arrested|apprehended|checked|stopped|suspect|suspects|burglars|perpetrator|witness)\s+(?:a |an |the |two |aged )?$',before,re.I))
   role=role or bool(re.match(r'^\s*(?:man |woman )?(?:driver|skipper|master|suspect|witness|officer)\b',after,re.I))
   role=role or bool(re.match(r'^\s*[^,;.!?]{0,25}?(?:set [^.;]{0,30}on fire|was released|was taken into (?:temporary )?custody|was.*under the influence|stole|resisted)',after,re.I))
   role=role or bool(re.match(r'^\s*(?:(?:man|woman|Bremen resident|tenant)\s+)?(?:(?:had |allegedly |reportedly |racially )?)(?:threatened|insulted|set [^.;]{0,20}on fire|fired|shot at|attacked|stole|broke into|attempted to steal|was.*(?:suspected|identified as a suspect))',after,re.I))
   role=role or bool(re.search(r'\b(?:suspects|perpetrators|drivers|witnesses|burglars|offenders)[^.;]{0,15}(?:aged |\()?$',before,re.I))
   if direct and exact:kind='explicit_text_older_victim';reason='Exact age '+str(ages[0])+' is directly linked to a reported target of violence, coercion or deception.'
   elif direct or harmed:kind='possible_older_victim_insufficient_evidence';reason='Older age/range and harmful-event wording occur together; exact age-to-victim role or accident responsibility needs confirmation.'
   elif role:kind='older_person_other_role';reason='The age '+str(ages)+' is linked to a suspect, witness, official or driver role without a clear victim link in this clause.'
   elif re.match(r'^\s*(?:tree|building|house|car|vehicle|ship|bridge|bomb|dog|cat|roebuck)\b',after,re.I):kind='no_evidence_of_older_victim';reason='The qualifying number describes an object or animal.'
   else:kind='unclear';reason='An older numeric age is present, but a reliable victim/other-person role link is unresolved.'
   findings.append((kind,sentence.strip(),reason,ages))
  if re.search(older_pattern,sentence,re.I) and not matches:
   targeted=bool(re.search(attack+r'[^.;]{0,45}(?:elderly|senior|pensioner)|(?:elderly|senior|pensioner)[^.;]{0,55}'+aux+adverbs+attack,sentence,re.I))
   if targeted:
    findings.append(('possible_older_victim_insufficient_evidence',sentence.strip(),'Older-person wording is linked to an apparent victim; the exact numeric age50+ threshold remains unsupported.',[]))
   elif not any(v[3] for v in findings):
    findings.append(('unclear',sentence.strip(),'Older-person wording appears without a supported exact age-to-victim link; generic prevention wording can be a false positive.',[]))
 numeric_ages={a for v in findings for a in v[3] if a>=50}
 other_ages={a for v in findings if v[0]=='older_person_other_role' for a in v[3] if a>=50}
 if numeric_ages and numeric_ages<=other_ages and not any(v[0] in ['explicit_text_older_victim','possible_older_victim_insufficient_evidence'] for v in findings):
  findings=[v for v in findings if v[0]!='unclear']
 priority=['explicit_text_older_victim','possible_older_victim_insufficient_evidence','unclear','older_person_other_role','no_evidence_of_older_victim']
 if findings:
  kind=next(k for k in priority if any(v[0]==k for v in findings))
  selected=[v for v in findings if v[0]==kind][:2]
  evidence=' | '.join(source[normalized.find(v[1]):normalized.find(v[1])+len(v[1])] for v in selected)
  reason=selected[0][2]
  ages=sorted({a for v in findings for a in v[3] if a>=50})
 else:
  kind='no_evidence_of_older_victim';evidence='';reason='The full-text rules identify no supported older-victim link; age references may concern objects or generic wording. This is a text-screen result.';ages=[]
 return kind,evidence,reason,json.dumps(ages)

values=[assess(r.title_en,r.description_en) for r in f.itertuples()]
f[['ai_victim_group','evidence_excerpt','ai_justification','qualifying_ages']]=pd.DataFrame(values,index=f.index)
f['description_sha256']=f.description_en.map(lambda s:hashlib.sha256(s.encode()).hexdigest())
f['assessment_method']='Conservative AI-authored age/person text rules on the complete title and description; unresolved links retained'
f['human_confirmation_required']=True
f['assessment_status']='ai_assisted_unapproved'
f=f.drop(columns='description_en')
context=pd.read_csv(out/'age50plus_context_assessments.csv',keep_default_na=False)
assert context.report_id.is_unique and set(context.report_id)<=set(f.report_id)
source=prepared.set_index('report_id')
for r in context.itertuples():
 assert hashlib.sha256(source.loc[r.report_id,'description_en'].encode()).hexdigest()==r.description_sha256
 combined=source.loc[r.report_id,'title_en']+'\n'+source.loc[r.report_id,'description_en']
 assert all(quote in combined for quote in r.evidence_excerpt.split(' | ')),r.report_id
f=f.set_index('report_id')
for column in ['ai_victim_group','ai_justification','evidence_excerpt','assessment_method']:
 f.loc[context.report_id,column]=context.set_index('report_id')[column]
result=f.reset_index()
existing=pd.read_csv(out/'age50plus_assessments.csv',keep_default_na=False)
pd.testing.assert_frame_equal(result,existing,check_dtype=False)
print('Saved computational classifications reproduce exactly; evidence file unchanged.')
print(f.ai_victim_group.value_counts().to_string())
print('Reports classified:',len(f),'| Additional AI context readings:',len(context))
