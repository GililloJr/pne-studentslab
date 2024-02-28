from Seq1 import Seq

s = Seq()

filename = f"../sequences/.txt"
s.read_fasta(filename)

print("NULL Seq created")
print("Sequence : (Length: {}) {}".format(len(s.sequence), s.sequence))
print("  Bases:", s.bases)
print("  Rev:  ", s.sequence[::-1])
complement_dict = {'A': 'T', 'T': 'A', 'C': 'G', 'G': 'C'}
complement_seq = ''.join(complement_dict.get(base, base) for base in s.sequence)
print("  Comp: ", complement_seq)


