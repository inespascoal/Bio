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
        match message:
                case "0":
                  control=Control()
                  for i in range(10):
                  control.forWard()
                  control.stop()
                case "1":
                  print("back")
                case "2":
                  print("right")
                case "3":
                  print("left")



start_server=websockets.serve(server, "localhost", 5000)

loop = asyncio.get_event_loop()

loop.run_until_complete(start_server)
loop.run_forever()

# asyncio.get_event_loop.stop()
# loop.stop()

# async def main():
#     async with websockets.serve(echo, "localhost", 8765):
#         print("WebSocket server listening on ws://localhost:8765")
#         await asyncio.Future()  # run forever

# asyncio.run(main())
