from pathlib import Path
from Seq0 import *
def seq_len(seq):
    genes = ["ADA", "U5", "FRAT1", "FXN"]

    for gene in genes:
        filename = "../sequences/" + gene + ".txt"
        file_contents = Path(filename).read_text()
        line_j = file_contents.find('\n')
        dna_code = file_contents[line_j:]
        seq = dna_code.replace('\n', '')
        print('Gene', gene, '-> Length:', len(seq))
