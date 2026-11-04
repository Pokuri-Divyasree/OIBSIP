# Chat Application - CLIENT (Beginner Tier)
# Oasis Infobyte - Python Programming Internship
#
# Run this file in a separate terminal for each user.

import os
import socket
import threading
from datetime import datetime

HOST = "127.0.0.1"
PORT = 5555


def timestamp():
    return datetime.now().strftime("[%H:%M]")


def receive_messages(sock):
    """Runs in a background thread and prints every message from the server."""
    buffer = ""
    while True:
        try:
            data = sock.recv(1024)
        except OSError:
            break
        if not data:
            break
        buffer += data.decode("utf-8")
        while "\n" in buffer:
            line, buffer = buffer.split("\n", 1)
            if line:
                print(f"\r{line}")

    print("\nDisconnected from the server.")
    os._exit(0)          # stop the program (the main thread may be waiting for input)


def main():
    name = ""
    while not name:
        name = input("Enter your name: ").strip()

    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        sock.connect((HOST, PORT))
    except ConnectionRefusedError:
        print("Could not connect. Start server.py first, then run this file again.")
        return

    sock.sendall((name + "\n").encode("utf-8"))
    threading.Thread(target=receive_messages, args=(sock,), daemon=True).start()

    try:
        while True:
            text = input()
            if text.strip().lower() == "quit":
                break
            if text.strip():
                sock.sendall((text + "\n").encode("utf-8"))
                print(f"{timestamp()} You: {text}")
    except (EOFError, KeyboardInterrupt):
        pass
    finally:
        sock.close()
        print("You left the chat. Bye!")


if __name__ == "__main__":
    main()