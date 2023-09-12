from enum import Enum
from typing import Union

from fastapi import FastAPI
from fastapi.responses import RedirectResponse

app = FastAPI()


### Start

@app.get("/")
async def root():
    """Redirect to docs"""
    return RedirectResponse(url="/docs/")


### Road Parameters

@app.get("/users/me")
async def read_user_me():
    """example: get current user"""
    return {"user_id": "the current user"}


@app.get("/users/{user_id}")
async def read_user(user_id: str):
    """example: get user by id"""
    return {"user_id": user_id}


class ModelName(str, Enum):
    """example: enum machine learning model name"""
    alexnet = "alexnet"
    resnet = "resnet"
    lenet = "lenet"


@app.get("/models/{model_name}")
async def get_model(model_name: ModelName):
    """example: get machine learning model by name"""
    if model_name is ModelName.alexnet:
        return {"model_name": model_name, "message": "Deep Learning FTW!"}

    if model_name.value == "lenet value":
        return {"model_name": model_name, "message": "LeCNN all the images"}

    return {"model_name": model_name, "message": "Have some residuals"}


@app.get("/files/{file_path:path}")
async def read_file(file_path: str):
    """example: path para"""
    return {"file_path": file_path}

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

### Request Body

if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app="official_demo_start:app", host="127.0.0.1", port=8080, reload=True)
