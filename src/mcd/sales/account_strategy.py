import pandas as pd


def assign_account_strategy(accounts: pd.DataFrame) -> pd.DataFrame:
    df = accounts.copy()

    df["Recommended_Action"] = df["Revenue_Tier"].map(
        {
            "A": "Immediate outreach; verify O&M agreement and decision-maker",
            "B": "Research ownership and prepare targeted outreach",
            "C": "Qualify after A/B tier accounts",
            "D": "Hold for future review",
        }
    )

    df["Sales_Priority"] = df["Revenue_Tier"].map(
        {
            "A": "Priority",
            "B": "High",
            "C": "Moderate",
            "D": "Low",
        }
    )

    return df