import pandas as pd

from mcd.crm.dashboard import build_pipeline_dashboard
from mcd.crm.pipeline import build_sales_pipeline
from mcd.utils.paths import EXPORTS_DIR, PROCESSED_DATA_DIR, ensure_directories


def main() -> None:
    ensure_directories()

    property_records_path = PROCESSED_DATA_DIR / "adams_unified_property_records.csv"
    pipeline_path = EXPORTS_DIR / "adams_sales_pipeline.csv"
    dashboard_path = EXPORTS_DIR / "adams_sales_pipeline_dashboard.csv"

    properties = pd.read_csv(property_records_path)

    pipeline = build_sales_pipeline(properties)
    dashboard = build_pipeline_dashboard(pipeline)

    pipeline.to_csv(pipeline_path, index=False)
    dashboard.to_csv(dashboard_path, index=False)

    print(f"Sales pipeline records: {len(pipeline)}")
    print(f"Total opportunity value: ${pipeline['Opportunity_Value'].sum():,.0f}")
    print(f"Weighted pipeline value: ${pipeline['Weighted_Value'].sum():,.0f}")
    print(f"Saved pipeline to {pipeline_path}")
    print(f"Saved dashboard to {dashboard_path}")


if __name__ == "__main__":
    main()
