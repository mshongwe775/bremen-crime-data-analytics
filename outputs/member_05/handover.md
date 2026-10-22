# Time patterns and unusual increases — handover

Status: IN PROGRESS. All-report results complete; category-level results pending Member 6.

Name: Ghofran Mahmoud
Reviewer: not assigned yet
Source/base SHA-256: 05c23babf442967832d277922f2bebe5ebeb43c8891a5e7aafa699644d1a9bf6 / e413c6bcca065480e00084bac8f18e338325803f3f79bf953b4b5f19c88c0534
Prepared dataset SHA-256: bf64238b7f929551cf20dadcdd314fa8bf17efe2cd7eab6174fd44dab1a1c139
Final categories SHA-256 (if used): not used (pending)
Python/package versions: 3.11.9; see run_metadata.json

## What I completed

- Sections 1 to 7 of the Role 5 notebook on all 5,124 included reports, by district.
- Coverage audit, monthly counts, district trend tests, seasonality, holiday-week comparison and a spike rule with manual reading of every candidate.
- Category-level trends and spikes are coded and switch on automatically once Member 6 publishes approved categories.

## Input files and inclusion rules

- outputs/member_01/reports_prepared.parquet (SHA-256 checked); include_in_analysis = True only (5,124 reports).
- Counting unit: published reports by date_posted (publication date, not incident date).
- Citywide window: 2020-08 to 2026-08 (complete months). District window: 2021-01 to 2026-08 (district labels change level before 2021).
- No reports exist between 2019-08 and 2020-06; this gap is not treated as zero crime.

## Output files and row counts

- monthly_counts.csv: 1824 rows (observed months x districts x categories, zero-filled within observed months).
- seasonal_summary.csv: 12 rows (calendar month x category, complete years 2021 to 2025).
- anomalies.csv: 10 candidate spikes, each with evidence URLs and a reviewed explanation.
- Figures: fig1_monthly_coverage.png, fig2_district_label_change.png, fig3_citywide_monthly.png, fig4_district_monthly.png, fig5_seasonality.png, fig6_spike_candidates.png in figures/member_05.

## Methods and parameter choices

- Trends: reports per month by year; Kendall tau on monthly counts per district, Holm correction across districts.
- Seasonality: reports per day by calendar month over complete years; Kruskal-Wallis across months.
- Holidays: weeks containing a Bremen public holiday, 24 Dec or 31 Dec vs other weeks (Mann-Whitney).
- Spikes: count vs mean of previous 12 months (district-month) or 26 weeks (district-week); flag if count >= 5 (4 for weeks), >= 2x (3x) baseline and Poisson p < 0.001. "Strong" also needs p < 0.05 / number of tests.

## Findings supported by saved outputs

- Q2 (trends and seasonality): citywide volume is stable (12-month average 60 to 80 reports; single months 53 to 92); no district shows a significant monotonic trend after correction; no significant seasonal peak (Kruskal-Wallis p = 0.28), with December lowest per day.
- Q3 (short-term spikes): 10 candidate district spikes against about 8 expected by chance; none pass the Bonferroni threshold. Reading the reports shows the larger ones are often one incident published several times (Vegesack June 2026, Vahr June 2026) or unrelated reports in the same week. Holiday weeks have fewer published reports, not more.

## Validation and reviewer comments

- Schemas match artifact_contracts.json; monthly totals reconcile to 5,124 included reports; files read back after export.
- Reviewer: not assigned yet.

## Limitations and unresolved questions

- Category-level answers (which crime types rise or spike) need Member 6's approved report_categories.csv; rerun this notebook when it is published.
- The dataset looks like a sample of press releases (max 8 per day, flat monthly volume), so trends describe publication, not crime levels.
- Unknown district reports rise from about 11 to 15 per month; district counts may understate later years.
- Recommendation for Member 1: map plain "Mitte" labels to Mitte; 65 of them fall before 2021 and empty Mitte in 2020.

## Where these results belong in the main notebook

- Section 7 (Time patterns, seasonality and investigated anomalies): import the three CSVs and figures fig1 to fig6.
- Answers Questions 2 and 3; Question 3 "drivers" come from the possible_explanation and evidence_url columns.
