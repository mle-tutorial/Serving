from dataclasses import asdict

from app.common.config import Config
from app.routes.api import router
from fastapi.middleware.gzip import GZipMiddleware
from starlette.middleware.cors import CORSMiddleware

from fastapi import FastAPI


def create_app() -> FastAPI:
    c = Config()
    conf_dict = asdict(c)
    app = FastAPI(
        version="0.0.1",
        title="Project Art-ficial Intelligence",
        docs_url=conf_dict["DOCS_URL"],
        redoc_url=conf_dict["REDOC_URL"],
    )

    app.add_middleware(GZipMiddleware, minimum_size=1000)
    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_methods=["*"],
        allow_headers=["*"],
    )
    app.include_router(router)
    return app


app = create_app()
