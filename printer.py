
import os  



def printDoc(printer_name, filename):
    print("PRINT-MAC",printer_name,filename);
    os.system("lpr -P " + printer_name + " " + filename)


def printDoc4(printer_name, filename):
    print("PRINT-WINDOWS-4",printer_name,filename);
    os.system("PDFtoPrinter.exe \"" + filename + "\" \"" + printer_name + "\"")
