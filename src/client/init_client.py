# Python 3.6.2
# Script automating the starting of the client individually.

import client
port = 3705

x = client.Client()
x.initialize(port=port, network_architecture="Complete", remote_addresses=["192.168.1.77"])
