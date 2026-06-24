import pandas as pd

from mcd.documents.search_terms import OM_SEARCH_TERMS


def build_om_search_targets(opportunities: pd.DataFrame, top_n: int = 100) -> pd.DataFrame:
    df = opportunities.copy()
    df = df.head(top_n)

    rows = []

    for _, row in df.iterrows():
        owner = str(row.get("Owner", "")).strip()
        pin = str(row.get("PIN", "")).strip()
        address = str(row.get("Property_Address", "")).strip()
        municipality = str(row.get("Municipality", "")).strip()

        base_terms = [
            owner,
            pin,
            address,
            municipality,
            "Butler County PA",
        ]

        for term in OM_SEARCH_TERMS:
            query = " ".join([value for value in base_terms + [term] if value and value.lower() != "nan"])

            rows.append(
                {
                    "PIN": pin,
                    "Owner": owner,
                    "Property_Address": address,
                    "Municipality": municipality,
                    "Document_Search_Term": term,
                    "Search_Query": query,
                    "Document_Status": "Not searched",
                    "Document_Type": "Unknown",
                    "Document_URL": "",
                    "Notes": "",
                }
            )

    return pd.DataFrame(rows)