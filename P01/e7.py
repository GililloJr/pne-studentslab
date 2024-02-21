from Seq1 import Seq

def main():

    sequence_list = [Seq(None), Seq("ACTGA"), Seq("ERROR")]

    if Seq(None):
        print("NULL sequence created")

    elif Seq("ACTGA"):
        print("New sequence created!")

    elif Seq(12345):
        print("INVALID sequence!")


    for i, seq in enumerate(sequence_list):
        print(f"Sequence {i}: (Length: {len(seq.seq)}) {seq.seq}")
        print("  Bases:", seq.count_bases())
        print("  Rev:  ", seq.reverse())

main()


