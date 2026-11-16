# Findings and limitations

This project analyses the supplied Bremen police-report snapshot using existing computational results. Counts refer to published reports. The collection is not a complete crime register, and no population denominator is available.

## Data and districts

All 5,126 report IDs remain. BR001569 and BR002114 are excluded duplicates, leaving 5,124 included reports. Frozen preparation SHA-256: `bf64238b7f929551cf20dadcdd314fa8bf17efe2cd7eab6174fd44dab1a1c139`.

The finer Ortsteil view locates 2,977 reports and leaves 2,147 Unknown. The broader district view locates 4,149 and leaves 975 Unknown. These are separate views of the same reports; their totals must not be added. The existing geographic evidence is retained; independent human validation was not performed and compatible map boundaries are unavailable.

Under the draft mapping, Traffic-related accounts for 658 reports (12.8%), Assault / threats for 526 (10.3%), and Public events / police information for 399 (7.8%). Another 1,427 reports (27.8%) are Unknown/Unclear and 335 (6.5%) are model noise. Unknown geography remains in category denominators.

Among named broader districts, Walle leads Traffic-related (85), Mitte leads Assault / threats (117) and Drug-related (62), and Neustadt leads Robbery (33) and Fire / explosion / ordnance (52). These are located-report counts, not risk rankings. No direct Theft or Weapons-related mapping does not mean these offenses are absent.

## Topic models and computational categories

| Candidate | Topics | Assigned | Unassigned |
|---|---:|---:|---:|
| Title NMF | 8 | 5,069 | 55 |
| Description NMF | 10 | 5,124 | 0 |
| Title embeddings / BERTopic | 59 | 4,583 | 541 |
| Description embeddings / BERTopic | 36 | 4,789 | 335 |

All exports retain the original IDs and two exclusions. Coverage measures assignment availability, not correctness. Topics can reflect appeals, places, mixed incidents and police language.

Description BERTopic remains the existing provisional proposal for its interpretable incident themes. It matches 25 of 60 computer-assisted held-out categories; title BERTopic matches 27, description NMF 17 and title NMF 13. These comparisons do not establish a winner: the same assistant assessed development and held-out reports, and the balanced sample does not represent the full collection. Independent accuracy and F1 are unavailable. The frozen mapping has not been retuned on these results.

Description NMF's historical 39 favorable judgments out of 50 (78%) are development observations. Human authorship cannot be independently verified. Original notes and report IDs remain preserved.

## Time patterns and unusual increases

The publication range is July 2019 to September 2026, with partial boundary months and 11 months without observations. Missing months remain missing, not zero. The comparable seasonal window is 2021-2025; collection completeness remains unknown even in these years.

August averages 75.0 reports per observed month and December 58.2. Annual peaks vary, so these means do not establish a stable seasonal mechanism. Category profiles retain annual ranges and reports-per-day measures.

The increase screen compares each month with its preceding 12 months, requiring an adequate baseline and excluding gaps and boundaries. Flags include Traffic-related reports in January 2023, June 2024 and March 2025. Stored source context identifies mixed circumstances and category boundaries, without verifying a common cause. These are exploratory flags, not significance tests or causal findings.

## Elderly Screening Results

Age 50+ is the working threshold, not a universal definition of elderly. The prepared-data screen finds 1,236 reports mentioning an age of at least 50 and 597 mentioning an age of at least 65. The 65+ group is contained within 50+. Wording-only matches expand the candidate queue to 1,267 reports.

Computer-assisted assessment covers those candidates and 40 noncandidate controls:

| Source-text assessment | Candidates | Controls |
|---|---:|---:|
| Explicit age linked to a reported victim or target | 767 | 0 |
| Possible older victim; insufficient evidence | 234 | 0 |
| Older person in another role | 252 | 0 |
| No evidence of an older victim | 6 | 40 |
| Unclear | 8 | 0 |
| Total | 1,267 | 40 |

Category and district summaries group these same saved assessments. Each view totals 1,307 separately. Unknown geography, unclear categories and model noise remain visible. These screened-subset counts do not estimate citywide prevalence. Explicit-text findings include attempts and traffic casualties and require confirmation. Forty controls do not establish sensitivity.

Among mapped categories within the 767 explicit-text findings, Fraud / deception has the largest count (153), followed by Traffic-related (117) and Robbery (69). Unknown/Unclear (253) and unassigned noise (95) are substantial. Schwachhausen has the largest named-district Fraud / deception count (13), while 23 such locations remain Unknown. Across all explicit-text findings, Mitte leads named districts (107). These rankings describe the assessed subset, not confirmed victim incidence.

## Method and provenance

All labels and older-person role findings are computer-assisted and exploratory. Independent human validation was not performed. The same assistant assessed development and held-out sources, so agreement is descriptive rather than independent accuracy. Nine prior development suggestions reflect user agreement with chat summaries, not independently read reference labels. The mapping remains unchanged after held-out assessment.

The optional team reader and approval system has been removed from the active project at the coordinator's request. This does not establish independent validation. Former human-approved outputs retain their original meaning in the legacy contract note and are not produced under those filenames.

The five course questions have computational results, source evidence, figures and limitations in the six notebooks. Main Working Station integration remains a separate submission step. See [the output guide](RESULTS_GUIDE.md).
