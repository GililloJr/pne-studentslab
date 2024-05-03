from Seq1 import Seq

s1 = Seq("")
s2 = Seq("ACTGA")
s3 = Seq("Invalid sequence")

sequences = [s1, s2, s3]
for i, seq in enumerate(sequences):
    print(f"Sequence {i}: (Length: {seq.len()}) {seq}")
    counts = {base: seq.count_base(base) for base in ['A', 'C', 'T', 'G']}
    print(f"  Bases: {counts}")





