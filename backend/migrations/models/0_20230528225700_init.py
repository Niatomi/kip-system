from tortoise import BaseDBAsyncClient


async def upgrade(db: BaseDBAsyncClient) -> str:
    return """
        CREATE TABLE IF NOT EXISTS "users" (
    "id" UUID NOT NULL  PRIMARY KEY,
    "username" VARCHAR(20) NOT NULL UNIQUE,
    "password_hash" VARCHAR(128),
    "email" VARCHAR(50) NOT NULL,
    "first_name" VARCHAR(50),
    "second_name" VARCHAR(50),
    "third_name" VARCHAR(50),
    "role" VARCHAR(6)   DEFAULT 'WORKER',
    "created_at" TIMESTAMPTZ NOT NULL  DEFAULT CURRENT_TIMESTAMP,
    "modified_at" TIMESTAMPTZ NOT NULL  DEFAULT CURRENT_TIMESTAMP
);
COMMENT ON COLUMN "users"."role" IS 'admin: ADMIN\nchief: CHIEF\nworker: WORKER';
COMMENT ON TABLE "users" IS 'The User model';
CREATE TABLE IF NOT EXISTS "devicespool" (
    "id" UUID NOT NULL  PRIMARY KEY,
    "mongo_id" VARCHAR(25) NOT NULL,
    "name" VARCHAR(50) NOT NULL,
    "check_intervals" BIGINT NOT NULL,
    "group" VARCHAR(30) NOT NULL,
    "price" DECIMAL(20,2) NOT NULL,
    "resource" INT NOT NULL
);
COMMENT ON TABLE "devicespool" IS 'The Devices Pool model';
CREATE TABLE IF NOT EXISTS "activedevices" (
    "id" UUID NOT NULL  PRIMARY KEY,
    "invent_number" VARCHAR(50) NOT NULL,
    "serial_number" VARCHAR(50) NOT NULL,
    "place" VARCHAR(60) NOT NULL,
    "device_id_id" UUID NOT NULL REFERENCES "devicespool" ("id") ON DELETE CASCADE
);
COMMENT ON TABLE "activedevices" IS 'The Active devices model';
CREATE TABLE IF NOT EXISTS "aerich" (
    "id" SERIAL NOT NULL PRIMARY KEY,
    "version" VARCHAR(255) NOT NULL,
    "app" VARCHAR(100) NOT NULL,
    "content" JSONB NOT NULL
);"""


async def downgrade(db: BaseDBAsyncClient) -> str:
    return """
        """
