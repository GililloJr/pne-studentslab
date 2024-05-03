class Seq:
    def __init__(self, sequence=""):
        if sequence == "":
            print("NULL sequence created")
            self.sequence = 'NULL'
            return
        bases = ["A", "G", "C", "T"]
        for j in sequence:
            if j not in bases:
                self.sequence = 'ERROR!!'
                print("INVALID sequence!")
                return
        self.sequence = sequence
        print("New sequence created")


    def __str__(self):
        return self.sequence

    def len(self):
        if self.sequence == "NULL" or self.sequence == "ERROR!!":
            return 0
        return len(self.sequence)

    def count_base(self, base):
        if self.sequence == "NULL" or self.sequence == "ERROR!!":
            return 0
        return self.sequence.count(base)

    def count(self):
        seq_count = {'A': 0, 'T': 0, 'C': 0, 'G': 0}
        for n in self.sequence:
            if n in seq_count:
                if self.sequence == "NULL" or self.sequence == "ERROR!!":
                    seq_count[n] = 0
                else:
                    seq_count[n] += 1
        return seq_count

    def reverse(self):
        if self.sequence == "NULL":
            return 'NULL'
        if self.sequence == "ERROR!!":
            return 'ERROR'
        return self.sequence[::-1]

    def complement(self):
        complement_dict = {'A': 'T', 'T': 'A', 'C': 'G', 'G': 'C'}
        complement_seq = ""
        if self.sequence == "NULL":
            return 'NULL'
        if self.sequence == "ERROR!!":
            return 'ERROR'
        for base in self.sequence:
            complement_seq += complement_dict.get(base, base)
        return complement_seq

    def read_fasta(self, filename):
        from pathlib import Path
        file_contents = Path(filename).read_text()
        first_line = file_contents.find("\n")
        seq_dna = file_contents[first_line:]
        seq = seq_dna.replace("\n", "")
        self.sequence = seq
        return seq
