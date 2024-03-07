from Seq1 import Seq

sequences = [None, "ACTGA", "ERROR"]

for i, seq in enumerate(sequences):
    if seq is None:
        print("NULL sequence created")
        seq_length = 0
        bases_count = {'A': 0, 'T': 0, 'C': 0, 'G': 0}
        reverse_seq = "NULL"
    elif seq == "ERROR":
        print("INVALID sequence!")
        seq_instance = Seq(seq)
        seq_length = len(seq_instance.sequence)
        bases_count = seq_instance.count()
        reverse_seq = seq_instance.reverse()
    else:
        print("New sequence created!")
        seq_instance = Seq(seq)
        seq_length = len(seq_instance.sequence)
        bases_count = seq_instance.count()
        reverse_seq = seq_instance.reverse()

    print(f"Sequence {i}: (Length: {seq_length}) {'NULL' if seq is None else seq}")
    print("  Bases:", bases_count)
    print("  Rev:  ", reverse_seq)

