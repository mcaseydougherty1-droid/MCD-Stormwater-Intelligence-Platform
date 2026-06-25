import pandas as pd


def recommend_maintenance(bmp_type: str) -> str:
    text = str(bmp_type).lower()

    if "underground" in text:
        return "Inspect structures; vacuum clean chambers/inlets as needed; verify outlet function"

    if "detention" in text:
        return "Mow basin; inspect outlet structure; remove sediment/debris; check erosion"

    if "retention" in text:
        return "Manage shoreline vegetation; inspect embankment; remove debris; monitor sediment"

    if "swale" in text:
        return "Trim vegetation; remove debris; check flow path and erosion"

    if "rain garden" in text:
        return "Weed vegetation; inspect mulch/media; verify infiltration and overflow path"

    return "Perform visual inspection and determine maintenance needs"


def estimate_action_cost(bmp_type: str) -> float:
    text = str(bmp_type).lower()

    if "underground" in text:
        return 6000

    if "detention" in text or "retention" in text:
        return 2750

    if "swale" in text or "rain garden" in text:
        return 1250

    return 500


def build_maintenance_actions(schedule: pd.DataFrame) -> pd.DataFrame:
    df = schedule.copy()

    df["Recommended_Maintenance"] = df["BMP_Type"].apply(recommend_maintenance)
    df["Estimated_Action_Cost"] = df["BMP_Type"].apply(estimate_action_cost)
    df["Maintenance_Status"] = "Pending field verification"
    df["Maintenance_Priority"] = "Medium"

    return df[
        [
            "BMP_ID",
            "Owner",
            "PIN",
            "Property_Address",
            "BMP_Type",
            "Recommended_Maintenance",
            "Estimated_Action_Cost",
            "Maintenance_Status",
            "Maintenance_Priority",
        ]
    ]
