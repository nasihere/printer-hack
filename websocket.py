

 # Importing the relevant libraries
import websockets
import asyncio
import json
import sys

_CONNECTIONID = ""
SOCKET = "wss://eelxzvivea.execute-api.us-east-2.amazonaws.com/production"

# The main function that will handle connection and communication 
# with the server
ws_disconnect_flag: bool = False

async def listen(recv):
    
    url = SOCKET
    # Connect to the server
    async with websockets.connect(url) as ws:
        await ws.send(json.dumps({"action": "profileMessage"}))
        # Stay alive forever, listening to incoming msgs
        while True:
            print("listeneing....")
            msg = await ws.recv()
            print("received")
            recv(msg)

def ws_run(recv):
    try:
        print("Waiting for socket")
        asyncio.get_event_loop().run_until_complete(listen(recv))
    except:
       recv(json.dumps({"action":"disconnect"}))
    

def ws_disconnect():
    ws_disconnect_flag = True

