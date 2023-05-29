import pytest


@pytest.fixture(scope="session")
async def device():
    return {
        "device_specs": {
            "description": "Description for device",
            "specifications": [
                {"spec1": "details"},
                {"spec2": "details"},
                {"spec3": "details"}
            ]
        },
        "device_info": {
            "name": "Device",
            "check_intervals": 123123,
            "group": "string",
            "price": 1000.01,
            "resource": 123123
        }
    }
