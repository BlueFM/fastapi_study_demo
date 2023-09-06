from sqlalchemy import select
from fastapi import APIRouter, Response, status
from app.db.models.pine_family import PineFamily
from app.schema.pine_family import PineFamilyResponse, PineFamilyDataInput
from app import db_client

router = APIRouter()


async def ret(sql):
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


@router.post("/pinefamilyinfo", response_model=PineFamilyResponse, name="pine_family:pinefamilyinfo")
async def pinefamilyinfo(data_input: PineFamilyDataInput, response: Response):
    member = PineFamily(name=data_input.name, age=data_input.age, sex=data_input.sex, profession=data_input.profession,
                        hobby=data_input.hobby,
                        motto=data_input.motto)
    # 插入之前先校验数据库中是否已经存在该成员
    sql = select(PineFamily.name).where(PineFamily.name == member.name)
    exist = await db_client.select(sql)
    res = exist.fetchone()
    if res:
        response.status_code = status.HTTP_400_BAD_REQUEST
        return {"code": 400, "data": {"error": "have same information !"}}
    await db_client.insert(member)
    sql = select(PineFamily.name, PineFamily.sex, PineFamily.age, PineFamily.profession, PineFamily.hobby,
                 PineFamily.motto).where(PineFamily.name == data_input.name)
    return await ret(sql)


@router.get("/pinefamilyinfo/getname", response_model=PineFamilyResponse)
async def get_info(input_name: str):
    sql = select(PineFamily.name, PineFamily.sex, PineFamily.profession, PineFamily.hobby, PineFamily.motto).where(
        PineFamily.name == input_name)
    return await ret(sql)
