import asyncio
import websockets
import time
from faker import Faker

fake = Faker()

async def handle_connection(websocket, path):
    j = 0
    while True:
        j += 1
        message = fake.name()
        await websocket.send(message)
        response = await websocket.recv()
        print(f"Received confirmation message from client: {response}")
        await asyncio.sleep(2) # delay of 2 seconds between messages

async def main():
    server = await websockets.serve(handle_connection, 'localhost', 12345)
    await server.wait_closed()

asyncio.run(main())

