from pathlib import Path
from Seq0 import seq_count_base

genes = ["U5", "ADA", "FRAT1", "FXN"]
bases = ["A", "C", "G", "T"]

for gene in genes:
    filename = f"../sequences/{gene}.txt"  # Using f-string for string formatting
    file_contents = Path(filename).read_text()
    dna_code = file_contents.strip()  # Removes leading/trailing whitespaces and newlines
    print(f"\nGene {gene}:")
    for base in bases:
        count = seq_count_base(dna_code, base)
        print(f" {base}: {count}")


