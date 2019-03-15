import asyncio
import websockets
import  danalise
import random

async def hello(websocket, path):
    name = await websocket.recv()
    print(f"< {name}")

    walue = danalise.spliting(danalise.txt)
    walue2 = danalise.spliting(danalise.txt2)
    walue3 = danalise.spliting(danalise.txt3)
    array = danalise.windowmake(walue)
    array = danalise.windowpeek(array, walue2)
    array = danalise.windowpeek(array, walue3)
    array = danalise.windowpeek(array, walue2)
    while True:
        data = array[random.randrange(4)]
        await websocket.send(data)
        print(f"> {data}")

start_server = websockets.serve(hello, 'localhost', 8765)

asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()