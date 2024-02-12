def seq_ping():
    print("OK")


def seq_read_fasta(filename):
    from pathlib import Path
    file_contents = Path(filename).read_text()
    line_j = file_contents.find('\n')
    dna_code = file_contents[line_j:]
    print("The first 20 bases : ", dna_code[0: 21])


#exercise3
def seq_len(seq):
    return(len(seq))

#execise 4
from pathlib import Path
def analyze_gene_sequences(genes):
    for gene in genes:
        filename = "../sequences/" + gene + ".txt"
        file_contents = Path(filename).read_text()

        counts = {'A': 0, 'C': 0, 'T': 0, 'G': 0}
        for base in file_contents:
            if base in counts:
                counts[base] += 1

        print(f"Gene {gene}:")
        for base, count in counts.items():
            print(f"  {base}: {count}")


# Test the function
if __name__ == "__main__":
    genes = ["U5", "ADA", "FRAT1", "FXN"]
    analyze_gene_sequences(genes)


#exercise 5
def seq_count(genes):
    gene_counts = {}
    for gene in genes:
        filename = f"../sequences/{gene}.txt"
        sequence = open(filename).read().strip()
        counts = {'A': 0, 'C': 0, 'T': 0, 'G': 0}
        for base in sequence:
            if base in counts:
                counts[base] += 1
        gene_counts[gene] = counts
    return gene_counts

    genes = ["U5", "ADA", "FRAT1", "FXN"]
    result = seq_count(genes)
    for gene, counts in result.items():
        print(f"Gene {gene}: {counts}")















