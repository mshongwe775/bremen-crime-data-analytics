# Model comparison, categories and older-person screening
Original owner: Mcolisi Austine Shongwe. Technical assistance: Aya Abdine.

Eight sections verify inputs, compare four models, explain the preferred description-embedding candidate, retain the 15-category codebook and conservative mappings, check full-ID categories, reproduce age screening, present findings and export results. No reader assignments, signature forms or approval gates remain active.

`computational_report_categories.csv` retains 3,362 mapped, 1,427 unclear, 335 unassigned and two excluded reports. The file is explicitly computational; the former human-approved category contract is not silently reused. No unclear cases were forced into categories.

The 60-report computer-assisted comparison matches 13/60 title-NMF labels, 17/60 description-NMF labels, 27/60 title-embedding labels and 25/60 description-embedding labels. The same assistant assessed development and held-out reports; these are descriptive agreements, not independent accuracy or F1. Existing frozen mappings are retained.

Age 50+ screening yields 1,267 candidates. Assessment of those candidates plus 40 controls yields 767 explicit-text target/casualty findings, 234 possible cases, 252 other-role cases, 46 no-evidence results and eight unclear cases. Rules and 941 saved context decisions reproduce the classifications exactly.

Among mapped explicit-text categories, Fraud / deception leads (153). Within that label Schwachhausen leads named districts (13), while 23 locations are Unknown. Across all explicit-text findings, Mitte leads named districts (107). Unknown/Unclear categories (253) and noise (95) limit these rankings. Findings include attempted offenses and traffic casualties; they are not confirmed full-dataset victim totals.

The source excerpts, original assessment time, methods, IDs and checksums remain in the descriptively named assessment files and `analysis_validation_manifest.json`. Independent human validation is not claimed. The Main Working Station is untouched.
