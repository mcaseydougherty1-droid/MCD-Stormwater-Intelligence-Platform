import pandas as pd

from mcd.reports.prospect_review import create_prospect_review
from mcd.utils.paths import PROCESSED_DATA_DIR, EXPORTS_DIR, ensure_directories


def main() -> None:
    ensure_directories()

    scored_path = PROCESSED_DATA_DIR / "adams_parcels_scored.csv"
    output_path = EXPORTS_DIR / "adams_top_prospects.csv"

    scored = pd.read_csv(scored_path)
    review = create_prospect_review(scored, output_path, top_n=250)

    print(f"Generated {len(review)} top prospects")
    print(f"Saved to {output_path}")


if __name__ == "__main__":
    main()