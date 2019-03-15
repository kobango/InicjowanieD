import asyncio
import websockets
import  danalise
import random

async def hello(websocket, path):
    name = await websocket.recv()
    print(f"< {name}")


    array = [danalise.txt,danalise.txt2,danalise.txt2,danalise.txt,danalise.txt3]
    while True:
        data = array[random.randrange(4)]
        await websocket.send(data)
        print(f"> {data}")

start_server = websockets.serve(hello, 'localhost', 8765)

asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()
