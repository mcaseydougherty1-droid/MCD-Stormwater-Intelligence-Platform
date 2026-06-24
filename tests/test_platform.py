from mcd.database.connection import get_connection
from mcd.utils.paths import PROJECT_ROOT


def test_project_root_exists():
    assert PROJECT_ROOT.exists()


def test_database_connection_opens():
    connection = get_connection()
    try:
        assert connection is not None
    finally:
        connection.close()