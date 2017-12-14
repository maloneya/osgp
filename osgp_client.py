import socket,pickle
#in a real networking environment this would be handled with DNS resolution presumably,
host_names = {"myface":"192.168.33.10","bookspace":"192.168.33.11"}

def snd_and_wait(op,msgs,dst_ip):
	TCP_PORT = 5005
	BUFFER_SIZE = 1024
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	s.connect((dst_ip,TCP_PORT))
	s.send(op)
	data = s.recv(BUFFER_SIZE)
	if data != "200":
		s.close()
		return data

	for msg in msgs:
		s.send(msg)

	data = s.recv(BUFFER_SIZE)
	s.close()
	return data

# def send_graph(social_graph,domain):
# 	dst_ip = host_names[domain]
# 	msg = pickle.dumps(social_graph)
# 	return snd_and_wait(msg,dst_ip)

def recieve_graph(serialized_social_graph):
	return pickle.loads(serialized_social_graph)

def request_graph(domain,name):
	if not host_names.has_key(domain): return "304"
	dst_ip = host_names[domain]
	return snd_and_wait("request_graph",[name],dst_ip)

def user_notify(domain,name, notification):
	if not host_names.has_key(domain): return "304"
	dst_ip = host_names[domain]
	return snd_and_wait("notify",[name,notification],dst_ip)
