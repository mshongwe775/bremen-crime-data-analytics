# Team and methodology guide

## Six original contributions

| Notebook | Original owner | Contribution |
|---|---|---|
| 01 | Meriam El Askri | Data preparation and district analysis |
| 02 | Not recorded | Title topic modeling; ownership remains unconfirmed |
| 03 | Zizipo Samanthur Ntshatsha | Description topic modeling |
| 04 | Aya Abdine | Both supplied-embedding experiments |
| 05 | Ghofran Mahmoud (Ghod) | Time patterns and anomaly screening |
| 06 | Mcolisi Austine Shongwe | Model/category comparison and older-person screening; technical assistance by Aya Abdine |

Computer-assisted maintenance does not invent ownership, human validation or approvals. Keep attribution in each notebook and handover.

## Assignment requirements

The supplied course slides 8-11 require data-science methods and answers on category/district distribution, changes over publication time, seasonal and short-term increases, district/category leaders and citywide composition, and older-person targeting. The data explanations suggest title/description topic modeling or clustering supplied embeddings. A dashboard is optional bonus work. Code belongs on GitHub, with the instructor invitation requested on slide 9 at submission time.

The course materials do not require the team's two-reader worksheets, signature forms or focused manual audit. Those optional procedures are no longer active. No upload, invitation, commit or push is made by this cleanup.

## Shared analytical rules

- Keep all 5,126 permanent IDs. Flag the two duplicates rather than deleting their rows.
- Use the frozen prepared file with SHA-256 `bf64238b7f929551cf20dadcdd314fa8bf17efe2cd7eab6174fd44dab1a1c139`.
- All four topic candidates use 5,124 eligible reports. Model IDs and local topic IDs stay unchanged.
- Join tables by `report_id`, checking uniqueness and the source version.
- Retain Unknown geography, Unknown/Unclear categories and unassigned model noise in totals.
- Interpret the two geographic views separately; they overlap.
- Use publication dates and retain observation gaps. Report counts are not incidence or risk rates.
- Age 50+ is the working threshold; 65+ is a nested comparison. Person-role screening is computer-assisted source-text evidence, not confirmed full-dataset victim counts.

## Workflow and outputs

Notebooks 02-04 verify saved experiments by default and retain their original optional fitting code. Notebook 06 compares models, retains the description embedding candidate and applies the existing conservative mapping. Notebooks 01 and 05 use the resulting computational categories directly. No reader assignments or approval forms block the analysis.

`artifact_contracts.json` records active computational filenames and schemas. Former approved-label and confirmed-victim deliverables are explicitly listed as not produced; their meanings have not been changed. [RESULTS_GUIDE.md](RESULTS_GUIDE.md) lists current outputs. Only the two small scripts for saved-result checks and screening aggregation support the notebooks.

The Main Working Station remains a separate future integration task. Before submission, integrate the six findings, inspect the final presentation, and follow the course's GitHub/instructor-sharing instructions.
