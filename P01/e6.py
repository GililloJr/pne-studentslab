from Seq1 import Seq

sequences = [None, "ACTGA", "ERROR"]

for i, seq in enumerate(sequences):
    if seq is None:
        print("NULL sequence created")
        seq_instance = Seq("")
    elif seq == "ERROR":
        print("INVALID sequence!")
        seq_instance = Seq(seq)
    else:
        print("New sequence created!")
        seq_instance = Seq(seq)

    if seq_instance.sequence:
        print(f"Sequence {i}: (Length: {len(seq_instance.sequence)}) {seq_instance.sequence}")
        print("  Bases:", seq_instance.count())
    else:
        print(f"Sequence {i}: (Length: 0) NULL")







