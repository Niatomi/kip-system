from tortoise import BaseDBAsyncClient


async def upgrade(db: BaseDBAsyncClient) -> str:
    return """
        ALTER TABLE "devicespool" RENAME COLUMN "group" TO "category";"""


async def downgrade(db: BaseDBAsyncClient) -> str:
    return """
        ALTER TABLE "devicespool" RENAME COLUMN "category" TO "group";"""
