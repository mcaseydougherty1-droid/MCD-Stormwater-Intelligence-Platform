import json
from pathlib import Path

import pandas as pd

from mcd.gis.arcgis import query_layer
from mcd.utils.paths import RAW_DATA_DIR, ensure_directories


BUTLER_PARCEL_LAYER_URL = (
    "https://geo.co.butler.pa.us/server/rest/services/PAT/ParcelAndBoundary/FeatureServer/0"
)


def download_adams_township_parcels(output_path: Path | None = None) -> pd.DataFrame:
    ensure_directories()

    where = "MunicipalityDescription LIKE '%ADAMS%'"

    parcels = query_layer(
        layer_url=BUTLER_PARCEL_LAYER_URL,
        where=where,
        out_fields="*",
        result_record_count=2000,
        max_records=50000,
    )

    if output_path is None:
        output_path = RAW_DATA_DIR / "adams_township_parcels.csv"

    output_path.parent.mkdir(parents=True, exist_ok=True)
    parcels.to_csv(output_path, index=False)

    json_path = output_path.with_suffix(".json")
    json_path.write_text(
        json.dumps(parcels.to_dict(orient="records"), indent=2),
        encoding="utf-8",
    )

    return parcels