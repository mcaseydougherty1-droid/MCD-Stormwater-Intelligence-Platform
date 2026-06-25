import math

import pandas as pd

from mcd.db.database import SessionLocal
from mcd.db.repositories.property_repository import upsert_property
from mcd.utils.paths import PROCESSED_DATA_DIR


def clean_value(value):
    if value is None:
        return None

    if isinstance(value, float) and math.isnan(value):
        return None

    if pd.isna(value):
        return None

    return value


def clean_float(value) -> float:
    value = clean_value(value)

    if value is None or value == "":
        return 0.0

    return float(value)


def clean_int(value) -> int:
    value = clean_value(value)

    if value is None or value == "":
        return 0

    return int(float(value))


def clean_bool(value) -> bool:
    value = clean_value(value)

    if value is None or value == "":
        return False

    if isinstance(value, bool):
        return value

    return str(value).strip().lower() in {"true", "1", "yes", "y"}


def main() -> None:
    input_path = PROCESSED_DATA_DIR / "adams_unified_property_records.csv"

    records = pd.read_csv(input_path)

    def main() -> None:
        input_path = PROCESSED_DATA_DIR / "adams_unified_property_records.csv"

    # Read the CSV once so we know how many total rows it contains
    source_records = pd.read_csv(input_path)

    print(f"Source rows: {len(source_records)}")

    # Keep only one record per unique parcel (PIN)
    records = (
        source_records
        .sort_values("PIN")
        .drop_duplicates(subset="PIN", keep="first")
    )

    print(f"Unique properties: {len(records)}")

    with SessionLocal() as session:
        for _, row in records.iterrows():
            upsert_property(
                session,
                pin=str(row["PIN"]),
                owner=clean_value(row.get("Owner")),
                property_address=clean_value(row.get("Property_Address")),
                municipality=clean_value(row.get("Municipality")),
                latitude=clean_value(row.get("Latitude")),
                longitude=clean_value(row.get("Longitude")),
                bmp_count=clean_int(row.get("BMP_Count")),
                estimated_total_annual_revenue=clean_float(
                    row.get("Estimated_Total_Annual_Revenue")
                ),
                expected_value=clean_float(row.get("Expected_Value")),
                hoa_flag=clean_bool(row.get("HOA_Flag")),
                owner_type=clean_value(row.get("Owner_Type")),
            )

        session.commit()

    print(f"Loaded property records into database: {len(records)}")

    with SessionLocal() as session:
        for _, row in records.iterrows():
            upsert_property(
                session,
                pin=str(row["PIN"]),
                owner=clean_value(row.get("Owner")),
                property_address=clean_value(row.get("Property_Address")),
                municipality=clean_value(row.get("Municipality")),
                latitude=clean_value(row.get("Latitude")),
                longitude=clean_value(row.get("Longitude")),
                bmp_count=clean_int(row.get("BMP_Count")),
                estimated_total_annual_revenue=clean_float(
                    row.get("Estimated_Total_Annual_Revenue")
                ),
                expected_value=clean_float(row.get("Expected_Value")),
                hoa_flag=clean_bool(row.get("HOA_Flag")),
                owner_type=clean_value(row.get("Owner_Type")),
            )

        session.commit()

    print(f"Loaded property records into database: {len(records)}")


if __name__ == "__main__":
    main()
