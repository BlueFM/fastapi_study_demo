from sqlalchemy import select
from fastapi import APIRouter
from app.db.models.cat import Cat
from app.schema.cat import CatInfoResponse, CatInfoDataInput
from app import db_client

router = APIRouter()


@router.post("/catinfo", response_model=CatInfoResponse, name="cat:catinfo")
async def catinfo(data_input: CatInfoDataInput):
    cat = Cat(name=data_input.name, breed=data_input.breed,
              skin_color=data_input.skin_color, age=data_input.age, owner=data_input.owner
              )
    await db_client.insert(cat)
    sql = select(Cat.name, Cat.breed, Cat.skin_color, Cat.owner).where(Cat.name == data_input.name,
                                                                       Cat.breed == data_input.breed)
    resp = await db_client.select(sql)
    row = resp.fetchone()
    cat_dict = {
        "name": row[0],
        "breed": row[1],
        "skin_color": row[2],
        "owner": row[3]
    }
    data_info = {"code": 200, "data": cat_dict}
    return CatInfoResponse.parse_obj(data_info)


@router.get("/catinfo/getname", response_model=CatInfoResponse)
async def get_name(input_name: str):
    sql = select(Cat.name, Cat.breed, Cat.skin_color, Cat.owner).where(Cat.name == input_name)
    resp = await db_client.select(sql)
    row = resp.fetchone()
    cat_dict = {
        "name": row[0],
        "breed": row[1],
        "skin_color": row[2],
        "owner": row[3]
    }
    data_info = {"code": 200, "data": cat_dict}
    return CatInfoResponse.parse_obj(data_info)
