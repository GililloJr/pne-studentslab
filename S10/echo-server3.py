import socket

# Configure the Server's IP and PORT
PORT = 8081
IP = "212.128.255.104" # this IP address is local, so only requests from the same machine are possible
number_con = 0
# -- Step 1: create the socket
ls = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# -- Step 2: Bind the socket to server's IP and PORT
ls.bind((IP, PORT))

# -- Step 3: Configure the socket for listening
ls.listen()

print("The server is configured!")

client = []

try:
    while True:
        print("Waiting for clients to connect")
        (rs, address) = ls.accept()
        print("A client has connected to the server!")

        number_con += 1
        print("CONNECTION: {}. Client IP, PORT: {}".format(number_con, address))
        client.append(f"Client {number_con - 1}: {address}")

        msg = rs.recv(2048).decode("utf-8")
        import termcolor
        print(f"Message received: {termcolor.cprint(msg, 'green')}")

        new_msg = f"ECHO: {msg}\n"
        rs.send(new_msg.encode())
        rs.close()
except KeyboardInterrupt:
    print("These clients have connected to the server:")
    for j in client:
        print(j)
# -- Close the socket
ls.close()

