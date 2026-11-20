# AI curriculum opportunity in U.S. high schools: CSE replication package

**Replication package, version 0.1.0 (20 November 2026).**

Repository: https://github.com/iriskk99/ai-curriculum-institutional-foundations

This package supports *The Institutional Foundations of AI Education: Educational Capacity and Curriculum Inequality in U.S. High Schools*, prepared for **Computer Science Education**. It contains prepared school-level analytical data and executable offline replication code. It is not a raw website crawl or a new classification of schools.

## Fixed analytical version

| Sample | Schools | AI-positive | LEAs | State-level jurisdictions |
|---|---:|---:|---:|---:|
| Full descriptive sample | 5,131 | 312 | 3,050 linked | — |
| Full logistic model | 3,827 | 258 | 2,222 | 36 |
| Existing-CS logistic model | 2,900 | 235 | 1,800 | 36 |

The outcome is qualifying formal AI/ML curriculum evidence observed in **June 2026**. The researcher reviewed the extracted text snippets for all 312 positive labels. Zero means that no qualifying evidence was observed, not a verified absence of all AI instruction. Labels are unchanged.

Both models use ordinary unpenalized binary logistic maximum likelihood, state fixed effects (Alabama reference), and LEA-clustered sandwich standard errors with finite-sample correction. Each has 22 non-state explanatory terms and 58 parameters. Official single-high-school LEAs have CS-LOO coded zero; other unresolved or non-calculable reports remain missing. Original university distances and all other selected covariate codings are retained.

## Files

* `data/schools_5131.csv`: descriptive analytical panel with only the variables needed for this version, source denominators, geography precision, and current model-membership flags. Historical model flags and unused candidate variables were excluded.
* `data/model_full_3827.csv` and `data/model_existing_cs_2900.csv`: exact selected regression samples, copied without recoding.
* `data/district_descriptives.csv`: official CRDC CS supply and sample-level AI/CS district summaries; not district population AI prevalence.
* `docs/variable_dictionary.csv` and `docs/VARIABLES.md`: 56 school-data field meanings, sources, periods, units, missing values, reporting contrasts, and valid/missing counts. `docs/district_variable_dictionary.csv` documents all 13 district-summary fields.
* `analysis_spec.json`: fixed predictors, comparison increments, estimator, and expected sample sizes.
* `reference_results/`: previously verified selected coefficients, covariance matrices, four probability curves, and all seven supplementary CSVs matching the current LaTeX results.
* `scripts/reproduce.py`: select the fixed samples, independently re-estimate both models, regenerate supplementary numerical results and four adjusted-probability curves, and check them against saved references.
* `scripts/verify_package.py`: standard-library integrity, ID, count, and checksum checks without fitting models.
* `checks/`: this package's execution and integrity records, not additional research experiments.

## Run

Use Python **3.14** for the exact tested dependency file (other environments have not been certified by this review package):

```bash
python -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
python scripts/verify_package.py
python scripts/reproduce.py
```

On Windows, activate with `.venv\Scripts\activate`. Run the commands from the repository root. Scripts resolve all inputs relative to their own location; they do not require the author's computer paths, internet access, an LLM, an API key, R, or commercial software. Generated outputs are written to `outputs/`, not over the reference data. This folder is ignored by `.gitignore`.

The original saved fits used Python 3.11.7, NumPy 1.26.4, pandas 2.3.3, and SciPy 1.17.1. The separate review execution environment and numerical differences are recorded in `checks/replication_test.json`.

## What is reproduced

The code rebuilds the 5,131 → 4,094 → 3,827 full-model flow and 3,693 → 3,087 → 2,900 existing-CS flow; both sets of regression coefficients, standard errors, intervals, contrasts, log-likelihoods and AIC; the 72 rows of Table S3; state, locale and region descriptions; school CS/AI overlap; and Figure 4's four probability-curve source tables. The two model specifications are fixed. No variable screening or additional robustness experiment is performed.

Maps are supported by the released school geography and district summaries, but **this package does not regenerate the final cartographic layouts**. Raw Census polygon archives and map-rendering scripts are not included. Raw crawling, historical website/PDF retrieval, original AI snippet adjudication, and the institutional name-to-campus match are not rerun by this package. The retained analytical variables are the starting inputs. See `docs/RESULTS_MAP.md` for exact panel-to-data mapping.

## Coding details that matter for replication

* Read school IDs (`_k`, 12 characters), LEA IDs (7 characters), and county GEOIDs (5 characters) as strings to preserve leading zeros. Empty CSV cells are missing, not zero. Boolean metadata flags use `True`/`False`.
* CS enrollment share uses 2021–22 CRDC enrollment for both numerator and denominator. Mixed-grade schools use total all-grade school enrollment. CS class density instead uses 2021–22 class counts and CCD 2023–24 enrollment.
* CS-LOO uses official eligible high schools, not only sampled schools. There are 1,712 descriptive-sample singleton-zero assignments, 1,146 in the main model and 929 in the restricted model. The remaining 132 descriptive records have missing LOO.
* `title1_cep_flag` is the retained code field for the **NSLP participation indicator**, not Title I/CEP eligibility. Existing zero coding of unreported statuses is preserved.
* `crdc_ds_offered` is a data science enrollment indicator; negative source enrollment codes were set to zero before checking positive enrollment. This is not a distance-learning indicator.
* AI patent density is `ln(rate + 0.01)`. Missing underlying rates retain `ln(0.01)`: 1,099 descriptive records, 780 main-model records and 540 restricted-model records. These are the analyzed legacy values, not new measured zeros.
* `csr_dist_km` is the archived kilometer field (5,131 records). It includes 53 county-centroid fallback locations. Regression proximity `cs_academic_proximity = -ln(1 + km)` is missing for those 53; it is valid for 5,078 school-point locations. Both supplied regression samples exclude them. This describes the actual retained filtering rule, without changing it.
* ACS population measures describe retained Census geographic school-district residents linked by LEA key, not the enrolled student population or a newly inferred containing geographic district. LEA identity and boundary coverage are not interchangeable.

## Sources and release status

Source families and known vintages are documented in `docs/SOURCES.md`. Files are **processed school-level data**, not individual student records. Raw course catalogs, copyrighted course PDFs, correspondence, signatures, the manuscript, credentials and personal computer paths are not bundled.

The processed data and replication code are hosted in the repository linked above. No DOI or open license has been assigned. Public access does not itself grant an open license; no blanket license is applied to third-party materials. The offline execution record in `checks/replication_test.json` describes the replication test, not the subsequent repository upload.

## Citation

Author order and the repository URL are recorded in `CITATION.cff`. No DOI has been assigned. The manuscript is a submission, not a publication acceptance claim.
