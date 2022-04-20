import pystray
import configparser
import math


from PIL import Image, ImageDraw
from pystray import Icon as icon, Menu as menu, MenuItem as item
# from messengerclient import sendMessage;
from printer import printDoc, printDoc4
import os
from pathlib import Path
from sys import platform

o = open('outfile','w')


path = Path(__file__)

if platform == "linux" or platform == "linux2":
    ROOT_DIR = path.parent.absolute()
elif platform == "darwin":
    ROOT_DIR = path.parent.absolute() 
elif platform == "win32":
    ROOT_DIR = "D:\\"

print(ROOT_DIR, file=o)
print("APP PATH", ROOT_DIR,  path.parent.absolute(), file=o)
config_path = os.path.join(ROOT_DIR, "myfile.ini")


Config = configparser.ConfigParser()
Config.read(config_path)

printDocName = Config.get('PRINTER','FILENAME')
printerName = Config.get('PRINTER','PRINTER_NAME')

print("INI", printDocName, printerName, file=o);

def create_image(width, height, color1, color2):
    config_path = os.path.join(path.parent.absolute(), "socket-icon.png")
    image = Image.open(config_path)
    return image

# In order for the icon to be displayed, you must provide an icon
icon = pystray.Icon(
    'RSC',
    icon=create_image(64, 64, '#ddddff', 'blue'), menu=menu(
           
             item(
                'Test Printer WINDOWS',
                lambda: printDoc4(printerName, printDocName)),
            item(
                'Test Printer MAC',
                lambda: printDoc(printerName, printDocName)),
            item(
                'Exit',
                lambda:  exit_action(icon))))

def exit_action(icon):
    icon.visible = False
    icon.stop()


o.close();
icon.run()
