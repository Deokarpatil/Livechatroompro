import socket
import threading

class ChatServer:
    def __init__(self, host='0.0.0.0', port=5555):
        """Initialize the chat server with the given host and port."""
        self.host = host
        self.port = port
        self.clients = []  # List to keep track of connected clients
        self.messages = []  # List to store all messages with their IDs
        self.message_id_counter = 1  # Message ID counter

        # Initialize the server socket
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server_socket.bind((self.host, self.port))
        self.server_socket.listen(5)
        print(f"Server started on {self.host}:{self.port}")

    def broadcast(self, message, client_socket, message_id=None):
        """Sends a message to all clients except the sender."""
        for client in self.clients:
            if client != client_socket:
                try:
                    # Include message ID for tracking and deleting messages
                    client.send(f"{message_id}:{message}".encode('utf-8'))
                except Exception as e:
                    print(f"Error broadcasting message: {e}")
                    client.close()
                    self.clients.remove(client)

    def handle_client(self, client_socket):
        """Handles communication with a connected client."""
        global message_id_counter
        
        try:
            # Send welcome message to the client
            client_socket.send("Welcome to the chat server! Please enter your username: ".encode('utf-8'))

            # Receive username
            username = client_socket.recv(1024).decode('utf-8')
            print(f"{username} has joined the chat.")

            # Broadcast that the user has joined
            self.broadcast(f"{username} has joined the chat.", client_socket, None)

            # Send all previous messages to the client
            for message_id, message in self.messages:
                client_socket.send(f"{message_id}:{message}".encode('utf-8'))

            while True:
                message = client_socket.recv(1024).decode('utf-8')  # Receive a message from the client

                if not message:
                    break  # Client has disconnected

                if message.startswith("/delete"):
                    # Delete command format: /delete <message_id>
                    try:
                        delete_message_id = int(message.split(" ")[1])
                        # Remove the message from the list
                        self.messages = [msg for msg in self.messages if msg[0] != delete_message_id]
                        print(f"Message ID {delete_message_id} deleted.")

                        # Notify all clients that the message was deleted
                        self.broadcast(f"Message ID {delete_message_id} has been deleted.", client_socket, None)
                    except ValueError:
                        client_socket.send("Invalid message ID for deletion.".encode('utf-8'))
                else:
                    # New message: add it to the list and broadcast it
                    message_id = self.message_id_counter
                    self.messages.append((message_id, message))
                    self.message_id_counter += 1
                    print(f"{username}: {message}")
                    self.broadcast(f"{username}: {message}", client_socket, message_id)

        except Exception as e:
            print(f"Error handling client: {e}")
        finally:
            # Remove the client from the list and close the connection
            self.clients.remove(client_socket)
            client_socket.close()
            print(f"Client {client_socket} disconnected.")

    def start_server(self):
        """Accepts incoming client connections and handles them."""
        while True:
            client_socket, client_address = self.server_socket.accept()
            print(f"New connection from {client_address}")
            self.clients.append(client_socket)
            # Create a new thread to handle the client
            threading.Thread(target=self.handle_client, args=(client_socket,)).start()

if __name__ == "__main__":
    chat_server = ChatServer()
    chat_server.start_server()
