from osgp_client import *
from social_graph import socialGraph

users = []
local_domain = None

def create_graph(name, age, location):
	return socialGraph(name,age,location)

def set_local_domain(host_name): local_domain = host_name

def get_user(idx):
	return users[idx]

def find_graph_op(name):
	for graph in users:
		if graph.owner.name == name:

			return graph

	return -1

def add_friend_by_name(user_idx,dst_domain,name):
	if dst_domain == local_domain:
		requested_graph = find_graph(name,users)
		if requested_graph == -1:
			print "User",name,"not found at",dst_domain
		else:
			users[user_idx].add_friend(requested_graph)

		return

	ret = request_graph(dst_domain,name,users[user_idx].owner.id)
	if (ret == "404"):
		print "User",name,"not found at",dst_domain
		return
	elif (ret == "304"):
		print "Domain",dst_domain,"not found"
		return

	requested_graph = recieve_graph(ret)
	users[user_idx].add_friend(requested_graph)

def add_friend_in_graph(user_idx):
	current_user = users[user_idx]
	non_friends_in_graph = list(current_user.getNonFriends())

	addusr_idx = -1
	for i,non_friends in enumerate(non_friends_in_graph):
		print i,non_friends.name

	addusr_idx = int(raw_input("Enter user number you wish to add: "))

	if addusr_idx == -1: return
	addusr = non_friends_in_graph[addusr_idx]
	add_friend_by_name(user_idx,addusr.owner_location,addusr.name)

def remove_friend(usr_idx):
	current_user = users[usr_idx]
	friends = list(current_user.getFriends())
	for i,u in enumerate(friends):
		print i,u.name

	remove_idx = int(raw_input("Enter user number you wish to remove: "))
	current_user.remove_friend(friends[remove_idx].name)

	send_notification(friends[remove_idx].owner_location,friends[remove_idx].name,"removefriend",current_user.owner.id)

def notification_handeler(type,local_user,msg):
	if type == "newfriend":
		print msg,"has added",local_user,"as a friend"
		if (raw_input("1. Add Back 2. Ignore: ")) ==  "1":
			for i,user in enumerate(users):
				if user.owner.name == local_user:
					id = msg.split('@')
					add_friend_by_name(i,id[1],id[0])

	elif type == "removefriend":
		print msg,"has removed",local_user,"as a friend"
		if (raw_input("1. remove 2. Ignore: ")) ==  "1":
			usr_to_remove = str(msg.split("@")[0])
			find_graph_op(local_user).remove_friend(usr_to_remove)


