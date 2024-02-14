class Seq:
    def __init__(self, strbases):
        bases = ["A", "C", "G", "T"]
        for j in strbases:
            if j not in bases:
                self.strbases = "ERROR!"
                print("ERROR!")
                return

        self.strbases = strbases
        print("New sequence created!")

    def __str__(self):
        return self.strbases

    def len(self):
        return len(self.strbases)

def generate_seqs(pattern, number):
    seq_list = []
    for i in range(1, number + 1):
        seq = pattern * i
        seq_list.append(seq)
        print("New sequence created!")
    return seq_list

def print_seqs(seq_list):
    for i, seq in enumerate(seq_list):
        print(f"Sequence {i}: (Length: {len(seq)}) {seq}")

# Test the function with this main program
seq_list1 = generate_seqs("A", 3)
seq_list2 = generate_seqs("AC", 5)

print("List 1:")
print_seqs(seq_list1)

print()
print("List 2:")
print_seqs(seq_list2)
