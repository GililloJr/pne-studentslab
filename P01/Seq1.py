class Seq:
    def __init__(self, sequence=""):
        self.sequence = sequence
        self.strbases = {'A': 0, 'T': 0, 'C': 0, 'G': 0}

    def __str__(self):
        return self.sequence

    def len(self):
        if self.sequence == "NULL" or self.sequence == "ERROR!!":
            return 0
        return len(self.sequence)

    def count_base(self, base):
        if not self.sequence or any(char not in 'ACTG' for char in self.sequence):
            return 0
        return self.sequence.count(base)

    def count(self):
        if not self.sequence or any(char not in 'ACTG' for char in self.sequence):
            return {'A': 0, 'T': 0, 'C': 0, 'G': 0}
        else:
            return {base: self.count_base(base) for base in 'ACTG'}

    def reverse(self):
        if not self.sequence or any(char not in 'ACTG' for char in self.sequence):
            return "NULL" if self.sequence == "NULL" else "ERROR"
        return self.sequence[::-1]

    def complement(self):
        if not self.sequence or any(char not in 'ACTG' for char in self.sequence):
            return "NULL" if self.sequence == "NULL" else "ERROR"
        complement_dict = {'A': 'T', 'T': 'A', 'C': 'G', 'G': 'C'}
        return ''.join(complement_dict.get(base, base) for base in self.sequence)

    def read_fasta(self, filename):
        with open(filename, 'r') as file:
            lines = file.readlines()
            self.sequence = "".join(lines[1:])
        return self.sequence