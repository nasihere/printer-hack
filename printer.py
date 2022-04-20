
import os  



def printDoc(printer_name, filename):
    print("PRINT-MAC",PRINTER_NAME,filename);
    os.system("lpr -P " + printer_name + " " + filename)


def printDoc4(printer_name, filename):
    print("PRINT-WINDOWS-4",PRINTER_NAME,filename);
    os.system("PRINT /D:" + printer_name + " " + filename)
