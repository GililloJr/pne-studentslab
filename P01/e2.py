class Sequence:
    def __init__(self, seq):
        self.seq = seq

def type_of_sequences():

    null_sequence = Sequence("NULL")
    print("NULL sequence created")

    valid_sequence = Sequence("TATAC")
    print("New sequence created!")

    print(f"Sequence 1: {null_sequence.seq}")
    print(f"Sequence 2: {valid_sequence.seq}")

print(type_of_sequences())

