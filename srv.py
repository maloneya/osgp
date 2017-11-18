import socket

s = socket.socket()
host = "192.168.33.11"
port = 5005
buffer_size = 1024
s.bind((host,port))

s.listen(5)
while True:
	conn, addr = s.accept()
	print "connected to ",addr

	data = conn.recv(buffer_size)
	print data

	conn.send("Connected!!")
	conn.close()