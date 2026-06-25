import pandas as pd

from mcd.inspections.inspection_scheduler import build_inspection_schedule
from mcd.inspections.maintenance_recommendations import build_maintenance_actions


def test_inspection_schedule_and_maintenance_actions():
    bmp_inventory = pd.DataFrame(
        [
            {
                "BMP_ID": "BMP-001",
                "Owner": "Test Owner",
                "PIN": "123",
                "Property_Address": "100 Main St",
                "BMP_Type": "detention basin",
            }
        ]
    )

    schedule = build_inspection_schedule(bmp_inventory)
    actions = build_maintenance_actions(schedule)

    assert len(schedule) == 1
    assert schedule.loc[0, "Inspection_Frequency"] == "Annual"
    assert schedule.loc[0, "Inspection_Status"] == "Scheduled"

    assert len(actions) == 1
    assert "Mow basin" in actions.loc[0, "Recommended_Maintenance"]
    assert actions.loc[0, "Estimated_Action_Cost"] == 2750
