
import os  
import win32api



def printDoc(printer_name, filename):
    print("PRINT-MAC",PRINTER_NAME,filename);
    os.system("lpr -P " + printer_name + " " + filename)


def printDoc2(printer_name, filename):
    print("PRINT-WINDOWS",PRINTER_NAME,filename);
    win32api.ShellExecute(0, "printto", filename, f'"{printer_name}"', ".", 0)

def printDoc3(printer_name, filename):
    print("PRINT-WINDOWS-3",PRINTER_NAME,filename);
    win32api.ShellExecute(0, "print", filename, f'"{printer_name}"', ".", 0)

def printDoc4(printer_name, filename):
    print("PRINT-WINDOWS-4",PRINTER_NAME,filename);
    os.system("PRINT /D:" + printer_name + " " + filename)
