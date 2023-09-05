from sqlalchemy import select
from fastapi import APIRouter
from app.schema.cat import CatInfoResponse, CatInfoDataInput
from app.db.models.cat import Cat
from app.db import db_client

router = APIRouter()


@router.post("/catinfo", response_model=CatInfoResponse, name="cat:catinfo")
async def catinfo(data_input: CatInfoDataInput):
    cat = Cat(name=data_input.name, breed=data_input.breed,
              skin_color=data_input.skin_color, age=data_input.age, owner=data_input.owner
              )


