from social_graph import socialGraph
from person import Person
from comm_opps import send_graph

alex = socialGraph(Person("alex",21))
tom = socialGraph(Person("Tom",40))
dan = socialGraph(Person("Dan",21))
rob = socialGraph(Person("Robbie",21))

tom.add_friend(friend_graph=dan)
tom.add_friend(friend_graph=rob)
alex.add_friend(friend_graph=tom)

send_graph(alex,"192.168.33.11")