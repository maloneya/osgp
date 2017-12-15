from social_network_ops import *
from Queue import Queue
import os

my_graph = None

def display_users():
	for i,user in enumerate(users):
		print i,user.owner.name

def run_client(host_name,notification_queue):
	print "\nWelcome to", host_name
	print "--------------------------"
	#create init user for this domain
	users.append(create_graph(raw_input("Enter Name: "),raw_input("Enter Age: "),host_name))
	set_local_domain(host_name)

	while True:
		clear = True
		while not notification_queue.empty():
			type,local_user, msg = notification_queue.get()
			notification_handeler(type,local_user,msg)

		print "Available operations: 1. add friend by name 2. add friend you may know 3. display my graph 4. create local user"
		print "5. Remove Friend"
		op = raw_input("Enter operation number: ")

		if   op == "1":
			display_users()
			usr_idx = int(raw_input("Enter user number: "))
			name = raw_input("Enter name of new friend: ")
			domain = raw_input("Enter domain of new friend: ")
			add_friend_by_name(usr_idx,domain,name)
		elif op == "2":
			display_users()
			add_friend_in_graph(int(raw_input("Enter user number: ")))
		elif op == "3":
			get_user(0).display_graph()
			clear = False
		elif op == "4":
			users.append(create_graph(raw_input("Enter Name: "),raw_input("Enter Age: "),host_name))
		elif op == "5":
			display_users()
			usr_idx = int(raw_input("Enter user number: "))
			remove_friend(usr_idx)

		else:
			print "Invalid op number"

		if clear: os.system('clear')

def find_graph(name):
	return find_graph_op(name)
