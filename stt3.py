import asyncio
import websockets
import time

async def handle_connection(websocket, path):
    while True:
        message = "Hello from the server"
        await websocket.send(message)
        await asyncio.sleep(2) 

async def main():
    server = await websockets.serve(handle_connection, 'localhost', 12345)
    await server.wait_closed()

asyncio.run(main())

