import pandas as pd


def summarize_bmp_inventory(inventory: pd.DataFrame) -> pd.DataFrame:
    summary = (
        inventory.groupby("Owner")
        .agg(
            BMP_Count=("BMP_ID", "count"),
            Estimated_Annual_Cost=("Estimated_Annual_Cost", "sum"),
            Average_Confidence=("Confidence_Score", "mean"),
        )
        .reset_index()
    )

    summary["Registry_Status"] = "Needs field/document verification"
    summary["Next_Action"] = "Confirm BMP type, ownership, and O&M obligation"

    return summary.sort_values(
        ["Estimated_Annual_Cost", "BMP_Count"],
        ascending=[False, False],
    )