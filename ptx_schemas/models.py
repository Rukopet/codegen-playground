from enum import Enum
from typing import Optional, List
from pydantic import BaseModel, Field

class UserRole(str, Enum):
    ADMIN = "admin"
    USER = "user"
    GUEST = "guest"

class UserBase(BaseModel):
    username: str = Field(..., min_length=3, max_length=50)
    email: str = Field(..., pattern=r"^[\w\.-]+@[\w\.-]+\.\w+$")
    role: UserRole = Field(default=UserRole.USER)

class UserCreate(UserBase):
    password: str = Field(..., min_length=8)

class UserResponse(UserBase):
    id: int
    is_active: bool = True

class ErrorResponse(BaseModel):
    code: str
    message: str
    details: Optional[dict] = None 