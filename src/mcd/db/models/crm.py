from sqlalchemy import Float, ForeignKey, Integer, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from mcd.db.schema import Base


class CRMOpportunity(Base):
    __tablename__ = "crm_opportunities"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    property_id: Mapped[int] = mapped_column(ForeignKey("properties.id"), index=True)
    sales_stage: Mapped[str | None] = mapped_column(String, nullable=True)
    opportunity_value: Mapped[float] = mapped_column(Float, default=0)
    probability_to_close: Mapped[float] = mapped_column(Float, default=0)
    weighted_value: Mapped[float] = mapped_column(Float, default=0)
    assigned_representative: Mapped[str | None] = mapped_column(String, nullable=True)

    property_record = relationship("Property", back_populates="crm_opportunities")
