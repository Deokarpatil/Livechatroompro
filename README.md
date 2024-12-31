# Livechatroompro
## Title: Multiclient Chat Application With SocketProgramming
## Name Of Team Member's :
 * Pawar Pruthviraj Dnyaneshwar
 * Deokar Vedant Rajendra
 * Gandhale Omkar Bhausaheb
 * Ratnaparkhi Nandini Shivaji

## Description:
  The Multiclient Chat Application Project is a multi-user communication system built using Python's socket programming. It allows multiple clients to connect to a central server, send and receive messages, and interact in real time. The server manages all the client connections and facilitates message broadcasting. The project demonstrates the use of sockets, threading, and synchronization in Python, providing a scalable and interactive chatroom solution.
## Key Features:
* 1.Real-Time Chat: Multiple clients can join the chatroom and exchange messages 
 simultaneously.
* 2.Broadcast Messaging: Messages from one client are relayed to all other connected 
 clients.
* 3.Message Tracking: Each message is assigned a unique ID for potential extensions like 
 editing or deleting messages.
* 4.Thread-Safe Operations: Uses threading locks to manage shared resources, avoiding 
 conflicts in a multi-threaded environment.
* 5.This project provides a solid foundation for learning socket programming and can be 
 scaled up with additional features.
## Why you select this project:
The above program was selected because it provides a comprehensive example of a real-world application of Python socket programming.
* 1. Educational Value: Multi-Threading: It showcases threading to handle multiple clients concurrently, which is essential in real-time applications.
* 2. Real-World Application: Interactive Communication: A multiclient chatapplication is a tangible and relatable project that simulates real-world applications.
* 3. Scalability and Flexibility: The code can be easily extended or modified to include
Advanced Features like message encryption, user authentication, or file sharing.
* 4. Challenges and Problem-Solving: This program teaches developers to Handle Connection Issues
## Is it Created from Scratch by Team or AI?
   We took reference from a project and added some features like multiclient interface, message reverting.
## Used Any Ready Project ?
   Yes, we used a client server project which was able to handle single client.
## Objective:
  Create a real-time chat system for multiple users connected to a server.
## Technologies Used:
* Programming Language: Python
* Socket Programming: For communication
* Threads: To handle multiple clients simultaneously
## Features:
* Multiple clients can join the chat.
* Server broadcasts messages to all connected clients.
* Each client can send and receive messages in real time.
## How It Works:
* 1.A server application runs to manage connections and messages.
* 2.Clients connect to the server using sockets.
* 3.Messages are exchanged between clients via the server.
  
## Challenges with their solution:
* 1.Handling Multiple Clients Simultaneously
  
Challenge: The original code only had a basic client-server setup, where one client could connect and interact with the server. However, if multiple clients attempted to connect at once, the server wouldn't be able to handle multiple connections concurrently, potentially causing delays or disconnections.

Solution: This was addressed by using the threading module in both the client and server. Each time a client connects to the server, a new thread is spawned to handle that client. This allows the server to communicate with multiple clients simultaneously without blocking.

* 2.Message Parsing and Protocols
  
Challenge: In the initial code, messages were sent in raw text format, without a clear structure. This made it difficult to differentiate between types of messages or handle special cases like private messaging or system messages.

Solution: The solution was to introduce structured messages using a simple delimiter (:) to separate the message_id from the actual content of the message. This allowed the server and client to differentiate between different types of information.

* 3.Graceful Handling of Client Disconnection
  
Challenge: The client and server had limited error handling, especially around disconnections. If a client unexpectedly closed its connection, the server or other clients could be left hanging or might not handle the error gracefully.

Solution: In the updated code, I implemented a try-except block for both sending and receiving messages, which helps gracefully handle errors when clients disconnect. The server also checks for empty messages (i.e., a closed connection) and exits the connection properly.

* 4.Sending and Receiving Messages Concurrently
  
Challenge: The client needs to both send and receive messages simultaneously without blocking on either task. Without concurrency, the client would either wait to send messages or wait to receive messages, but not both at the same time.

Solution: This was addressed by using threading. A separate thread is dedicated to receiving messages from the server, and another thread handles sending messages to the server. This way, the client is free to listen for incoming messages while typing and sending its own messages concurrently.

* 5.Server Message Broadcasting
  
Challenge: The server in the initial code was simply receiving and sending messages to the client, but it did not have the capability to broadcast messages to multiple clients simultaneously.

Solution: The solution here involves broadcasting messages to all connected clients. The server stores a list of connected clients, and when a new message is received, it sends the message to all clients in the list.

## Output
 ### Server Screen 
 ### 
![WhatsApp Image 2024-12-31 at 10 17 55 PM](https://github.com/user-attachments/assets/7cc3ca3d-fff9-448e-b0ea-f605b09909a6)
## Client: Omkar
![image](https://github.com/user-attachments/assets/31865360-a27b-4822-ba52-e7b0394c25f0)
### Deleted the Msg "Id3:How are you" by omkar
## Client: Vedant
![WhatsApp Image 2024-12-31 at 10 21 53 PM](https://github.com/user-attachments/assets/0f33e7ad-42cb-4b44-92ea-e5367abb1575)
## It shows the message "Id3 How are you"deleted by omkar
## client: Vedant
![WhatsApp Image 2024-12-31 at 10 21 53 PM (1)](https://github.com/user-attachments/assets/738b4f99-3a5e-44f1-b341-83e38daf6089)
## Client vedant "leaved" the chat room and Relogin to Chatroom and display all "Previous" chat in Chatroom.
## Client: Omkar
![image](https://github.com/user-attachments/assets/d8ff1ca9-ecd7-4240-aec1-75c1bf5a3c2d)
## Client omkar Notify that vedant rejoin the chat.






