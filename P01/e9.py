from Seq1 import Seq

def main():
    s = Seq()
    print("NULL Seq created")
    s.read_fasta("U5.txt")
    print(f"Sequence : (Length: {len(s.sequence)}) {s.sequence}")
    print("  Bases:", s.count())
    print("  Rev:", s.reverse())
    print("  Comp:", s.complement())

main()

