

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
        while not ws_disconnect_flag:
            msg = await ws.recv()
            print("received")
            recv(msg)

def ws_run(recv):
    asyncio.get_event_loop().run_until_complete(listen(recv))

def ws_disconnect():
    ws_disconnect_flag = True


def onWSmessage(msg):
    print(msg)
    body = json.loads(msg)
    action = body['action'];
    if action == "profileMessage":
        _CONNECTIONID = body['connectionId']
        print("Profile COnnection id received")
    elif action == "printRequest":
        print("printRequest")
        link = body['link']
        printerName = body['printerName']
        print(f"link {link} printerName {printerName}")
        # printDoc4(printerName, link)



ws_run(onWSmessage)