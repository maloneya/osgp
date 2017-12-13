import socket,pickle

TCP_IP = "192.168.33.11"

def send_graph(social_graph,desination):
	TCP_IP = desination
	TCP_PORT = 5005
	BUFFER_SIZE = 1024

	msg = pickle.dumps(social_graph)

	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	s.connect((TCP_IP,TCP_PORT))
	s.send(msg)
	data = s.recv(BUFFER_SIZE)
	s.close()

	print "got: ",data

def recieve_graph(serialized_social_graph):
	return pickle.loads(serialized_social_graph)

