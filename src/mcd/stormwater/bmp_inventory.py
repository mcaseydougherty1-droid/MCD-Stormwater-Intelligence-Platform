import pandas as pd


def infer_bmp_type(row: pd.Series) -> str:
    category = str(row.get("MCD_Target_Category", ""))
    likely_types = str(row.get("Likely_BMP_Types", ""))

    if category == "HOA/Common Area":
        return "detention basin / retention pond / swale"

    if category == "Commercial":
        return "underground chambers / detention basin / inlet-outlet structures"

    if category == "Institutional":
        return "detention basin / rain garden / swale"

    if likely_types and likely_types.lower() != "nan":
        return likely_types

    return "unknown"


def estimate_maintenance_frequency(row: pd.Series) -> str:
    category = str(row.get("MCD_Target_Category", ""))

    if category == "HOA/Common Area":
        return "Monthly during growing season; annual inspection"

    if category == "Commercial":
        return "Quarterly inspection; seasonal vegetation maintenance"

    if category == "Institutional":
        return "Semiannual inspection; seasonal maintenance"

    return "As-needed"


def estimate_annual_cost(row: pd.Series) -> float:
    category = str(row.get("MCD_Target_Category", ""))
    acres = float(row.get("Acres", 0) or 0)

    if category == "HOA/Common Area":
        return 3500 + min(acres, 20) * 150

    if category == "Commercial":
        return 2800 + min(acres, 20) * 125

    if category == "Institutional":
        return 2200 + min(acres, 20) * 100

    return 0


def build_bmp_inventory(opportunities: pd.DataFrame) -> pd.DataFrame:
    df = opportunities.copy()
    df = df[df["Likely_BMP_Present"] == True].copy()

    records = []

    for index, row in df.iterrows():
        bmp_id = f"BMP-{index + 1:05d}"

        records.append(
            {
                "BMP_ID": bmp_id,
                "Owner": row.get("Owner", ""),
                "PIN": row.get("PIN", ""),
                "Property_Address": row.get("Property_Address", ""),
                "Municipality": row.get("Municipality", ""),
                "BMP_Type": infer_bmp_type(row),
                "Source": "Inferred from parcel ownership, land use, and stormwater opportunity score",
                "Confidence_Score": row.get("MCD_Opportunity_Score", 0),
                "Inspection_Required": True,
                "Maintenance_Frequency": estimate_maintenance_frequency(row),
                "Estimated_Annual_Cost": estimate_annual_cost(row),
                "Next_Action": "Verify BMP location using aerial imagery, SWM plan, or O&M agreement",
            }
        )

    return pd.DataFrame(records)