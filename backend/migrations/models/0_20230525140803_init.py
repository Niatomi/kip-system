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
    "created_at" TIMESTAMPTZ NOT NULL  DEFAULT CURRENT_TIMESTAMP,
    "modified_at" TIMESTAMPTZ NOT NULL  DEFAULT CURRENT_TIMESTAMP
);
COMMENT ON TABLE "users" IS 'The User model';
CREATE TABLE IF NOT EXISTS "aerich" (
    "id" SERIAL NOT NULL PRIMARY KEY,
    "version" VARCHAR(255) NOT NULL,
    "app" VARCHAR(100) NOT NULL,
    "content" JSONB NOT NULL
);"""


async def downgrade(db: BaseDBAsyncClient) -> str:
    return """
        """
