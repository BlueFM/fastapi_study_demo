from typing import Any

from fastapi import FastAPI
from pydantic import BaseModel, EmailStr
from starlette.responses import RedirectResponse

app = FastAPI()


class Item(BaseModel):
    """example: response model"""
    name: str
    description: str | None = None
    price: float
    tax: float | None = None
    tags: list[str] = []


# FastAPI 将使用此 response_model 来：
# 将输出数据转换为其声明的类型。
# 校验数据。
# 在 OpenAPI 的路径操作中为响应添加一个 JSON Schema。
# 并在自动生成文档系统中使用。
# 但最重要的是：
#     会将输出数据限制在该模型定义内。

@app.post("/items/", response_model=Item)
async def create_item(item: Item) -> Any:
    """example: response model"""
    return item


@app.get("/items/", response_model=list[Item])
async def read_items() -> Any:
    """ example: response model """
    return [
        {"name": "Portal Gun", "price": 42.0},
        {"name": "Plumbus", "price": 32.0},
    ]


@app.get("/")
async def root():
    """Redirect to docs"""
    return RedirectResponse(url="/docs/")


class UserIn(BaseModel):
    """example: response model"""
    username: str
    password: str
    email: EmailStr
    full_name: str | None = None


# Don't do this in production!
# 永远不要存储用户的明文密码，也不要在响应中发送密码。
@app.post("/user/")
async def create_user(user: UserIn) -> UserIn:
    """example: response model"""
    return user


class UserOut(BaseModel):
    """没有明文密码的输出模型"""
    username: str
    email: EmailStr
    full_name: str | None = None


@app.post("/user2/", response_model=UserOut)
async def create_user2(user: UserIn) -> Any:
    """FastAPI 将会负责过滤掉未在输出模型中声明的所有数据"""
    return user


"""当你在 NoSQL 数据库中保存了具有许多可选属性的模型，但你又不想发送充满默认值的很长的 JSON 响应。

使用 response_model_exclude_unset 参数"""
class Item2(BaseModel):
    name: str
    description: str | None = None
    price: float
    tax: float = 10.5
    tags: list[str] = []


items = {
    "foo": {"name": "Foo", "price": 50.2},
    "bar": {"name": "Bar", "description": "The bartenders", "price": 62, "tax": 20.2},
    "baz": {"name": "Baz", "description": None, "price": 50.2, "tax": 10.5, "tags": []},
}


@app.get("/items2/{item_id}", response_model=Item2, response_model_exclude_unset=True)
async def read_item(item_id: str):
    return items[item_id]
"""
你还可以使用路径操作装饰器的 response_model_include 和 response_model_exclude 参数。

它们接收一个由属性名称 str 组成的 set 来包含（忽略其他的）或者排除（包含其他的）这些属性。

如果你只有一个 Pydantic 模型，并且想要从输出中移除一些数据，则可以使用这种快捷方法
"""

if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app="response_model:app", host="127.0.0.1", port=8080, reload=True)
