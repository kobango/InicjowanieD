import asyncio
import websockets

host = 'ws://192.168.102.59:1234/'
ws = websockets.connect(host)


async def __get_input_async(host_name):
    async with websockets.connect(host_name) as websocket:
        while True:
            a = await websocket.recv()
            print(a)
        

def get_input(host_name):
    a = asyncio.get_event_loop().run_until_complete(__get_input_async(host_name))
    return a

asyncio.get_event_loop().run_until_complete(__get_input_async(host))


