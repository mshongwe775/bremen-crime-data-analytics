# Bremen Crime Data — group working guide

## Choose one notebook

This is Project 2: Bremen Police Reports Data Analytics (slides 8–11). Choose one of the six team notebooks, fill in your name/reviewer and tell the group. The existing MAIN WORKING STATION Bremen Crime Data.ipynb is the main workstation/final report.

| Assignment | Work | Early handover | Final receiver |
|---|---|---|---|
| 01 | Preparation and district analysis | Frozen prepared data and quality/lookup/duplicate files | Models first; main district analysis later |
| 02 | NMF topic modeling of titles | Candidate assignments, topics, examples and settings | 06 and main |
| 03 | NMF topic modeling of descriptions | Candidate assignments, topics, examples and settings | 06 and main |
| 04 | BERTopic on both supplied embedding columns | Two candidate runs and readable cluster/topic evidence | 06 and main |
| 05 | Time trends, seasonality and anomalies | Coverage assessment and planned aggregation rules | Main after approved categories |
| 06 | Validation/category selection and elderly victims | Approved final model/categories | 01/05 first; main elderly analysis later |

## Work in stages

1. **Preparation:** 01 prepares a frozen common dataset. Others read source reports, prepare methods or review rules. Everybody agrees one Python environment and category/victim definitions.
2. **Model candidates:** 02–04 work in parallel on the same prepared version. 06 coordinates shared manual review; every member contributes reading and a peer review.
3. **Category selection:** compare the four models, freeze the mapping and selected labels, and publish the report_categories checksum. Do not claim modeled topics are crime categories before reviewing them.
4. **Final analyses:** 01 completes district distribution/maps/composition, 05 completes time/anomaly analysis, and 06 completes elderly analysis. All use the same approved labels.
5. **Integration:** each owner contributes their main-notebook section and interpretation. One coordinator merges files/sections; the entire group checks questions, totals, charts, limitations and a clean top-to-bottom run. No one is assigned all the final writing.

The six roles differ in complexity. Balance work by effort: use the initial modeling milestone to assess progress and move chart/review tasks to members who finish earlier. Do not split the dataset into six unrelated analyses.

## Folder layout

- MAIN WORKING STATION Bremen Crime Data.ipynb: main workstation and final report.
- team_notebooks/: six assignment notebooks; work here to avoid editing conflicts.
- shared/reports_base.parquet: immutable source snapshot with stable IDs; not cleaned or classified.
- shared/source_manifest.json: source/base checksums, ID rules and expected rows.
- outputs/member_01 … member_06/: completed handover files only.
- figures/member_01 … member_06/: readable plots, maps and evidence figures.
- templates/member_XX/: empty schema/handover examples. They are not analytical results.
- artifact_contracts.json: agreed output filenames, columns, statuses and join rules.
- requirements.txt: packages to install in the agreed environment; record exact tested versions afterwards.

## Obtain the complete working folder

Clone the GitHub repository to obtain the notebooks, shared input files, contracts, templates and course references together. A notebook attachment alone cannot run without its inputs. Keep paths relative; never hard-code the coordinator's Windows account or course path.

The base snapshot adds report_id and otherwise keeps raw columns/values. IDs depend on the supplied source version and are already assigned. Do not rebuild them locally. Do not silently replace the source file or regenerate embeddings.

## Input and join rules

The prepared table keeps all 5,126 IDs/original text/embedding columns. Member 1 converts date_posted, adds district_clean, include_in_analysis and exclusion_reason, and freezes a checksum. Flag exclusions rather than deleting rows. Missing district is not a reason to lose a report from citywide totals or text modeling.

Each model's assignments cover all base IDs, one row per report. Status identifies assigned/unassigned/excluded/missing_text/invalid_embedding. NMF weights are not category probabilities. HDBSCAN topic -1 is unassigned. topic_id is local to model_id; Topic 2 in two models need not mean the same thing.

Final report_categories also covers all IDs, one selected model, one primary category per report. Keep unknown/non-crime cases visible. Document manual overrides. Member 1 and 5 join using report_id with validate="one_to_one" and reject input version mismatches. Mapping/label updates require rebuilding dependent outputs.

CSV: UTF-8, index=False, exact contract column names. Dates: YYYY-MM-DD; monthly keys: YYYY-MM. Report-level IDs remain strings. Parameters can be JSON text inside run CSVs; metadata JSON also records full settings and package versions. Optional plots or models do not replace mandatory tabular outputs.

Copy the metadata JSON template and fill its shared keys; do not invent a different metadata format. Shares/agreement rates are fractions from 0 to 1. Topic keywords use semicolon-separated text. Preserve literal None in the raw district lookup when reading CSVs. Skeleton starters for text-only roles load selected columns to avoid bringing both embedding arrays into memory unnecessarily.

## Review and labeling

Use the same evaluation report IDs across models, chosen from their common eligible cohort. A starting review sample of 120 reports can be divided across six members; a second reader checks disagreements. Separate development samples from held-out review. Document the sample selection, category definitions and any ambiguity; the reference labels are a human-reviewed sample, not official ground truth.

Category labels must reflect keywords and actual report descriptions. Some reports contain multiple offenses or are appeals/updates. Agree a primary-category rule before making district/time tables. Topic count and map color alone do not establish valid categories.

Decide the elderly definition explicitly: a threshold such as 65+ is a proposal. Read victim context and keep yes/no_evidence/unclear/not_reviewed/excluded statuses. No_evidence means the detection method found no evidence, not that the victim is definitely not elderly. Verify confirmed cases and sample likely negatives. Report methodological limits.

## Requirements from the slides

Answer all five questions: category/district distribution; trends and seasonal peaks; short-period spikes and possible explanations; highest district by category/citywide composition; elderly-victim category/district. Code belongs on GitHub and the instructor must be invited as requested in slide 9 (Stefanopinto@hotmail.de). A dashboard is a bonus, not a prerequisite for sound modeling.

The slides show made-up example results. Do not copy their numbers or treat their example categories as observed findings. The local Parquet supports this analysis without setting up PostgreSQL/Psycopg2; those are suggested tools, not an additional task in this starter workflow.

## Before final submission

Check source/prepared/label versions, complete ID coverage, status handling, denominators and reconciliation. Confirm geographic mapping coverage, date boundaries, publication-date interpretation and uncertainty. Every major question needs a table/figure and a supported interpretation. Run all notebooks in order, save outputs and inspect figures at reading size. Keep raw data, embeddings and identifying details out of long output dumps. Submit no placeholder conclusions.

Create the optional dashboard only after the group agrees the final labels. The public repository holds the shared starter; group members should contribute their own notebook and role outputs through a branch and pull request as described in CONTRIBUTING.md.

## Work through GitHub

Read CONTRIBUTING.md. Claim one assignment, work on a role branch or personal fork, and submit your notebook/role outputs through a pull request. Keep shared inputs and other members' notebooks unchanged unless the group agrees a change. The coordinator reviews and integrates accepted results into the main workstation.

Public repository access allows reading, cloning and fork-based pull requests. Direct pushing requires the coordinator to invite your GitHub username as a collaborator. Individual invitation links are generated after those invitations are created; the repository URL itself is not a write-access invitation.
