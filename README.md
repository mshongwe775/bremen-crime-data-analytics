# Bremen Crime Data Analytics

A master's-level university project analysing categories, geographic patterns, publication trends and older-person evidence in Bremen police reports.

The six notebooks are complete as a **computational, exploratory analysis**. Classifications are computer-assisted and have not been independently human-validated. Counts describe published reports, not confirmed crimes or population risk.

## Start here

Read [project findings](PROJECT_RESULTS.md), [the results guide](RESULTS_GUIDE.md) and [the completion report](COMPLETION_REPORT.md).

| Notebook | Original owner | Analysis |
|---|---|---|
| [01](team_notebooks/01_data_and_districts.ipynb) | Meriam El Askri | Frozen data, geographic cleaning and district patterns |
| [02](team_notebooks/02_title_topic_modeling.ipynb) | Owner not recorded | Title TF-IDF and NMF |
| [03](team_notebooks/03_description_topic_modeling.ipynb) | Zizipo Samanthur Ntshatsha | Description TF-IDF and NMF |
| [04](team_notebooks/04_embedding_topic_modeling.ipynb) | Aya Abdine | Title and description embedding models |
| [05](team_notebooks/05_time_and_anomalies.ipynb) | Ghofran Mahmoud (Ghod) | Trends, seasonality and unusual increases |
| [06](team_notebooks/06_validation_and_elderly.ipynb) | Mcolisi Austine Shongwe; technical assistance Aya Abdine | Model comparison, computational categories and older-person screening |

Maintenance across the notebooks does not transfer authorship of original contributions. The Main Working Station has intentionally not been changed or executed.

## Run the notebooks

Use Python 3.12+ in a virtual environment with a Jupyter kernel:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
```

Run each notebook from the project root or `team_notebooks`. Notebooks 02-04 default to verifying and displaying saved experiments. Set `REFIT_MODELS = True` only to reproduce model fitting; use the exact versions recorded in each model's metadata, including `pynndescent==0.6.0` for the embedding models. No model downloads or new embeddings are needed for saved-results mode.

The required computational category file already exists. Notebook 06 recomputes the mapping in memory, checks it against that saved file, and regenerates the screening summaries; it expects the saved category file to exist. Run Notebook 06 before regenerating the geographic and time summaries in Notebooks 01 and 05. Run the lightweight project checks with:

```powershell
python scripts/check_project.py
```

The original snapshot has 5,126 reports, dated 14 July 2019 to 3 September 2026. Two duplicate exclusions leave 5,124 eligible reports. `date_posted` is a publication date. Frozen preparation: `outputs/member_01/reports_prepared.parquet`; it is never overwritten.

Optional team reader worksheets and approval gates have been removed from the active workflow. The current contract explicitly identifies computational outputs; it does not reinterpret former human-approved deliverables. The verified local recovery archive is described in [the completion report](COMPLETION_REPORT.md).

Course requirements and team roles are in [TEAM_GUIDE.md](TEAM_GUIDE.md). Original supplied data, slide deck and explanations remain unchanged. No blanket reuse license is asserted for supplied materials.
