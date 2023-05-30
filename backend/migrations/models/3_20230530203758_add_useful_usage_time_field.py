from tortoise import BaseDBAsyncClient


async def upgrade(db: BaseDBAsyncClient) -> str:
    return """
        ALTER TABLE "devicespool" ADD "resource_of_useful_usage" INT NOT NULL  DEFAULT 5;
        ALTER TABLE "devicespool" ALTER COLUMN "check_intervals" TYPE INT USING "check_intervals"::INT;
        ALTER TABLE "devicespool" ALTER COLUMN "check_intervals" TYPE INT USING "check_intervals"::INT;
        ALTER TABLE "devicespool" ALTER COLUMN "check_intervals" TYPE INT USING "check_intervals"::INT;
        ALTER TABLE "devicespool" ALTER COLUMN "check_intervals" TYPE INT USING "check_intervals"::INT;"""


async def downgrade(db: BaseDBAsyncClient) -> str:
    return """
        ALTER TABLE "devicespool" DROP COLUMN "resource_of_useful_usage";
        ALTER TABLE "devicespool" ALTER COLUMN "check_intervals" TYPE BIGINT USING "check_intervals"::BIGINT;
        ALTER TABLE "devicespool" ALTER COLUMN "check_intervals" TYPE BIGINT USING "check_intervals"::BIGINT;
        ALTER TABLE "devicespool" ALTER COLUMN "check_intervals" TYPE BIGINT USING "check_intervals"::BIGINT;
        ALTER TABLE "devicespool" ALTER COLUMN "check_intervals" TYPE BIGINT USING "check_intervals"::BIGINT;"""
