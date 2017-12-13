import networkx as nx
from person import Person
from comm_opps import send_graph

class socialGraph:
	def __init__(self,owner):
		self.graph = nx.Graph()
		self.owner = owner
		self.graph.add_node(owner)

	def add_friend(self,person=None,friend_graph=None):
		if person is not None:
			self.graph.add_node(person)
			self.graph.add_edge(self.owner,person)

		elif friend_graph is not None:
			self.graph.add_node(friend_graph.owner)
			self.graph.add_edge(self.owner,friend_graph.owner)

			exisiting_nodes = set(self.graph.nodes)
			new_nodes = set(friend_graph.graph.nodes)
			for friend in new_nodes:
				if friend not in exisiting_nodes:
					self.graph.add_node(friend)

				self.graph.add_edge(friend_graph.owner,friend)

		else:
			print "Plese provide a person object or graph to add"

	def display_graph(self):
		print "Owner", self.owner

		nodes = set(list(self.graph.nodes))
		friends = set(list(self.graph.neighbors(self.owner)));
		non_friends = nodes - friends - set([self.owner])
		print "Friends:",friends
		print "People you may know:",non_friends