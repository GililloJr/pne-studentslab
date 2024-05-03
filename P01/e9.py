from Seq1 import Seq

s = Seq()

# Call read_fasta method with the file path
s.read_fasta("../sequences/U5.txt")
sequences = [s]
for i, seq in enumerate(sequences):
    print(f"Sequence {i}: (Length: {seq.len()}) {seq}")
    counts = {base: seq.count_base(base) for base in ['A', 'C', 'T', 'G']}
    print(f"  Bases: {counts}")
    print(f"  Rev: {seq.reverse()}")
    print(f"  Comp: {seq.complement()}")



