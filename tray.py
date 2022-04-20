import pystray
from PIL import Image, ImageDraw
from pystray import Icon as icon, Menu as menu, MenuItem as item
# from messengerclient import sendMessage;
from printer import printDoc, printDoc4
import os
printIP = os.environ['IP']
printPort = int(os.environ['PORT']) 
printDocName = os.environ['FILENAME'] 
printerName = os.environ['PRINTER_NAME']

print("ENV", printIP, printPort, printDocName, printerName);

def create_image(width, height, color1, color2):
    # Generate an image and draw a pattern
    image = Image.new('RGB', (width, height), color1)
    dc = ImageDraw.Draw(image)
    dc.rectangle(
        (width // 2, 0, width, height // 2),
        fill=color2)
    dc.rectangle(
        (0, height // 2, width // 2, height),
        fill=color2)

    return image


# In order for the icon to be displayed, you must provide an icon
icon = pystray.Icon(
    'RSC',
    icon=create_image(64, 64, 'black', 'white'), menu=menu(
           
             item(
                'Test Printer WINDOWS',
                lambda: printDoc4(printerName, printDocName)),
            item(
                'Test Printer MAC',
                lambda: printDoc(printerName, printDocName))))


icon.run()
