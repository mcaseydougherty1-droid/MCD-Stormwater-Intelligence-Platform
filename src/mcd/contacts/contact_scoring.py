import pandas as pd


def score_contact_priority(contact_registry: pd.DataFrame) -> pd.DataFrame:
    df = contact_registry.copy()

    df["Contact_Priority_Score"] = (
        df["Owner_Intelligence_Score"].fillna(0)
        + df["BMP_Count"].fillna(0) * 3
        + df["Expected_Value"].fillna(0) / 1000
        + df["HOA_Flag"].astype(int) * 10
    ).round(0).astype(int)

    df["Contact_Priority_Tier"] = pd.cut(
        df["Contact_Priority_Score"],
        bins=[-1, 49, 74, 99, 999],
        labels=["Low", "Moderate", "High", "Priority"],
    )

    df["Outreach_Status"] = "Not contacted"

    df["Contact_Next_Action"] = df["Contact_Priority_Tier"].astype(str).map(
        {
            "Priority": "Find decision-maker and prepare outreach",
            "High": "Research property manager or owner contact",
            "Moderate": "Add to secondary research queue",
            "Low": "Hold for future coverage",
        }
    )

    return df.sort_values(
        ["Contact_Priority_Score", "Expected_Value"],
        ascending=[False, False],
    )