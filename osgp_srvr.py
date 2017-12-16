import socket,pickle
from social_network import find_graph, is_friend
from Queue import Queue

#in a real networking environment this would be handled with DNS resolution presumably,
host_names = {"myface":"192.168.33.10","bookspace":"192.168.33.11"}

buffer_size = 1024
port = 5005

def start_graph_srvr(host_name,notification_queue):
	s = socket.socket()
	s.bind((host_names[host_name],port))

	s.listen(5)
	while True:
		conn, addr = s.accept()
		# print "connected to ",addr
		op = conn.recv(buffer_size)

		if   op == "request_graph":
			conn.send("200");
			msgs = conn.recv(buffer_size).split("/")
			name = msgs[0]
			requester_id = msgs[1]
			graph = find_graph(name)
			if graph == -1:
				conn.send("404")
			else:
				conn.send(pickle.dumps(graph))
				notification_queue.put_nowait(("newfriend",name,requester_id))

		elif op == "request_posts":
			conn.send("200")
			msgs = conn.recv(buffer_size).split("/")
			local_usr = msgs[0]
			graph = find_graph(local_usr)
			if graph == -1:
				conn.send("404")
			else:
				sender = msgs[1]
				if not is_friend(local_usr,sender):
					conn.send("401")
				else:
					conn.send(pickle.dumps(graph.owner.posts))

		elif op == "notify":
			conn.send("200")
			msgs = conn.recv(buffer_size).split("/")
			usr_to_notify = msgs[0]
			if find_graph(usr_to_notify) == -1:
				conn.send("404")
			else:
				notificaiton = msgs[1]
				sender = msgs[2]
				notification_queue.put_nowait((notificaiton,usr_to_notify,sender))
				conn.send("200")

		else:
			conn.send("400")

		conn.close()