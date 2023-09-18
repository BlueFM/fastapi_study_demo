from fastapi import FastAPI
from fastapi.responses import RedirectResponse
from db import main
app = FastAPI()

app.include_router(main.router, tags=["aha"])

@app.get("/")
async def root():
    """Redirect to docs"""
    return RedirectResponse(url="/docs/")


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app="nico_start:app", host="127.0.0.1", port=8000, reload=True)
