from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker

from mcd.api.config import settings

engine = create_engine(settings.database_url, future=True)

SessionLocal = sessionmaker(
    bind=engine,
    autoflush=False,
    autocommit=False,
)


def test_connection() -> str:
    with engine.connect() as connection:
        result = connection.execute(text("SELECT version();"))
        return result.scalar_one()
