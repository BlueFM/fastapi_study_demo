from fastapi import FastAPI
from fastapi.responses import RedirectResponse
import uvicorn
from demo_1.routers import routers_path
from demo_1.core.config import API_PREFIX, VERSION, TITLE, DESCRIPTION

app = FastAPI(title=TITLE, description=DESCRIPTION, version=VERSION)
app.include_router(routers_path.router, prefix=API_PREFIX)


@app.get("/")
async def root():
    # return "hello world!"
    return RedirectResponse(url="/docs/")


if __name__ == "__main__":
    uvicorn.run(app="demo_1_start:app", host="127.0.0.1", port=8000, reload=True)
