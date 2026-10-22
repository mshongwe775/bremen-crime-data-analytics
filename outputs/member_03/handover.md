# NMF Topic Modelling Handover

## 1. Project overview

This analysis applies Non-negative Matrix Factorization (NMF)
to English descriptions of Bremen police reports.

The objective is to identify recurring themes in police reports
and provide topic assignments for further evaluation.

## 2. Input data

- Prepared input: `outputs/member_01/reports_prepared.parquet`
- Total reports in prepared dataset: 5,126
- Reports included in NMF modelling: 5,124
- Reports excluded from NMF modelling: 2
- Total assignment records: 5,126
- Text field: `description_en`
- Input checksum (SHA-256): `bf64238b7f929551cf20dadcdd314fa8bf17efe2cd7eab6174fd44dab1a1c139`
- Input verification: Member 1's prepared dataset was checked, and the SHA-256 checksum remained unchanged during verification.

## 3. Modelling approach

- Method: NMF
- Text representation: TF-IDF
- Selected number of topics: 10
- Random seed: 42
- Initialisation: nndsvda
- Maximum iterations: 500

The 10-topic solution was retained after comparing models
with 8, 10 and 12 topics.

## 4. Identified topics

| Topic ID | Proposed category | Reports |
|---|---|---:|
| 1 | Police Arrests and Apprehension | 1022 |
| 2 | Robberies and Suspect Descriptions | 812 |
| 3 | Road Traffic Accidents | 649 |
| 4 | Football Matches and Public Safety | 98 |
| 5 | Graffiti and Property Damage | 742 |
| 6 | Public Appeals and Investigations | 366 |
| 7 | Drug-Related Offences | 450 |
| 8 | Fraud, Impersonation and Theft | 405 |
| 9 | Public Demonstrations and Assemblies | 489 |
| 10 | Bomb Discoveries and Disposal Operations | 91 |

## 5. Assignment coverage

- Total input reports: 5126
- Assigned reports: 5126
- Unassigned reports: 0
- Missing descriptions: 0

All reports in the prepared input received topic assignments.

## 6. Preliminary evaluation

The NMF model produced several interpretable topics,
including road traffic accidents, football-related public
safety, and bomb disposal operations.

Manual inspection also identified potentially ambiguous
assignments. For example, some reports assigned to the
public demonstrations topic primarily concerned other
police incidents.

These observations show that NMF topics reflect recurring
language patterns and should not be interpreted as
definitive crime classifications.

Models with 8, 10 and 12 topics were compared.
The 10-topic model was retained as a provisional balance
between interpretability and topic detail.

Independent label agreement and cross-model comparison
remain pending.

## 7. Files provided

- `nmf_descriptions_assignments.csv`
- `nmf_descriptions_topics.csv`
- `nmf_descriptions_samples.csv`
- `nmf_descriptions_run.csv`
- `run_metadata.json`
- `handover.md`

The analysis notebook is:
`team_notebooks/03_description_topic_modeling.ipynb`

## 8. Notes for Member 6

Use `report_id` to match the NMF topic assignments
with the other topic modelling outputs.

Use a common review set for fair cross-model evaluation.

Review topic interpretability, assignment coverage,
topic sizes, label agreement, parameter sensitivity,
and potentially ambiguous assignments.

NMF topic weights should not be directly compared
with HDBSCAN assignment strengths.

## 9. Outstanding limitations

- Results remain provisional until Member 1 confirms
  the final prepared dataset.
- Original model fitting time was not recorded.
- Independent human validation is still required.
- Some reports may contain multiple themes that are
  not fully represented by a single topic assignment.

## 10. Reproducibility

The notebook contains the Python code used to prepare the text, fit the NMF model, evaluate its topics, and export the candidate results.

Software versions and model settings are recorded in `run_metadata.json`.

A clean-run reproducibility test was completed on 23 October 2026 by restarting the Python kernel and executing the notebook from beginning to end.

The regenerated outputs confirmed that:

- The NMF model retained its 10 topics and the topic assignments for the 5,124 modelled reports.
- Of the 5,126 original reports, 5,124 were assigned to topics and two duplicate reports were excluded.
- The assignment file and run summary consistently report 5,124 assigned, zero unassigned, and two excluded reports.
- The topic counts sum to 5,124.

The model uses `random_state=42` to support reproducibility. Independent human validation and cross-model comparison remain pending.
