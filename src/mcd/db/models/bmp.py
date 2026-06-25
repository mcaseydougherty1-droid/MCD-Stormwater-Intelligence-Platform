from sqlalchemy import Float, ForeignKey, Integer, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from mcd.db.schema import Base


class BMPAsset(Base):
    __tablename__ = "bmp_assets"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    property_id: Mapped[int] = mapped_column(ForeignKey("properties.id"), index=True)
    bmp_type: Mapped[str | None] = mapped_column(String, nullable=True)
    estimated_annual_cost: Mapped[float] = mapped_column(Float, default=0)
    inspection_status: Mapped[str | None] = mapped_column(String, nullable=True)
    next_inspection_date: Mapped[str | None] = mapped_column(String, nullable=True)

    property_record = relationship("Property", back_populates="bmp_assets")
    inspections = relationship("Inspection", back_populates="bmp_asset", cascade="all, delete-orphan")
