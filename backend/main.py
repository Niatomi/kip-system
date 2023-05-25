from src.database import init_db
from fastapi import FastAPI
import uvicorn
from fastapi.middleware.cors import CORSMiddleware

from src.config import network_config
from src.config import middleware_config
from src.config import api_config

from src.auth.router import router as auth_router
from fastapi_pagination import add_pagination

app = FastAPI(
    title="КИП",
    description="API для приложения учёта КИП процессов в геофизике",
    version=api_config.api_version
)


app.include_router(router=auth_router,
                   prefix=api_config.api_version_path)


origins = [middleware_config.cors_hosts]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["POST", "GET", "DELETE", 'PUT'],
    allow_headers=["*"],
)

init_db(app)
add_pagination(app)


def main():
    uvicorn.run("main:app",
                reload=api_config.is_dev,
                port=network_config.port,
                host=network_config.host)


if __name__ == "__main__":
    main()
