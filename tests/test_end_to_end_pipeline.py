from pathlib import Path


EXPECTED_OUTPUTS = [
    "data/processed/adams_unified_property_records.csv",
    "data/exports/adams_sales_pipeline.csv",
    "data/exports/adams_inspection_schedule.csv",
]


def test_expected_pipeline_outputs_exist():
    missing = [path for path in EXPECTED_OUTPUTS if not Path(path).exists()]

    assert not missing, f"Missing expected pipeline outputs: {missing}"
