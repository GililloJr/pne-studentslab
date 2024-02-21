class Seq:
    def __init__(self, seq=None):
        self.seq = seq

def sequencesss():

    s1 = Seq()
    print("NULL sequence created")

    s2 = Seq("ACTGA")
    print("New sequence created!")

    s3 = Seq("Invalid sequence")
    print("INVALID sequence!")

    print(f"Sequence 1: {s1.seq if s1.seq else 'NULL'}")
    print(f"Sequence 2: {s2.seq}")
    print(f"Sequence 3: {'ERROR' if s3.seq and not all(char in 'ACTG' for char in s3.seq) else s3.seq}")

print(sequencesss())

