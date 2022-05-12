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
import time
import subprocess

def copy2clip(txt):
    cmd='echo '+txt.strip()+'|clip'
    return subprocess.check_call(cmd, shell=True)

    
o = open('LOGGER--OUTPUT','w')


path = Path(__file__)

userid = "NA";
if platform == "linux" or platform == "linux2":
    userid = macWhoAmI();
elif platform == "darwin":
    userid = macWhoAmI();
elif platform == "win32":
    userid = winWhoAmI();

WS_CONNECTION_ID = 'NOT'



def create_image(width, height, color1, color2):
    config_path = os.path.join(path.parent.absolute(), "socket-icon.png")
    image = Image.open(config_path)
    return image


def create_red(width, height, color1, color2):
    config_path = os.path.join(path.parent.absolute(), "socket-red.png")
    image = Image.open(config_path)
    return image

# In order for the icon to be displayed, you must provide an icon


def exit_action(icon):
    print('quit')
    ws_disconnect()
    icon.visible = False
    icon.stop()
    for t in all_threads:
        t.stop()

def printConnectionDetails():
    print("connection details")
    print(WS_CONNECTION_ID)

def tray_failure():
    icon = pystray.Icon('RSC',icon=create_red(64, 64, '#ddddff', 'blue'), 
            menu=menu(
                item(
                    'Connect ',
                    lambda: restart_app(icon)),
                item(
                    'Exit ',
                    lambda: exit_action(icon)),
        ))
    icon.run()


def tray_success(WS_CONNECTION_ID):
    print("syccess trey -")
    print(WS_CONNECTION_ID + " TRAQT")
    print("syccess trey e")
    icon = pystray.Icon('RSC',icon=create_image(64, 64, '#ddddff', 'blue'), 
        menu=menu(
            item(
                'Copy ' + WS_CONNECTION_ID,
                lambda: copy2clip(WS_CONNECTION_ID)),
            item(
                'Exit ',
                lambda: exit_action(icon)),
    ))
    icon.run()



def onWSmessage(msg):
    print(msg)
    body = json.loads(msg)
    action = body['action'];
    if action == "profileMessage":
        o = open('LOGGER--SOCKET--ID','w')
        WS_CONNECTION_ID = body['connectionId']
        print(WS_CONNECTION_ID,file=o)
        print(userid, file=o)
        o.close()
        x = threading.Thread(target=tray_success, args=(WS_CONNECTION_ID,))
        all_threads.append(x)
        x.start()
    elif action == "printRequest":
        print("printRequest")
        link = body['link']
        printerName = body['printerName']
        print(f"link {link} printerName {printerName}")
        printDoc4(printerName, link)
    elif action == "disconnect":
        print("disconnected")
        x = threading.Thread(target=tray_failure, args=())
        all_threads.append(x)
        x.start()
o.close();

def restart_app(icon):
    print("this will run after every 5 sec")
    icon.stop()
    
    time.sleep(5)
    ws_run(onWSmessage)
        
       
        
    

all_threads = []

try:
    print("Waiting for client")
    ws_run(onWSmessage)
except KeyboardInterrupt:
    print("Stopped by Ctrl+C")
    ws_disconnect()
    icon.stop()

finally:
    for t in all_threads:
        t.join()
    