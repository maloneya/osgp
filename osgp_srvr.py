import socket,pickle
from social_network import find_graph
from Queue import Queue

#in a real networking environment this would be handled with DNS resolution presumably,
host_names = {"myface":"192.168.33.10","bookspace":"192.168.33.11"}

def start_graph_srvr(host_name,notification_queue):
	s = socket.socket()
	port = 5005
	buffer_size = 1024
	s.bind((host_names[host_name],port))
	print "Server started:",host_names[host_name]
	s.listen(5)
	while True:
		conn, addr = s.accept()
		# print "connected to ",addr
		op = conn.recv(buffer_size)

		if   op == "request_graph":
			conn.send("200");
			name = conn.recv(buffer_size)
			graph = find_graph(name)
			if graph == -1:
				conn.send("404")
			else:
				conn.send(pickle.dumps(graph))

		elif op == "notify":
			conn.send("200")
			usr_to_notify = conn.recv()
			if find_graph(usr_to_notify) == -1:
				conn.send("404")
			else:
				notificaiton = conn.recv()
				notification_queue.put_nowait((usr_to_notify,notificaiton))

		else:
			conn.send("401")

		conn.close()

#todo - when a graph is reqeusted the server should send a
#message to the client that a user added them, and prompt them to add the user back

#posts - need to authenticate that both users have eachtoher as friends in their graph

#remove - send a notify msg that a user has removed this user.