import socket
import random


# Create a socket object
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect to the server
host = '127.0.0.1'  # Server IP
port = 12345
client_socket.connect((host, port))

# Receive response
response = client_socket.recv(1024).decode()
p, g, Al= map(int, response.split(','))
print(f"Server says: {p}, {g}, {Al}")
b = random.randint(1, p-2)
Bo = (g**b)%p
shared_secret = (Al**b)%p
print(shared_secret)


# Send message
client_socket.send(f"{Bo}".encode())


# Close connection
client_socket.close()

