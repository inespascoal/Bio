# -*- coding: utf-8 -*-
"""
Created on Fri May  5 09:08:08 2023

@author: Utilizador
"""

import asyncio
import websockets
from Control import *
     
async def server(websocket, path):
    async for message in websocket:
        await websocket.send(f'Got your msg its: {message}')
        if message == "0":
          control=Control()
          for i in range(10):
               control.forWard()
               control.stop()
        elif message == "1":
            print("back")
        elif message == "2":
            print("right")
        elif message == "3":
            print("left")
   



start_server=websockets.serve(server, "10.0.7.199", 5000)

loop = asyncio.get_event_loop()

loop.run_until_complete(start_server)
loop.run_forever()

# asyncio.get_event_loop.stop()
# loop.stop()

# async def main():
#     async with websockets.serve(echo, "10.0.7.199", 8765):
#         print("WebSocket server listening on ws://localhost:8765")
#         await asyncio.Future()  # run forever

# asyncio.run(main())
