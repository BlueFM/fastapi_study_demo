from fastapi import FastAPI, status
from fastapi.responses import RedirectResponse
from pydantic import BaseModel

app = FastAPI()


### Start

@app.get("/")
async def root():
    """Redirect to docs"""
    return RedirectResponse(url="/docs/")


class Item(BaseModel):
    name: str
    description: str | None = None
    price: float
    tax: float | None = None
    tags: set[str] = set()


@app.post(
    "/items/",
    response_model=Item,
    tags=["items"],
    status_code=status.HTTP_201_CREATED,
    summary="Create an item",
    description=""
                "Create an item with all the information, name, "
                "description, price, tax and a set of unique tags",

)
# 路径装饰器还支持 summary 和 description 这两个参数
# 状态码在响应中使用，并会被添加到 OpenAPI 概图。
async def create_item(item: Item):
    return item


# tags 参数的值是由 str 组成的 list （一般只有一个 str ），tags 用于为路径操作添加标签：


@app.get("/items/", tags=["items"])
async def read_items():
    return [{"name": "Foo", "price": 42}]


# 描述内容比较长且占用多行时，可以在函数的 docstring 中声明路径操作的描述，FastAPI 支持从文档字符串中读取描述内容。
# 文档字符串支持 Markdown，能正确解析和显示 Markdown 的内容，但要注意文档字符串的缩进。
@app.get("/users/", tags=["users"])
async def read_users():
    """
    Create an item with all the information:

    - **name**: each item must have a name
    - **description**: a long description
    - **price**: required
    - **tax**: if the item doesn't have tax, you can omit this
    - **tags**: a set of unique tag strings for this item
    """
    return [{"username": "johndoe"}]


@app.get("/elements/", tags=["items"], deprecated=True)
async def read_elements():
    """deprecated 参数可以把路径操作标记为弃用，无需直接删除它们。"""
    return [{"item_id": "Foo"}]


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app="pathOP:app", host="127.0.0.1", port=8080, reload=True)
