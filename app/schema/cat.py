from typing import Any, Dict, Optional
from pydantic import BaseModel


class CatInfoDataInput(BaseModel):
    permalink: str
    name: str = 'nico'
    breed: str = 'unknown'
    skin_color: str = 'unknown'
    age: Optional[int] = None
    owner: str = 'itself'


class CatInfoResponse(BaseModel):
    code: int
    data: Dict[str, Any]