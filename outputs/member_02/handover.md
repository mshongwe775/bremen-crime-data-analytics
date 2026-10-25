# Assignment 02: Topic modeling using titles

## Model
- Model ID: `nmf_titles`
- Method: TF-IDF + NMF
- Selected topic count: 8
- Input: `outputs/member_01/reports_prepared.parquet`
- Input SHA-256: `bf64238b7f929551cf20dadcdd314fa8bf17efe2cd7eab6174fd44dab1a1c139`

## Method settings
- TF-IDF stop words: English
- N-gram range: (1, 2)
- Maximum document frequency: 0.90
- Minimum document frequency: 2
- NMF initialization: `nndsvda`
- Random state: 42
- Maximum iterations: 400

## Topic interpretation
Topic labels in `nmf_titles_topics.csv` are proposed interpretations based on top keywords and representative report titles. They are not verified crime classifications.

Topics 0, 3, 4 and 6 showed relatively consistent patterns in the inspected examples. Topics 1, 2 and 5 combine different report types and should be interpreted cautiously. Topic 7 captures police-operation reports with varied circumstances.

## Assignment coverage
- Prepared reports: 5126
- Assigned: 5100
- Unassigned due to zero TF-IDF features: 24
- Excluded: 2
- Missing text: 0
- Invalid embedding: 0

## Limitations
- NMF groups titles by word patterns; it does not establish what happened in a report.
- Topic scores are not calibrated probabilities.
- A report is assigned to its highest-scoring topic only if its TF-IDF row has nonzero features.
- Reconstruction error alone does not establish topic quality.
- The proposed categories require reviewer validation.

## Peer review and outstanding questions
- Peer reviewer: Member 06.
- Compare these topics with Member 03's description-based model.
- Review mixed topics and confirm whether the proposed labels are appropriate.
- Record reviewer feedback and any changes here before final submission.

## Output inventory
- `nmf_titles_assignments.csv`
- `nmf_titles_topics.csv`
- `nmf_titles_samples.csv`
- `nmf_titles_run.csv`
- `run_metadata.json`
- `handover.md`
