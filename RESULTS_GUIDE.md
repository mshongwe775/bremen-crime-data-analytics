# Results and file guide

All current category and age/person outputs are computational and exploratory. Descriptive filenames do not turn computer-assisted classifications into independent human labels.

| Result | Location |
|---|---|
| Frozen prepared data | `outputs/member_01/reports_prepared.parquet` |
| Source checks and geographic evidence | `shared/source_manifest.json`, `outputs/member_01/`, Notebook 01 metadata |
| District categories, composition and rankings | [Geographic results](outputs/member_01/geographic_results/) |
| Title NMF assignments, topics, samples and run settings | [Member 02](outputs/member_02/) |
| Description NMF and corrected representatives | [Member 03](outputs/member_03/) |
| Title/description embedding experiments | [Member 04](outputs/member_04/) |
| Monthly citywide counts and screening | [Monthly counts](outputs/member_05/citywide_monthly_counts.csv), [anomaly screen](outputs/member_05/citywide_anomaly_screen.csv) |
| Seasonal, district/category trends and anomaly evidence | [Time results](outputs/member_05/time_results/) |
| Computational categories | [Report assignments](outputs/member_06/computational_report_categories.csv) |
| Category definitions and mappings | [Codebook](outputs/member_06/category_codebook.csv), [mapping](outputs/member_06/category_mapping.csv) |
| Preferred model and comparison | [Preference](outputs/member_06/preferred_model.json), [comparison](outputs/member_06/model_comparison.csv) |
| Computer-assisted evaluation | [Model assessment](outputs/member_06/model_assessment.csv), development/held-out category assessments and comparisons in the same folder |
| Age 50+ candidates | [Candidates](outputs/member_06/age50plus_candidates.csv) |
| Older-person assessments | [Source evidence](outputs/member_06/age50plus_assessments.csv), [five-group summary](outputs/member_06/age50plus_screening_summary.csv) |
| Older-person category/district findings | [Screening results](outputs/member_06/elderly_screening_results.csv) |
| Assessment method and provenance | [Method](outputs/member_06/age50plus_assessment_method.py), [manifest](outputs/member_06/analysis_validation_manifest.json), [summary hashes](outputs/member_06/screening_results_provenance.json) |
| Figures | `figures/member_01` through `figures/member_06` |

The 60 development and 60 held-out assessments were produced by the same assistant. Nine earlier development suggestions reflect user agreement with chat summaries, not independent full-report human labels. The description model's historical `human_judgment` column has unverified authorship; its original values are retained with that limitation.

The contract explicitly separates these outputs from former approved-label and confirmed-victim deliverables. Original assessment dates, model settings, seeds and scientific values remain traceable. Removed optional workflow files, old duplicate drafts and prior maintenance records are recoverable from the verified backup described in [COMPLETION_REPORT.md](COMPLETION_REPORT.md).
