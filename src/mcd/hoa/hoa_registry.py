import pandas as pd


def build_hoa_registry(hoa_parcels: pd.DataFrame) -> pd.DataFrame:
    registry = (
        hoa_parcels.groupby("Owner")
        .agg(
            Parcel_Count=("PIN", "count"),
            Total_Acres=("Acres", "sum"),
            Average_Priority_Score=("Priority_Score", "mean"),
            Estimated_BMP_Count=("Likely_BMP_Present", "sum"),
            Estimated_Annual_Revenue=("Estimated_Annual_Contract", "sum"),
        )
        .reset_index()
        .rename(columns={"Owner": "HOA_Name"})
    )

    registry["Sales_Status"] = "Research"
    registry["Next_Action"] = "Verify HOA board/property manager and O&M records"

    return registry.sort_values(
        ["Estimated_Annual_Revenue", "Average_Priority_Score"],
        ascending=[False, False],
    )