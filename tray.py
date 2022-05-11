import pystray
import configparser
import math
from whoami import winWhoAmI, macWhoAmI
from PIL import Image, ImageDraw
from pystray import Icon as icon, Menu as menu, MenuItem as item
# from messengerclient import sendMessage;
from printer import printDocMac, printDoc4
import os
from pathlib import Path
from sys import platform
import asyncio
import json
from websocket import ws_run,ws_disconnect
import threading
import sys

o = open('LOGGER--OUTPUT','w')


path = Path(__file__)

userid = "NA";
if platform == "linux" or platform == "linux2":
    userid = macWhoAmI();
elif platform == "darwin":
    userid = macWhoAmI();
elif platform == "win32":
    userid = winWhoAmI();

config_path = 'myfile.ini'

WS_CONNECTION_ID = ''

Config = configparser.ConfigParser()
Config.read(config_path)
printDocName = Config.get('PRINTER','FILENAME')
printerName = Config.get('PRINTER','PRINTER_NAME')


print(userid, printDocName, printerName, file=o);

def create_image(width, height, color1, color2):
    config_path = os.path.join(path.parent.absolute(), "socket-icon.png")
    image = Image.open(config_path)
    return image

# In order for the icon to be displayed, you must provide an icon
icon = pystray.Icon(
    'RSC',
    icon=create_image(64, 64, '#ddddff', 'blue'), menu=menu(
            item(
                'YOU ARE ' + WS_CONNECTION_ID + "!",
                lambda: print(WS_CONNECTION_ID)),
             item(
                'Test Printer WINDOWS',
                lambda: printDoc4(printerName, printDocName)),
            item(
                'Test Printer MAC',
                lambda: printDocMac(printerName, printDocName)),
            item(
                'Exit',
                lambda:  exit_action(icon))))

def exit_action(icon):
    ws_disconnect()
    icon.visible = False
    icon.stop()
    app.stop()
    sys.exit()
    

def onWSmessage(msg):
    print(msg)
    body = json.loads(msg)
    _CONNECTIONID = body['connectionId']
    action = body['action'];
    if action == "profileMessage":
        print("Profile COnnection id received")
    elif action == "printRequest":
        print("printRequest")
        link = body['link']
        printerName = body['printerName']
        print(f"link {link} printerName {printerName}")
        # printDoc4(printerName, link)

    print(connectionId)



o.close();
# Start the connection
# asyncio.get_event_loop().run_until_complete(listen(recv_websocket))
# Create two threads as follows

try:
   ws_run(onWSmessage)
   #icon.run()

#    thread.start_new_thread( asyncio.get_event_loop().run_until_complete()  )
#    thread.start_new_thread( icon.run())
except:
   print("Error: unable to start thread")

while 1:
    pass