from Client0 import Client
PRACTICE = 2
EXERCISE = 3
print(f"-----| Practice {PRACTICE}, Exercise {EXERCISE} |------")
IP = "212.128.255.64"
PORT = 8081
c = Client(IP, PORT)
print(c)

print("Sending a message to the server...")
response = c.talk("que viene de fabrica aaaabbbeeeee")
print(f"Response: {response}")

