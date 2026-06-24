import pandas as pd

from mcd.hoa.hoa_extractor import extract_hoa_candidates
from mcd.hoa.hoa_registry import build_hoa_registry
from mcd.utils.paths import EXPORTS_DIR, PROCESSED_DATA_DIR, ensure_directories


def main() -> None:
    ensure_directories()

    opportunities_path = EXPORTS_DIR / "adams_stormwater_opportunities.csv"
    output_path = PROCESSED_DATA_DIR / "adams_hoa_registry.csv"

    opportunities = pd.read_csv(opportunities_path)

    hoa_candidates = extract_hoa_candidates(opportunities)
    registry = build_hoa_registry(hoa_candidates)

    registry.to_csv(output_path, index=False)

    print(f"HOA candidate parcels: {len(hoa_candidates)}")
    print(f"HOA entities: {len(registry)}")
    print(f"Estimated HOA annual revenue: ${registry['Estimated_Annual_Revenue'].sum():,.0f}")
    print(f"Saved to {output_path}")


if __name__ == "__main__":
    main()