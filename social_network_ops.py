from osgp_client import *
from social_graph import socialGraph

def create_graph(name, age, location):
	return socialGraph(name,age,location)

def find_graph(name,users):
	for graph in users:
		if graph.owner.name == name:

			return graph

	return -1

def add_friend_by_name(users,user_idx,local_domain,dst_domain,name):
	if dst_domain == local_domain:
		requested_graph = find_graph(name,users)
		if requested_graph == -1:
			print "User",name,"not found at",dst_domain
		else:
			users[user_idx].add_friend(requested_graph)

		return

	ret = request_graph(dst_domain,name)
	if (ret == "404"):
		print "User",name,"not found at",dst_domain
		return
	elif (ret == "304"):
		print "Domain",dst_domain,"not found"
		return

	requested_graph = recieve_graph(ret)
	users[user_idx].add_friend(requested_graph)

def add_friend_in_graph(users,user_idx,local_domain):
	current_user = users[user_idx]
	non_friends_in_graph = list(current_user.getNonFriends())

	addusr_idx = -1
	for i,non_friends in enumerate(non_friends_in_graph):
		print i,non_friends.name

	addusr_idx = int(raw_input("Enter user number you wish to add: "))

	if addusr_idx == -1: return
	addusr = non_friends_in_graph[addusr_idx]
	add_friend_by_name(users,user_idx,local_domain,addusr.owner_location,addusr.name)


