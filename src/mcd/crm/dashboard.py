import pandas as pd


def build_pipeline_dashboard(pipeline: pd.DataFrame) -> pd.DataFrame:
    summary = (
        pipeline.groupby("Sales_Stage")
        .agg(
            Opportunity_Count=("Opportunity_ID", "count"),
            Total_Value=("Opportunity_Value", "sum"),
            Weighted_Value=("Weighted_Value", "sum"),
        )
        .reset_index()
    )

    return summary.sort_values("Weighted_Value", ascending=False)
