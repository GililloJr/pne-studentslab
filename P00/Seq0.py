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
    return len(seq)

#execise 4
def seq_count_base(seq, base):
    count = seq.count(base)
    return count

#execise 5
def seq_count(genes):
    bases = {"A": 0, "C": 0, "G": 0, "T": 0}
    for row in genes:
        for b in row:
            if b in bases:
                bases[b] += 1

    print(bases)

#exercise 6
def seq_reverse(seq, n):
    print("Fragment:", seq[0:n])
    print("Reverse:", seq[:n][::-1])

#exercise 7
def seq_complement(seq):
    complement_dict = {'A': 'T', 'T': 'A', 'C': 'G', 'G': 'C'}
    complement_seq = ''.join(complement_dict[base] for base in seq)
    return complement_seq

#exercise 8




























