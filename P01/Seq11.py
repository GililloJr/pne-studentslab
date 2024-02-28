class Seq:
    def __init__(self, sequence):
        self.sequence = sequence if sequence else ""

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

