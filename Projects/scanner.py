import asyncio
from bleak import BleakScanner

async def scan_devices():
    print("Scanning for BLE devices...\n")

    devices = await BleakScanner.discover()

    for d in devices:
        print(f"Name: {d.name}, Address: {d.address}")

asyncio.run(scan_devices())
