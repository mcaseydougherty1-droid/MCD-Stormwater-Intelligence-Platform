from sqlalchemy import ForeignKey, Integer, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from mcd.db.schema import Base


class Owner(Base):
    __tablename__ = "owners"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    property_id: Mapped[int] = mapped_column(ForeignKey("properties.id"), index=True)
    owner_name: Mapped[str | None] = mapped_column(String, nullable=True)
    owner_type: Mapped[str | None] = mapped_column(String, nullable=True)

    property_record = relationship("Property", back_populates="owners")
