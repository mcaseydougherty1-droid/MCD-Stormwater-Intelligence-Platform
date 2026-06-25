import pandas as pd

from mcd.property.property_schema import UNIFIED_PROPERTY_COLUMNS


def finalize_property_records(records: pd.DataFrame) -> pd.DataFrame:
    df = records.copy()

    for column in UNIFIED_PROPERTY_COLUMNS:
        if column not in df.columns:
            df[column] = ""

    return df[UNIFIED_PROPERTY_COLUMNS].copy()
