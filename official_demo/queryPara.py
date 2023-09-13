from typing import Union

from fastapi import FastAPI
from fastapi.responses import RedirectResponse

app = FastAPI()



@app.get("/")
async def root():
    """Redirect to docs"""
    return RedirectResponse(url="/docs/")
### Query Parameters

fake_items_db = [{"item_name": "Foo"}, {"item_name": "Bar"}, {"item_name": "Baz"}]


@app.get("/items/")
async def read_item(skip: int = 0, limit: int = 10):
    """example: 默认值"""
    return fake_items_db[skip: skip + limit]


@app.get("/items/{item_id}")
async def read_item_2(item_id: str, q: Union[str, None] = None):
    """example: 可选参数"""
    if q:
        return {"item_id": item_id, "q": q}
    return {"item_id": item_id}


@app.get("/items/3_{item_id}")
async def read_item_3(item_id: str, q: Union[str, None] = None, short: bool = False):
    """example: 可选参数和类型转换"""
    item = {"item_id": item_id}
    if q:
        item.update({"q": q})
    if not short:
        item.update(
            {"description": "This is an amazing item that has a long description"}
        )
    return item


@app.get("/users/{user_id}/items/{item_id}")
async def read_user_item(
        user_id: int, item_id: str, q: Union[str, None] = None, short: bool = False
):
    """example: 多路径参数"""
    item = {"item_id": item_id, "owner_id": user_id}
    if q:
        item.update({"q": q})
    if not short:
        item.update(
            {"description": "This is an amazing item that has a long description"}
        )
    return item


@app.get("/items/user{item_id}")
async def read_user_item_2(item_id: str, needy: str):
    """example: 必须参数"""
    item = {"item_id": item_id, "needy": needy}
    return item


@app.get("/items/syn{item_id}")
async def read_user_item(
        item_id: str, needy: str, skip: int = 0, limit: Union[int, None] = None
):
    """example: 查询参数综合"""
    item = {"item_id": item_id, "needy": needy, "skip": skip, "limit": limit}
    return item


"""
值得说明的是，可以在路径参数中使用枚举类
"""

if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app="queryPara:app", host="127.0.0.1", port=8080, reload=True)