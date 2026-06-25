import pandas as pd

from mcd.crm.activity import add_activity_fields
from mcd.crm.opportunity import build_opportunity_records


PIPELINE_COLUMNS = [
    "Opportunity_ID",
    "PIN",
    "Owner",
    "Property_Address",
    "Municipality",
    "Owner_Type",
    "BMP_Count",
    "BMP_Types",
    "Sales_Stage",
    "Opportunity_Value",
    "Probability_to_Close",
    "Weighted_Value",
    "Assigned_Representative",
    "Last_Contact_Date",
    "Next_Follow_Up_Date",
    "Expected_Close_Date",
    "Proposal_Status",
    "Inspection_Status",
    "Contact_Priority_Tier",
    "Outreach_Status",
    "Recommended_Action",
    "CRM_Notes",
]


def build_sales_pipeline(properties: pd.DataFrame) -> pd.DataFrame:
    opportunities = build_opportunity_records(properties)
    pipeline = add_activity_fields(opportunities)

    for column in PIPELINE_COLUMNS:
        if column not in pipeline.columns:
            pipeline[column] = ""

    return pipeline[PIPELINE_COLUMNS].sort_values(
        ["Weighted_Value", "Opportunity_Value"],
        ascending=[False, False],
    )
