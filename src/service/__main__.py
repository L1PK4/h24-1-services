import asyncio
from hypercorn.config import Config
from hypercorn.asyncio import serve

from fastapi.middleware.cors import CORSMiddleware

from service.app.app import create_app

if __name__ == "__main__":
    app = create_app()
    app.add_middleware(
        CORSMiddleware,
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )
    conf = Config()
    conf.bind = ["0.0.0.0:8001"]
    asyncio.run(serve(app, conf))  # type: ignore
