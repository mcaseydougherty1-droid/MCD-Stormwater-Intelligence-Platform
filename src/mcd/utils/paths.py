from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[3]

DATA_DIR = PROJECT_ROOT / "data"
RAW_DATA_DIR = DATA_DIR / "raw"
PROCESSED_DATA_DIR = DATA_DIR / "processed"
EXPORTS_DIR = DATA_DIR / "exports"

INPUT_DIR = PROJECT_ROOT / "input"
OUTPUT_DIR = PROJECT_ROOT / "output"
LOGS_DIR = PROJECT_ROOT / "logs"
PROPOSALS_DIR = PROJECT_ROOT / "proposals"

DATABASE_DIR = PROJECT_ROOT / "database"
DATABASE_PATH = DATABASE_DIR / "stormwater.db"


def ensure_directories() -> None:
    for path in [
        DATA_DIR,
        RAW_DATA_DIR,
        PROCESSED_DATA_DIR,
        EXPORTS_DIR,
        INPUT_DIR,
        OUTPUT_DIR,
        LOGS_DIR,
        PROPOSALS_DIR,
        DATABASE_DIR,
    ]:
        path.mkdir(parents=True, exist_ok=True)