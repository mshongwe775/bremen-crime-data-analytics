"""Check the six notebooks and their computational results without refitting models."""
from pathlib import Path
import ast
import hashlib
import json
import re
from urllib.parse import unquote
import nbformat
import pandas as pd

ROOT = Path(__file__).resolve().parents[1]

def sha256(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()

def check_project(root=ROOT):
    contract = json.loads((root / "artifact_contracts.json").read_text())
    source = json.loads((root / "shared/source_manifest.json").read_text())
    assert sha256(root / source["raw_file"]) == source["raw_sha256"]
    assert sha256(root / "shared/reports_base.parquet") == contract["base_sha256"]
    prepared_hash = sha256(root / "outputs/member_01/reports_prepared.parquet")
    assert prepared_hash == "bf64238b7f929551cf20dadcdd314fa8bf17efe2cd7eab6174fd44dab1a1c139"
    notebooks = sorted((root / "team_notebooks").glob("*.ipynb"))
    assert len(notebooks) == 6
    code_cells = 0
    for path in notebooks:
        notebook = nbformat.read(path, as_version=4)
        nbformat.validate(notebook)
        headings = {int(match.group(1)) for cell in notebook.cells if cell.cell_type == "markdown"
            for match in [re.match(r"## (\d+)\.", cell.source)] if match}
        assert headings == set(range(1, 9 if path.name.startswith("06") else 8)), path
        for cell in notebook.cells:
            if cell.cell_type == "code":
                ast.parse(cell.source, filename=str(path))
                code_cells += 1
                assert not any(output.output_type == "error" for output in cell.get("outputs", [])), path
    expected_ids = {f"BR{number:06d}" for number in range(5126)}
    expected = {"nmf_titles": ("02", 8, 5069, 55), "nmf_descriptions": ("03", 10, 5124, 0),
        "bertopic_titles": ("04", 59, 4583, 541), "bertopic_descriptions": ("04", 36, 4789, 335)}
    for model_id, (number, n_topics, assigned, unassigned) in expected.items():
        folder = root / "outputs" / f"member_{number}"
        metadata = json.loads((folder / "run_metadata.json").read_text())
        assert metadata["prepared_sha256"] == prepared_hash
        tables = {}
        for kind in ["assignments", "topics", "samples", "run"]:
            name = f"{model_id}_{kind}.csv"
            table = pd.read_csv(folder / name)
            assert table.columns.tolist() == contract["roles"][f"member_{number}"]["csv_schemas"][name]
            tables[kind] = table
        a, t, samples = [tables[key] for key in ["assignments", "topics", "samples"]]
        assert a.report_id.is_unique and set(a.report_id) == expected_ids
        assert set(a.loc[a.assignment_status.eq("excluded"), "report_id"]) == {"BR001569", "BR002114"}
        assert a.assignment_status.eq("assigned").sum() == assigned
        assert a.assignment_status.eq("unassigned").sum() == unassigned
        assert t.topic_id.ge(0).sum() == n_topics
        sizes = a.loc[a.topic_id.notna()].groupby("topic_id").size()
        assert all(sizes.get(row.topic_id, 0) == row.n_reports for row in t.itertuples())
        assert len(samples.merge(a, on=["report_id", "model_id", "topic_id"], validate="many_to_one")) == len(samples)
    for role in contract["roles"].values():
        for name in role["required_files"]:
            assert (root / role["output_folder"] / name).is_file(), (role["output_folder"], name)
    folder = root / "outputs/member_06"
    categories = pd.read_csv(folder / "computational_report_categories.csv")
    assert categories.report_id.is_unique and set(categories.report_id) == expected_ids
    assert categories.category_status.value_counts().to_dict() == {"mapped_topic": 3362, "unclear": 1427, "unassigned": 335, "excluded": 2}
    preference = json.loads((folder / "preferred_model.json").read_text())
    assert preference["status"] == "preferred_computational_candidate"
    assert preference["independent_human_validation"] is False
    assert not (folder / "report_categories.csv").exists() and not (folder / "elderly_summary.csv").exists()
    manifest = json.loads((folder / "analysis_validation_manifest.json").read_text())
    for name, digest in manifest["files"].items():
        assert sha256(folder / name) == digest, name
    geo = pd.read_csv(root / "outputs/member_01/geographic_results/counts.csv")
    assert geo.groupby("geography_level").report_count.sum().eq(5124).all()
    city = pd.read_csv(root / "outputs/member_05/citywide_monthly_counts.csv")
    assert city.report_count.sum() == 5124 and city.report_count.isna().sum() == 11
    assert city.loc[city.month.eq("2021-03"), "report_count"].iloc[0] == 92
    screen = pd.read_csv(root / "outputs/member_05/citywide_anomaly_screen.csv")
    assert screen.evaluable.sum() == 62 and screen.flagged.sum() == 0
    flags = pd.read_csv(root / "outputs/member_05/time_results/anomaly_candidates.csv")
    assert len(flags) == 7 and flags.report_count.ge(flags.threshold).all()
    screening = pd.read_csv(folder / "elderly_screening_results.csv")
    assert screening.groupby("view").report_count.sum().to_dict() == {"category": 1307, "district": 1307}
    saved_groups = pd.read_csv(folder / "age50plus_screening_summary.csv").set_index("ai_victim_group")
    for view in ["category", "district"]:
        assert screening.loc[screening.view.eq(view)].groupby("ai_victim_group").report_count.sum().to_dict() == saved_groups[["candidate", "noncandidate_control"]].sum(axis=1).to_dict()
    provenance = json.loads((folder / "screening_results_provenance.json").read_text())
    for name, digest in provenance["sha256"].items():
        assert sha256(folder / name) == digest
    for path in notebooks + list(root.glob("*.md")):
        if path.suffix == ".ipynb":
            text = "\n".join(c.source for c in nbformat.read(path, as_version=4).cells if c.cell_type == "markdown")
        else:
            text = path.read_text(encoding="utf-8")
        for target in re.findall(r"\]\(([^)]+)\)", text):
            if not target.startswith(("https:", "http:", "#")):
                assert (path.parent / unquote(target.split("#")[0])).exists(), (path, target)
    return {"status": "passed", "notebooks": 6, "compiled_code_cells": code_cells,
        "models_refitted": False, "independent_human_validation": False,
        "checks": ["source and frozen preparation hashes", "notebook schemas, sections and Python syntax",
            "saved error outputs", "four model results, IDs and samples", "required computational outputs",
            "category and geographic totals", "seasonal/anomaly findings", "screening totals and hashes", "local links"]}

if __name__ == "__main__":
    print(json.dumps(check_project(), indent=2))
