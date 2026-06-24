import pandas as pd

from mcd.stormwater.asset_registry import summarize_bmp_inventory
from mcd.stormwater.bmp_inventory import build_bmp_inventory
from mcd.utils.paths import EXPORTS_DIR, PROCESSED_DATA_DIR, ensure_directories


def main() -> None:
    ensure_directories()

    opportunities_path = EXPORTS_DIR / "adams_stormwater_opportunities.csv"
    inventory_path = PROCESSED_DATA_DIR / "adams_bmp_inventory.csv"
    summary_path = EXPORTS_DIR / "adams_bmp_owner_summary.csv"

    opportunities = pd.read_csv(opportunities_path)

    inventory = build_bmp_inventory(opportunities)
    summary = summarize_bmp_inventory(inventory)

    inventory.to_csv(inventory_path, index=False)
    summary.to_csv(summary_path, index=False)

    print(f"BMP assets identified: {len(inventory)}")
    print(f"Unique owners: {summary['Owner'].nunique()}")
    print(f"Estimated annual maintenance value: ${inventory['Estimated_Annual_Cost'].sum():,.0f}")
    print(f"Saved inventory to {inventory_path}")
    print(f"Saved owner summary to {summary_path}")


if __name__ == "__main__":
    main()