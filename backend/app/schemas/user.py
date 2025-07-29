from pydantic import BaseModel, EmailStr
from typing import Optional

class UserBase(BaseModel):
    username: str
    email: Optional[EmailStr] = None
    is_active: bool = True
