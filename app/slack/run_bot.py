from fastapi import FastAPI

from app import config

from .handlers import router

app = FastAPI(title=config.WEB_SERVER_NAME, version=config.APP_VERSION, debug=config.WEB_SERVER_DEBUG)

app.include_router(router)


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host=config.WEB_SERVER_HOST, port=config.WEB_SERVER_PORT)
