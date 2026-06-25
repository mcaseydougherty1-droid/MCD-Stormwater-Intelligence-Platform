import pandas as pd


def assign_sales_stage(row: pd.Series) -> str:
    if row.get("Contact_Priority_Tier", "") == "Priority":
        return "Researching"

    if row.get("BMP_Count", 0) > 0:
        return "Identified"

    return "Hold"


def assign_probability(stage: str) -> float:
    return {
        "Identified": 0.05,
        "Researching": 0.10,
        "Contact Located": 0.20,
        "Initial Outreach": 0.25,
        "Meeting Scheduled": 0.40,
        "Site Visit": 0.50,
        "Proposal Sent": 0.65,
        "Negotiating": 0.80,
        "Won": 1.00,
        "Lost": 0.00,
        "Hold": 0.00,
    }.get(stage, 0.05)


def build_opportunity_records(properties: pd.DataFrame) -> pd.DataFrame:
    df = properties.copy()

    df["Opportunity_ID"] = df["PIN"].apply(lambda value: f"OPP-{value}")
    df["Sales_Stage"] = df.apply(assign_sales_stage, axis=1)
    df["Probability_to_Close"] = df["Sales_Stage"].apply(assign_probability)
    df["Opportunity_Value"] = pd.to_numeric(
        df["Estimated_Total_Annual_Revenue"],
        errors="coerce",
    ).fillna(0)
    df["Weighted_Value"] = df["Opportunity_Value"] * df["Probability_to_Close"]

    return df
