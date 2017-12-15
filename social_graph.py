import networkx as nx
from person import Person

class socialGraph:
	def __init__(self,name,age,location):
		self.graph = nx.Graph()
		self.owner = Person(name,age,location)
		self.graph.add_node(self.owner)

	def add_friend(self,friend_graph):
		self.graph.add_node(friend_graph.owner)
		self.graph.add_edge(self.owner,friend_graph.owner)

		exisiting_nodes = set(self.graph.nodes)
		new_nodes = set(friend_graph.graph.nodes)
		for friend in new_nodes:
			if friend not in exisiting_nodes:
				self.graph.add_node(friend)

			self.graph.add_edge(friend_graph.owner,friend)

	def remove_friend(self,person_to_remove):
		for node in self.graph.nodes:
			if node.name == person_to_remove:
				self.graph.remove_edge(self.owner,node)
				return 0

		return -1

	def getFriends(self):
		return set(list(self.graph.neighbors(self.owner)));

	def getNonFriends(self):
		nodes = set(list(self.graph.nodes))
		friends = set(list(self.graph.neighbors(self.owner)));
		non_friends = nodes - friends - set([self.owner])
		return non_friends

	def display_graph(self):
		print "Owner", self.owner
		print "Friends:",self.getFriends()
		print "People you may know:",self.getNonFriends()