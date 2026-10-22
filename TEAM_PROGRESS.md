# Team progress

Reviewed on 22 October 2026 (Europe/Berlin).

## Integration

All four non-main remote branch tips visible during this review are contained in main. No forks or open pull requests remained after integration. Source branches are retained so members can continue working and submit new pull requests.

- Book 1: already merged through [PR #2](https://github.com/mshongwe775/bremen-crime-data-analytics/pull/2).
- Book 3: already in main at [f062f30](https://github.com/mshongwe775/bremen-crime-data-analytics/commit/f062f301f9d7a049088a0e1bb96e4145646aac1f). The branch named member-01-data-districts actually contains this description-model contribution; its older files were not copied over newer preparation work.
- Book 5: role claim already merged through [PR #1](https://github.com/mshongwe775/bremen-crime-data-analytics/pull/1).
- Book 6: merged through [PR #3](https://github.com/mshongwe775/bremen-crime-data-analytics/pull/3), including the coordinator's previously uncommitted execution outputs.

Merging accepts the submitted work into the shared repository. Analytical results keep their existing provisional/review status; the merge does not establish final category labels or confirm elderly victims.

## Notebook progress

| Book | Owner evidence | Submitted progress | Remaining work |
|---|---|---|---|
| 01: Data and districts | Meriam El Askri in notebook | Prepared 5,126 rows; 5,124 included and two duplicate exclusions. Submitted quality checks, reviewed district lookup, duplicate review and metadata. | Peer review and preparation-version agreement; category-dependent district tables/maps and rankings. |
| 02: Title topics | Owner not filled in submitted notebook | Starter notebook only; no role output files submitted. | Claim/update the notebook, fit title NMF on the agreed prepared cohort, and provide the required handover. |
| 03: Description topics | ZNtshatsha is the contribution's commit author; owner field remains blank | NMF candidate with 10 topics, 5,126 assignment rows, topic table, 50 examples, run table, metadata, handover and topic-size chart. Compared 8/10/12 topics. | Rerun on the agreed prepared input; respect exclusions; use the common metadata format; complete independent validation and owner/reviewer fields. |
| 04: Embedding topics | Owner not filled in submitted notebook | Starter notebook only; no role output files submitted. | Both supplied embedding pipelines, UMAP/HDBSCAN/BERTopic candidates and required handovers. |
| 05: Time and anomalies | Ghofran Mahmoud in notebook | Role claimed; status In progress. No analytical outputs submitted. | Temporal coverage review and time/anomaly analyses; category-specific results need approved labels. |
| 06: Validation and age 50+ | Mcolisi Austine Shongwe in notebook | Source checks, draft review rules/plan, age screening, comparison chart and 1,225 candidate reports. Age 50+ is the working definition. | Refresh against the agreed prepared input, review victim roles, compare all four models, approve labels and produce final age/category/district results. |

This describes work pushed to this repository, not unpublished work on teammates' computers. As of this review, the invitation to ayaa137 remains pending.

## Verified preparation

- Prepared file: outputs/member_01/reports_prepared.parquet.
- SHA-256: bf64238b7f929551cf20dadcdd314fa8bf17efe2cd7eab6174fd44dab1a1c139.
- All 5,126 permanent IDs are retained and unique. Source text, original district labels, URLs and both embedding arrays match the base snapshot in report-ID order. Dates are datetime values matching the source dates.
- BR001569 and BR002114 are excluded duplicates; their rows remain present. Models fit on the included 5,124 rows and still export all 5,126 assignment IDs, marking those two as excluded.
- The shared geographic representation has 4,149 mapped included reports and 975 included reports with Unknown district. Keep Unknown in citywide totals.
- Preparation metadata and handover still state peer review is pending. Integrity checks here do not replace that independent review or verify every geographic decision.

## Compatibility findings

1. Book 3 used shared/reports_base.parquet with base SHA-256 e413c6bcca065480e00084bac8f18e338325803f3f79bf953b4b5f19c88c0534. It assigns all 5,126 rows, including the two excluded duplicates. Preserve this as a provisional baseline, then rerun on the agreed prepared cohort and record its exact checksum before final comparison.
2. Book 3's CSV files contain the required columns, but its run_metadata.json uses different keys and lacks the shared prepared_sha256, author/reviewer and other common fields. Preserve its useful model settings while adopting templates/member_03/run_metadata.json as the common structure.
3. Book 6's saved screening used the base snapshot: 1,201 reports have a 50+ age-pattern match, versus 590 at 65+. Another 24 have elderly wording without a detected 50+ age, giving 1,225 unique candidates. All victim-review statuses are not_reviewed. These are not confirmed victim totals. Neither excluded duplicate appears in this candidate queue, but the final analysis still needs the agreed prepared cohort and denominators.
4. Book 6's saved availability table predates the merge and shows zero available inputs. The merged folder now contains Book 1's prepared file and Book 3's assignment file; the title and two embedding model assignments are still absent. Refresh the checks on the next notebook run.
5. No selected_model.json, approved report_categories.csv or completed elderly/district/time findings have been submitted. The main workstation's final question-by-question results remain pending.

## Next work order

1. Peer-review Book 1's preparation and agree its frozen checksum.
2. Rerun Book 3 against that version; Books 2 and 4 use the same included report cohort and common handover format.
3. Book 6 coordinates the common manual review, model comparison, category mapping and final label approval. Everyone helps with review. Separately review the age 50+ candidate queue for victim context.
4. Books 1, 5 and 6 build district, time and age-specific results from the same approved labels, retaining Unknown/unassigned cases and consistent inclusion rules.
5. The coordinator integrates reviewed results into the main workstation; the group checks the complete report before submission.

## Review scope

All seven notebooks pass nbformat validation; no saved error outputs were found. Submitted preparation integrity, CSV schemas, description assignment-ID coverage and Book 6 candidate statuses were checked. This integration did not refit models, rerun the analyses, re-evaluate geographic references, perform victim-role annotation or visually re-review all submitted plots. Saved outputs remain attributable to their original runs.
