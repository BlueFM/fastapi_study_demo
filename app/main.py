import uvicorn
from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

from api.routes.api import router as api_router
from core.events import create_start_app_handler
from core.config import API_PREFIX, VERSION

def get_application() -> FastAPI:
    application = FastAPI(title="Pine AI Family! (with cats)", version=VERSION)
    application.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )
    application.include_router(api_router, prefix=API_PREFIX)
    pre_load = True
    if pre_load:
        application.add_event_handler("startup", create_start_app_handler(application))
    return application


app = get_application()

if __name__ == '__main__':
    uvicorn.run(app='main:app', host="0.0.0.0", port=8000, reload=True)
