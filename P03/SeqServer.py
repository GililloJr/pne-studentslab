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