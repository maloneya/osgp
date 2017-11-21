import socket

def send_msg(msg)
	TCP_IP = "192.168.33.11"
	TCP_PORT = 5005
	BUFFER_SIZE = 1024


	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	s.connect((TCP_IP,TCP_PORT))
	s.send(mgs)
	data = s.recv(BUFFER_SIZE)
	s.close()

	print "got: ",data

