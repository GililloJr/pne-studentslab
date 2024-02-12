from pathlib import Path
def base_number(genes):
    for gene in genes:
        filename = "../sequences/" + gene + ".txt"
        file_contents = Path(filename).read_text()

        counts = {'A': 0, 'C': 0, 'T': 0, 'G': 0}
        for base in file_contents:
            if base in counts:
                counts[base] += 1

        print("Gene", gene, ":")
        for base, count in counts.items():
            print(base, ":", count)
