from tortoise import BaseDBAsyncClient


async def upgrade(db: BaseDBAsyncClient) -> str:
    return """
        ALTER TABLE "users" ALTER COLUMN "role" SET DEFAULT 'WORKER';
        ALTER TABLE "devicespool" ADD "mongo_id" VARCHAR(25) NOT NULL DEFAULT 'NO CODE';"""


async def downgrade(db: BaseDBAsyncClient) -> str:
    return """
        ALTER TABLE "users" ALTER COLUMN "role" DROP DEFAULT;
        ALTER TABLE "devicespool" DROP COLUMN "mongo_id";"""
