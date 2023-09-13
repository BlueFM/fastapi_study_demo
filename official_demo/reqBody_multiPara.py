from typing import Annotated

from fastapi import FastAPI, Path, Body
from pydantic import BaseModel
from fastapi.responses import RedirectResponse

app = FastAPI()
### Start


@app.get("/")
async def root():
    """Redirect to docs"""
    return RedirectResponse(url="/docs/")


class Item(BaseModel):
    """example: request body"""
    name: str
    description: str | None = None
    price: float
    tax: float | None = None


@app.put("/items/{item_id}")
async def update_item(
    item_id: Annotated[int, Path(title="The ID of the item to get", ge=0, le=1000)],
    q: str | None = None,
    item: Item | None = None,
):
    """混合使用 Path、Query 和请求体参数"""
    results = {"item_id": item_id}
    if q:
        results.update({"q": q})
    if item:
        results.update({"item": item})
    return results


class User(BaseModel):
    """example: request body"""
    username: str
    full_name: str | None = None


@app.put("/items2/{item_id}")
async def update_item2(item_id: int, item: Item, user: User):
    """多个请求体参数"""
    results = {"item_id": item_id, "item": item, "user": user}
    return results


@app.put("/items3/{item_id}")
async def update_item3(
    item_id: int, item: Item, user: User, importance: Annotated[int, Body()]
):
    """多个请求体参数➕请求体的单一值"""
    results = {"item_id": item_id, "item": item, "user": user, "importance": importance}
    return results


@app.put("/items4/{item_id}")
async def update_item4(
    *,
    item_id: int,
    item: Item,
    user: User,
    importance: Annotated[int, Body(gt=0)],
    q: str | None = None,
):
    """
    除了请求体参数外，你还可以在任何需要的时候声明额外的查询参数。
    由于默认情况下单一值被解释为查询参数，因此你不必显式地添加 Query，你可以仅执行以下操作：
    """
    results = {"item_id": item_id, "item": item, "user": user, "importance": importance}
    if q:
        results.update({"q": q})
    return results


@app.put("/items5/{item_id}")
async def update_item5(item_id: int, item: Annotated[Item, Body(embed=True)]):
    """
    假设你只有一个来自 Pydantic 模型 Item 的请求体参数 item。
    默认情况下，FastAPI 将直接期望这样的请求体。
    但是，如果你希望它期望一个拥有 item 键并在值中包含模型内容的 JSON，
    就像在声明额外的请求体参数时所做的那样，则可以使用一个特殊的 Body 参数 embed
    """
    results = {"item_id": item_id, "item": item}
    return results


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app="reqBody_multiPara:app", host="127.0.0.1", port=8080, reload=True)