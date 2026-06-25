import pandas as pd

from mcd.crm.pipeline import build_sales_pipeline


def test_sales_pipeline_calculates_weighted_value():
    properties = pd.DataFrame(
        [
            {
                "PIN": "123",
                "Owner": "Test Owner",
                "Property_Address": "100 Main St",
                "Municipality": "Adams Township",
                "Owner_Type": "HOA / Common Area",
                "BMP_Count": 1,
                "BMP_Types": "detention basin",
                "Estimated_Total_Annual_Revenue": 10000,
                "Contact_Priority_Tier": "Priority",
                "Outreach_Status": "Not contacted",
                "Recommended_Action": "Research",
                "Inspection_Status": "Scheduled",
            }
        ]
    )

    pipeline = build_sales_pipeline(properties)

    assert len(pipeline) == 1
    assert pipeline.loc[0, "Sales_Stage"] == "Researching"
    assert pipeline.loc[0, "Opportunity_Value"] == 10000
    assert pipeline.loc[0, "Weighted_Value"] == 1000
