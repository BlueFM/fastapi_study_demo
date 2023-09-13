from enum import Enum

from fastapi import FastAPI
from fastapi.responses import RedirectResponse

app = FastAPI()


@app.get("/")
async def root():
    """Redirect to docs"""
    return RedirectResponse(url="/docs/")


### Road Parameters

@app.get("/users/me")
async def read_user_me():
    """example: get current user"""
    return {"user_id": "the current user"}


@app.get("/users/{user_id}")
async def read_user(user_id: str):
    """example: get user by id"""
    return {"user_id": user_id}


class ModelName(str, Enum):
    """example: enum machine learning model name"""
    alexnet = "alexnet"
    resnet = "resnet"
    lenet = "lenet"


@app.get("/models/{model_name}")
async def get_model(model_name: ModelName):
    """example: get machine learning model by name"""
    if model_name is ModelName.alexnet:
        return {"model_name": model_name, "message": "Deep Learning FTW!"}

    if model_name.value == "lenet value":
        return {"model_name": model_name, "message": "LeCNN all the images"}

    return {"model_name": model_name, "message": "Have some residuals"}


@app.get("/files/{file_path:path}")
async def read_file(file_path: str):
    """example: path para"""
    return {"file_path": file_path}


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app="roadPara:app", host="127.0.0.1", port=8080, reload=True)