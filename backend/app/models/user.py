from sqlalchemy import String, Text, TIMESTAMP, func
from sqlalchemy.orm import relationship, Mapped, mapped_column
from core.database import Base

class User(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(primary_key=True)
    username: Mapped[str] = mapped_column(String(32), unique=True, nullable=False)
    email: Mapped[str] = mapped_column(String(100), unique=True, nullable=True)
    hashed_password: Mapped[str] = mapped_column(Text, nullable=False)
    created_at: Mapped[TIMESTAMP] = mapped_column(TIMESTAMP, server_default=func.now())
    updated_at: Mapped[TIMESTAMP] = mapped_column(TIMESTAMP, server_default=func.now(), onupdate=func.now())

    roles = relationship(
        "UserRole",
        back_populates="users",
        cascade="all, delete"
    )
    posts = relationship(
        "Post",
        back_populates="author",
    )
    topics = relationship(
        "Topic",
        back_populates="creator",
    )