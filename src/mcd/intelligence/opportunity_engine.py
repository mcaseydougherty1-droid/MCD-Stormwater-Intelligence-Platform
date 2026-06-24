import pandas as pd


CONFIDENCE_POINTS = {
    "High": 30,
    "Medium-High": 25,
    "Medium": 20,
    "Low": 0,
}


def score_stormwater_opportunities(df: pd.DataFrame) -> pd.DataFrame:
    df = df.copy()

    score = df["Priority_Score"].fillna(0)
    score += df["BMP_Confidence"].map(CONFIDENCE_POINTS).fillna(0)
    score += df["Likely_BMP_Present"].astype(int) * 20

    df["MCD_Opportunity_Score"] = score.clip(0, 100).round(0).astype(int)

    df["Opportunity_Tier"] = pd.cut(
        df["MCD_Opportunity_Score"],
        bins=[-1, 39, 59, 79, 100],
        labels=["Low", "Moderate", "High", "Priority"],
    )

    df["Recommended_Action"] = df["Opportunity_Tier"].astype(str).map(
        {
            "Priority": "Research O&M agreement and prepare outreach",
            "High": "Verify ownership and inspect GIS/aerial imagery",
            "Moderate": "Review parcel context and document availability",
            "Low": "Hold for later review",
        }
    )

    return df.sort_values(
        ["MCD_Opportunity_Score", "Estimated_Annual_Contract", "Owner"],
        ascending=[False, False, True],
    )