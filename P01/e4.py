from Seq1 import Seq

def length_of_sequences():
    s1 = Seq()
    s2 = Seq("ACTGA")
    s3 = Seq("Invalid sequence")

    print("Sequence 1: (Length:", len(s1), ")", s1)
    print("Sequence 2: (Length:", len(s2), ")", s2)
    print("Sequence 3: (Length:", len(s3), ")", s3)

length_of_sequences()
