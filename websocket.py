

 # Importing the relevant libraries
import websockets
import asyncio
import json
import sys

SOCKET = "wss://g1q8o7g387.execute-api.us-east-2.amazonaws.com/production"

# The main function that will handle connection and communication 
# with the server
ws_disconnect_flag: bool = False

async def listen(recv):
    url = SOCKET
    # Connect to the server
    async with websockets.connect(url) as ws:
        print(ws)
        await ws.send(json.dumps({"action": "sendMessage", "message":"hello"}))
        # Stay alive forever, listening to incoming msgs
        while not ws_disconnect_flag:
            msg = await ws.recv()
            print(msg)
            recv(msg)

def ws_run(recv):
    asyncio.get_event_loop().run_until_complete(listen(recv))

def ws_disconnect():
    ws_disconnect_flag = True

def onmessage(msg):
    print(msg)


ws_run(onmessage)