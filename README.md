# Bremen Crime Data Analytics

A six-person course project for Digital Transformation and Innovation: Bremen Police Reports Project 2 — Data Analytics.

## Start here

1. Read [TEAM_GUIDE.md](TEAM_GUIDE.md).
2. Choose one [assignment notebook](team_notebooks/), add your name/reviewer, and tell the group.
3. Use [MAIN WORKING STATION Bremen Crime Data.ipynb](MAIN%20WORKING%20STATION%20Bremen%20Crime%20Data.ipynb) for reviewed group results.
4. Follow [CONTRIBUTING.md](CONTRIBUTING.md) to submit your own work through GitHub.

## The six assignments

| Assignment | Notebook | Work |
|---|---|---|
| 01 | [Preparation and districts](team_notebooks/01_data_and_districts.ipynb) | Shared preparation, district counts and maps |
| 02 | [Title topics](team_notebooks/02_title_topic_modeling.ipynb) | TF-IDF + NMF on title_en |
| 03 | [Description topics](team_notebooks/03_description_topic_modeling.ipynb) | TF-IDF + NMF on description_en |
| 04 | [Embedding topics](team_notebooks/04_embedding_topic_modeling.ipynb) | Supplied embeddings + UMAP + HDBSCAN + BERTopic |
| 05 | [Time patterns](team_notebooks/05_time_and_anomalies.ipynb) | Trends, seasonal peaks and anomalies |
| 06 | [Validation and elderly victims](team_notebooks/06_validation_and_elderly.ipynb) | Reviewed categories, model selection and elderly-victim analysis |

## Set up your computer

Clone the repository. Python 3.12+ is the course recommendation; use one agreed compatible version for the four model runs.

```bash
git clone https://github.com/mshongwe775/bremen-crime-data-analytics.git
cd bremen-crime-data-analytics
python -m venv .venv
```

Activate the environment:

```powershell
# Windows PowerShell
.\.venv\Scripts\Activate.ps1
```

```bash
# macOS / Linux
source .venv/bin/activate
```

Install the required packages:

```bash
python -m pip install -r requirements.txt
```

Open the folder in VS Code, select the .venv Python kernel, and open your assigned notebook. Run setup cells first. Modeling packages must be installed before the relevant analytical cells are implemented.

## Shared inputs and outputs

- bremen_crime_data_2026.parquet: original supplied reports.
- shared/reports_base.parquet: unchanged report values with permanent report_id values.
- shared/source_manifest.json: source checksums, source version and ID rules.
- artifact_contracts.json: required handover filenames, columns and statuses.
- templates/member_XX/: empty examples; they are not submitted results.
- outputs/member_XX/ and figures/member_XX/: each member's completed handover files.
- explanations.html and the supplied course slide deck: source instructions.

The input snapshot has 5,126 reports, publication dates from 14 July 2019 to 3 September 2026, English titles/descriptions, district labels, URLs and two 768-dimensional embeddings. Treat counts as reports and date_posted as a publication date.

## Dependency order

Member 1 publishes the prepared input first. Members 2–4 then compare four topic-model candidates. Member 6 coordinates shared review and approved final labels. Members 1, 5 and 6 use those labels for district, time and elderly-victim analysis. Everyone writes their own interpretation and reviews another member's work.

## Project status

The starter notebooks and shared input checks run successfully. Topic models, reviewed labels and final findings are still TODO. Read each notebook's final handover checklist before submitting.

The five instructor questions concern categories/district distribution, temporal/seasonal patterns, short-term anomalies, highest district/category and citywide composition, and elderly victims. A dashboard is optional bonus work after validation.

## Sources and reuse

The dataset and course references were supplied for this project; their original authors retain their rights. No blanket reuse license is asserted for those materials. Keep source URLs and the supplied instruction references traceable.
