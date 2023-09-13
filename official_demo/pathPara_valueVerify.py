from typing import Annotated

from fastapi import FastAPI, Query, Path
from fastapi.responses import RedirectResponse

app = FastAPI()


### Start

@app.get("/")
async def root():
    """Redirect to docs"""
    return RedirectResponse(url="/docs/")


@app.get("/items/{item_id}")
async def read_items(
        item_id: Annotated[int, Path(title="The ID of the item to get")],
        q: Annotated[str | None, Query(alias="item-query")] = None,
):
    """
    可以声明与 Query 相同的所有参数，但是它们将被用作路径参数。
    Annotated(py39) 为变量或函数参数附加额外的元数据
    如标题、描述、默认值、最小值、最大值等。
    """
    results = {"item_id": item_id}
    if q:
        results.update({"q": q})
    return results


@app.get("/items2/{item_id}")
async def read_items2(*, item_id: Annotated[int, Path(title="The ID of the item to get")], q: str):
    """
    按需对参数排序的技巧
    <>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
    如果你想不使用 Query 声明没有默认值的查询参数 q
    同时使用 Path 声明路径参数 item_id
    并使它们的顺序与上面不同，Python 对此有一些特殊的语法。
    传递 * 作为函数的第一个参数。
    Python 不会对该 * 做任何事情，
    但是它将知道之后的所有参数都应作为关键字参数（键值对）
    也被称为 kwargs，来调用。即使它们没有默认值。
    """
    results = {"item_id": item_id}
    if q:
        results.update({"q": q})
    return results


@app.get("/items3/{item_id}")
async def read_items3(
        *,
        item_id: Annotated[int, Path(title="The ID of the item to get",
                                     ge=1, le=100)],
        q: str
):
    """
    数值校验
    <>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
    使用 Query 和 Path（以及你将在后面看到的其他类）
    可以声明字符串约束，但也可以声明数值约束。
    像下面这样，添加 ge=1 后，
    item_id 将必须是一个大于（greater than）或等于（equal）1 的整数。
    同样的规则适用于：
    gt：大于（greater than）
    le：小于等于（less than or equal）
    数值校验同样适用于 float 值
    """
    results = {"item_id": item_id}
    if q:
        results.update({"q": q})
    return results


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app="pathPara_valueVerify:app", host="127.0.0.1", port=8080, reload=True)
