import pandas as pd

from mcd.inspections.inspection_forms import build_field_inspection_forms
from mcd.inspections.inspection_report import build_compliance_calendar
from mcd.inspections.inspection_scheduler import build_inspection_schedule
from mcd.inspections.maintenance_recommendations import build_maintenance_actions
from mcd.utils.paths import EXPORTS_DIR, PROCESSED_DATA_DIR, ensure_directories


def main() -> None:
    ensure_directories()

    bmp_inventory_path = PROCESSED_DATA_DIR / "adams_bmp_inventory.csv"

    inspection_schedule_path = EXPORTS_DIR / "adams_inspection_schedule.csv"
    field_inspections_path = EXPORTS_DIR / "adams_field_inspections.csv"
    maintenance_actions_path = EXPORTS_DIR / "adams_maintenance_actions.csv"
    compliance_calendar_path = EXPORTS_DIR / "adams_compliance_calendar.csv"

    bmp_inventory = pd.read_csv(bmp_inventory_path)

    schedule = build_inspection_schedule(bmp_inventory)
    field_forms = build_field_inspection_forms(schedule)
    maintenance_actions = build_maintenance_actions(schedule)
    compliance_calendar = build_compliance_calendar(schedule)

    schedule.to_csv(inspection_schedule_path, index=False)
    field_forms.to_csv(field_inspections_path, index=False)
    maintenance_actions.to_csv(maintenance_actions_path, index=False)
    compliance_calendar.to_csv(compliance_calendar_path, index=False)

    print(f"Inspection schedule records: {len(schedule)}")
    print(f"Field inspection forms: {len(field_forms)}")
    print(f"Maintenance actions: {len(maintenance_actions)}")
    print(f"Compliance calendar records: {len(compliance_calendar)}")
    print(f"Saved inspection schedule to {inspection_schedule_path}")
    print(f"Saved maintenance actions to {maintenance_actions_path}")


if __name__ == "__main__":
    main()
