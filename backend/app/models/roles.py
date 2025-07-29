from sqlalchemy import Integer, String, Text, ForeignKey
from sqlalchemy.orm import relationship, Mapped, mapped_column
from core.database import Base

class Role(Base):
    __tablename__ = "roles"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String(32), unique=True, nullable=False)
    description: Mapped[str] = mapped_column(Text, nullable=True)

    permissions = relationship(
        "RolePermission",
        back_populates="role",
    )

class Permission(Base):
    __tablename__ = "permissions"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String(32), unique=True, nullable=False)
    description: Mapped[str] = mapped_column(Text, nullable=True)

    roles = relationship(
        "RolePermission",
        back_populates="permission",
    )

class RolePermission(Base):
    __tablename__ = "role_permissions"
    
    role_id: Mapped[int] = mapped_column(ForeignKey("roles.id", ondelete="CASCADE"), primary_key=True)
    permission_id: Mapped[int] = mapped_column(ForeignKey("permissions.id", ondelete="CASCADE"), primary_key=True)

    role = relationship(
        "Role",
        back_populates="permissions"
    )
    permission = relationship(
        "Permission",
        back_populates="roles"
    )
    
class UserRole(Base):
    __tablename__ = "user_roles"
    
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id", ondelete="CASCADE"), primary_key=True)
    role_id: Mapped[int] = mapped_column(ForeignKey("roles.id", ondelete="CASCADE"), primary_key=True)

    user = relationship(
        "User",
        back_populates="roles"
    )
    role = relationship(
        "Role"
    )