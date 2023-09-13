from enum import Enum
from typing import Union

from fastapi import FastAPI
from fastapi.responses import RedirectResponse
from pydantic import BaseModel

app = FastAPI()


@app.get("/")
async def root():
    """Redirect to docs"""
    return RedirectResponse(url="/docs/")


### Request Parameters
class Item(BaseModel):
    """example: request body"""
    name: str
    description: str | None = None
    price: float
    tax: float | None = None


@app.post("/items/")
async def create_item(item: Item):
    """example: request body"""
    return item


@app.post("/items2/")
async def create_item2(item: Item):
    """example: request body and response"""
    item_dict = item.dict()
    if item.tax:
        price_with_tax = item.price + item.tax
        item_dict.update({"price_with_tax": price_with_tax})
    return item_dict


@app.put("/items/{item_id}")
async def create_item3(item_id: int, item: Item):
    """example: request body and path para"""
    return {"item_id": item_id, **item.dict()}


@app.put("/items/{item_id}")
async def create_item4(item_id: int, item: Item, q: str | None = None):
    """example: request body, path para and query para"""
    result = {"item_id": item_id, **item.dict()}
    if q:
        result.update({"q": q})
    return result


"""
函数参数将依次按如下规则进行识别：

如果在路径中也声明了该参数，它将被用作路径参数。
如果参数属于单一类型（比如 int、float、str、bool 等）它将被解释为查询参数。
如果参数的类型被声明为一个 Pydantic 模型，它将被解释为请求体。
"""

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app="requestPara:app", host="127.0.0.1", port=8080, reload=True)
