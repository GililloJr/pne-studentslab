from Seq1 import Seq

genes = ["U5", "ADA", "FRAT1", "FXN", "RNU6_269P"]
for gene in genes:
    filename = (f"../sequences/{gene}.txt")
    s = Seq()
    s.read_fasta(filename)
    counts = {base: s.count_base(base) for base in ['A', 'C', 'T', 'G']}
    most_frequent_base = max(counts, key=counts.get)
    print(f"Gene {gene}: Most frequent Base: {most_frequent_base}")


