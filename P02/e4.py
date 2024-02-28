from Client0 import Client
from Seq1 import Seq

PRACTICE = 2
EXERCISE = 4
print(f"-----| Practice {PRACTICE}, Exercise {EXERCISE} |------")

IP = "212.128.255.96"
PORT = 8081

c = Client(IP, PORT)
print(c)

print("Sending a message to the server...")
genes = ["ADA", "U5", "FRAT1"]

for gene in genes:
    filename = "../sequences/" + gene + ".txt"
    s = Seq()
    s.read_fasta(filename)
    message = f"Sending {gene} Gene to server... Sequence: {s.sequence}"
    response = c.talk(message)
    print(f"Response: {response}")


