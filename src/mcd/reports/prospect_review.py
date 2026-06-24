from pathlib import Path

import pandas as pd


REVIEW_COLUMNS = [
    "Pipeline_Tier",
    "Priority_Score",
    "MCD_Target_Category",
    "Owner",
    "PIN",
    "Property_Address",
    "Municipality",
    "Acres",
    "Land_Use",
    "Likely_BMP_Types",
    "Estimated_Maintenance_Need",
    "Estimated_Annual_Revenue",
    "Sales_Stage",
    "Next_Action",
]


def create_prospect_review(
    scored_parcels: pd.DataFrame,
    output_path: Path,
    top_n: int = 250,
) -> pd.DataFrame:
    output_path.parent.mkdir(parents=True, exist_ok=True)

    review = scored_parcels.copy()
    review = review[review["Target_Flag"] == True]
    review = review.sort_values(
        ["Pipeline_Tier", "Priority_Score", "Estimated_Annual_Revenue"],
        ascending=[True, False, False],
    )

    available_columns = [column for column in REVIEW_COLUMNS if column in review.columns]
    review = review[available_columns].head(top_n)

    review.to_csv(output_path, index=False)

    return review