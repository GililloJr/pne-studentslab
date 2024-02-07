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
    from pathlib import Path
    genes = {"ADA", "U5", "FRAT1", "FXN"}
    for gene in genes:
        filename = "../sequences/" + gene + ".txt"
        file_contents = Path(filename).read_text()
        line_j = file_contents.find('\n')
        dna_code = file_contents[line_j:]
        seq = dna_code.replace('\n', '')
        print(len(seq))





