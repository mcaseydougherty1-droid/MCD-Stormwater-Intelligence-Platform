import pandas as pd


def build_field_inspection_forms(schedule: pd.DataFrame) -> pd.DataFrame:
    df = schedule.copy()

    df["Inspection_ID"] = df["BMP_ID"].apply(lambda value: f"INS-{value}")
    df["Inspection_Date"] = ""
    df["Inspector"] = ""
    df["Condition_Rating"] = "Not inspected"
    df["Vegetation_Status"] = ""
    df["Sediment_Status"] = ""
    df["Erosion_Status"] = ""
    df["Outlet_Condition"] = ""
    df["Photos_Taken"] = False
    df["Follow_Up_Required"] = False
    df["Inspection_Notes"] = ""

    return df[
        [
            "Inspection_ID",
            "BMP_ID",
            "Owner",
            "PIN",
            "Property_Address",
            "BMP_Type",
            "Inspection_Date",
            "Inspector",
            "Condition_Rating",
            "Vegetation_Status",
            "Sediment_Status",
            "Erosion_Status",
            "Outlet_Condition",
            "Photos_Taken",
            "Follow_Up_Required",
            "Inspection_Notes",
        ]
    ]
