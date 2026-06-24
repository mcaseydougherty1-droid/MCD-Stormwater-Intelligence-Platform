import pandas as pd

from mcd.intelligence.bmp_detector import detect_likely_bmps
from mcd.intelligence.opportunity_engine import score_stormwater_opportunities
from mcd.utils.paths import EXPORTS_DIR, PROCESSED_DATA_DIR, ensure_directories


def main() -> None:
    ensure_directories()

    scored_path = PROCESSED_DATA_DIR / "adams_parcels_scored.csv"
    output_path = EXPORTS_DIR / "adams_stormwater_opportunities.csv"

    scored = pd.read_csv(scored_path)

    detected = detect_likely_bmps(scored)
    opportunities = score_stormwater_opportunities(detected)

    opportunities = opportunities[opportunities["Likely_BMP_Present"] == True]
    opportunities.to_csv(output_path, index=False)

    print(f"Stormwater opportunities: {len(opportunities)}")
    print(f"Priority opportunities: {int((opportunities['Opportunity_Tier'].astype(str) == 'Priority').sum())}")
    print(f"Estimated annual contract value: ${opportunities['Estimated_Annual_Contract'].sum():,.0f}")
    print(f"Saved to {output_path}")


if __name__ == "__main__":
    main()