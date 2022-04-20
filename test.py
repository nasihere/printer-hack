import socket
mysocket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)         
host = "10.0.0.7" 
port = 9100   
try:           
	mysocket.connect((host, port)) #connecting to host
	mysocket.send(b"Socket Test")#using bytes
	mysocket.close () #closing connection
except:
	print("Error with the connection")
