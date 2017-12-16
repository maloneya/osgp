import socket,pickle
#in a real networking environment this would be handled with DNS resolution presumably,
host_names = {"myface":"192.168.33.10","bookspace":"192.168.33.11"}

def snd_and_wait(op, msgs, dst_ip):
	TCP_PORT = 5005
	BUFFER_SIZE = 1024
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	s.connect((dst_ip,TCP_PORT))
	s.send(op)
	data = s.recv(BUFFER_SIZE)
	if data != "200":
		s.close()
		return data

 	data = ""
	for msg in msgs:
		data += msg + "/"

	s.send(data)
	data = s.recv(BUFFER_SIZE)
	s.close()
	return data

def recieve_graph(serialized_social_graph):
	return pickle.loads(serialized_social_graph)

def request_graph(domain, name, requesting_id):
	if not host_names.has_key(domain): return "304"
	dst_ip = host_names[domain]
	return snd_and_wait("request_graph",[name,requesting_id],dst_ip)

def send_notification(domain, name, notification, sender_id):
	if not host_names.has_key(domain): return "304"
	dst_ip = host_names[domain]
	return snd_and_wait("notify",[name,notification,sender_id],dst_ip)
#fixme - need to deserialize and not clear screen!
def request_posts(domain, name, sender_id):
	if not host_names.has_key((domain)):
		print "Domain",dst_domain,"not found"
		return

	dst_ip = host_names[domain]

	ret = snd_and_wait("request_posts",[name,sender_id],dst_ip)
	if ret == "404":
		print name,"not found at",domain
		return -1
	elif ret == "401":
		print "Can not view posts"
		print name,"has not added you as a friend"
		return -1
	else:
		return pickle.loads(ret)
