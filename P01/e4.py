class Seq:
    def __init__(self, seq=None):
        self.seq = seq

    def __len__(self):
        if self.seq is None or not isinstance(self.seq, str) or not all(char in 'ACTG' for char in self.seq):
            return 0
        return len(self.seq)

def main():

    s1 = Seq()
    print("NULL sequence created")

    s2 = Seq("ACTGA")
    print("New sequence created!")

    s3 = Seq("Invalid sequence")
    print("INVALID sequence!")

    print(f"Sequence 1: (Length: {len(s1)}) {s1.seq if s1.seq else 'NULL'}")
    print(f"Sequence 2: (Length: {len(s2)}) {s2.seq}")
    print(f"Sequence 3: (Length: {len(s3)}) {'ERROR' if s3.seq and not all(char in 'ACTG' for char in s3.seq) else s3.seq}")

print(main())

