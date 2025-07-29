from sqlalchemy import Text, TIMESTAMP, func, ForeignKey
from sqlalchemy.orm import relationship, Mapped, mapped_column
from core.database import Base

class Post(Base):
    __tablename__ = "posts"

    id: Mapped[int] = mapped_column(primary_key=True)
    topic_id: Mapped[int] = mapped_column(ForeignKey("topics.id", ondelete="CASCADE"), nullable=False)
    author_id: Mapped[int] = mapped_column(ForeignKey("users.id", ondelete="SETNULL"), nullable=True)
    content: Mapped[str] = mapped_column(Text, nullable=False)
    created_at: Mapped[TIMESTAMP] = mapped_column(TIMESTAMP, server_default=func.now())
    updated_at: Mapped[TIMESTAMP] = mapped_column(TIMESTAMP, server_default=func.now(), onupdate=func.now())

    topic = relationship(
        "Topic",
        back_populates="posts"
    )
    author = relationship(
        "User",
        back_populates="posts"
    )