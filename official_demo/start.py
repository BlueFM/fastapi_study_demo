from fastapi import FastAPI
from fastapi.responses import RedirectResponse

app = FastAPI()


### Start

@app.get("/")
async def root():
    """Redirect to docs"""
    return RedirectResponse(url="/docs/")


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app="start:app", host="127.0.0.1", port=8080, reload=True)
