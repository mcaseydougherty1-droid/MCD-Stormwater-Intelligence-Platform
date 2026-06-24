import pandas as pd

from mcd.sales.account_strategy import assign_account_strategy
from mcd.sales.target_ranker import rank_target_accounts
from mcd.utils.paths import EXPORTS_DIR, ensure_directories


def main() -> None:
    ensure_directories()

    revenue_path = EXPORTS_DIR / "adams_revenue_forecast.csv"
    output_path = EXPORTS_DIR / "adams_target_accounts.csv"

    revenue = pd.read_csv(revenue_path)

    ranked = rank_target_accounts(revenue)
    accounts = assign_account_strategy(ranked)

    accounts.to_csv(output_path, index=False)

    print(f"Target accounts: {len(accounts)}")
    print(f"A-tier accounts: {int((accounts['Revenue_Tier'] == 'A').sum())}")
    print(f"Priority accounts: {int((accounts['Sales_Priority'] == 'Priority').sum())}")
    print(f"Total expected value: ${accounts['Expected_Value'].sum():,.0f}")
    print(f"Saved to {output_path}")


if __name__ == "__main__":
    main()