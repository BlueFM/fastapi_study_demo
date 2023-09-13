from typing import Annotated

from fastapi import FastAPI, Body
from fastapi.responses import RedirectResponse
from pydantic import BaseModel, Field

app = FastAPI()


### Start

@app.get("/")
async def root():
    """Redirect to docs"""
    return RedirectResponse(url="/docs/")


"""
您可以在JSON模式中定义额外的信息。
一个常见的用例是添加一个将在文档中显示的example。
有几种方法可以声明额外的 JSON 模式信息。
"""


# 1.Pydantic schema_extra

class Item(BaseModel):
    """这些额外的信息将按原样添加到输出的JSON模式中"""
    name: str
    description: str | None = None
    price: float
    tax: float | None = None

    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "name": "Foo",
                    "description": "A very nice Item",
                    "price": 35.4,
                    "tax": 3.2,
                }
            ]
        }
    }


@app.put("/items/{item_id}")
async def update_item(item_id: int, item: Item):
    """Pydantic schema_extra"""
    results = {"item_id": item_id, "item": item}
    return results


# 2.使用Field

class Item2(BaseModel):
    """
    使用Field
    传递的那些额外参数不会添加任何验证，只会添加注释，用于文档的目的
    """
    name: str = Field(example="Foo")
    description: str | None = Field(default=None, example="A very nice Item")
    price: float = Field(example=35.4)
    tax: float | None = Field(default=None, example=3.2)


@app.put("/items2/{item_id}")
async def update_item2(item_id: int, item: Item2):
    """使用Field"""
    results = {"item_id": item_id, "item": item}
    return results


# 3.使用Body

class Item3(BaseModel):
    name: str
    description: str | None = None
    price: float
    tax: float | None = None


@app.put("/items3/{item_id}")
async def update_item3(
        item_id: int,
        item: Annotated[
            Item3,
            Body(
                example=
                {
                    "name": "Foo",
                    "description": "A very nice Item",
                    "price": 35.4,
                    "tax": 3.2,
                }

            ),
        ],
):
    results = {"item_id": item_id, "item": item}
    return results


"""
关于 example 和 examples...
JSON Schema在最新的一个版本中定义了一个字段 examples ，
但是 OpenAPI 基于之前的一个旧版JSON Schema，并没有 examples.
所以 OpenAPI为了相似的目的定义了自己的 example (使用 example, 而不是 examples), 
这也是文档 UI 所使用的 (使用 Swagger UI).
所以，虽然 example 不是JSON Schema的一部分，但它是OpenAPI的一部分，这将被文档UI使用。
其他信息
同样的方法，你可以添加你自己的额外信息，这些信息将被添加到每个模型的JSON模式中，例如定制前端用户界面，等等。
"""


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app="moduleExtra:app", host="127.0.0.1", port=8080, reload=True)
