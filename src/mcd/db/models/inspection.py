from sqlalchemy import ForeignKey, Integer, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from mcd.db.schema import Base


class Inspection(Base):
    __tablename__ = "inspections"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    bmp_asset_id: Mapped[int] = mapped_column(ForeignKey("bmp_assets.id"), index=True)
    inspection_status: Mapped[str | None] = mapped_column(String, nullable=True)
    next_inspection_date: Mapped[str | None] = mapped_column(String, nullable=True)
    assigned_to: Mapped[str | None] = mapped_column(String, nullable=True)
    notes: Mapped[str | None] = mapped_column(String, nullable=True)

    bmp_asset = relationship("BMPAsset", back_populates="inspections")
