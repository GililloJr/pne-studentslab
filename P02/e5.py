from Client0 import Client
from Seq1 import Seq

PRACTICE = 2
EXERCISE = 6
print(f"-----| Practice {PRACTICE}, Exercise {EXERCISE} |------")

IP = "212.128.255.64"
PORT = 8081
c = Client(IP, PORT)
print(c)
filename = "../sequences/FRAT1.txt"
s = Seq()
s.read_fasta(filename)

print("NULL Seq created")
print("Gene FRAT1:", s.sequence)

fragments = [s.sequence[i:i+10] for i in range(0, len(s.sequence), 10)]

for i, fragment in enumerate(fragments, start=1):
    print(f"Fragment {i}: {fragment}")
    message = f"Fragment {i}: {fragment}"
    response = c.talk(message)
    print(f"Response: {response}")

