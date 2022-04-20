import socket


def printDoc(ipAdd, portNo, filename):
    mysocket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)         
    host = ipAdd;
    port = portNo;   
    try:           
        mysocket.connect((host, port)) #connecting to host
        mysocket.send(b"t\n/Subtype /Image\n/BitsPerComponent 1\n/Width 232\n/Height 25\n/ImageMask true\n/Filter /JBIG2Decode\n/DecodeParms << /JBIG2Globals 9 0 R\n>>\n\n>>\n\nstream\n\x00\x00\x00\x120\x00\x01\x00\x00\x00\x13\x00\x00\x00\xe8\x00\x00\x00\x19\x00\x00.#\x00\x00.#\x00\x80\x18\x00\x00\x00\x13\x00\x01\x01\x00\x00\x00\xfb\x08\x00\x02\xff\x00\x00\x00\x0b\x00\x00\x00\x0b*6Q\xb2{d\xee\xef\xed\xe1\x9b\rFA\xd3\x83\xa7@\x91\xc2M\x07w\x035\x0f\xbc\x18\x13\x87\xff\nE\xcc\xf6NI#:\xe6\xc3f\x85]Q\x7f\xaaX\xc2k\xb4\xc0?\xbf\x86\x9b\x89\xdf>\x04\x18xI\x00\xda\xf9:j\xf3Kwc\x13\xa3\x06\xe1\xa4U\xf3\xd0\x9e\x8d\xb9\x02\x12\xdc\x98\xdbV\x9c\x98\xa2\xf6 \x1b\xe4\t\xd9\xb5\xa0\xfe\xe2a\xc5\xd2\xd6\xaa=\x98\xd1\x83\xc2\xa3\xb6\xc9f\x17\xd4.\xc3\xb3P\xbcd\x97\x8dQ\x94ZxQ\x95\xe6j`\x1br$\xcd\x1c\xaal\xc0i\xc4#$\x07\xf5\x87\x06\xbeE\x89\x14b\x99\xe0\xa2\xa4\xcb\x01\x80\xd0M^Q\xffu\x8f\xd4\x9c\x18\x10\xec%\n\x9c]\xf0\xe8\xd9\xe5\x84F\x99\x13\xce\xb5q\xba\x19G\xac>\xe7\xec\xaf\x0b\xdc(\x04\xd3\xab\x03\x0c\xbc\xdd\xe0T\xac\x03\xf4\xf7+\x0eB\xde.;\x83)\xd7\xea\x0b\xf8\x8e\x1a\xa1y\x8f!\x16 F\x82_\xff\xac\x00\x00\x00\x142\x00\x01\x00\x00\x00\x04\x00\x00\x00\x01\x00\x00\x00\x15\x06B\x00\x13\x01\x00\x00\x00'\x00\x00\x00\xe8\x00\x00\x00\x18\x00\x00\x00\x00\x00\x00\x00\x01\x00\x14\x00\x00\x00\x00\x0b\x88\xce\xd6d\xf68\xc5\x11\xf8\xa3\xf7\xb2\x15\x16\xff\xac\nendstream\n\nendobj\n\n14 0 obj\n<< /CreationDate (D:20211215204110-05'00')\n/Creator (Xerox AltaLink C8045)\n/Producer (Xerox AltaLink C8045)\n>>\nendobj\n\nxref\n0 15\n0000000000 65535 f \n0000000016 00000 n \n0000000066 00000 n \n0000000124 00000 n \n0000000329 00000 n \n0000000434 00000 n \n0000002948 00000 n \n0000002970 00000 n \n0000003717 00000 n \n0000007326 00000 n \n0000007422 00000 n \n0000008992 00000 n \n0000009737 00000 n \n0000010203 00000 n \n0000010767 00000 n \n\ntrailer\n<< /Size 15\n/Root 1 0 R\n/Info 14 0 R\n/ID [<e47311c")#using bytes
        
        mysocket.close () #closing connection
    except:
        print("Error with the connection")

BUFFER_SIZE = 1024 * 4 #4KB

def printDoc2(ipAdd, portNo, filename):
    mysocket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)         
    host = ipAdd;
    port = portNo;   
    print(filename)
    mysocket.connect((host, port)) 

    try:
        with open(filename, "rb") as f:
            print("Reading File")
            while True:
                bytes_read = f.read(BUFFER_SIZE)
                print("Reading Byte")
                if not bytes_read:
                    break
                print("BYETS")
                print(bytes_read)
                mysocket.sendall(bytes_read)
    finally:
        print("Error with the connection")
        mysocket.close()
