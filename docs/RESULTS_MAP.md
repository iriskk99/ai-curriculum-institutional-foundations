# Manuscript results and reproduction scope

| Manuscript element | Inputs | This package |
|---|---|---|
| Figures 1–2: geography, states, locales, regions | schools_5131; eligible school points; region/locale/state fields | Reproduces counts and proportions; no map layout redraw |
| Figure 3: CS/AI overlap | cs_observed_status, AI_final; district_descriptives | Reproduces school cross-tabulation and locale summaries; map polygons/layout not rebuilt |
| Figure 4: full model and four probability panels | model_full_3827; analysis_spec; fitted coefficients/covariance | Re-estimates model and regenerates curve numerical source data |
| Figure 5a–c: existing-CS descriptions | CS-positive subset of schools_5131; district summaries | Reproduces descriptive counts/locale rates; map layouts not rebuilt |
| Figure 5d | model_existing_cs_2900 | Re-estimates all 22 non-state associations |
| Table 1: illustrative course excerpts | Original catalogs/snippet evidence | Not redistributed or re-adjudicated |
| Table 2: variables and methods | variable dictionary; analysis_spec | Documents all fitted predictors and coding |
| Table 3: sample composition | schools_5131, model memberships, district summaries | Reproduces model sample flows; archived polygon coverage not independently reconstructed |
| Tables S1a–d | two model samples | Reproduces specified contrasts and all parameters |
| Table S2 | all schools grouped by state | Checks state counts and proportions |
| Table S3 | all schools and two selected samples | Reproduces 72 descriptive-statistic rows |
| Table S4 | two fitted models | Reproduces model information without the removed iteration row |

District fields: `sample_n`/`sample_ai` use linked website schools; `cs_sample_n`/`cs_sample_ai` use website schools reporting CS; `official_highschools`, `valid_cs_reporters`, and `cs_offering_highschools` use the full official CRDC universe. `sample_ai_percent` and `cs_sample_ai_percent` are sample percentages, not population prevalence. `official_cs_percent` is 100*cs_offering_highschools/valid_cs_reporters; `reporting_coverage` is valid_cs_reporters/official_highschools; `sample_coverage` is sample_n/official_highschools. District descriptive proportions include the focal school; regression CS-LOO excludes it except the stipulated singleton-zero case.
