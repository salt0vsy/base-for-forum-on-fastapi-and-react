from sqlalchemy import TIMESTAMP, func, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column
from core.database import Base

class Friends(Base):
    __tablename__ = "friends"

    user_id: Mapped[int] = mapped_column(ForeignKey("users.id", ondelete="CASCADE"), primary_key=True)
    friend_id: Mapped[int] = mapped_column(ForeignKey("users.id", ondelete="CASCADE"), primary_key=True)
    created_at: Mapped[TIMESTAMP] = mapped_column(TIMESTAMP, server_default=func.now())
    status: Mapped[bool] = mapped_column(default=False)