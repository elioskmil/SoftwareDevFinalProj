from p2pnetwork.node import Node

def node_callback(event, main_node, connected_node, data):
    try:
        if event!= 'node_request_to_stop':
            #node_request_to_stop doesn't have any connected_nodes while it is
            #the main node that is stopping
            print('Event: {} from main node {}: connected node {}: {}'.format(
                    event, main_node.id, connected_node.id, data
            ))
    except Exception as e:
        print(e)

class P2PNode(Node):
    def __init__(self, host, port, image, id=None, callback=None, max_connections=0):
        super(P2PNode, self).__init__(host, port, id, callback, max_connections)
        self.image = image
        self.start()

    def outbound_node_connected(self, connected_node):
        print("outbound_node_connected: " + connected_node.id)

    def inbound_node_connected(self, connected_node):
        print("inbound_node_connected: " + connected_node.id)

    def inbound_node_disconnected(self, connected_node):
        print("inbound_node_disconnected: " + connected_node.id)

    def outbound_node_disconnected(self, connected_node):
        print("outbound_node_disconnected: " + connected_node.id)

    def node_message(self, connected_node, data):
        print("node_message from " + connected_node.id + ": " + str(data))

    def node_disconnect_with_outbound_node(self, connected_node):
        print("node wants to disconnect with other outbound node: " + connected_node.id)

    def node_request_to_stop(self):
        print("node is requested to stop!")