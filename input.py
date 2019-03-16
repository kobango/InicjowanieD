import asyncio
import websockets
import  data_analise

host = 'ws://192.168.102.59:1234/YQ=='
ws = websockets.connect(host)


async def __get_input_list_async(host_name, length):
    async with websockets.connect(host_name) as websocket:
        values = []
        for i in range(length):
            values.append(await websocket.recv())
        return values

async def __get_input_async(host_name):
    async with websockets.connect(host_name) as websocket:
        first = await websocket.recv()
        second = await websocket.recv()
        return first, second
        



a = asyncio.get_event_loop().run_until_complete(__get_input_list_async(host,2))
print(a)

