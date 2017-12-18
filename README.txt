Alex Maloney 
Computer Networks 

OSGP Testing 
README 

This application was tested in virtual machines deployed using vagrant. sub directories box1 and box2 contain the vagrant configuration files that set up the private network and mount the file share. Provison.sh should automatically install needed application dependencies

This application can be tested without vagrant, however you would need to manually install python dependencies and change the IP addresses stored in the domain dictionary in osgp_client and osgp_srvr. 

github project link: https://github.com/maloneya/osgp/ 

File overview 
—————————————
main.py - entry point for the application, starts the server thread and social network client thread
	“python main.py myface” or “python main.py bookspace” 

social_network.py - responsible for interacting with the user. waits for operating input and makes the social network api call 
social_network_ops.py - application layer social network api, performs all of the social network applications and makes calls down to the osgp_client when necessary 

osgp_client.py - implements all the client requests for the osgp protocol. implements python sockets to send and receive messages over a tcp connection 

osgp_srvr.py - started in a separate thread by the main program. Listens for incoming messages on port 5005 and preforms the server duties for the various osgp requests. Passes notifications back up to the user social network thread via a sync queue 

social_graph.py social graph class that exports server api calls for graph modifications such as add and remove friend and for graph queries such as get friend and get non friends. underlying graph data structure implemented via networkx graph library 

person.py - social graph data object class. stores and maintains the data for each node in the graph, name age id and posts. 

