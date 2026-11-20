# Variable dictionary

Field names are preserved for reproducibility. Blank cells indicate missing values unless a field-specific rule states otherwise. Valid/missing counts refer to the 5,131-school descriptive panel.

## `_k`
**School identifier**. Retained 12-character school linkage key. Read as text to preserve leading zeros.
- Source/period: Linked analytical school roster; Retained study roster.
- Units/type: identifier; string.
- Missing values: Blank = missing; retained values are not recoded.
- Valid/missing: 5131 / 0.
- Model role: identifier. Reported contrast: not a model contrast.

## `school_name`
**School name**. Retained school name; no new name correction in this package.
- Source/period: Study roster; Retained study roster.
- Units/type: text; string.
- Missing values: Blank = missing; retained values are not recoded.
- Valid/missing: 5131 / 0.
- Model role: identifier. Reported contrast: not a model contrast.

## `state_abbr`
**State or DC**. Two-letter state abbreviation; DC is a separate state-level jurisdiction.
- Source/period: Linked school records; Retained study roster.
- Units/type: category; string.
- Missing values: Blank = missing; retained values are not recoded.
- Valid/missing: 5131 / 0.
- Model role: fixed_effect. Reported contrast: not a model contrast.

## `county_geoid`
**County GEOID**. Retained five-character county geography key; preserve leading zeros.
- Source/period: Linked geographic background data; Inherited geography vintage.
- Units/type: identifier; string.
- Missing values: Blank = missing; retained values are not recoded.
- Valid/missing: 5131 / 0.
- Model role: geographic_context. Reported contrast: not a model contrast.

## `lea_crdc`
**Administering LEA identifier**. Seven-character CRDC local education agency key; not a newly assigned geographic containing district.
- Source/period: CRDC; 2021-22.
- Units/type: identifier; string.
- Missing values: Blank = missing; retained values are not recoded.
- Valid/missing: 4999 / 132.
- Model role: cluster_and_district_key. Reported contrast: not a model contrast.

## `locale`
**School locale**. City, Suburb, Town, Rural; retained coding.
- Source/period: NCES locale, retained school records; Retained roster vintage.
- Units/type: category; string.
- Missing values: Blank = missing; retained values are not recoded.
- Valid/missing: 5131 / 0.
- Model role: description. Reported contrast: not a model contrast.

## `region`
**Census region**. Northeast, Midwest, South, West; state-based grouping.
- Source/period: Census region grouping; Study grouping.
- Units/type: category; string.
- Missing values: Blank = missing; retained values are not recoded.
- Valid/missing: 5131 / 0.
- Model role: description. Reported contrast: not a model contrast.

## `AI_final`
**Observed formal AI curriculum**. Final binary label: qualifying formal AI/ML teaching content observed in course evidence. All 312 positive extracted text snippets were reviewed by the researcher. No relabeling here.
- Source/period: Official school/district course evidence; June 2026.
- Units/type: 0/1; integer.
- Missing values: No missing labels; 0 = no qualifying evidence observed.
- Valid/missing: 5131 / 0.
- Model role: outcome. Reported contrast: not a model contrast.

## `district_cs_loo`
**Other-school LEA CS proportion**. Other official high schools with >=1 CS class / other official high schools with valid CS reports. Official single-high-school LEAs assigned zero.
- Source/period: Full eligible CRDC high-school universe and LEA link; 2021-22.
- Units/type: proportion 0-1; numeric.
- Missing values: Blank = missing; retained values are not recoded.
- Valid/missing: 4999 / 132.
- Model role: P2. Reported contrast: Other district HS with CS (+10 pp).

## `cs_per_100_students`
**CS classes per 100 students**. 100 * CRDC CS classes / CCD enrollment. Numerator and denominator have different years.
- Source/period: CRDC; CCD; 2021-22 numerator; 2023-24 denominator.
- Units/type: classes per 100 students; numeric.
- Missing values: Blank = missing; retained values are not recoded.
- Valid/missing: 4994 / 137.
- Model role: P1. Reported contrast: CS classes / 100 students (+1).

## `City`
**City vs rural**. Locale dummy; rural is the model reference.
- Source/period: NCES locale; Retained roster vintage.
- Units/type: 0/1; integer.
- Missing values: Blank = missing; retained values are not recoded.
- Valid/missing: 5131 / 0.
- Model role: P1. Reported contrast: City vs rural.

## `Suburb`
**Suburb vs rural**. Locale dummy; rural is the model reference.
- Source/period: NCES locale; Retained roster vintage.
- Units/type: 0/1; integer.
- Missing values: Blank = missing; retained values are not recoded.
- Valid/missing: 5131 / 0.
- Model role: P1. Reported contrast: Suburb vs rural.

## `Town`
**Town vs rural**. Locale dummy; rural is the model reference.
- Source/period: NCES locale; Retained roster vintage.
- Units/type: 0/1; integer.
- Missing values: Blank = missing; retained values are not recoded.
- Valid/missing: 5131 / 0.
- Model role: P1. Reported contrast: Town vs rural.

## `log_enrollment`
**Log school enrollment**. Natural logarithm of retained total school enrollment.
- Source/period: CCD; 2023-24.
- Units/type: log students; numeric.
- Missing values: Blank = missing; retained values are not recoded.
- Valid/missing: 5125 / 6.
- Model role: P1. Reported contrast: Student enrollment (doubling).

## `charter_use`
**Charter status**. Retained binary charter-school indicator.
- Source/period: CCD; 2023-24.
- Units/type: 0/1; integer.
- Missing values: Blank = missing; retained values are not recoded.
- Valid/missing: 5131 / 0.
- Model role: P1. Reported contrast: Charter.

## `stem_name_flag`
**STEM school-name flag**. Case-insensitive stem/science/technology/engineering or standalone tech match.
- Source/period: School names; Retained study roster.
- Units/type: 0/1; integer.
- Missing values: Blank = missing; retained values are not recoded.
- Valid/missing: 5131 / 0.
- Model role: P1. Reported contrast: STEM name.

## `academy_name_flag`
**Academy school-name flag**. Case-insensitive academy/prep/scholar/governor match.
- Source/period: School names; Retained study roster.
- Units/type: 0/1; integer.
- Missing values: Blank = missing; retained values are not recoded.
- Valid/missing: 5131 / 0.
- Model role: P1. Reported contrast: Academy name.

## `st_ratio_use`
**Student-teacher ratio**. Retained students per teacher, capped at 50.
- Source/period: CCD; 2023-24.
- Units/type: students per teacher; numeric.
- Missing values: Blank = missing; retained values are not recoded.
- Valid/missing: 4841 / 290.
- Model role: P1. Reported contrast: Student–teacher ratio (+1).

## `cd_ba_plus_share`
**District BA+ attainment**. ACS B15003 categories 022-025 / B15003_001, population aged 25+. Retained geographic-district ACS records joined by LEA key.
- Source/period: ACS; 2019-2023 five-year estimates.
- Units/type: proportion 0-1; numeric.
- Missing values: Blank = missing; retained values are not recoded.
- Valid/missing: 4461 / 670.
- Model role: P3. Reported contrast: District BA+ share (+10 pp).

## `cd_log_med_income`
**Log district household income**. Natural logarithm of ACS median household income B19013_001; retained geographic-district ACS records joined by LEA key.
- Source/period: ACS; 2019-2023 five-year estimates.
- Units/type: log USD; numeric.
- Missing values: Blank = missing; retained values are not recoded.
- Valid/missing: 4460 / 671.
- Model role: P3. Reported contrast: District median income (+10%).

## `qcew_selected_tech_lq`
**County technology employment LQ**. Retained selected-technology-sector employment location quotient; exact constituent industries/vintage not reconstructed in this package.
- Source/period: BLS QCEW-derived county table; Inherited source vintage.
- Units/type: location quotient; numeric.
- Missing values: Blank = missing; retained values are not recoded.
- Valid/missing: 5128 / 3.
- Model role: P3. Reported contrast: County tech employment LQ (+1).

## `title1_cep_flag`
**NSLP participation indicator**. Retained internal name. Public meaning is National School Lunch Program participation, NOT Title I or independent CEP status. Unreported statuses were retained as zero.
- Source/period: CCD; 2023-24.
- Units/type: 0/1; integer.
- Missing values: Blank = missing; retained values are not recoded.
- Valid/missing: 5131 / 0.
- Model role: P1. Reported contrast: NSLP participation indicator.

## `cs_enrollment_share`
**CS enrollment share**. CRDC male+female CS enrollment / same-year male+female total school enrollment. All grades retained in mixed-grade schools.
- Source/period: CRDC; 2021-22.
- Units/type: proportion 0-1; numeric.
- Missing values: Blank = missing; retained values are not recoded.
- Valid/missing: 4998 / 133.
- Model role: P1. Reported contrast: CS enrollment / all students (+10 pp).

## `crdc_ds_offered`
**Data science enrollment indicator**. Positive male+female data science enrollment after negative male/female report codes are set to zero; not distance learning.
- Source/period: CRDC; 2021-22.
- Units/type: 0/1; integer.
- Missing values: Blank = missing; retained values are not recoded.
- Valid/missing: 5002 / 129.
- Model role: P1. Reported contrast: Data science enrollment indicator.

## `log_ai_patents_per_10k`
**Log county AI patent density**. ln(AI patents per 10,000 residents + 0.01). Missing underlying rates retain ln(0.01), not independently observed zero patent activity.
- Source/period: Retained PatentsView-derived county measure; 2023.
- Units/type: log(rate+0.01); numeric.
- Missing values: Blank = missing; retained values are not recoded.
- Valid/missing: 5131 / 0.
- Model role: P3. Reported contrast: AI patent density (doubling rate + 0.01).

## `fixed_100_20_pct`
**Fixed broadband availability**. Retained 100/20 Mbps availability percentage.
- Source/period: FCC-derived linked background data; Inherited source vintage.
- Units/type: percent 0-100; numeric.
- Missing values: Blank = missing; retained values are not recoded.
- Valid/missing: 5054 / 77.
- Model role: P3. Reported contrast: Broadband availability (+10 pp).

## `r1_within_25mi`
**R1 institution within 25 miles**. Retained indicator for an R1 university within 25 miles; distinct from CSRankings proximity.
- Source/period: Retained R1 university geography; Inherited source vintage.
- Units/type: 0/1; integer.
- Missing values: Blank = missing; retained values are not recoded.
- Valid/missing: 5131 / 0.
- Model role: P3. Reported contrast: R1 university within 25 miles.

## `log_gdp_total`
**Log county GDP**. Natural logarithm of retained county total GDP.
- Source/period: BEA-derived county data; 2023.
- Units/type: log county GDP; numeric.
- Missing values: Blank = missing; retained values are not recoded.
- Valid/missing: 4983 / 148.
- Model role: P3. Reported contrast: County GDP (doubling).

## `cs_academic_proximity`
**CSRankings-linked proximity**. -ln(1 + nearest matched institution distance in km). Original name-matched CSRankings/IPEDS measure retained; county-centroid school locations are missing in this regression field.
- Source/period: Retained CSRankings-linked campus matching; IPEDS coordinates; IPEDS 2021; retained roster snapshot.
- Units/type: negative log(1+km); numeric.
- Missing values: Blank = missing; retained values are not recoded.
- Valid/missing: 5078 / 53.
- Model role: P3. Reported contrast: CSRankings proximity (50 to 25 km).

## `log_certified_adv_stem_classes`
**Certified advanced-STEM classes (log)**. ln(1 + certified-teacher-taught calculus, physics, and advanced-mathematics classes); counts classes, not teachers.
- Source/period: CRDC; 2020-21.
- Units/type: log(1+classes); numeric.
- Missing values: Blank = missing; retained values are not recoded.
- Valid/missing: 5052 / 79.
- Model role: P1. Reported contrast: Certified STEM classes (2×[1+n]).

## `csr_dist_km`
**Archived university distance**. Original kilometer distance field, available for 5,131 records. Includes 53 county-centroid fallback locations; do not treat those 53 as eligible school-point regression distances.
- Source/period: Retained CSRankings/IPEDS-linked school output; IPEDS 2021 coordinates; retained matching.
- Units/type: km; numeric.
- Missing values: Blank = missing; retained values are not recoded.
- Valid/missing: 5131 / 0.
- Model role: support. Reported contrast: not a model contrast.

## `final_latitude`
**Retained latitude**. Latitude used by the retained location pipeline; consult precision and school_point_available before mapping school points.
- Source/period: Linked school geography; Retained geography vintage.
- Units/type: degrees north; numeric.
- Missing values: Blank = missing; retained values are not recoded.
- Valid/missing: 5131 / 0.
- Model role: support. Reported contrast: not a model contrast.

## `final_longitude`
**Retained longitude**. Longitude used by the retained location pipeline; consult precision and school_point_available before mapping school points.
- Source/period: Linked school geography; Retained geography vintage.
- Units/type: degrees east; numeric.
- Missing values: Blank = missing; retained values are not recoded.
- Valid/missing: 5131 / 0.
- Model role: support. Reported contrast: not a model contrast.

## `final_location_source`
**Location source**. Retained location-source category.
- Source/period: Linked school geography; Retained geography vintage.
- Units/type: category; string.
- Missing values: Blank = missing; retained values are not recoded.
- Valid/missing: 5131 / 0.
- Model role: support. Reported contrast: not a model contrast.

## `final_location_precision`
**Location precision**. Retained precision category. county_centroid records do not qualify as school points.
- Source/period: Linked school geography; Retained geography vintage.
- Units/type: category; string.
- Missing values: Blank = missing; retained values are not recoded.
- Valid/missing: 5131 / 0.
- Model role: support. Reported contrast: not a model contrast.

## `school_point_available`
**Eligible school point**. True for retained eligible school/campus coordinates. 5,078 true; 53 county-centroid false.
- Source/period: Location precision filter; Retained geography vintage.
- Units/type: true/false; boolean.
- Missing values: Blank = missing; retained values are not recoded.
- Valid/missing: 5131 / 0.
- Model role: support. Reported contrast: not a model contrast.

## `cs_enrollment_mf_2122`
**CS enrollment numerator**. Retained male+female CS enrollment numerator used in aligned CS share construction.
- Source/period: CRDC; 2021-22.
- Units/type: students; numeric.
- Missing values: Blank = missing; retained values are not recoded.
- Valid/missing: 4998 / 133.
- Model role: support. Reported contrast: not a model contrast.

## `school_enrollment_mf_2122`
**Same-year school enrollment denominator**. Retained male+female total school enrollment denominator for CS share. Includes all school grades.
- Source/period: CRDC; 2021-22.
- Units/type: students; numeric.
- Missing values: Blank = missing; retained values are not recoded.
- Valid/missing: 5002 / 129.
- Model role: support. Reported contrast: not a model contrast.

## `grade_scope`
**Grade range category**. Retained grade-scope category used to identify mixed-grade schools; not a high-school-only denominator correction.
- Source/period: CRDC-linked school grade records; 2021-22.
- Units/type: category; string.
- Missing values: Blank = missing; retained values are not recoded.
- Valid/missing: 5131 / 0.
- Model role: support. Reported contrast: not a model contrast.

## `structural_zero_from_no_CS_classes`
**Structural CS enrollment zero**. Flag identifying original structural-zero treatment for no-CS-class reports and zero/negative enrollment fields.
- Source/period: CS enrollment alignment construction; 2021-22.
- Units/type: true/false; boolean.
- Missing values: Blank = missing; retained values are not recoded.
- Valid/missing: 5131 / 0.
- Model role: support. Reported contrast: not a model contrast.

## `SCH_COMPCLASSES_CSCI`
**Raw reported CS class count**. Source class count. Negative administrative codes are unavailable reports, not no-CS observations.
- Source/period: CRDC; 2021-22.
- Units/type: classes; numeric.
- Missing values: Blank or negative source code = unavailable for CS provision.
- Valid/missing: 5002 / 129.
- Model role: support. Reported contrast: not a model contrast.

## `certified_adv_stem_classes`
**Certified advanced-STEM class count**. Retained unlogged count underlying log_certified_adv_stem_classes.
- Source/period: CRDC; 2020-21.
- Units/type: classes; numeric.
- Missing values: Blank = missing; retained values are not recoded.
- Valid/missing: 5052 / 79.
- Model role: support. Reported contrast: not a model contrast.

## `official_highschools`
**Official LEA high schools**. Eligible official high-school count in the administering LEA.
- Source/period: Official CRDC high-school universe and LEA relation; 2021-22.
- Units/type: schools; numeric.
- Missing values: Blank = missing; retained values are not recoded.
- Valid/missing: 4999 / 132.
- Model role: support. Reported contrast: not a model contrast.

## `valid_cs_reporters`
**Valid LEA CS reporters**. Eligible official LEA high schools with valid CS class reports.
- Source/period: Official CRDC high-school universe and LEA relation; 2021-22.
- Units/type: schools; numeric.
- Missing values: Blank = missing; retained values are not recoded.
- Valid/missing: 4999 / 132.
- Model role: support. Reported contrast: not a model contrast.

## `cs_offering_highschools`
**LEA CS-offering schools**. Eligible official LEA high schools reporting at least one CS class.
- Source/period: Official CRDC high-school universe and LEA relation; 2021-22.
- Units/type: schools; numeric.
- Missing values: Blank = missing; retained values are not recoded.
- Valid/missing: 4999 / 132.
- Model role: support. Reported contrast: not a model contrast.

## `reporting_coverage`
**LEA CS reporting coverage**. valid_cs_reporters / official_highschools.
- Source/period: Official CRDC high-school universe; 2021-22.
- Units/type: proportion 0-1; numeric.
- Missing values: Blank = missing; retained values are not recoded.
- Valid/missing: 4999 / 132.
- Model role: support. Reported contrast: not a model contrast.

## `other_valid_cs_reporters`
**Other valid LEA CS reporters**. Valid reporting denominator after excluding the focal school where applicable.
- Source/period: Official CRDC high-school universe and LEA relation; 2021-22.
- Units/type: schools; numeric.
- Missing values: Blank = missing; retained values are not recoded.
- Valid/missing: 4999 / 132.
- Model role: support. Reported contrast: not a model contrast.

## `other_offering_highschools`
**Other LEA CS-offering schools**. Other high schools reporting at least one CS class; LOO numerator.
- Source/period: Official CRDC high-school universe and LEA relation; 2021-22.
- Units/type: schools; numeric.
- Missing values: Blank = missing; retained values are not recoded.
- Valid/missing: 4999 / 132.
- Model role: support. Reported contrast: not a model contrast.

## `other_official_highschools`
**Other official LEA high schools**. Official LEA high-school count excluding the focal school.
- Source/period: Official CRDC high-school universe and LEA relation; 2021-22.
- Units/type: schools; numeric.
- Missing values: Blank = missing; retained values are not recoded.
- Valid/missing: 4999 / 132.
- Model role: support. Reported contrast: not a model contrast.

## `other_reporting_coverage`
**Peer CS reporting coverage**. other_valid_cs_reporters / other_official_highschools where the denominator is positive.
- Source/period: Official CRDC high-school universe; 2021-22.
- Units/type: proportion 0-1; numeric.
- Missing values: Blank = missing; retained values are not recoded.
- Valid/missing: 3287 / 1844.
- Model role: support. Reported contrast: not a model contrast.

## `cs_observed_status`
**Observed CS class provision**. 1 = >=1 reported CS class; 0 = reported zero classes; blank = unavailable.
- Source/period: CRDC; 2021-22.
- Units/type: 0/1; numeric.
- Missing values: Blank = missing; retained values are not recoded.
- Valid/missing: 4998 / 133.
- Model role: support. Reported contrast: not a model contrast.

## `cs_existing`
**Existing CS descriptive subset**. True if CS class count >=1. Use cs_observed_status to distinguish zero from unavailable.
- Source/period: CRDC class provision; 2021-22.
- Units/type: true/false; boolean.
- Missing values: Blank = missing; retained values are not recoded.
- Valid/missing: 5131 / 0.
- Model role: support. Reported contrast: not a model contrast.

## `cs_offered_raw`
**Retained CS provision flag**. Administrative binary CS provision field retained in the selected model sample.
- Source/period: CRDC; 2021-22.
- Units/type: 0/1; numeric.
- Missing values: Blank = missing; retained values are not recoded.
- Valid/missing: 4998 / 133.
- Model role: support. Reported contrast: not a model contrast.

## `cs_loo_singleton_zero_applied`
**Single-high-school LOO zero applied**. True when other_official_highschools==0; 1,712 schools in the descriptive sample.
- Source/period: Approved CSE coding convention; CSE selected version.
- Units/type: true/false; boolean.
- Missing values: Blank = missing; retained values are not recoded.
- Valid/missing: 5131 / 0.
- Model role: support. Reported contrast: not a model contrast.

## `in_full_model_cse`
**Full-model membership**. Exact selected 3,827-school model membership. Recomputed from saved model school IDs, not inherited old model flags.
- Source/period: Selected CSE model sample; CSE selected version.
- Units/type: true/false; boolean.
- Missing values: Blank = missing; retained values are not recoded.
- Valid/missing: 5131 / 0.
- Model role: support. Reported contrast: not a model contrast.

## `in_existing_cs_model_cse`
**Existing-CS model membership**. Exact selected 2,900-school model membership.
- Source/period: Selected CSE model sample; CSE selected version.
- Units/type: true/false; boolean.
- Missing values: Blank = missing; retained values are not recoded.
- Valid/missing: 5131 / 0.
- Model role: support. Reported contrast: not a model contrast.
