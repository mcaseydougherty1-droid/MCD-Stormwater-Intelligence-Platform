import sqlite3
from pathlib import Path

from mcd.utils.paths import DATABASE_PATH, ensure_directories


def get_connection(database_path: Path = DATABASE_PATH) -> sqlite3.Connection:
    ensure_directories()

    connection = sqlite3.connect(database_path)
    connection.row_factory = sqlite3.Row

    return connection