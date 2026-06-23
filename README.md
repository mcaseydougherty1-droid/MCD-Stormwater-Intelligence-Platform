# MCD Stormwater Intelligence Platform v1.1

## Setup in VS Code / PowerShell

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
pip install -r requirements.txt
copy .env.example .env
python run_pipeline.py
streamlit run app.py
```

## Outputs

- `output/MCD_Stormwater_Intelligence_Platform.xlsx`
- `output/raw_parcels.csv`
- `proposals/` generated proposal drafts

## Operating sequence

1. Run `python run_pipeline.py`
2. Open the Excel workbook in `output/`
3. Add O&M/SWM links to `input/document_crosswalk.csv`
4. Rerun `python run_pipeline.py`
5. Run `streamlit run app.py` for dashboard/map
6. Run `python generate_proposals.py` for proposal drafts
