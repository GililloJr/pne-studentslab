import socket

# Configure the Server's IP and PORT
PORT = 8081
IP = "212.128.255.104" # it depends on the machine the server is running
MAX_OPEN_REQUESTS = 5

# Counting the number of connections
number_con = 0

# create an INET, STREAMing socket
serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
try:
    serversocket.bind((IP, PORT))
    # become a server socket
    # MAX_OPEN_REQUESTS connect requests before refusing outside connections
    serversocket.listen(MAX_OPEN_REQUESTS)

    while True:
        # accept connections from outside
        print("Waiting for connections at {}, {} ".format(IP, PORT))
        (clientsocket, address) = serversocket.accept()

        # Another connection!e
        number_con += 1

        # Print the connection number
        print("CONNECTION: {}. From the IP: {}".format(number_con, address))

        # Read the message from the client, if any
        msg = clientsocket.recv(2048).decode("utf-8")
        print("Message from client: {}".format(msg))

        # Send the message
        message = "Hello from gilillo's server\n"
        send_bytes = str.encode(message)
        # We must write bytes, not a string
        clientsocket.send(send_bytes)
        clientsocket.close()

except socket.error:
    print("Problems using ip {} port {}. Is the IP correct? Do you have port permission?".format(IP, PORT))

except KeyboardInterrupt:
    print("Server stopped by the user")
    serversocket.close()




import socket
import termcolor

class SeqServer:
    def __init__(self):
        self.PORT = 8080
        self.IP = "127.0.0.1"

        ls = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        ls.bind((self.IP, self.PORT))

        ls.listen()
        print("SEQ server is configured!")

        try:
            while True:
                print("Waiting for clients to connect")
                (rs, address) = ls.accept()
                print("A client has connected to the server!")
                msg = rs.recv(2048).decode("utf-8")

                if msg.strip() == "PING":
                    termcolor.cprint("PING COMMAND", 'green')
                    new_msg = "OK!\n"
                    rs.send(new_msg.encode())
                    rs.close()
                else:
                    termcolor.cprint(msg, 'green')
        except KeyboardInterrupt:
            print("These clients have connected to the server:")
        finally:
            # -- Close the socket
            ls.close()

server = SeqServer()
print(server)


def return_response(self, msg):
    def ping_response(self, msg):
        if msg != "PING":
            return "PING ERROR: Unexpected extra information"