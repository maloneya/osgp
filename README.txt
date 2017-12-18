{\rtf1\ansi\ansicpg1252\cocoartf1504\cocoasubrtf830
{\fonttbl\f0\fswiss\fcharset0 Helvetica;}
{\colortbl;\red255\green255\blue255;}
{\*\expandedcolortbl;;}
\margl1440\margr1440\vieww13580\viewh14340\viewkind0
\pard\tx720\tx1440\tx2160\tx2880\tx3600\tx4320\tx5040\tx5760\tx6480\tx7200\tx7920\tx8640\pardirnatural\partightenfactor0

\f0\fs24 \cf0 Alex Maloney \
Computer Networks \
\
OSGP Testing \
README \
\
This application was tested in virtual machines deployed using vagrant. sub directories box1 and box2 contain the vagrant configuration files that set up the private network and mount the file share. Provison.sh should automatically install needed application dependencies\
\
This application can be tested without vagrant, however you would need to manually install python dependencies and change the IP addresses stored in the domain dictionary in osgp_client and osgp_srvr. \
\
github project link: https://github.com/maloneya/osgp/ \
\
File overview \
\'97\'97\'97\'97\'97\'97\'97\'97\'97\'97\'97\'97\'97\
main.py - entry point for the application, starts the server thread and social network client thread\
	\'93python main.py myface\'94 or \'93python main.py bookspace\'94 \
\
social_network.py - responsible for interacting with the user. waits for operating input and makes the social network api call \
social_network_ops.py - application layer social network api, performs all of the social network applications and makes calls down to the osgp_client when necessary \
\
osgp_client.py - implements all the client requests for the osgp protocol. implements python sockets to send and receive messages over a tcp connection \
\
osgp_srvr.py - started in a separate thread by the main program. Listens for incoming messages on port 5005 and preforms the server duties for the various osgp requests. Passes notifications back up to the user social network thread via a sync queue \
\
social_graph.py social graph class that exports server api calls for graph modifications such as add and remove friend and for graph queries such as get friend and get non friends. underlying graph data structure implemented via networkx graph library \
\
person.py - social graph data object class. stores and maintains the data for each node in the graph, name age id and posts. \
\
}