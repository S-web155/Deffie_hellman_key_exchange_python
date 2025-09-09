import socket
import random

def setup_server_socket(host, port):
    # Create a socket object
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


    server_socket.bind((host, port))

# Listen for incoming connections
    server_socket.listen(1)
    print(f"Server listening on {host}:{port}...")

# Accept a connection
    conn, addr = server_socket.accept()
    print(f"Connection from {addr} established.")


    p = 23
    g = random.randint(1, 9)
    a = random.randint(1, p-2)
    Al = (g**a)%p
    conn.send(f"{p}, {g}, {Al}".encode())
# Receive data
    data = conn.recv(1024).decode()
    Bo = int(data)
    shared = (Bo**a)%p


# Send response
    
# Close connection
    conn.close()
    return shared
