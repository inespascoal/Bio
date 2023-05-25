# -*- coding: utf-8 -*-
"""
Created on Fri May  5 09:08:08 2023

@author: Utilizador
"""

import asyncio
import websockets
from Control import *
from Ultrasonic import *
from Buzzer import *

control = Control()
ultrasonic = Ultrasonic()
buzzer = Buzzer()




async def server(websocket, path):
    t0 = time.time()
    async for message in websocket:
        await websocket.send(f'Got your msg its: {message}')
        control.stop()
        if message == "0":
            d = ultrasonic.getDistance()
            if (d>5):
                control.forWard()

                # ativar o buzzer se d in [5,20]
                if d < 20: 
                    buzzer.run(d)
                
        elif message == "1":
           control.backWard()
        elif message == "2":
            control.turnRight()
        elif message == "3":
            control.turnLeft()
   



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
