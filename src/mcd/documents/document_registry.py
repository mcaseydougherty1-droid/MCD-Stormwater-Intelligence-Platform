import pandas as pd


REGISTRY_COLUMNS = [
    "PIN",
    "Owner",
    "Property_Address",
    "Municipality",
    "Document_Type",
    "Document_Status",
    "Document_URL",
    "Recording_Number",
    "Recording_Date",
    "Source",
    "Verified",
    "Notes",
]


def build_empty_document_registry(search_targets: pd.DataFrame) -> pd.DataFrame:
    records = []

    base = search_targets[
        ["PIN", "Owner", "Property_Address", "Municipality"]
    ].drop_duplicates()

    for _, row in base.iterrows():
        records.append(
            {
                "PIN": row.get("PIN", ""),
                "Owner": row.get("Owner", ""),
                "Property_Address": row.get("Property_Address", ""),
                "Municipality": row.get("Municipality", ""),
                "Document_Type": "Unknown",
                "Document_Status": "Pending manual search",
                "Document_URL": "",
                "Recording_Number": "",
                "Recording_Date": "",
                "Source": "Butler County / Adams Township records",
                "Verified": False,
                "Notes": "",
            }
        )

    return pd.DataFrame(records, columns=REGISTRY_COLUMNS)