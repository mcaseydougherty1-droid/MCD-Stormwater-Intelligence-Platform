from sqlalchemy import Float, ForeignKey, Integer, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from mcd.db.schema import Base


class Proposal(Base):
    __tablename__ = "proposals"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    property_id: Mapped[int] = mapped_column(ForeignKey("properties.id"), index=True)
    proposal_status: Mapped[str | None] = mapped_column(String, nullable=True)
    proposal_amount: Mapped[float] = mapped_column(Float, default=0)
    proposal_path: Mapped[str | None] = mapped_column(String, nullable=True)

    property_record = relationship("Property", back_populates="proposals")
