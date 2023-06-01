from tortoise import BaseDBAsyncClient


async def upgrade(db: BaseDBAsyncClient) -> str:
    return """
        ALTER TABLE "activedevices" DROP CONSTRAINT "activedevices_device_id_id_fkey";
        ALTER TABLE "activedevices" RENAME COLUMN "device_id_id" TO "device_id";
        ALTER TABLE "activedevices" ADD CONSTRAINT "activedevices_device_id_fkey" FOREIGN KEY ("device_id") REFERENCES "devicespool" ("id") ON DELETE CASCADE;"""


async def downgrade(db: BaseDBAsyncClient) -> str:
    return """
        ALTER TABLE "activedevices" DROP CONSTRAINT "fk_activede_devicesp_4409c391";
        ALTER TABLE "activedevices" RENAME COLUMN "device_id" TO "device_id_id";
        ALTER TABLE "activedevices" ADD CONSTRAINT "fk_activede_devicesp_45969e90" FOREIGN KEY ("device_id_id") REFERENCES "devicespool" ("id") ON DELETE CASCADE;"""
