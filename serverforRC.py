#!/usr/bin/env python
from socket import *
from time import ctime          # Import necessary modules   

ctrl_cmd = ['forward', 'backward', 'left', 'right', 'stop', 'read cpu_temp', 'home', 'distance', 'x+', 'x-', 'y+', 'y-', 'xy_home']

HOST = ''           # The variable of HOST is null, so the function bind( ) can be bound to all valid addresses.
PORT = 21567
BUFSIZ = 1024       # Size of the buffer
ADDR = (HOST, PORT)

tcpSerSock = socket(AF_INET, SOCK_STREAM)    # Create a socket.
tcpSerSock.bind(ADDR)    # Bind the IP address and port number of the server. 
tcpSerSock.listen(5)     # The parameter of listen() defines the number of connections permitted at one time. Once the 
                         # connections are full, others will be rejected. 

while True:
	print('Waiting for connection...')
	# Waiting for connection. Once receiving a connection, the function accept() returns a separate 
	# client socket for the subsequent communication. By default, the function accept() is a blocking 
	# one, which means it is suspended before the connection comes.
	tcpCliSock, addr = tcpSerSock.accept() 
	print('...connected from :', addr)     # Print the IP address of the client connected with the server.

	while True:
		data = ''
		data = tcpCliSock.recv(BUFSIZ)    # Receive data sent from the client. 
		# Analyze the command received and control the car accordingly.
		if not data:
			break
		if data == ctrl_cmd[0]:
			print('motor moving forward')
		elif data == ctrl_cmd[1]:
			print('recv backward cmd')
		elif data == ctrl_cmd[2]:
			print('recv left cmd')
		elif data == ctrl_cmd[3]:
			print('recv right cmd')
		else:
			print('Command Error! Cannot recognize command: ' + str(data))

tcpSerSock.close()



