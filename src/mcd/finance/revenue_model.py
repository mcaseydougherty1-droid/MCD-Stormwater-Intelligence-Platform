import pandas as pd

from mcd.finance.contract_estimator import (
    estimate_dredging_allowance,
    estimate_inspection_revenue,
    estimate_mowing_revenue,
    estimate_repair_allowance,
)


def assign_revenue_tier(value: float) -> str:
    if value >= 15000:
        return "A"
    if value >= 7500:
        return "B"
    if value >= 3000:
        return "C"
    return "D"


def build_revenue_forecast(owner_summary: pd.DataFrame) -> pd.DataFrame:
    df = owner_summary.copy()

    df["Estimated_Mowing_Revenue"] = df.apply(estimate_mowing_revenue, axis=1)
    df["Estimated_Inspection_Revenue"] = df.apply(estimate_inspection_revenue, axis=1)
    df["Estimated_Dredging_Revenue"] = df.apply(estimate_dredging_allowance, axis=1)
    df["Estimated_Repair_Revenue"] = df.apply(estimate_repair_allowance, axis=1)

    df["Estimated_Total_Annual_Revenue"] = (
        df["Estimated_Mowing_Revenue"]
        + df["Estimated_Inspection_Revenue"]
        + df["Estimated_Dredging_Revenue"]
        + df["Estimated_Repair_Revenue"]
    )

    df["Revenue_Tier"] = df["Estimated_Total_Annual_Revenue"].apply(assign_revenue_tier)

    df["Probability_of_Close"] = df["Revenue_Tier"].map(
        {
            "A": 0.35,
            "B": 0.25,
            "C": 0.15,
            "D": 0.05,
        }
    )

    df["Expected_Value"] = (
        df["Estimated_Total_Annual_Revenue"] * df["Probability_of_Close"]
    )

    df["Next_Action"] = df["Revenue_Tier"].map(
        {
            "A": "Prioritize outreach and verify O&M agreement",
            "B": "Review owner and document status",
            "C": "Qualify after higher-tier prospects",
            "D": "Hold for future review",
        }
    )

    return df.sort_values(
        ["Estimated_Total_Annual_Revenue", "Expected_Value"],
        ascending=[False, False],
    )