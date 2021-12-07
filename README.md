# Massive Whiteboard
Software Development Final Project
Elijah Ahlstrom and Bonheur Shyaka

###P2PNode.py
Handles the peer to peer connections

**Node_callback(event, main_node, connected_node, data)**
If the event is not a request to stop, prints the event, main and connected nodes, and any recieved data

**P2PNode(Node)**
Extends the node class from the p2pnetwork module. Allows for the programs to have a peer to peer connection with each other, and save their images to be applied to the connected program.

**__init__(host, port, image, id=None, callback=None, max_connections=0)**
Takes in a host(string), port(int), image(QImage), id(string), callback(string), and max_connections(int) to make a P2PNode.

**outbound_node_connected(connected_node)**
Is called when the current node initialises a connection with another node. prints the other node's ID in the console.

**inbound_node_connected(connected_node)**
Is called when another node initialises a connection with the current one. Prints the other node's ID.

**outbound_node_disconnected(connected_node)**
Is called when the current node disconnects with another node. Prints the other node's ID.

**inbound_node_disconnected(connected_node)**
Is called when a connected node disconnects with the current node. Print's the other node's ID.

**node_message(connected_node, data)**
Is called when a connected node sends a message to this one. Prints the other node's ID and its message.

**node_request_to_stop()**
Is called when the node is requested to stop, whether from within the program or from another connection. Prints the request to stop.


###QtPaint.py
Generated from QtPaintLayout.ui. Generates the GUI in python. Do not edit.

###Window.py
Includes Main. Allows the user to draw on a blank image, and connect to another user so multiple users can draw on the same canvas.

**__init__(self, host='localhost', port=5000)**
Initialises the Window. Defaults the host and port to localhost:5000, though different strings and ints can be passed into host and port, respectively.

**mousePressEvent(event)**
Called on an event, if it's a left click, starts drawing at the mouse cursor

**mouseMoveEvent(event)**
Called on an event, if it's the mouse moving, checks if the left mouse button is also being pressed. If so, draws with the currently selected color and size.

**mouseReleaseEvent(event)**
Called on an event, if it's the left button being released, stops drawing.

**drawUpdate(event)**
Updates the drawing based on what the other node sends. e.g. If one user draws a line, the same line will appear on the other program

**makeJson()**
Makes a json dictionary based on the last drawn point, selected color, and size. This is then sent to any connected nodes

**jsonPaint(json_dict)**
Takes a json dictionary made by makeJson() to draw given the point, color, and size within the dictionary

**updateClient(json_dict=None)**
Calls jsonPaint with the given json_dict. should be called when a connected user updates their drawing

**updatePeers()**
Sends a json dictionary, made by makeJson, to update the drawings of connected users.

**save()**
Saves the image

**SmallSize()**
**MediumSize()**
**LargeSize()**
Changes the brush size to 4, 7, and 10 pixels, respectively

**blackB()**
**whiteB()**
**redB()**
**greenB()**
**blueB()**
Changes the brush color to the given image, based on Qt's colors (e.g. Qt.black)

**manageConnections()**
Called when the user clicks the manage connections button. Pops up a prompt requesting an IP to connect to, then attempts to connect to the node at the given IP and port.