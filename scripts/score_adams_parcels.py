import pandas as pd

from mcd.intelligence.parcel_normalizer import normalize_columns
from mcd.intelligence.parcel_classifier import classify_parcels
from mcd.intelligence.prospect_scoring import score_pipeline
from mcd.utils.paths import RAW_DATA_DIR, PROCESSED_DATA_DIR, ensure_directories


def main() -> None:
    ensure_directories()

    raw_path = RAW_DATA_DIR / "adams_township_parcels.csv"
    normalized_path = PROCESSED_DATA_DIR / "adams_parcels_normalized.csv"
    scored_path = PROCESSED_DATA_DIR / "adams_parcels_scored.csv"

    raw = pd.read_csv(raw_path)

    normalized = normalize_columns(raw)
    classified = classify_parcels(normalized)
    scored = score_pipeline(classified)

    normalized.to_csv(normalized_path, index=False)
    scored.to_csv(scored_path, index=False)

    print(f"Raw parcels: {len(raw)}")
    print(f"Scored parcels: {len(scored)}")
    print(f"Targets: {int(scored['Target_Flag'].sum())}")
    print(f"A-tier prospects: {int((scored['Pipeline_Tier'].astype(str) == 'A').sum())}")
    print(f"Estimated annual pipeline: ${scored['Estimated_Annual_Revenue'].sum():,.0f}")
    print(f"Saved normalized parcels to {normalized_path}")
    print(f"Saved scored parcels to {scored_path}")


if __name__ == "__main__":
    main()