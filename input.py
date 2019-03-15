import asyncio
import websockets

host = 'ws://192.168.102.59:1234/'
ws = websockets.connect(host)


async def __get_input_async(host_name):
    async with websockets.connect(host_name) as websocket:
        a = await websocket.recv()
        b = await websocket.recv()
        return a, b

'''
a , b = asyncio.get_event_loop().run_until_complete(__get_input_async(host))

print(a, b)
'''
