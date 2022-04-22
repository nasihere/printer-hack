
from pathlib import Path
import os
from s3download import s3download
path = Path(__file__)
dest_folder="mydownload"

pdf2Print = os.path.join(path.parent.absolute(), "printPDF.exe")

def printDocMac(printer_name, filename):
    o = open('printfile','w')
    s3Request(filename)
    diskFilename = filename.split('/')[-1].replace(" ", "_")  # be careful with file names
    s3DownloadedFilename = os.path.join(path.parent.absolute(), dest_folder + "/" + diskFilename)
    print("S3 Disk Location",s3DownloadedFilename,file=o);

    os.system("lpr -P " + printer_name + " " + s3DownloadedFilename)
    os.remove(s3DownloadedFilename)
    o.close();


def printDoc4(printer_name, filename):
    o = open('printfile','w')
    print("S3 Request",filename,file=o);

    s3Request(filename)
    diskFilename = filename.split('/')[-1].replace(" ", "_")  # be careful with file names
    s3DownloadedFilename = os.path.join(dest_folder + "\\" + diskFilename)
    print("S3 Disk Location",s3DownloadedFilename,file=o);

    
    print("Printer Driver",pdf2Print,file=o);
    print(pdf2Print + " \"" + s3DownloadedFilename + "\" \"" + printer_name + "\"", file=o)
    
    os.system(pdf2Print + " \"" + s3DownloadedFilename + "\" \"" + printer_name + "\"")
    os.remove(s3DownloadedFilename)
    o.close();

def s3Request(filename):
    s3download(filename, dest_folder)