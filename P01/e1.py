class Seq:
    def __init__(self, seq):
        self.seq = seq

def sequence_length():

    sequence = Seq("ACTGA")
    print("New sequence created!")
    print(f"Sequence 1: (Length: {len(sequence.seq)}) {sequence.seq}")

print(sequence_length())


class Seq:
    def __init__(self, sequence):
        self.sequence = sequence if sequence else ""