from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker

DATABASE_URL = "postgresql+psycopg://postgres:McD155217@localhost:5432/mcd_stormwater"

engine = create_engine(DATABASE_URL, future=True)

SessionLocal = sessionmaker(
    bind=engine,
    autoflush=False,
    autocommit=False,
)


def test_connection() -> str:
    with engine.connect() as connection:
        result = connection.execute(text("SELECT version();"))
        return result.scalar_one()
