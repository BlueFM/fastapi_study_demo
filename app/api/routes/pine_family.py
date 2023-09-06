from sqlalchemy import select
from fastapi import APIRouter
from app.db.models.pine_family import PineFamily
from app.schema.pine_family import PineFamilyResponse, PineFamilyDataInput
from app import db_client

router = APIRouter()


@router.post("/pinefamilyinfo", response_model=PineFamilyResponse, name="pine_family:pinefamilyinfo")
async def pinefamilyinfo(data_input: PineFamilyDataInput):
    member = PineFamily(name=data_input.name, age=data_input.age, sex=data_input.sex, profession=data_input.profession,
                        hobby=data_input.hobby,
                        motto=data_input.motto)
    await db_client.insert(member)
    sql = select(PineFamily.name, PineFamily.sex, PineFamily.age, PineFamily.profession, PineFamily.hobby,
                 PineFamily.motto).where(PineFamily.name == data_input.name)
    resp = await db_client.select(sql)
    row = resp.fetchone()
    member_dict = {
        "name": row[0],
        "sex": row[1],
        "age": row[2],
        "profession": row[3],
        "hobby": row[4],
        "motto": row[5]
    }
    data_info = {"code": 200, "data": member_dict}
    return PineFamilyResponse.parse_obj(data_info)


@router.get("/pinefamilyinfo/getname", response_model=PineFamilyResponse)
async def get_info(input_name: str):
    sql = select(PineFamily.name, PineFamily.sex, PineFamily.profession, PineFamily.hobby, PineFamily.motto).where(
        PineFamily.name == input_name)
    resp = await db_client.select(sql)
    row = resp.fetchone()
    member_dict = {
        "name": row[0],
        "sex": row[1],
        "age": row[2],
        "profession": row[3],
        "hobby": row[4],
        "motto": row[5]
    }
    data_info = {"code": 200, "data": member_dict}
    return PineFamilyResponse.parse_obj(data_info)