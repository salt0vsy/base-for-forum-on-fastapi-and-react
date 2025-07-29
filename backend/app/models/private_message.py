from sqlalchemy import Text, TIMESTAMP, func, ForeignKey
from sqlalchemy.orm import relationship, Mapped, mapped_column
from core.database import Base

class PrivateMessage(Base):
    __tablename__ = "private_messages"

    id: Mapped[int] = mapped_column(primary_key=True)
    sender_id: Mapped[int] = mapped_column(ForeignKey("users.id", ondelete="CASCADE"), nullable=False)
    receiver_id: Mapped[int] = mapped_column(ForeignKey("users.id", ondelete="CASCADE"), nullable=False)
    content: Mapped[str] = mapped_column(Text, nullable=False)
    sent_at: Mapped[TIMESTAMP] = mapped_column(TIMESTAMP, server_default=func.now())
    is_read: Mapped[bool] = mapped_column(default=False)

    sender = relationship(
        "User",
        foreign_keys=[sender_id],
        back_populates="sent_messages"
    )
    receiver = relationship(
        "User",
        foreign_keys=[receiver_id],
        back_populates="received_messages"
    )