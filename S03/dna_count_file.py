
bases = {"A": 0, "C": 0, "G": 0, "T": 0}
for row in seq:
    for b in row:
        if b in bases:
            bases[b] += 1

print(bases)