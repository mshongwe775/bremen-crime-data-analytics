# Six-notebook completion report

## Recovery and scope

A complete local backup was created before any removals. Every ZIP entry was read back and checked against the SHA-256 inventory. See [RECOVERY.md](RECOVERY.md) for the archive location and safe recovery instructions. The affected-file inventory records removals and renames. Uncommitted starting work is included.

The course slides and data explanations were checked. They require five analytical questions, not the team's optional reader/signature/audit system. That optional infrastructure has been removed from active analysis. No independent human validation, signatures or approved classifications are claimed.

## Notebook changes

| Notebook | Implemented change |
|---|---|
| 01 | Removed approved-category gates; retained frozen-data checks and original geographic evidence; directly joined computational labels; generated district counts, shares, leaders, composition and coverage figures |
| 02 | Preserved title NMF and original fitting code; added default saved-result verification with tables, sensitivity evidence and the original figure; removed obsolete pending-review instructions |
| 03 | Preserved description NMF, corrected representative alignment and development evidence; added saved-result execution; retained the unverified authorship caveat for historical judgments |
| 04 | Preserved both supplied-vector pipelines, sensitivity evidence, assignments, samples and four figures; added default saved-result execution and embedding checks; retained exact-environment guidance for optional refits |
| 05 | Removed approval gates and inactive duplicate branches; directly computed category/district time profiles, seasonal comparisons, anomaly flags and source evidence |
| 06 | Replaced workflow management with eight analytical sections: input verification, model comparison, model choice, codebook/mapping, report assignments, age screening, findings/limits and exports |

The modeling notebooks default to `REFIT_MODELS = False`. Fresh-kernel execution verifies and displays their completed experiments without retraining. Original fitting code remains available with the recorded dependencies. This maintenance does not claim a new model fit.

## Removed and renamed files

Removed active files include optional first/second-reader worksheets, approval instructions, exposure declarations, review packets, signature workbooks, focused-audit protocols, duplicate frozen snapshots, obsolete screening drafts and superseded maintenance records. They remain recoverable in the backup. Geographic evidence, computational category definitions, assessment evidence and model outputs were preserved.

Computational files now use descriptive names, including `age50plus_assessments.csv`, `age50plus_screening_summary.csv`, `development_category_comparison.csv`, `held_out_category_comparison.csv`, `model_assessment.csv`, `topic_mapping_assessment.csv` and `analysis_validation_manifest.json`. Geographic and temporal results are in `geographic_results/` and `time_results/`. The full rename/removal list is in the backup's `affected_files.json`; current outputs are indexed in [RESULTS_GUIDE.md](RESULTS_GUIDE.md).

The active contract explicitly distinguishes computational assignments from the former approved-label contract. It does not reinterpret an approved `report_categories.csv` or confirmed `elderly_summary.csv`.

## Preserved findings

- Source: 5,126 IDs, 5,124 eligible reports and two exclusions. The frozen preparation checksum remains `bf64238b7f929551cf20dadcdd314fa8bf17efe2cd7eab6174fd44dab1a1c139`.
- Models: title NMF 8 topics / 5,069 assigned / 55 unassigned; description NMF 10 / 5,124 / 0; title embeddings 59 / 4,583 / 541; description embeddings 36 / 4,789 / 335. Original settings, seeds, keywords, samples and model-result CSV values are retained.
- Categories: 3,362 mapped, 1,427 unclear, 335 unassigned, two excluded. Traffic-related has 658 reports, Assault / threats 526 and Public events / police information 399. Unclear and noise remain visible.
- Geography: finer view 2,977 located / 2,147 Unknown; broader view 4,149 / 975. Each independently totals 5,124. Walle leads named-area Traffic-related reports (85); Mitte leads Assault / threats (117) and Drug-related (62); Neustadt leads Robbery (33) and Fire / explosion / ordnance (52).
- Time: March 2021 has 92 reports; 11 months lack observations. Seasonal comparisons use 2021-2025. August averages 75.0 and December 58.2. The retained rule finds zero citywide flags over 62 evaluable months and seven category/district candidates. Explanations remain source context, not verified causes.
- Older-person screening: 1,267 candidates plus 40 controls. The 1,307 computational assessments contain 767 explicit target/casualty findings, 234 possible cases, 252 other-role cases, 46 no-evidence cases and eight unclear cases. The saved rule/context method reproduces these assessments exactly without rewriting evidence.
- Within mapped explicit-text categories, Fraud / deception leads (153). Schwachhausen leads its named districts (13), with 23 Unknown locations. Across all explicit-text findings, Mitte leads named districts (107). Unknown/Unclear categories (253) and model noise (95) limit these rankings. These are not confirmed full-dataset victim counts.

## Verification and remaining submission work

All six notebooks were tested from fresh kernels in an isolated copy, including execution from both supported working-directory forms. Modeling notebooks used their documented saved-results mode. Final results and file checks are recorded in `completion_checks.json`.

Checks cover notebook sections and syntax, source/prepared hashes, model IDs and samples, category totals, district denominators, missing-month handling, seasonal/anomaly results, screening evidence, output presence, paths and figure readability. The original computational age/person assessment method was also replayed and matched all 1,307 saved classifications exactly.

The remaining submission step is integration and final presentation in the Main Working Station, followed by the course's GitHub/instructor-sharing requirements. Those actions were not performed. Collection completeness, population denominators, compatible map boundaries, independently validated category accuracy and verified anomaly causes remain analytical limitations. Notebook 02's owner remains unrecorded.

The Main Working Station and frozen data are unchanged. No commit or push was made.

## Exact filename changes

- `age50plus_review_queue.csv` -> `age50plus_candidates.csv`
- `age_threshold_prepared.csv` -> `age_threshold_summary.csv`
- `ai_age50plus_context_reviews.csv` -> `age50plus_context_assessments.csv`
- `ai_age50plus_review_method.py` -> `age50plus_assessment_method.py`
- `ai_age50plus_reviews.csv` -> `age50plus_assessments.csv`
- `ai_age50plus_summary.csv` -> `age50plus_screening_summary.csv`
- `ai_development_changes.csv` -> `development_category_changes.csv`
- `ai_development_comparison.csv` -> `development_category_comparison.csv`
- `ai_development_reviews.csv` -> `development_category_assessments.csv`
- `ai_held_out_comparison.csv` -> `held_out_category_comparison.csv`
- `ai_held_out_disagreements.csv` -> `held_out_category_disagreements.csv`
- `ai_held_out_reviews.csv` -> `held_out_category_assessments.csv`
- `ai_mapping_freeze.json` -> `category_mapping_snapshot.json`
- `ai_model_assessment.csv` -> `model_assessment.csv`
- `ai_topic_mapping_reviews.csv` -> `topic_mapping_assessment.csv`
- `ai_validation_manifest.json` -> `analysis_validation_manifest.json`
- `description_topic_mapping_review.csv` -> `description_topic_mapping_assessment.csv`
- `description_topic_review_evidence.csv` -> `description_topic_evidence.csv`
- `elderly_noncandidate_checks.csv` -> `age50plus_controls.csv`
- `nmf_manual_evaluation_50.csv` -> `description_development_assessments.csv`
- `preliminary_citywide_anomaly_screen.csv` -> `citywide_anomaly_screen.csv`
- `preliminary_citywide_anomaly_screen.png` -> `citywide_anomaly_screen.png`
- `preliminary_citywide_monthly.csv` -> `citywide_monthly_counts.csv`
- `preliminary_citywide_monthly_and_yearly.png` -> `citywide_monthly_and_yearly.png`
- `preliminary_citywide_seasonal.csv` -> `citywide_seasonal_summary.csv`
- `preliminary_citywide_seasonal.png` -> `citywide_seasonal.png`
- `prepared_age_screening.csv` -> `age50plus_screening_features.csv`
- `prepared_age_screening_and_role_cues.png` -> `age50plus_screening_and_role_cues.png`
- `provenance_audit.json` -> `description_model_provenance.json`
- `provisional_exploratory_categories.csv` was temporarily renamed `category_analysis_data.csv`, then archived as a duplicate context export; it is not an active output. Prepared data, computational categories and development evidence remain available separately.
- `provisional_mapping_changes.csv` -> `category_mapping_changes.csv`
- `provisional_report_categories.csv` -> `computational_report_categories.csv`
- `templates/member_06/report_categories.csv` -> `templates/member_06/computational_report_categories.csv` (empty template only; no human-approved result was relabeled)
- `representative_alignment_audit.csv` -> `representative_alignment.csv`
- `review_sample.csv` -> `evaluation_sample.csv`
- `review_sampling_manifest.json` -> `evaluation_sampling.json`
- `selected_model.json` -> `preferred_model.json`
- `shared_topic_review_sample.csv` -> `description_topic_sample.csv`
- `topic_evidence.csv` -> `model_topic_evidence.csv`
- `topic_mapping_review_notes.json` -> `topic_mapping_notes.json`

Additional folder renames: `member_01/exploratory` -> `member_01/geographic_results`; `member_05/exploratory` -> `member_05/time_results`, in both outputs and figures. Duplicate-decision evidence is now `duplicate_decisions.csv`.

The exact modified/added/removed inventory is in [completion_checks.json](completion_checks.json). All 16 primary model-result CSVs are byte-identical to the pre-cleanup backup. The 27 geographic/time-series tables keep the same numerical findings. There are 23 current figures.
