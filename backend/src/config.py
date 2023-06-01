from pydantic import BaseSettings
from typing import List


class SettingsBase(BaseSettings):

    class Config:
        env_file = ".env"
        env_file_encoding = 'utf-8'


class DbConfig(SettingsBase):
    db_user: str
    db_pass: str
    db_host: str
    db_port: str
    db_name: str
    ddl_show: bool = False


class EnvConfig(SettingsBase):
    env_name: str


class MiddleWareConfig(SettingsBase):
    cors_hosts: List[str]


class AuthConfig(SettingsBase):
    jwt_secret: str
    jwt_alg: str
    jwt_exp: int = 60


class ApiConfig(SettingsBase):
    api_version_path: str
    api_version: str
    is_dev: bool = False


class NetworkConfig(SettingsBase):
    port: int = 8000
    host: str = '0.0.0.0'


class MongoDbConfig(SettingsBase):
    mongo_username: str
    mongo_password: str
    database_name: str = 'kip_system_db'
    db_collection: str = 'device_description'


network_config = NetworkConfig()
db_config = DbConfig()
mongo_db_config = MongoDbConfig()
api_config = ApiConfig()
auth_config = AuthConfig()
middleware_config = MiddleWareConfig()
env_config = EnvConfig()
