from Seq1 import Seq

s = Seq()

# Call read_fasta method with the file path
s.read_fasta("../sequences/U5.txt")

print("NULL Seq created")
print("Sequence : (Length: {}) {}".format(len(s.sequence), s.sequence))
print("  Bases:", s.bases)
print("  Rev:  ", s.reverse())
complement_dict = {'A': 'T', 'T': 'A', 'C': 'G', 'G': 'C'}
complement_seq = ''.join(complement_dict.get(base, base) for base in s.sequence)
print("  Comp: ", s.complement())



