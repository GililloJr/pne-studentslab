from Seq1 import Seq

sequences = [None, "ACTGA", "ERROR"]

for i, seq in enumerate(sequences):
    if seq is None:
        print("NULL sequence created")
    elif all(char in 'ACTG' for char in seq):
        print("New sequence created!")
    else:
        print("INVALID sequence!")
    print(f"Sequence {i}: (Length: {len(seq) if seq else 0}) {seq if seq else 'NULL'}")

    if seq:
        seq_obj = Seq(seq)
        counts = {base: seq_obj.count_base(base) for base in 'ACTG'}
        for base, count in counts.items():
            print(f"  {base}: {count},", end="")
        print()



