import socket
import termcolor
from Seq1 import Seq

class SeqServer:
    def __init__(self):
        self.PORT = 8084
        self.IP = "127.0.0.1"

        self.ls = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        self.ls.bind((self.IP, self.PORT))

        self.ls.listen()
        print("SEQ server is configured!")

        try:
            while True:
                print("Waiting for clients to connect")
                (rs, address) = self.ls.accept()
                print("A client has connected to the server!")
                msg = rs.recv(2048).decode("utf-8")

                if msg.strip() == "PING":
                    termcolor.cprint("PING COMMAND", 'green')
                    new_msg = "OK!\n"
                    rs.send(new_msg.encode())
                    rs.close()
                elif msg.strip().startswith("GET"):
                    termcolor.cprint("GET", 'green')
                    response = self.get_response(msg)
                    rs.send(response.encode())
                    rs.close()
                else:
                    termcolor.cprint(msg, 'green')
        except KeyboardInterrupt:
            print("These clients have connected to the server:")
        finally:
                self.ls.close()


    def return_response(self, msg):
        if msg.startswith("PING"):
            print("PING")
            return self.ping_response()
        if msg.startswith("GET"):
            print("GET")
            return self.get_response(msg)
    def ping_response(self):
        print("PING COMMAND")
        return "OK!\n"

    def get_response(self, msg):
        sequences = ["ATGCAGWA", "ATGGTCCG", "TGCAGTGT", "TTGACCTA"]
        for j in msg:
            if j.isdigit():
                if 0 <= int(j) <= 3:
                    b = sequences[int(j)]
                    print(b)
                    return b + "\n"
                else:
                    return "Not valid command"

    def info_response(self, msg):
        sequence = Seq(msg.replace("INFO", "").strip())
        seq_obj = Seq(sequence)
        info =
        return info

server = SeqServer()


