import pandas as pd


def rank_target_accounts(revenue_forecast: pd.DataFrame) -> pd.DataFrame:
    df = revenue_forecast.copy()

    df["Target_Account_Score"] = (
        df["Expected_Value"].fillna(0) / 1000
        + df["BMP_Count"].fillna(0) * 5
        + df["Average_Confidence"].fillna(0) / 2
    ).round(0).astype(int)

    df["Rank"] = df["Target_Account_Score"].rank(
        method="first",
        ascending=False,
    ).astype(int)

    return df.sort_values("Rank")