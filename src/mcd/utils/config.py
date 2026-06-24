from pathlib import Path
from dotenv import load_dotenv
import os

ROOT = Path(__file__).resolve().parents[2]
load_dotenv(ROOT / ".env")

PARCEL_LAYER_URL = os.getenv("BUTLER_PARCEL_LAYER_URL", "https://geo.co.butler.pa.us/server/rest/services/PAT/ParcelAndBoundary/MapServer/0")
MUNICIPALITY = os.getenv("MUNICIPALITY", "Adams Twp")
OUTPUT_EXCEL = ROOT / os.getenv("OUTPUT_EXCEL", "output/MCD_Stormwater_Intelligence_Platform.xlsx")
MAX_RECORDS = int(os.getenv("MAX_RECORDS", "50000"))
INPUT_DIR = ROOT / "input"
OUTPUT_DIR = ROOT / "output"
PROPOSAL_DIR = ROOT / "proposals"
