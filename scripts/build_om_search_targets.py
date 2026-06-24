import pandas as pd

from mcd.documents.om_discovery import build_om_search_targets
from mcd.utils.paths import EXPORTS_DIR, ensure_directories


def main() -> None:
    ensure_directories()

    opportunities_path = EXPORTS_DIR / "adams_stormwater_opportunities.csv"
    output_path = EXPORTS_DIR / "adams_om_search_targets.csv"

    opportunities = pd.read_csv(opportunities_path)
    targets = build_om_search_targets(opportunities, top_n=100)

    targets.to_csv(output_path, index=False)

    print(f"Built {len(targets)} O&M document search targets")
    print(f"Saved to {output_path}")


if __name__ == "__main__":
    main()