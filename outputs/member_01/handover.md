# Data preparation and district analysis — handover

Status: LOCAL PREPARATION FOR REVIEW — peer review and publication pending.

Name: Meriam El Askri
Reviewer: Not assigned; pending
Source/base SHA-256: 05c23babf442967832d277922f2bebe5ebeb43c8891a5e7aafa699644d1a9bf6 / e413c6bcca065480e00084bac8f18e338325803f3f79bf953b4b5f19c88c0534
Prepared dataset SHA-256: bf64238b7f929551cf20dadcdd314fa8bf17efe2cd7eab6174fd44dab1a1c139
Final categories SHA-256 (if used): pending; not used
Python/package versions: 3.12.2; exact distributions in run_metadata.json.

## What I completed

Prepared all 5,126 rows with 5,124 included and two duplicate flags. Both geographic reviews and internal outcomes remain in the notebook. Final category-dependent analyses are not complete.


## Input files and inclusion rules

Immutable raw/base inputs match source_manifest.json. Dates are publication dates, not incident dates. BR001569 is excluded as a match of retained BR001568; BR002114 is excluded as a match of retained BR002113. All other rows remain included. Original IDs, labels, text, URLs and both 768-dimensional embeddings remain aligned and unchanged.


## Output files and row counts

reports_prepared.parquet: 5,126 rows, 11 columns.
data_quality.csv: 43 checks.
district_lookup.csv: 273 original-label defaults, with JSON report_overrides in notes.
duplicate_review.csv: four report decisions.
run_metadata.json and handover.md: metadata and instructions.
Final district_category_counts.csv and highest_district_by_category.csv await approved categories.


## Methods and parameter choices

Shared representation: Stadtteile plus standalone Ortsteile. Borgfeld, Blockland, Seehausen and Strom retain their official names without invented parents or codes. Oberneuland uses its reviewed Stadtteil identity; no Ortsteil is invented. Unverified spelling candidates, combined labels, landmarks, ambiguous and other-municipality candidates remain Unknown. BR001277, BR003479, BR003518 and BR001797 remain Unknown and included. Apply JSON report_overrides from lookup notes after label defaults; a label must never override these exceptions.

To reproduce: select the project Python 3.12.2 .venv and run setup plus Sections 1–4 in order. The export switch defaults to False; existing artifacts are never overwritten. No network calls, geocoding or new embeddings are required. Revised preparation needs agreement and dependent reruns.


## Findings supported by saved outputs

                               level  all_rows  included  mapped_included  unknown_included
                           Ortsteile      5126      5124             2977              2147
Stadtteile plus standalone Ortsteile      5126      5124             4149               975

Both levels count reports once with identical inclusion flags. Never add their totals together. Unknown stays in citywide denominators.


## Validation and reviewer comments

Source rows/IDs/content, finite vectors, dates, flags, schemas and report-level geography validated. The export validation cell checks serialized files, inventory and checksum. Reviewer not assigned; peer review pending. No acceptance or publication is claimed.


## Limitations and unresolved questions

Conservative geography partly relies on reviewed exact names, not a fresh individual review of every report. Reports can be updates, appeals or cover several incidents; counts are reports, not confirmed crimes or risk rates. Unknown retains missing/unresolved information. Standalone names are known locations, not missing parent relationships. References: indexed Bremen street directory November 2025, cross-checked with Die Ortsteile der Stadt Bremen 2015 (published May 2016); latest version and map-boundary compatibility remain unverified. Official URLs and report evidence remain in Section 3 and district_lookup.csv. Package versions do not establish successful model runs. Notebook kernel metadata is inherited; execution here used the project .venv Python, not a verified editor kernel session.


## Where these results belong in the main notebook

Use Data preparation now; district distribution and citywide composition follow approved categories later. The Main Working Station must check full ID coverage, source preservation and exact prepared checksum before accepting this local handover.

Members 02–04: verify SHA-256 against run_metadata.json, then load outputs/member_01/reports_prepared.parquet with pandas.read_parquet. Select eligible = prepared.loc[prepared['include_in_analysis']].copy(). Build text and embedding inputs from that SAME frame/order; never sort separately. Keep report_id strings. Assignment exports must still cover all 5,126 IDs, with assignment_status='excluded' for the two excluded rows. Join using report_id and validate='one_to_one', never URL. Record the exact prepared-file SHA-256 in each run_metadata.json.

Member 06: use the same prepared version. Approved report_categories.csv must cover all IDs, with selected_model.json and matching input checksums. Later join categories one-to-one for BOTH internal analyses; retain identical inclusion flags and Unknown in denominators. Do not invent categories. Any preparation change requires version agreement and rebuilding dependent results.
