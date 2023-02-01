import asyncio
import websockets
import time

async def main(uri):
    i = 0
    block_number = 0
    while True:
        try:
            async with websockets.connect(uri) as websocket:
                messages = []
                print("Connection established for Client 4")
                while True:
                    message = await websocket.recv()
                    if message:
                        i += 1
                        messages.append((message, time.time()))
                        print(f"Received message {i} from server: {message}")
                        await websocket.send("...")
                        if len(messages) == 15: 
                            block_start = messages[0][1]
                            block_end = messages[-1][1]
                            block_time = block_end - block_start
                            block_number += 1
                            with open('log4.txt', 'a') as f:
                                f.write(f'Block received at: {block_end} (took {block_time} seconds)\n')
                                for m in messages:
                                    f.write(f'Message: {m[0]} received at {m[1]}\n')
                            response = f"Client 4 received {block_number} block in {block_time} time"
                            await websocket.send(response)
                            messages = []
        except:
            print("Connection closed by server. Reconnecting in 5 seconds...")
            await asyncio.sleep(5)
            
asyncio.run(main('ws://localhost:12345'))   

