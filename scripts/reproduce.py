"""Reproduce the fixed CSE analysis from the prepared school-level data.

Offline only. No crawling, downloads, Git operations, or repository uploads.
The two model specifications and their samples are fixed in analysis_spec.json.
"""
from pathlib import Path
import json
import platform
import sys
import numpy as np
import pandas as pd
import scipy
from scipy.optimize import minimize
from scipy.special import expit,logit
from scipy.stats import norm

ROOT=Path(__file__).resolve().parents[1]
OUT=ROOT/'outputs'
SPEC=json.loads((ROOT/'analysis_spec.json').read_text())
FEATURES=SPEC['features']
REF=ROOT/'reference_results'
Z=norm.ppf(.975)
ID_TYPES={'_k':str,'lea_crdc':str,'county_geoid':str}

def save(d,name):
    path=OUT/name;path.parent.mkdir(parents=True,exist_ok=True)
    d.to_csv(path,index=False)

def select_samples(p):
    complete=p[[*FEATURES,'AI_final','state_abbr','lea_crdc']].notna().all(axis=1)
    full=p.loc[complete].copy()
    full=full.loc[full.groupby('state_abbr').AI_final.transform('nunique').eq(2)]
    cs=p.loc[p.cs_observed_status.eq(1)&complete].copy()
    cs=cs.loc[cs.groupby('state_abbr').AI_final.transform('nunique').eq(2)]
    for key,d in [('full',full),('cs_existing',cs)]:
        n=SPEC['models'][key]['n'];ai=SPEC['models'][key]['AI'];g=SPEC['models'][key]['LEAs']
        assert (len(d),int(d.AI_final.sum()),d.lea_crdc.nunique(),d.state_abbr.nunique())==(n,ai,g,36)
        fixed=pd.read_csv(ROOT/'data'/SPEC['models'][key]['sample_file'],dtype=ID_TYPES)
        assert set(d._k)==set(fixed._k),(key,'sample IDs differ')
        # Match the saved row order, then confirm all model values exactly.
        d=d.set_index('_k').loc[fixed._k].reset_index()
        for term in FEATURES:assert np.allclose(d[term],fixed[term]),(key,term)
        yield key,d

def fit(key,d):
    xs=d[FEATURES].astype(float);binary=xs.nunique().le(2)
    center=xs.mean().where(~binary,0.);scale=xs.std(ddof=0).where(~binary,1.)
    states=pd.get_dummies(d.state_abbr,prefix='state',drop_first=True,dtype=float)
    assert sorted(d.state_abbr.unique())[0]=='AL'
    names=['intercept',*FEATURES,*states.columns]
    x=np.column_stack([np.ones(len(d)),(xs-center)/scale,states]);y=d.AI_final.to_numpy(float)
    n,k=x.shape;g=d.lea_crdc.nunique();assert k==58
    def objective(b):
        eta=x@b
        return float(np.logaddexp(0,eta).sum()-y@eta)
    def score(b):return x.T@(expit(x@b)-y)
    def hessian(b):
        p=expit(x@b)
        return x.T@(x*(p*(1-p))[:,None])
    initial=np.zeros(k);initial[0]=logit(y.mean())
    result=minimize(objective,initial,jac=score,hess=hessian,method='trust-exact',options={'gtol':1e-9,'maxiter':1000})
    b=result.x;mu=expit(x@b);maxscore=float(np.abs(score(b)).max());assert maxscore<1e-6
    bread=np.linalg.inv(hessian(b))
    scores=pd.DataFrame(x*(y-mu)[:,None]).assign(lea=d.lea_crdc.to_numpy()).groupby('lea').sum().to_numpy()
    covariance=bread@(scores.T@scores)@bread*(g/(g-1))*((n-1)/(n-k))
    transform=np.eye(k)
    for j,term in enumerate(FEATURES,1):
        transform[j,j]=1/scale[term];transform[0,j]=-center[term]/scale[term]
    beta=transform@b;cov=transform@covariance@transform.T;se=np.sqrt(np.diag(cov))
    co=pd.DataFrame(dict(term=names,beta=beta,SE_LEA=se,CI_beta_low=beta-Z*se,CI_beta_high=beta+Z*se,p=2*norm.sf(np.abs(beta/se))))
    expected=pd.read_csv(REF/f'{key}_all_parameters.csv')
    assert names==expected.term.tolist()
    err=float(np.abs(beta-expected.beta).max());seerr=float(np.abs(se-expected.SE_LEA).max())
    assert err<1e-6 and seerr<1e-6,(key,err,seerr)
    summary=dict(n=n,AI=int(y.sum()),LEAs=g,states=36,parameters=k,log_likelihood=-objective(b),AIC=2*objective(b)+2*k,
        converged=maxscore<1e-6,max_abs_score=maxscore,max_saved_beta_difference=err,max_saved_SE_difference=seerr)
    (OUT/key).mkdir(parents=True,exist_ok=True)
    save(co,f'{key}/all_parameters.csv');np.save(OUT/key/'covariance_original_units.npy',cov)
    (OUT/key/'model_summary.json').write_text(json.dumps(summary,indent=2))
    save(d[['_k','AI_final','state_abbr','lea_crdc']].assign(predicted_probability=mu),f'{key}/predictions.csv')
    contrasts=[];lookup=co.set_index('term')
    for item in SPEC['contrasts']:
        r=lookup.loc[item['term']];factor=item['factor']
        contrasts.append(dict(**item,log_odds=r.beta*factor,se=r.SE_LEA*factor,
            odds_ratio=np.exp(r.beta*factor),or_low=np.exp(r.CI_beta_low*factor),or_high=np.exp(r.CI_beta_high*factor),p_value=r.p))
    contrasts=pd.DataFrame(contrasts)
    fixed=pd.read_csv(REF/'supplementary_data'/f'Supplementary_Table_S1_{key}_contrasts.csv')
    for term in ['odds_ratio','or_low','or_high','p_value']:
        assert np.allclose(contrasts[term],fixed[term],rtol=1e-6,atol=1e-7),(key,term)
    save(contrasts,f'tables/Supplementary_Table_S1_{key}_contrasts.csv')
    reported=co.rename(columns={'beta':'coefficient','SE_LEA':'se_lea','CI_beta_low':'ci_low','CI_beta_high':'ci_high','p':'p_value'}).copy()
    factor=np.where(reported.term.eq('district_cs_loo'),.1,1.)
    for column in ['coefficient','se_lea','ci_low','ci_high']:reported[column]*=factor
    reported['odds_ratio']=np.exp(reported.coefficient);reported['or_low']=np.exp(reported.ci_low);reported['or_high']=np.exp(reported.ci_high)
    fixed=pd.read_csv(REF/'supplementary_data'/f'Supplementary_Table_S1_{key}_all_terms.csv')
    assert reported.term.tolist()==fixed.term.tolist()
    reported['unit']=fixed.unit
    reported['internal_scaled_coefficient']=b
    for column in ['coefficient','se_lea','ci_low','ci_high','p_value']:
        assert np.allclose(reported[column],fixed[column],rtol=1e-6,atol=1e-6),(key,column)
    save(reported,f'tables/Supplementary_Table_S1_{key}_all_terms.csv')
    return d,co,cov,summary

def probability_curves(d,co,cov):
    names=co.term.tolist();b=co.beta.to_numpy()
    x=np.column_stack([np.ones(len(d)) if t=='intercept' else d.state_abbr.eq(t[6:]).to_numpy(float) if t.startswith('state_') else d[t] for t in names])
    rows=[]
    for term in SPEC['probability_curve_predictors']:
        raw=d[term]*100 if term in ['cs_enrollment_share','district_cs_loo'] else np.exp(d[term]) if term=='cd_log_med_income' else np.expm1(-d[term])
        low,high=np.quantile(raw,[.05,.95])
        for value in np.linspace(low,high,81):
            tvalue=value/100 if term in ['cs_enrollment_share','district_cs_loo'] else np.log(value) if term=='cd_log_med_income' else -np.log1p(value)
            xp=x.copy();xp[:,names.index(term)]=tvalue;p=expit(xp@b);m=p.mean()
            grad=np.mean(xp*(p*(1-p))[:,None],axis=0);se=np.sqrt(grad@cov@grad)
            lo,hi=expit(logit(m)+np.array([-1,1])*Z*se/(m*(1-m)))
            rows.append(dict(term=term,x=value,mean=m,low=lo,high=hi,se=se,n=len(d)))
    table=pd.DataFrame(rows);fixed=pd.read_csv(REF/'full_probability_curves.csv')
    for c in ['x','mean','low','high','se']:assert np.allclose(table[c],fixed[c],rtol=1e-5,atol=1e-7),c
    save(table,'full/probability_curves.csv')

def descriptions(p,models):
    rows=[]
    ref=pd.read_csv(REF/'supplementary_data/Supplementary_Table_S3_descriptive_statistics.csv')
    sets={'Full descriptive sample':p,'Full-model estimation sample':models['full'][0],'CS-providing estimation sample':models['cs_existing'][0]}
    for item in ref.itertuples():
        d=sets[item.sample]
        if item.term=='Rural':v=1-d[['City','Suburb','Town']].sum(axis=1)
        elif item.term=='csr_dist_km':
            v=d.csr_dist_km if 'csr_dist_km' in d else np.expm1(-d.cs_academic_proximity)
        else:v=d[item.term].copy()
        if item.term in ['cs_enrollment_share','district_cs_loo','cd_ba_plus_share']:v=v*100
        elif item.term in ['log_enrollment','cd_log_med_income']:v=np.exp(v)
        elif item.term=='log_certified_adv_stem_classes':v=np.expm1(v)
        v=v.dropna();r=item._asdict()
        r['n']=len(v)
        if item.type=='continuous':
            r.update(mean=v.mean(),sd=v.std(),median=v.median(),q1=v.quantile(.25),q3=v.quantile(.75))
            assert np.allclose([r[c] for c in ['mean','sd','median','q1','q3']],[getattr(item,c) for c in ['mean','sd','median','q1','q3']],rtol=1e-10,atol=1e-10)
        else:
            r.update(positive_n=int(v.sum()),percent=100*v.mean())
            assert np.allclose([r['positive_n'],r['percent']],[item.positive_n,item.percent])
        assert r['n']==item.n
        rows.append(r)
    save(pd.DataFrame(rows),'tables/Supplementary_Table_S3_descriptive_statistics.csv')
    states=pd.read_csv(REF/'supplementary_data/Supplementary_Table_S2_state_distribution.csv')
    counts=p.groupby('state_abbr').AI_final.agg(['size','sum'])
    for r in states.itertuples():
        n=int(counts.loc[r.state_abbr,'size']) if r.state_abbr in counts.index else 0
        ai=int(counts.loc[r.state_abbr,'sum']) if r.state_abbr in counts.index else 0
        assert (n,ai)==(r.n,r.ai)
    save(states,'tables/Supplementary_Table_S2_state_distribution.csv')
    for grouping in ['locale','region']:
        d=p.groupby(grouping).AI_final.agg(n='size',ai='sum').reset_index();d['ai_percent']=100*d.ai/d.n
        save(d,f'descriptive/{grouping}_distribution.csv')
    cs=p[p.cs_observed_status.eq(1)]
    d=cs.groupby('locale').AI_final.agg(n='size',ai='sum').reset_index();d['ai_percent']=100*d.ai/d.n
    save(d,'descriptive/existing_cs_locale.csv')
    save(p[p.cs_observed_status.notna()].groupby(['cs_observed_status','AI_final']).size().rename('n').reset_index(),'descriptive/CS_AI_joint_counts.csv')
    rows=[]
    for label,d in [('all_schools',p),('existing_cs',cs)]:
        c=d.dropna(subset=[*FEATURES,'lea_crdc','state_abbr','AI_final'])
        retain=c.groupby('state_abbr').AI_final.transform('nunique').eq(2)
        rows.append(dict(sample=label,descriptive_n=len(d),descriptive_AI=int(d.AI_final.sum()),complete_n=len(c),complete_AI=int(c.AI_final.sum()),excluded_constant_state_n=int((~retain).sum()),model_n=int(retain.sum()),model_AI=int(c.loc[retain,'AI_final'].sum())))
    save(pd.DataFrame(rows),'sample_flow.csv')
    f=models['full'][3];c=models['cs_existing'][3]
    info=[('Schools',f['n'],c['n']),('AI-positive schools',f['AI'],c['AI']),('LEA clusters',f['LEAs'],c['LEAs']),('State-level jurisdictions',36,36),('Estimated parameters (including intercept)',58,58),('Converged','Yes','Yes'),('Log-likelihood',round(f['log_likelihood'],2),round(c['log_likelihood'],2)),('AIC',round(f['AIC'],2),round(c['AIC'],2))]
    save(pd.DataFrame(info,columns=['Model characteristic','Full model','Existing-CS model']),'tables/Supplementary_Table_S4_model_information.csv')

def main():
    OUT.mkdir(exist_ok=True)
    p=pd.read_csv(ROOT/'data/schools_5131.csv',dtype=ID_TYPES)
    assert len(p)==5131 and int(p.AI_final.sum())==312 and p._k.is_unique
    assert int(p.cs_loo_singleton_zero_applied.sum())==1712
    assert p.district_cs_loo.notna().sum()==4999
    fitted={}
    for key,d in select_samples(p):
        print('Reproducing',key,'N=',len(d),flush=True)
        fitted[key]=fit(key,d)
        print(json.dumps(fitted[key][3]),flush=True)
    probability_curves(*fitted['full'][:3]);descriptions(p,fitted)
    result=dict(status='PASS',new_model_specifications=False,upload_performed=False,
        models={k:v[3] for k,v in fitted.items()},descriptive_statistics_rows_verified=72,
        probability_curve_points_verified=324,software=dict(python=platform.python_version(),numpy=np.__version__,pandas=pd.__version__,scipy=scipy.__version__))
    (OUT/'verification.json').write_text(json.dumps(result,indent=2))
    print('PASS: both fixed models, descriptive statistics, and probability curves reproduced. No files uploaded.')

if __name__=='__main__':main()
