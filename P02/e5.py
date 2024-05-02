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
seq = s.read_fasta(filename)

print("NULL Seq created")
print("Gene FRAT1:", seq)

fragments = []

for i in range(0, len(seq) - 9):  # Ensure the loop doesn't go out of bounds
    fragment = seq[i:i+10]
    fragments.append(fragment)

for i, fragment in enumerate(fragments[:5], 1):  # Loop over first 5 fragments
    msg = f"Fragment {i}: {fragment}"
    print(msg)
    print(c.talk(msg))




