import socket
from comm_opps import recieve_graph
from social_graph import socialGraph

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
	graph = recieve_graph(data)
	print "got -"
	print graph.display_graph()

	conn.send("Connected!!")
	conn.close()