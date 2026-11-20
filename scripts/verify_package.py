"""Offline package integrity checks using only the Python standard library."""
from pathlib import Path
import csv
import hashlib
import json
import re

ROOT=Path(__file__).resolve().parents[1]

def rows(name):
    with (ROOT/name).open(encoding='utf-8-sig',newline='') as f:return list(csv.DictReader(f))

def main():
    checksum=ROOT/'SHA256SUMS'
    assert checksum.exists(),'SHA256SUMS missing; use the complete replication package.'
    count=0
    for line in checksum.read_text().splitlines():
        digest,name=line.split('  ',1)
        assert hashlib.sha256((ROOT/name).read_bytes()).hexdigest()==digest,name
        count+=1
    panel=rows('data/schools_5131.csv')
    assert len(panel)==5131 and sum(int(r['AI_final']) for r in panel)==312
    assert len({r['_k'] for r in panel})==5131
    assert all(re.fullmatch(r'\d{12}',r['_k']) for r in panel)
    assert all(not r['lea_crdc'] or re.fullmatch(r'\d{7}',r['lea_crdc']) for r in panel)
    dictionary={r['variable'] for r in rows('docs/variable_dictionary.csv')}
    assert set(panel[0])<=dictionary
    for file,n,ai,leas in [('model_full_3827.csv',3827,258,2222),('model_existing_cs_2900.csv',2900,235,1800)]:
        sample=rows('data/'+file)
        assert len(sample)==n and sum(int(r['AI_final']) for r in sample)==ai
        assert len({r['lea_crdc'] for r in sample})==leas
        assert len({r['state_abbr'] for r in sample})==36
        assert set(sample[0])<=dictionary
    spec=json.loads((ROOT/'analysis_spec.json').read_text())
    assert len(spec['features'])==22 and spec['parameters']==58
    assert spec['status']=='PUBLIC_REPOSITORY'
    print(f'PASS: {count} checksums; 5131/312 labels; 3827/258 and 2900/235 model samples; all data fields documented. Verification performs no upload.')

if __name__=='__main__':main()
