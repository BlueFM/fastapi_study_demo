from typing import  Annotated

from fastapi import FastAPI, Body
from fastapi.responses import RedirectResponse
from pydantic import BaseModel, Field

app = FastAPI()


### Start

@app.get("/")
async def root():
    """Redirect to docs"""
    return RedirectResponse(url="/docs/")


class Item(BaseModel):
    """example: request body which use Field"""
    name: str
    description: str | None = Field(
        default=None, title="The description of the item", max_length=300
    )
    price: float = Field(gt=0, description="The price must be greater than zero")
    tax: float | None = None


@app.put("/items/{item_id}")
async def update_item(item_id: int, item: Annotated[Item, Body(embed=True)]):
    """使用 Field 为请求体参数添加元数据"""
    results = {"item_id": item_id, "item": item}
    return results


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app="reqBody_Field:app", host="127.0.0.1", port=8080, reload=True)
