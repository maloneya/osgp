from social_network_ops import *
from Queue import Queue

users = []
my_graph = None

def display_users():
	for i,user in enumerate(users):
		print i,user.owner.name

def run_client(host_name,notification_queue):
	print "\nWelcome to", host_name
	print "--------------------------"
	#create init user for this domain
	users.append(create_graph(raw_input("Enter Name: "),raw_input("Enter Age: "),host_name))

	while True:
		if not notification_queue.empty():
			#todo process notificaitons
			print notification_queue.get()

		print "Available operations: 1. add friend by name 2. add friend you may know 3. display my graph 4. create local user"
		op = raw_input("Enter operation number: ")

		if   op == "1":
			display_users()
			usr_idx = int(raw_input("Enter user number: "))
			name = raw_input("Enter name of new friend: ")
			domain = raw_input("Enter domain of new friend: ")
			add_friend_by_name(users,usr_idx,host_name,domain,name)
		elif op == "2":
			display_users()
			add_friend_in_graph(users,int(raw_input("Enter user number: ")),host_name)
		elif op == "3":
			users[0].display_graph()
		elif op == "4":
			users.append(create_graph(raw_input("Enter Name: "),raw_input("Enter Age: "),host_name))

		else:
			print "Invalid op number"


def find_graph(name):
	for graph in users:
		if graph.owner.name == name:
			return graph

	return -1
