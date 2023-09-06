from typing import Any, Dict, Optional
from pydantic import BaseModel


class PineFamilyDataInput(BaseModel):
    name: str = 'family'
    sex: str = 'secret'
    age: int = 18
    profession: str = 'fighter'
    hobby: str = 'party'
    motto: str = 'pine AI is the best company in the 710 !'


class PineFamilyResponse(BaseModel):
    code: int
    data: Dict[str, Any]
