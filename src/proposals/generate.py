from pathlib import Path
import pandas as pd

excel_path = Path("output/MCD_Stormwater_Intelligence_Platform.xlsx")
out_dir = Path("proposals")
out_dir.mkdir(exist_ok=True)

if not excel_path.exists():
    raise SystemExit("Run python run_pipeline.py first.")

pipeline = pd.read_excel(excel_path, sheet_name="Ranked Sales Pipeline")
for _, r in pipeline.head(25).iterrows():
    safe_pin = str(r.get("PIN", "parcel")).replace("/", "-").replace("\\", "-")
    body = f"""MCD Consulting LLC - Stormwater Maintenance Opportunity\n\nOwner: {r.get('Owner','')}\nProperty: {r.get('Property_Address','')}\nParcel: {r.get('PIN','')}\nCategory: {r.get('MCD_Target_Category','')}\nPriority Score: {r.get('Priority_Score','')}\nLikely BMPs: {r.get('Likely_BMP_Types','')}\nEstimated Annual Maintenance Need: {r.get('Estimated_Maintenance_Need','')}\nEstimated Annual Revenue: ${r.get('Estimated_Annual_Revenue',0):,.0f}\n\nRecommended next step:\nVerify the recorded O&M agreement, SWM plan, easements, BMP inventory, and responsible owner contact. Then schedule a field inspection and prepare a formal maintenance proposal.\n"""
    (out_dir / f"proposal_{safe_pin}.txt").write_text(body, encoding="utf-8")
print(f"Created proposal drafts in {out_dir.resolve()}")
