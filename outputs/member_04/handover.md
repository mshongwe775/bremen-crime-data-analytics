# Topic modeling using supplied embeddings - handover

Name: Aya Abdine
Reviewer: Pending - not assigned
Status: Executed candidates; peer/group acceptance pending.
Source/base SHA-256: 05c23babf442967832d277922f2bebe5ebeb43c8891a5e7aafa699644d1a9bf6 / e413c6bcca065480e00084bac8f18e338325803f3f79bf953b4b5f19c88c0534
Prepared SHA-256: bf64238b7f929551cf20dadcdd314fa8bf17efe2cd7eab6174fd44dab1a1c139
Final categories: not used. Python: 3.13.7; packages in run_metadata.json.

## What I completed

Two unchanged BERTopic candidates, three-setting sensitivity study, representative/random evidence and four figures. Aya Abdine's cleaned notebook reproduces previous assignments, topics, samples and parameters.

## Input files and inclusion rules

outputs/member_01/reports_prepared.parquet: 5,126 IDs, 5,124 eligible. BR001569/BR002114 excluded. Texts and finite numeric 768D vectors are validated/aligned. Preparation acceptance pending.

## Output files and row counts

- bertopic_titles_assignments.csv: 5,126 rows.
- bertopic_titles_topics.csv: 60 rows.
- bertopic_titles_samples.csv: 298 rows.
- bertopic_titles_run.csv: 1 rows.
- bertopic_descriptions_assignments.csv: 5,126 rows.
- bertopic_descriptions_topics.csv: 37 rows.
- bertopic_descriptions_samples.csv: 183 rows.
- bertopic_descriptions_run.csv: 1 rows.
- run_metadata.json; handover.md.
- figures/member_04/bertopic_titles_umap2d.png
- figures/member_04/bertopic_descriptions_umap2d.png
- figures/member_04/bertopic_titles_topic_sizes.png
- figures/member_04/bertopic_descriptions_topic_sizes.png

## Methods and parameter choices

Supplied embeddings -> 5D cosine UMAP (15 neighbors, min_dist=0, seed=42) -> Euclidean HDBSCAN (30/5, EOM) -> c-TF-IDF keywords. Original sensitivity settings retained; independent 2D views. Balanced is a working granularity compromise; full parameters/tradeoffs are in the notebook and metadata.

## Findings supported by saved outputs

- bertopic_titles: 59 topics, 4,583 assigned, 541 noise (10.56%), 21.19 s.
- bertopic_descriptions: 36 topics, 4,789 assigned, 335 noise (6.54%), 25.42 s.

Readable traffic, burglary/theft, drug, fraud, graffiti and public-event themes coexist with mixed groups. Random reports BR001827 (title topic 0) and BR000504 (description topic 4) contrast with representatives. No validated model ranking; see notebook evidence.

## Validation and reviewer comments

Hashes, source preservation, full IDs, exclusions, schemas, statuses, topic/sample consistency and CSV serialization passed before publication. Reviewer unassigned; proposals are not approved categories.

## Limitations and unresolved questions

Reports are not confirmed crimes. Geometry, parameters and mixed themes limit interpretation. Common environment and independent validation pending. Member 2 exports unavailable. Member 3 fitted 5,126 base rows including duplicates: coordinate prepared-version rerun, missing runtime/checksum and keyword-delimiter correction. Common-ID comparison remains descriptive.

## Where these results belong in the main notebook

Member 6 reviews both candidate sets, joining report_id one-to-one with checksum checks and noise -1 preserved. After acceptance, import tables/four figures into Embedding topic modeling and Model comparison and approved labels. Final district/time/elderly analyses require validated categories.
