from Client0 import Client
from Seq1 import Seq

PRACTICE = 2
EXERCISE = 5
print(f"-----| Practice {PRACTICE}, Exercise {EXERCISE} |------")

IP = "212.128.255.104"  # Corrected IP address
PORT = 8081  # Corrected PORT number
c = Client(IP, PORT)
print(c)
filename = "../sequences/FRAT1.txt"
s = Seq()
seq = s.read_fasta(filename)  # Corrected method call

print("NULL Seq created")
print("Gene FRAT1:", seq)  # Corrected accessing the sequence

fragments = []

for i in range(0, len(seq) - 9):  # Adjusted the loop for generating fragments
    fragment = seq[i:i+10]
    fragments.append(fragment)

for i, fragment in enumerate(fragments[:5], 1):  # Loop over first 5 fragments
    msg = f"Fragment {i}: {fragment}"
    print(msg)
    print(c.talk(msg))  # Sending fragment message to the server



