import socket
import random

class NumberGuesser:
    def __init__(self):
        self.secret_number = random.randint(1, 100)
        self.attempts = []

    def guess(self, number):
        self.attempts.append(number)
        if number == self.secret_number:
            return f'You won after {len(self.attempts)} attempts'
        elif number < self.secret_number:
            return 'Higher'
        else:
            return 'Lower'

    def __init__(self):
        self.PORT = 8081
        self.IP = "127.0.0.1"
        self.ls = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.ls.bind((self.IP, self.PORT))
        self.ls.listen()
        print("SEQ server is configured!")

        try:
            while True:
                print("Waiting for clients to connect")
                (rs, address) = self.ls.accept()
                msg = rs.recv(2048).decode("utf-8")
                response = self.response(str(msg))
                send_bytes = str.encode(response)
                rs.send(send_bytes)
                rs.close()
        except KeyboardInterrupt:
            print("These clients have connected to the server:")

        self.ls.close()

