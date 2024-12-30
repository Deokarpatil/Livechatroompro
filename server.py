import socket
import threading

# List to hold all client sockets
clients = []

# Function to handle communication with clients
def handle_client(client_socket, client_address):
    print(f"[NEW CONNECTION] {client_address} connected.")

    # Welcome message to the client
    client_socket.send("Welcome to the chat! Type 'exit' to leave.".encode())

    # Broadcast function to send messages to all connected clients
    def broadcast_message(message, client_socket):
        for client in clients:
            if client != client_socket:  # Don't send the message back to the sender
                try:
                    client.send(message)
                except:
                    client.close()
                    clients.remove(client)

    # Receive and handle messages from the client
    while True:
        try:
            message = client_socket.recv(1024)
            if not message:  # If client disconnects
                break

            # If client types 'exit', close the connection
            if message.decode().lower() == 'exit':
                print(f"[DISCONNECTED] {client_address} has disconnected.")
                client_socket.send("You have left the chat.".encode())
                break

            print(f"[{client_address}] {message.decode()}")
            broadcast_message(message, client_socket)  # Broadcast the message to others

        except Exception as e:
            print(f"[ERROR] {e}")
            break

    # Close client connection
    clients.remove(client_socket)
    client_socket.close()

# Function to start the server and accept connections
def start_server():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(("0.0.0.0", 5555))  # Bind to all IPs on port 5555
    server.listen(5)  # Max number of clients the server can handle simultaneously
    print("Server started. Listening on port 5555...")

    while True:
        # Accept a new client connection
        client_socket, client_address = server.accept()
        clients.append(client_socket)  # Add client socket to list
        # Start a new thread for handling the client
        client_thread = threading.Thread(target=handle_client, args=(client_socket, client_address))
        client_thread.start()

if __name__ == "__main__":
    start_server()
