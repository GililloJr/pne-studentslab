from Seq1 import Seq

def method_len():
    s1 = Seq("")
    print("NULL sequence created")

    s2 = Seq("ACTGA")
    print("New sequence created!")

    s3 = Seq("")
    print("INVALID sequence!")

    print(f"Sequence 1: (Length: {len(s1.sequence)}) {'NULL' if not s1.sequence else s1.sequence}")
    print(f"Sequence 2: (Length: {len(s2.sequence)}) {'NULL' if not s2.sequence else s2.sequence}")
    print(f"Sequence 3: (Length: {len(s3.sequence)}) {'ERROR'}")

print(method_len())


