from tortoise import BaseDBAsyncClient


async def upgrade(db: BaseDBAsyncClient) -> str:
    return """
        ALTER TABLE "devicespool" ALTER COLUMN "name" TYPE VARCHAR(150) USING "name"::VARCHAR(150);"""


async def downgrade(db: BaseDBAsyncClient) -> str:
    return """
        ALTER TABLE "devicespool" ALTER COLUMN "name" TYPE VARCHAR(50) USING "name"::VARCHAR(50);"""
