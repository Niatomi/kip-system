from src.devices.device_pool.router import router as device_pool_router
from src.models import Users
from src.database import init_db
from fastapi import FastAPI
import uvicorn
from fastapi.middleware.cors import CORSMiddleware

from src.config import network_config
from src.config import middleware_config
from src.config import api_config

from fastapi_pagination import add_pagination

from src.auth.router import router as auth_router
from src.devices.devices_in_use.router import router as active_devices_router
import sys

app = FastAPI(
    title="КИП",
    description="API для приложения учёта КИП процессов в геофизике",
    version=api_config.api_version
)


app.include_router(router=auth_router,
                   prefix=api_config.api_version_path)
app.include_router(device_pool_router,
                   prefix=api_config.api_version_path)
app.include_router(router=active_devices_router,
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


@app.on_event("startup")
async def startup_event():
    try:
        await Users.first()
    except Exception:
        sys.exit(-2)


@app.get(f'{api_config.api_version_path}/ping',
         tags=['Healthcheck'],
         include_in_schema=False)
@app.get('/', include_in_schema=False)
def ping_api():
    return 'Pong'


def main():
    uvicorn.run("src.__main__:app",
                reload=api_config.is_dev,
                port=network_config.port,
                host=network_config.host)


if __name__ == "__main__":
    main()