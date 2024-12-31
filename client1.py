import socket
import threading

class ChatClient:
    def __init__(self, server_ip='localhost', server_port=5555):
        """Initialize the client with server IP and port."""
        self.server_ip = server_ip
        self.server_port = server_port
        self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.username = None

    def connect_to_server(self):
        """Connect the client to the server."""
        try:
            self.client_socket.connect((self.server_ip, self.server_port))
            print(f"Connected to server {self.server_ip}:{self.server_port}")
        except Exception as e:
            print(f"Error connecting to server: {e}")
            exit(1)

    def receive_messages(self):
        """Handles receiving messages from the server."""
        while True:
            try:
                data = self.client_socket.recv(1024).decode('utf-8')
                if not data:
                    break  # Connection closed
                message_id, message = data.split(":", 1)  # Extract message_id and the message
                print(f"Message ID {message_id}: {message}")
            except Exception as e:
                print(f"Error receiving message: {e}")
                break

    def send_message(self):
        """Handles sending messages to the server."""
        while True:
            message = input(f"{self.username}: ")  # User types a message
            if message:
                try:
                    self.client_socket.send(message.encode('utf-8'))  # Send to server
                except Exception as e:
                    print(f"Error sending message: {e}")
                    break

    def start_chat(self):
        """Starts the chat by requesting a username and then starting threads for receiving and sending messages."""
        try:
            # Receive welcome message and username request from server
            welcome_message = self.client_socket.recv(1024).decode('utf-8')
            print(welcome_message)

            # Ask the user for their username and send it to the server
            self.username = input("Enter your username: ")
            self.client_socket.send(self.username.encode('utf-8'))

            # Start threads to handle receiving and sending messages
            threading.Thread(target=self.receive_messages, args=()).start()
            threading.Thread(target=self.send_message, args=()).start()
        except Exception as e:
            print(f"Error starting chat: {e}")
            exit(1)

def start_client():
    """Initialize the ChatClient and start the chat."""
    client = ChatClient()
    client.connect_to_server()
    client.start_chat()

if __name__ == "__main__":
    start_client()
