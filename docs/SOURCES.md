# Source families and construction

This is a processed analytical-data release candidate. Source attribution does not assert that redistribution permissions have been reviewed.

| Fields | Source and retained period | Construction |
|---|---|---|
| School roster, names, final AI labels | Niche-derived roster; official school/district course evidence, June 2026 | Final 5,131 labels; 312 positive extracted snippets manually reviewed |
| School/LEA links; CS classes and enrollment; district CS | CRDC 2021–22 | Same-year CS participation denominator; valid official high-school reports for district environment |
| School scale, student-teacher ratio, charter, NSLP | NCES CCD 2023–24 | Retained transformed variables and original binary coding |
| Certified calculus/physics/advanced-math classes | CRDC 2020–21 | ln(1+sum of certified-teacher-taught class counts) |
| District BA+ and household income | ACS 2019–2023 five-year estimates | B15003 categories 022–025 / B15003_001; ln(B19013_001); retained LEA-key join |
| University proximity | Original CSRankings affiliation/name matching; IPEDS 2021 campus coordinates | Exact normalized-name match then first substring match for keys longer than four characters; equirectangular distance, Earth radius 6,371 km and mean institution latitude; nearest institution, -ln(1+km) |
| Technology employment LQ | Retained BLS QCEW-derived county data | Exact industry membership and extraction vintage not rebuilt here |
| County AI patent density | Retained 2023 PatentsView-derived field | ln(rate per 10,000 residents + 0.01), including legacy missing-rate floors |
| Fixed broadband | Retained FCC 100/20 Mbps measure | Original percentage; inherited source vintage |
| R1 proximity | Retained R1 institutional geography | Indicator for institution within 25 miles; inherited source vintage |
| County GDP | BEA-derived 2023 total GDP | Natural logarithm |
| Mapping context | Retained Census 2022 unified/secondary district boundary linkage | School location precision is supplied; polygon archives are not bundled |

Raw third-party source tables, historical web/PDF downloads, and the institution-level campus crosswalk are not included. The package reproduces selected analysis from the supplied processed variables; it does not recreate every upstream acquisition step. No raw source vintage or campus validation is invented where the retained files do not establish it.
