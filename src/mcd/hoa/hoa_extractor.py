import pandas as pd


HOA_TERMS = [
    "HOMEOWNER",
    "HOME OWNER",
    "HOA",
    "ASSOCIATION",
    "CONDOMINIUM",
    "CONDO",
    "COMMON",
    "OPEN SPACE",
]


def extract_hoa_candidates(parcels: pd.DataFrame) -> pd.DataFrame:
    df = parcels.copy()

    owner_text = df["Owner"].fillna("").str.upper()

    hoa_mask = owner_text.apply(
        lambda value: any(term in value for term in HOA_TERMS)
    )

    return df[hoa_mask].copy()