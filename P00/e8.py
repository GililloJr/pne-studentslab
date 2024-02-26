
from Seq0 import *
def main():
    genes = ["U5", "ADA", "FRAT1", "FXN"]
    for gene in genes:
        filename = f"../sequences/{gene}.txt"
        sequence = Path(filename).read_text().strip()

        base_counts = count_bases(sequence)

        most_freq_base = most_frequent_base(base_counts)

        print(f"Gene {gene}: Most frequent Base: {most_freq_base}")

