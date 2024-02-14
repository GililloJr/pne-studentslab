from pathlib import Path
genes = ["U5", "ADA", "FRAT1", "FXN"]
for gene in genes:
    filename = f"../sequences/{gene}.txt"  # Using f-string for string formatting
    file_contents = Path(filename).read_text()

    counts = {'A': 0, 'C': 0, 'T': 0, 'G': 0}
    for base in file_contents:
        if base in counts:
            counts[base] += 1
    print(f"Gene {gene}:")
    print(counts)
