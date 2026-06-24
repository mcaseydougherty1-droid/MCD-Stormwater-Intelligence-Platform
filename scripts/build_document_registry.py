import pandas as pd

from mcd.documents.document_matcher import summarize_document_registry
from mcd.documents.document_registry import build_empty_document_registry
from mcd.utils.paths import EXPORTS_DIR, PROCESSED_DATA_DIR, ensure_directories


def main() -> None:
    ensure_directories()

    search_targets_path = EXPORTS_DIR / "adams_om_search_targets.csv"
    registry_path = PROCESSED_DATA_DIR / "adams_document_registry.csv"
    review_path = EXPORTS_DIR / "adams_document_review_queue.csv"

    search_targets = pd.read_csv(search_targets_path)

    registry = build_empty_document_registry(search_targets)
    review_queue = summarize_document_registry(registry)

    registry.to_csv(registry_path, index=False)
    review_queue.to_csv(review_path, index=False)

    print(f"Document registry records: {len(registry)}")
    print(f"Saved registry to {registry_path}")
    print(f"Saved review queue to {review_path}")


if __name__ == "__main__":
    main()