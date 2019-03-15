import asyncio
import websockets


host = 'ws://192.168.102.59:1234/'
async def hello():
    async with websockets.connect(host) as ws:
        while True:
            data = await ws.recv()
            print(data)
            #print(type(data))

asyncio.get_event_loop().run_until_complete(hello())
