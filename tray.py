import pystray
import configparser
import math

from PIL import Image, ImageDraw
from pystray import Icon as icon, Menu as menu, MenuItem as item
# from messengerclient import sendMessage;
from printer import printDoc, printDoc4
import os
from pathlib import Path

path = Path(__file__)
ROOT_DIR = path.parent.absolute();
print(ROOT_DIR)
config_path = os.path.join(ROOT_DIR, "myfile.ini")


Config = configparser.ConfigParser()
Config.read(config_path)

printIP = Config.get('PRINTER','IP')
printPort = int(Config.get('PRINTER','PORT')) 
printDocName = Config.get('PRINTER','FILENAME')
printerName = Config.get('PRINTER','PRINTER_NAME')

print("ENV", printIP, printPort, printDocName, printerName);

def create_image(width, height, color1, color2):
    config_path = os.path.join(ROOT_DIR, "socket-icon.png")
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
                lambda: printDoc(printerName, printDocName))))


icon.run()
