"""Summarize saved computer-assisted age/person evidence."""
from pathlib import Path
import hashlib
import json

import pandas as pd
from matplotlib.figure import Figure


def build_screening_results(root):
    folder = root / "outputs/member_06"
    sources = ["age50plus_assessments.csv", "age50plus_screening_summary.csv",
               "age50plus_candidates.csv", "age50plus_controls.csv",
               "computational_report_categories.csv"]
    evidence = pd.read_csv(folder / sources[0], keep_default_na=False)
    categories = pd.read_csv(folder / sources[-1], keep_default_na=False)
    assert evidence.report_id.is_unique and categories.report_id.is_unique
    prepared_path = root / "outputs/member_01/reports_prepared.parquet"
    prepared = pd.read_parquet(prepared_path, columns=["report_id", "district_clean", "include_in_analysis"])
    categories = categories.merge(prepared, on="report_id", validate="one_to_one")
    candidates = set(pd.read_csv(folder / sources[2]).report_id)
    controls = set(pd.read_csv(folder / sources[3]).report_id)
    assert not candidates & controls
    assert set(evidence.report_id) == candidates | controls
    joined = evidence.merge(categories, on="report_id", validate="one_to_one")
    assert len(joined) == len(evidence) and joined.include_in_analysis.all()
    joined["assessment_cohort"] = joined.report_id.map(
        lambda report_id: "candidate" if report_id in candidates else "noncandidate_control")
    joined["category"] = joined.crime_category.where(
        joined.category_status.ne("unassigned"), "Unassigned (model noise)")

    # Each report appears once per view. Category and district totals are separate views.
    tables = []
    for field in ["category", "district_clean"]:
        table = joined.groupby([field, "assessment_cohort", "ai_victim_group"]).size().reset_index(name="report_count")
        assert table.report_count.sum() == len(evidence)
        table = table.rename(columns={field: "group"})
        table.insert(0, "view", "category" if field == "category" else "district")
        table["assessment_status"] = "computer_assisted_provisional"
        tables.append(table)
    results = pd.concat(tables, ignore_index=True)
    results.to_csv(folder / "elderly_screening_results.csv", index=False)
    joint = joined.groupby(["category", "district_clean", "assessment_cohort", "ai_victim_group"]).size().reset_index(name="report_count")
    assert joint.report_count.sum() == len(evidence)
    joint.to_csv(folder / "age50plus_category_district_counts.csv", index=False)
    labels = {
        "explicit_text_older_victim": "Explicit victim/target evidence",
        "possible_older_victim_insufficient_evidence": "Possible older victim",
        "older_person_other_role": "Older person in another role",
        "no_evidence_of_older_victim": "No older-victim evidence",
        "unclear": "Unclear",
    }
    counts = evidence.ai_victim_group.value_counts().reindex(labels)
    fig = Figure(figsize=(10, 4.5))
    ax = fig.subplots()
    bars = ax.barh(list(labels.values()), counts, color="#327b88")
    ax.bar_label(bars, padding=4)
    ax.invert_yaxis()
    ax.set(title="Elderly Screening Results — provisional", xlabel="Assessed reports (1,267 candidates + 40 controls)", xlim=(0, counts.max() * 1.14))
    fig.text(.5, .01, "Computer-assisted source-text evidence; age 50+; not confirmed victim totals", ha="center", fontsize=9)
    fig.tight_layout(rect=(0, .05, 1, 1))
    figure_path = root / "figures/member_06/elderly_screening_results.png"
    fig.savefig(figure_path, dpi=170, bbox_inches="tight")
    files = sources + ["elderly_screening_results.csv", "age50plus_category_district_counts.csv"]
    provenance = {
        "status": "computer_assisted_provisional",
        "method": "Group saved AI age/person classifications by existing provisional category and prepared district; no new classifications or human decisions.",
        "screened_reports": len(evidence), "candidates": len(candidates), "controls": len(controls),
        "denominator": "Assessed reports only; each view totals 1,307 separately. Do not add views or interpret counts as prevalence.",
        "limitations": ["Age 50+ is the project working threshold.",
                       "Categories and victim roles are computational; explicit-text findings include attempts and traffic casualties.",
                       "Unclear categories, model noise and Unknown geography remain included.",
                       "The 40 controls do not establish screening sensitivity."],
        "sha256": {name: hashlib.sha256((folder / name).read_bytes()).hexdigest() for name in files},
        "prepared_sha256": hashlib.sha256(prepared_path.read_bytes()).hexdigest(),
        "figure": {"path": figure_path.relative_to(root).as_posix(),
                   "sha256": hashlib.sha256(figure_path.read_bytes()).hexdigest()},
    }
    (folder / "screening_results_provenance.json").write_text(json.dumps(provenance, indent=2) + "\n", encoding="utf-8")
    return results


if __name__ == "__main__":
    root = Path(__file__).resolve().parents[1]
    results = build_screening_results(root)
    print("Elderly Screening Results: saved category and district summaries; all findings remain provisional.")
