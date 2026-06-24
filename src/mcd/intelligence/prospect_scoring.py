import pandas as pd


def score_pipeline(df: pd.DataFrame) -> pd.DataFrame:
    df = df.copy()

    score = df["Target_Flag"].astype(int) * 20
    score += df["MCD_Target_Category"].eq("HOA/Common Area").astype(int) * 20
    score += df["MCD_Target_Category"].eq("Commercial").astype(int) * 15
    score += df["MCD_Target_Category"].eq("Institutional").astype(int) * 10
    score += df["Acres"].fillna(0).clip(0, 20) * 2

    df["Priority_Score"] = score.round(0).astype(int)
    df["Pipeline_Tier"] = pd.cut(
        df["Priority_Score"],
        bins=[-1, 19, 39, 59, 999],
        labels=["D", "C", "B", "A"],
    )

    df["Estimated_Annual_Revenue"] = df["Priority_Score"].apply(
        lambda score_value: 0 if score_value < 20 else 1500 + score_value * 75
    )

    df["Sales_Stage"] = "Research"
    df["Next_Action"] = "Verify O&M/SWM records and owner contact"

    return df.sort_values(["Priority_Score", "Owner"], ascending=[False, True])