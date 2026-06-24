import pandas as pd


def assign_priority_tier(score: float) -> str:
    if score >= 90:
        return "Priority"
    if score >= 70:
        return "High"
    if score >= 40:
        return "Moderate"
    return "Low"


def score_owner_intelligence(owner_profiles: pd.DataFrame) -> pd.DataFrame:
    df = owner_profiles.copy()

    df["Owner_Intelligence_Score"] = (
        df["Expected_Value"].fillna(0) / 1000
        + df["BMP_Count"].fillna(0) * 5
        + df["HOA_Flag"].astype(int) * 15
        + df["Document_Record_Count"].fillna(0) * 3
    ).round(0)

    df["Priority_Tier"] = df["Owner_Intelligence_Score"].apply(assign_priority_tier)

    df["Recommended_Action"] = df["Priority_Tier"].map(
        {
            "Priority": "Immediate outreach; verify O&M agreement and decision-maker",
            "High": "Research ownership, documents, and BMP evidence",
            "Moderate": "Review after priority/high accounts",
            "Low": "Hold for later market coverage",
        }
    )

    return df.sort_values(
        ["Owner_Intelligence_Score", "Expected_Value"],
        ascending=[False, False],
    )