import asyncio
import websockets
import time

async def main(uri):
    while True:
        try:
            async with websockets.connect(uri) as websocket:
                messages = []
                print("Connection established for Client 2")
                while True:
                    message = await websocket.recv()
                    if message:
                        messages.append((message, time.time()))
                        if len(messages) == 10: 
                            block_start = messages[0][1]
                            block_end = messages[-1][1]
                            block_time = block_end - block_start
                            with open('logs1.txt', 'a') as f:
                                f.write(f'Block received at: {block_end} (took {block_time} seconds)\n')
                                for m in messages:
                                    f.write(f'Message: {m[0]} received at {m[1]}\n')
                            response = "Response from client"
                            await websocket.send(response)
                            messages = []
        except:
            print("Connection closed by server. Reconnecting in 5 seconds...")
            await asyncio.sleep(5)
            
asyncio.run(main('ws://localhost:12345'))

