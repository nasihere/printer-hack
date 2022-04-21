
from pathlib import Path
import os
path = Path(__file__)

pdf2Print = os.path.join(path.parent.absolute(), "PDFtoPrinter.exe")

def printDoc(printer_name, filename):
    o = open('printfile','w')
    print("PRINT-MAC",printer_name,filename,file=o);
    os.system("lpr -P " + printer_name + " " + filename)
    o.close();


def printDoc4(printer_name, filename):
    o = open('printfile','w')
    print("PRINT-WINDOWS-4",pdf2Print+printer_name,filename,file=o);
    print(pdf2Print + " \"" + filename + "\" \"" + printer_name + "\"", file=o)
    os.system(pdf2Print + " \"" + filename + "\" \"" + printer_name + "\"")
    o.close();
