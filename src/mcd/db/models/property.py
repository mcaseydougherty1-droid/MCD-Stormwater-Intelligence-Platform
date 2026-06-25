from sqlalchemy import Boolean, Float, Integer, String
from sqlalchemy.orm import Mapped, mapped_column

from mcd.db.schema import Base


class Property(Base):
    __tablename__ = "properties"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    pin: Mapped[str] = mapped_column(String, unique=True, index=True)
    owner: Mapped[str | None] = mapped_column(String, nullable=True)
    property_address: Mapped[str | None] = mapped_column(String, nullable=True)
    municipality: Mapped[str | None] = mapped_column(String, nullable=True)
    latitude: Mapped[float | None] = mapped_column(Float, nullable=True)
    longitude: Mapped[float | None] = mapped_column(Float, nullable=True)
    bmp_count: Mapped[int] = mapped_column(Integer, default=0)
    estimated_total_annual_revenue: Mapped[float] = mapped_column(Float, default=0)
    expected_value: Mapped[float] = mapped_column(Float, default=0)
    hoa_flag: Mapped[bool] = mapped_column(Boolean, default=False)
    owner_type: Mapped[str | None] = mapped_column(String, nullable=True)
