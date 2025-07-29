from sqlalchemy import String, TIMESTAMP, func, ForeignKey, Enum
from sqlalchemy.orm import relationship, Mapped, mapped_column
from core.database import Base
import enum

class MediaType(enum.Enum):
    IMAGE = "image"
    VIDEO = "video"
    AUDIO = "audio"
    DOCUMENT = "document"

class MediaFile(Base):
    __tablename__ = "media_files"

    id: Mapped[int] = mapped_column(primary_key=True)
    file_path: Mapped[str] = mapped_column(String(255), nullable=False)
    file_type: Mapped[MediaType] = mapped_column(Enum(MediaType), nullable=False)

    post_id: Mapped[int | None] = mapped_column(ForeignKey("posts.id", ondelete="CASCADE"), nullable=True)
    message_id: Mapped[int | None] = mapped_column(ForeignKey("private_messages.id", ondelete="CASCADE"), nullable=True)
    uploaded_by_id: Mapped[int | None] = mapped_column(ForeignKey("users.id", ondelete="SETNULL"), nullable=True)
    uploaded_at: Mapped[TIMESTAMP] = mapped_column(TIMESTAMP, server_default=func.now())

    post = relationship(
        "Post",
        back_populates="media_files"
    )
    message = relationship(
        "PrivateMessage",
        back_populates="media_files"
    )
    uploaded_by = relationship(
        "User",
        back_populates="uploaded_media_files"
    )
    