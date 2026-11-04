# Chat Application - SERVER (Beginner Tier)
# Oasis Infobyte - Python Programming Internship
#
# Run this file FIRST. It waits for two clients and passes
# messages between them.

import socket
import threading
from datetime import datetime

HOST = "127.0.0.1"   # localhost (same computer)
PORT = 5555
MAX_CLIENTS = 2

clients = {}                 # connection -> user name
clients_lock = threading.Lock()


def timestamp():
    """Returns the current time like [14:35]."""
    return datetime.now().strftime("[%H:%M]")


def send_line(conn, text):
    """Sends one message. A newline marks the end of every message."""
    try:
        conn.sendall((text + "\n").encode("utf-8"))
    except OSError:
        pass


def broadcast(text, sender=None):
    """Sends a message to everyone except the sender."""
    with clients_lock:
        for conn in list(clients):
            if conn is not sender:
                send_line(conn, text)


def handle_client(conn, address):
    """Runs in its own thread: one thread for each connected client."""
    name = None
    buffer = ""
    try:
        while True:
            data = conn.recv(1024)
            if not data:                      # client closed the connection
                break
            buffer += data.decode("utf-8")

            while "\n" in buffer:
                line, buffer = buffer.split("\n", 1)
                line = line.strip()
                if not line:
                    continue

                if name is None:              # the first message is the user name
                    name = line
                    with clients_lock:
                        clients[conn] = name
                    print(f"{timestamp()} {name} connected from {address}")
                    send_line(conn, f"Welcome {name}! Type 'quit' to leave.")
                    broadcast(f"{timestamp()} {name} joined the chat.", sender=conn)
                else:
                    message = f"{timestamp()} {name}: {line}"
                    print(message)
                    broadcast(message, sender=conn)
    except (ConnectionResetError, OSError):
        pass
    finally:
        with clients_lock:
            clients.pop(conn, None)
        conn.close()
        if name:
            print(f"{timestamp()} {name} disconnected")
            broadcast(f"{timestamp()} {name} has left the chat.")


def main():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server.bind((HOST, PORT))
    server.listen()
    print(f"Server started on {HOST}:{PORT}. Waiting for clients... (Ctrl+C to stop)")

    try:
        while True:
            conn, address = server.accept()
            with clients_lock:
                is_full = len(clients) >= MAX_CLIENTS
            if is_full:
                send_line(conn, "Sorry, the chat is full (only 2 users allowed).")
                conn.close()
                continue
            threading.Thread(target=handle_client, args=(conn, address), daemon=True).start()
    except KeyboardInterrupt:
        print("\nServer stopped.")
    finally:
        server.close()


if __name__ == "__main__":
    main()