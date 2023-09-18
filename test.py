from typing import Annotated

from fastapi import BackgroundTasks, FastAPI, Depends
from starlette.responses import RedirectResponse

app = FastAPI()


def write_log(message: str):
    with open("log.txt", mode="a") as log:
        log.write(message)


def get_query(background_tasks: BackgroundTasks, q: str | None = None):
    if q:
        message = f"found query: {q}\n"
        background_tasks.add_task(write_log, message)
    return q


@app.post("/send-notification/{email}")
async def send_notification(
    email: str, background_tasks: BackgroundTasks, q: Annotated[str, Depends(get_query)]
):
    message = f"message to {email}\n"
    background_tasks.add_task(write_log, message)
    return {"message": "Message sent"}

@app.get("/")
async def root():
    """Redirect to docs"""
    return RedirectResponse(url="/docs/")


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app="test:app", host="127.0.0.1", port=8080, reload=True)