from Client0 import Client
PRACTICE = 2
EXERCISE = 3
print(f"-----| Practice {PRACTICE}, Exercise {EXERCISE} |------")
IP = "192.168.0.1"
PORT = 8081
c = Client(IP, PORT)
print(c)

print("Sending a message to the server...")
response = c.talk("que viene de fabrica aaaabbbeeeee")
print(f"Response: {response}")



from Client0 import Client
from Seq1 import Seq

PRACTICE = 2
EXERCISE = 6
print(f"-----| Practice {PRACTICE}, Exercise {EXERCISE} |------")

IP = "192.168.1.45"  # Assuming this is the correct server IP
PORT = 8080
print(f"Connection to SERVER at {IP}, PORT: {PORT}")
c = Client(IP, PORT)
print(c)

filename = "../sequences/FRAT1.txt"
s = Seq()
gene = s.read_fasta(filename)

print("NULL Seq created")
fragments = [gene.sequence[i:i+10] for i in range(0, 50, 10)]


# Send the fragments to the server
for i, fragment in enumerate(fragments, 1):
    print(f"Fragment {i}: {fragment}")
    response = c.talk(fragment)
    print(f"Server response: {response}")