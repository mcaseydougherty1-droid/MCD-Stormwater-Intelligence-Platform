import pandas as pd

from mcd.proposals.proposal_builder import build_proposals
from mcd.utils.paths import EXPORTS_DIR, ensure_directories


def main() -> None:
    ensure_directories()

    target_accounts_path = EXPORTS_DIR / "adams_contact_registry.csv"
    output_dir = EXPORTS_DIR / "proposals"

    target_accounts = pd.read_csv(target_accounts_path)
    proposals = build_proposals(target_accounts, output_dir, top_n=10)

    print(f"Generated proposals: {len(proposals)}")
    print(f"Saved to {output_dir}")


if __name__ == "__main__":
    main()