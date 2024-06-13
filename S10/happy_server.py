import socket

# Configure the Server's IP and PORT
PORT = 8081
IP = "127.0.0.1" # this IP address is local, so only requests from the same machine are possible

# -- Step 1: create the socket
ls = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# -- Step 2: Bind the socket to server's IP and PORT
ls.bind((IP, PORT))

# -- Step 3: Configure the socket for listening
ls.listen()

print("The server is configured!")

while True:
    (rs, address) = ls.accept()

    print(f"Client {address}")

    msg = rs.recv(2048).decode("utf-8")

    print("The client says ..." + msg)
    new_msg = "I am a happy server"
    rs.send(new_msg.encode())
    rs.close()
# -- Close the socket
ls.close()
