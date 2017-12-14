import sys
from threading import Thread
from osgp_srvr import start_graph_srvr
from social_network import run_client
from Queue import Queue

if len(sys.argv) != 2:
	print "Correct usage - python main.py domain"
	exit()

LOCAL_DOMAIN = sys.argv[1]
notification_queue = Queue()

srv_thd = Thread(target=start_graph_srvr,args=(LOCAL_DOMAIN,notification_queue))
srv_thd.daemon = True
srv_thd.start()

run_client(LOCAL_DOMAIN,notification_queue)