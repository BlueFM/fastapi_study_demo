from typing import List

from fastapi import FastAPI, Query
from fastapi.responses import RedirectResponse
from pydantic import Required

app = FastAPI()


@app.get("/")
async def root():
    """Redirect to docs"""
    return RedirectResponse(url="/docs/")


@app.get("/items/")
async def read_items(q: str | None = Query(default=None, max_length=50)):
    """example: query para Verify default value and max length"""
    results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
    if q:
        results.update({"q": q})
    return results


@app.get("/items2/")
async def read_items2(
    q: str | None = Query(
        default=None, min_length=3, max_length=50, pattern="^fixedquery$"
    )
):
    """example: query para Verify default value, min length, max length and regex"""
    results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
    if q:
        results.update({"q": q})
    return results


@app.get("/items3/")
async def read_items3(q: str = Query(default="fixedquery", min_length=3)):
    """example: query para Verify default value and min length"""
    results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
    if q:
        results.update({"q": q})
    return results


@app.get("/items4/")
async def read_items4(q: str = Query(default=..., min_length=3)):
    """可以显式的声明一个值是必需的，即将默认参数的默认值设为 ... """
    results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
    if q:
        results.update({"q": q})
    return results


@app.get("/items5/")
async def read_items5(q: str | None = Query(default=..., min_length=3)):
    """你可以声明一个参数可以接收None值，但它仍然是必需的。这将强制客户端发送一个值，即使该值是None"""
    results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
    if q:
        results.update({"q": q})
    return results


@app.get("/items6/")
async def read_items6(q: str = Query(default=Required, min_length=3)):
    """如果你觉得使用 ... 不舒服，你也可以从 Pydantic 导入并使用 Required"""
    results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
    if q:
        results.update({"q": q})
    return results


@app.get("/items7/")
async def read_items7(q: List[str] | None = Query(default=None)):
    """example: query para Verify list"""
    query_items = {"q": q}
    return query_items


@app.get("/items8/")
async def read_items8(q: List[str] = Query(default=["foo", "bar"])):
    """example: query para Verify list default value"""
    query_items = {"q": q}
    return query_items


@app.get("/items9/")
async def read_items9(q: list = Query(default=[])):
    """你也可以直接使用 list 代替 List [str]"""
    query_items = {"q": q}
    return query_items


@app.get("/items10/")
async def read_items10(
    q: str | None = Query(
        default=None,
        title="Query string",
        description="Query string for the items to search in the database that have a good match",
        min_length=3,
    )
):
    """你可以添加更多有关该参数的信息（title，description），这些信息将显示在自动生成的文档中"""
    results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
    if q:
        results.update({"q": q})
    return results


@app.get("/items11/")
async def read_items11(q: str | None = Query(default=None, alias="item-query")):
    """
    假设你想要查询参数为 item-query。
    但是 item-query 不是一个有效的 Python 变量名称。
    最接近的有效名称是 item_query。
    但是你仍然要求它在 URL 中必须是 item-query...
    这时你可以用 alias 参数声明一个别名，该别名将用于在 URL 中查找查询参数值
    """
    results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
    if q:
        results.update({"q": q})
    return results


"""
弃用参数
现在假设你不再喜欢此参数。
你不得不将其保留一段时间，因为有些客户端正在使用它，但你希望文档清楚地将其展示为已弃用。
那么将参数 deprecated=True 传入 Query：
"""


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app="queryPara_stringVerify:app", host="127.0.0.1", port=8080, reload=True)
