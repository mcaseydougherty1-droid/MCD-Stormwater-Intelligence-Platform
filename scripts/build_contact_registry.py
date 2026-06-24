import pandas as pd

from mcd.contacts.contact_registry import build_contact_registry
from mcd.contacts.contact_scoring import score_contact_priority
from mcd.utils.paths import EXPORTS_DIR, ensure_directories


def main() -> None:
    ensure_directories()

    owner_intelligence_path = EXPORTS_DIR / "adams_owner_intelligence.csv"
    output_path = EXPORTS_DIR / "adams_contact_registry.csv"

    owner_intelligence = pd.read_csv(owner_intelligence_path)

    registry = build_contact_registry(owner_intelligence)
    scored = score_contact_priority(registry)

    scored.to_csv(output_path, index=False)

    print(f"Contact registry records: {len(scored)}")
    print(f"Priority contacts: {int((scored['Contact_Priority_Tier'].astype(str) == 'Priority').sum())}")
    print(f"High-priority contacts: {int((scored['Contact_Priority_Tier'].astype(str) == 'High').sum())}")
    print(f"Contacts needing HOA lookup: {int((scored['HOA_Contact_Status'] == 'Needs HOA board or management company lookup').sum())}")
    print(f"Saved to {output_path}")


if __name__ == "__main__":
    main()