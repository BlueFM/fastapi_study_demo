from fastapi import FastAPI
from fastapi.responses import RedirectResponse
from pydantic import BaseModel, Field, HttpUrl

app = FastAPI()


### Start

@app.get("/")
async def root():
    """Redirect to docs"""
    return RedirectResponse(url="/docs/")


# 1. 嵌套模型
class Item(BaseModel):
    """example: request body with nested model"""
    name: str
    description: str | None = None
    price: float
    tax: float | None = None
    tags: dict = Field(default=..., description="The tags for this item")


@app.put("/items/{item_id}")
async def update_item(item_id: int, item: Item):
    """嵌套模型"""
    results = {"item_id": item_id, "item": item}
    return results


# 2. 嵌套模型和子模型
class Image(BaseModel):
    """example: request body with nested model"""
    url: HttpUrl
    name: str


class Item2(BaseModel):
    """example: request body with nested model"""
    name: str
    description: str | None = None
    price: float
    tax: float | None = None
    tags: dict = Field(default=..., description="The tags for this item")
    image: list[Image] | None = None


@app.put("/items2/{item_id}")
async def update_item2(item_id: int, item: Item2):
    """嵌套模型和子模型"""
    results = {"item_id": item_id, "item": item}
    return results


# 3. 任意深度的嵌套模型

class Offer(BaseModel):
    name: str
    description: str | None = None
    price: float
    items: list[Item2] | None = None


@app.post("/offers/")
async def create_offer(offer: Offer):
    """任意深度的嵌套模型"""
    return offer


# 4. 纯列表请求体
@app.post("/images/multiple/")
async def create_multiple_images(images: list[Image]):
    """纯列表请求体"""
    return images


# 5. 任意 dict 构成的请求体
# 你也可以将请求体声明为使用某类型的键和其他类型值的 dict。
# 无需事先知道有效的字段/属性（在使用 Pydantic 模型的场景）名称是什么。
# 如果你想接收一些尚且未知的键，这将很有用。
@app.post("/index-weights/")
async def create_index_weights(weights: dict[int, float] | None = {12: 1.22}):
    if weights is None:
        weights = {12: 1.2}
    return weights


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app="reqBody_nestedQuery:app", host="127.0.0.1", port=8080, reload=True)
