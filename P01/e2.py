from Seq1 import Seq

def type_of_sequences():
    null_sequence = Seq(None)
    print("NULL sequence created")

    valid_sequence = Seq("TATAC")
    print("New sequence created!")

    print(f"Sequence 1: {null_sequence.sequence}", "NULL")
    print(f"Sequence 2: {valid_sequence.sequence}")

type_of_sequences()


