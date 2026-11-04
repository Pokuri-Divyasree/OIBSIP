# Chat Application (Python)

A simple real-time chat between two users in the command line, built with Python sockets and threads.
Created as part of the Oasis Infobyte Python Programming Internship (Task 5, Beginner Tier).

## Features
- Server script that listens for incoming client connections
- Client script that connects to the server
- Real-time two-way messages between two connected clients
- Every message has a timestamp, example: `[14:35] Alice: Hello`
- When one user leaves, the other user is notified
- Runs on one computer using localhost (127.0.0.1)

## Requirements
- Python 3.x (no extra libraries needed)

## How to Run
1. Open a terminal in this folder and start the server:
   `python server.py`
2. Open a second terminal and start the first client:
   `python client.py`
3. Open a third terminal and start the second client:
   `python client.py`
4. Enter a name in each client window and start chatting.
5. Type `quit` to leave the chat.

## Example Output

Alice's window:
```
Enter your name: Alice
Welcome Alice! Type 'quit' to leave.
[14:35] Bob joined the chat.
Hello Bob
[14:35] You: Hello Bob
[14:36] Bob: Hi Alice!
[14:37] Bob has left the chat.
```

## How It Works
- `socket` creates the network connection between server and clients.
- `threading` lets the server handle each client at the same time, and lets each client
  send and receive at the same time.
- Every message ends with a new line, so the receiver knows where one message stops.

## Limitations
- Only 2 users are allowed at one time.
- Messages are not encrypted and not saved.
- Works only on the same computer (localhost).

## Tech Used
- Python 3
- `socket`, `threading`, `datetime` modules

## Author
Pokuri Divya Sumana Sree
Oasis Infobyte - Python Programming Internship