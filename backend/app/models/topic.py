from sqlalchemy import String, Text, TIMESTAMP, func, ForeignKey
from sqlalchemy.orm import relationship, Mapped, mapped_column
from core.database import Base

class Topic(Base):
    __tablename__ = "topics"

    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str] = mapped_column(String(255), nullable=False)
    content: Mapped[str] = mapped_column(Text, nullable=False)
    created_at: Mapped[TIMESTAMP] = mapped_column(TIMESTAMP, server_default=func.now())
    updated_at: Mapped[TIMESTAMP] = mapped_column(TIMESTAMP, server_default=func.now(), onupdate=func.now())
    creator_id: Mapped[int] = mapped_column(ForeignKey("users.id", ondelete="CASCADE"), nullable=False)

    creator = relationship(
        "User",
        back_populates="topics"
    )
    posts = relationship(
        "Post",
        back_populates="topic",
        cascade="all, delete"
    )