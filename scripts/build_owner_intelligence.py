import pandas as pd

from mcd.owners.owner_profile import enrich_owner_profiles
from mcd.owners.owner_registry import build_owner_registry
from mcd.owners.owner_scoring import score_owner_intelligence
from mcd.utils.paths import EXPORTS_DIR, PROCESSED_DATA_DIR, ensure_directories


def main() -> None:
    ensure_directories()

    revenue_path = EXPORTS_DIR / "adams_revenue_forecast.csv"
    targets_path = EXPORTS_DIR / "adams_target_accounts.csv"
    bmp_path = PROCESSED_DATA_DIR / "adams_bmp_inventory.csv"
    hoa_path = PROCESSED_DATA_DIR / "adams_hoa_registry.csv"
    documents_path = PROCESSED_DATA_DIR / "adams_document_registry.csv"
    output_path = EXPORTS_DIR / "adams_owner_intelligence.csv"

    revenue = pd.read_csv(revenue_path)
    targets = pd.read_csv(targets_path)
    bmp = pd.read_csv(bmp_path)
    hoa = pd.read_csv(hoa_path)
    documents = pd.read_csv(documents_path)

    registry = build_owner_registry(
        revenue_forecast=revenue,
        target_accounts=targets,
        bmp_inventory=bmp,
        hoa_registry=hoa,
        document_registry=documents,
    )

    profiles = enrich_owner_profiles(registry)
    scored = score_owner_intelligence(profiles)

    scored.to_csv(output_path, index=False)

    print(f"Owner intelligence records: {len(scored)}")
    print(f"Priority owners: {int((scored['Priority_Tier'] == 'Priority').sum())}")
    print(f"High-priority owners: {int((scored['Priority_Tier'] == 'High').sum())}")
    print(f"Total expected value: ${scored['Expected_Value'].sum():,.0f}")
    print(f"Saved to {output_path}")


if __name__ == "__main__":
    main()