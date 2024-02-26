from Seq1 import Seq

def sequencesss():
    s1 = Seq("")
    print("NULL sequence created")

    s2 = Seq("ACTGA")
    print("New sequence created!")

    s3 = Seq("Invalid sequence")
    print("INVALID sequence!")

    print(f"Sequence 1: {s1.sequence if s1.sequence else 'NULL'}")
    print(f"Sequence 2: {s2.sequence}")
    print(f"Sequence 3: {'ERROR' if s3.sequence and not all(char in 'ACTG' for char in s3.sequence) else s3.sequence}")

sequencesss()


