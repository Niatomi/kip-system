from pydantic import BaseSettings
from typing import List


class SettingsBase(BaseSettings):

    class Config:
        env_file = ".env"
        env_file_encoding = 'utf-8'


class PostgresDbConfig(SettingsBase):
    postgres_user: str
    postgres_password: str
    postgres_host: str
    postgres_port: str
    postgres_db_name: str
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


class ClickhouseDbConfig(SettingsBase):
    clickhouse_user: str
    clickhouse_password: str
    clickhouse_host: str
    clickhouse_db_name: str


network_config = NetworkConfig()
postgres_db_config = PostgresDbConfig()
clickhouse_db_config = ClickhouseDbConfig()
mongo_db_config = MongoDbConfig()
api_config = ApiConfig()
auth_config = AuthConfig()
middleware_config = MiddleWareConfig()
env_config = EnvConfig()
