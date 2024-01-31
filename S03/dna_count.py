dna_sequence = input("Enter a DNA sequence: ").upper()
total_length = len(dna_sequence)
bases = {"A": 0, "C": 0, "G": 0, "T": 0}

for b in dna_sequence:
    if b == "A":
        bases["A"] += 1
    elif b == "C":
        bases["C"] += 1
    elif b == "G":
        bases["G"] += 1
    elif b == "T":
        bases["T"] += 1

print("DNA sequence is:", dna_sequence)
print("Total length is:", total_length)
for base, count in bases.items():
    print(f"{base}: {count}")

