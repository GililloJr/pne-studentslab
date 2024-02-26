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

for i, seq in enumerate(sequences):
    seq_instance = Seq(seq)
    print(f"Sequence {i}: (Length: {len(seq_instance.sequence)}) {'NULL' if not seq_instance.sequence else seq_instance.sequence}")
    counts = {base: seq_instance.count_base(base) for base in 'ACTG'}
    print("  " + ", ".join([f"{base}: {counts[base]}" for base in 'ACTG']))




