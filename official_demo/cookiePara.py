from typing import Annotated

from fastapi import Cookie, FastAPI, Header
from starlette.responses import RedirectResponse

app = FastAPI()


@app.get("/items/")
async def read_items(ads_id: Annotated[str | None, Cookie()] = None):
    """使用cookie"""
    return {"ads_id": ads_id}


@app.get("/itemsh/")
async def read_itemsh(user_agent: Annotated[str | None, Header()] = None):
    """使用header"""
    return {"User-Agent": user_agent}


# 自动转换
# Header 在 Path, Query 和 Cookie 提供的功能之上有一点额外的功能。
# 大多数标准的headers用 "连字符" 分隔，也称为 "减号" (-)。
# 但是像 user-agent 这样的变量在Python中是无效的。
# 因此, 默认情况下, Header 将把参数名称的字符从下划线 (_) 转换为连字符 (-) 来提取并记录 headers.
# 同时，HTTP headers 是大小写不敏感的，因此，因此可以使用标准Python样式(也称为 "snake_case")声明它们。
# 因此，您可以像通常在Python代码中那样使用 user_agent ，而不需要将首字母大写为 User_Agent 或类似的东西。
# 如果出于某些原因，你需要禁用下划线到连字符的自动转换，设置Header的参数 convert_underscores 为 False
# 重复的 headers
# 有可能收到重复的headers。这意味着，相同的header具有多个值。
# 您可以在类型声明中使用一个list来定义这些情况。
# 你可以通过一个Python list 的形式获得重复header的所有值。

@app.get("/")
async def root():
    """Redirect to docs"""
    return RedirectResponse(url="/docs/")


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app="cookiePara:app", host="127.0.0.1", port=8080, reload=True)