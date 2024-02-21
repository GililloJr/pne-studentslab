from Seq1 import Seq

sequence_list = [Seq(None), Seq("ACTGA"), Seq("ERROR")]

for i, seq in enumerate(sequence_list):
    if seq.seq is None:
        print("NULL sequence created")
        print(f"Sequence {i}: (Length: 0) NULL")
    elif all(char in 'ACTG' for char in seq.seq):
        print("New sequence created!")
        print(f"Sequence {i}: (Length: {len(seq.seq)}) {seq.seq}")
    else:
        print("INVALID sequence!")
        print(f"Sequence {i}: (Length: {len(seq.seq)}) {seq.seq}")

    counts = seq.count()
    print("  Bases:", counts)



