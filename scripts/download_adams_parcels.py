import json
from pathlib import Path

from src.gis.client import ArcGISClient
from src.gis.pagination import ArcGISPaginator


PARCEL_LAYER_URL = "https://geo.co.butler.pa.us/server/rest/services/PAT/ParcelAndBoundary/FeatureServer/0"

OUTPUT_DIR = Path("data/raw")
OUTPUT_FILE = OUTPUT_DIR / "adams_township_parcels.json"


def main():
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    client = ArcGISClient(PARCEL_LAYER_URL)
    paginator = ArcGISPaginator(client)

    features = paginator.fetch_all(
        layer_endpoint="",
        where="MUNI_NAME = 'ADAMS TWP'",
        out_fields="*",
        return_geometry=True,
        page_size=2000,
    )

    with OUTPUT_FILE.open("w", encoding="utf-8") as file:
        json.dump(features, file, indent=2)

    print(f"Downloaded {len(features)} Adams Township parcel records")
    print(f"Saved to {OUTPUT_FILE}")


if __name__ == "__main__":
    main()