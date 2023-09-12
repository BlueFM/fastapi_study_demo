import asyncio

from sqlalchemy import select
from fastapi import APIRouter, HTTPException

from demo_1 import db_client
from demo_1.db.schema import CatInfoResponse, CatInfoDataInput
from demo_1.db.models import Cat

router = APIRouter()


async def ret(sql):
    session = db_client.Session
    async with session as s:
        async with s.begin():
            resp = await db_client.select(sql, s)
            if not resp:
                raise HTTPException(status_code=404, detail="Cat not found")
            l = resp.fetchall()
            if len(l) == 0:
                return HTTPException(status_code=404, detail="Cat not found")
            data_dict = {}
            for each in l:
                dic = {"name": each[0].name, "breed": each[0].breed, "skin color": each[0].skin_color,
                       "owner": each[0].owner}
                data_dict[f"{each[0].age}岁的{each[0].name}的信息:"] = dic
    return CatInfoResponse(code=200, data=data_dict)


@router.get("/catInfo/get", response_model=CatInfoResponse)
async def get_cat_info_name(name: str):
    sql = select(Cat).where(Cat.name == name)
    return await ret(sql)


@router.get("/catInfo/getAll", response_model=CatInfoResponse)
async def get_cat_info_all():
    sql = select(Cat).where(Cat.name != None)
    return await ret(sql)


@router.post("/catInfo", response_model=CatInfoResponse, name="post_cat_info")
async def post_cat_info(data: CatInfoDataInput):
    sql = select(Cat).where(Cat.name == data.name and Cat.age == data.age)
    session = db_client.Session
    async with session as s:
        async with s.begin():
            resp = await db_client.select(sql, s)
            l = resp.fetchall()
            if len(l) != 0:
                raise HTTPException(status_code=400, detail="Cat already registered")
    cat_dict = Cat.to_dict(
                               [data.name, data.breed, data.skin_color, data.owner],
                               ["name", "breed", "skin color", "owner"]
                           )
    print(cat_dict)
    await db_client.insert(Cat(name=data.name, breed=data.breed, skin_color=data.skin_color,
                               age=data.age, owner=data.owner))
    return CatInfoResponse(code=200, data=cat_dict)
