import pystray
from PIL import Image, ImageDraw
from pystray import Icon as icon, Menu as menu, MenuItem as item
# from messengerclient import sendMessage;
from printer import printDoc, printDoc2;
import os
printIP = os.environ['IP']
printPort = int(os.environ['PORT']) 
printDocName = os.environ['FILENAME'] 
print("ENV", printIP, printPort, printDocName);

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
                'Test Printer 1',
                lambda: testPrinter()),
            item(
                'Test Printer 2',
                lambda: testPrinter2())))

# sendMessage("Hello Nasir")
def testPrinter():
    printDoc(printIP, printPort, printDocName);
def testPrinter2():
    printDoc2(printIP, printPort, printDocName);
# To finally show you icon, call run
icon.run()
