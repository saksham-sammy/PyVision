import asyncio
from bleak import BleakClient

DEVICE_ADDRESS = "PASTE_DEVICE_ADDRESS_HERE"
CHAR_UUID = "0000ffe1-0000-1000-8000-00805f9b34fb"

async def send_message():

    async with BleakClient(DEVICE_ADDRESS) as client:

        message = "Hello from Python BLE!"
        data = message.encode()

        await client.write_gatt_char(CHAR_UUID, data)

        print("Message sent successfully!")

asyncio.run(send_message())