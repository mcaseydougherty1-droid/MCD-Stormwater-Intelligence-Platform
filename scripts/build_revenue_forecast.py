import pandas as pd

from mcd.finance.revenue_model import build_revenue_forecast
from mcd.utils.paths import EXPORTS_DIR, ensure_directories


def main() -> None:
    ensure_directories()

    owner_summary_path = EXPORTS_DIR / "adams_bmp_owner_summary.csv"
    output_path = EXPORTS_DIR / "adams_revenue_forecast.csv"

    owner_summary = pd.read_csv(owner_summary_path)
    forecast = build_revenue_forecast(owner_summary)

    forecast.to_csv(output_path, index=False)

    print(f"Revenue forecast records: {len(forecast)}")
    print(f"Estimated total annual revenue: ${forecast['Estimated_Total_Annual_Revenue'].sum():,.0f}")
    print(f"Expected value: ${forecast['Expected_Value'].sum():,.0f}")
    print(f"A-tier accounts: {int((forecast['Revenue_Tier'] == 'A').sum())}")
    print(f"Saved to {output_path}")


if __name__ == "__main__":
    main()