import pandas as pd


def build_owner_registry(
    revenue_forecast: pd.DataFrame,
    target_accounts: pd.DataFrame,
    bmp_inventory: pd.DataFrame,
    hoa_registry: pd.DataFrame,
    document_registry: pd.DataFrame,
) -> pd.DataFrame:
    owners = revenue_forecast.copy()

    owners = owners.rename(columns={"Owner": "Owner_Name"})

    bmp_summary = (
        bmp_inventory.groupby("Owner")
        .agg(
            BMP_Count=("BMP_ID", "count"),
            Estimated_BMP_Annual_Cost=("Estimated_Annual_Cost", "sum"),
            Average_BMP_Confidence=("Confidence_Score", "mean"),
        )
        .reset_index()
        .rename(columns={"Owner": "Owner_Name"})
    )

    hoa_summary = hoa_registry.copy().rename(columns={"HOA_Name": "Owner_Name"})
    hoa_summary["HOA_Flag"] = True

    document_summary = (
        document_registry.groupby("Owner")
        .agg(
            Document_Record_Count=("Document_Type", "count"),
            Verified_Document_Count=("Verified", "sum"),
        )
        .reset_index()
        .rename(columns={"Owner": "Owner_Name"})
    )

    target_summary = target_accounts[
        ["Owner", "Rank", "Target_Account_Score", "Sales_Priority"]
    ].rename(columns={"Owner": "Owner_Name"})

    owners = owners.merge(bmp_summary, on="Owner_Name", how="left")
    owners = owners.merge(
        hoa_summary[["Owner_Name", "HOA_Flag"]],
        on="Owner_Name",
        how="left",
    )
    owners = owners.merge(document_summary, on="Owner_Name", how="left")
    owners = owners.merge(target_summary, on="Owner_Name", how="left")

    owners["HOA_Flag"] = owners["HOA_Flag"].fillna(False)
    owners["Document_Record_Count"] = owners["Document_Record_Count"].fillna(0)
    owners["Verified_Document_Count"] = owners["Verified_Document_Count"].fillna(0)

    if "BMP_Count_x" in owners.columns:
        owners["BMP_Count"] = owners["BMP_Count_x"]

    if "BMP_Count_y" in owners.columns:
        owners["BMP_Count"] = owners["BMP_Count_y"].fillna(owners.get("BMP_Count", 0))

    if "Estimated_Annual_Cost" in owners.columns and "Estimated_BMP_Annual_Cost" not in owners.columns:
        owners["Estimated_BMP_Annual_Cost"] = owners["Estimated_Annual_Cost"]

    if "Average_Confidence_x" in owners.columns:
        owners["Average_Confidence"] = owners["Average_Confidence_x"]

    if "Average_Confidence_y" in owners.columns:
        owners["Average_Confidence"] = owners["Average_Confidence_y"].fillna(
            owners.get("Average_Confidence", 0)
        )

    return owners