from typing import Any, Dict, Optional
from pydantic import BaseModel


class User(BaseModel):
    username: str
    email: str


class UserInDB(User):
    hashed_password: str


class UserCreate(User):
    password: str


class CatInfoDataInput(BaseModel):
    title: str
    description: str
    img_url: str
    location_lat: float
    location_lng: float


class CatInfoResponse(BaseModel):
    data: Dict[str, Any]


class CommentDataInput(BaseModel):
    content: str

