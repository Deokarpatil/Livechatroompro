import socket
import threading

# Function to receive messages from the server
def receive_messages(client_socket):
    while True:
        try:
            message = client_socket.recv(1024).decode()  # Receive message from server
            if message:
                print(f"\n{message}")  # Display the received message
        except:
            print("[ERROR] Connection lost.")
            break

# Function to send messages to the server
def send_messages(client_socket):
    while True:
        message = input()  # Read input from the user
        if message.lower() == 'exit':
            client_socket.send(message.encode())  # Send 'exit' to server
            client_socket.close()
            break
        client_socket.send(message.encode())  # Send the message to server

def start_client():
    server_ip = input("Enter the server IP address: ")  # Ask user for the server IP
    server_port = 5555  # Port number to connect to

    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # Create socket
    try:
        client_socket.connect((server_ip, server_port))  # Connect to the server
        print("Connected to the server. You can start chatting!")

        # Start threads for sending and receiving messages
        receive_thread = threading.Thread(target=receive_messages, args=(client_socket,))
        receive_thread.start()
        send_thread = threading.Thread(target=send_messages, args=(client_socket,))
        send_thread.start()

    except Exception as e:
        print(f"[ERROR] Unable to connect to the server: {e}")

if __name__ == "__main__":
    start_client()
