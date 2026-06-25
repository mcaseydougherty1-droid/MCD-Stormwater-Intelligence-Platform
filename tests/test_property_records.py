import pandas as pd

from mcd.property.property_record import finalize_property_records
from mcd.property.property_schema import UNIFIED_PROPERTY_COLUMNS


def test_finalize_property_records_includes_required_columns():
    source = pd.DataFrame(
        [
            {
                "PIN": "123",
                "Owner": "Test Owner",
                "Property_Address": "100 Main St",
            }
        ]
    )

    result = finalize_property_records(source)

    assert list(result.columns) == UNIFIED_PROPERTY_COLUMNS
    assert result.loc[0, "PIN"] == "123"
    assert result.loc[0, "Owner"] == "Test Owner"
