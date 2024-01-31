
with open("dna.txt", "r") as file:
    bases = {"A": 0, "C": 0, "G": 0, "T": 0}
    for row in file:
        for b in row:
            if b in bases:
                bases[b] += 1

print(bases)