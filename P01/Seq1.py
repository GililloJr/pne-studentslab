#ex1
class Seq:
    def __init__(self, strbases):
        self.strbases = strbases

    def __str__(self):
        return self.strbases

    def len(self):
        return len(self.strbases)


#ex2
class Seq:
    def __init__(self, strbases=None):
        if strbases is None:
            self.strbases = "NULL"
            print("NULL sequence created")
            return
        self.strbases = strbases
        print("New sequence created!")

    def __str__(self):
        return self.strbases

#ex3
class Seq:
    def __init__(self, strbases=None):
        if strbases is None:
            self.strbases = "NULL"
            print("NULL sequence created")
        elif all(base in "ATCG" for base in strbases):
            self.strbases = strbases
            print("New sequence created!")
        else:
            self.strbases = "ERROR"
            print("INVALID sequence!")

    def __str__(self):
        return self.strbases


#ex4
class Seq:
    def __init__(self, strbases=None):
        if strbases is None:
            self.strbases = "NULL"
            print("NULL sequence created")
        elif all(base in "ATCG" for base in strbases):
            self.strbases = strbases
            print("New sequence created!")
        else:
            self.strbases = "ERROR"
            print("INVALID sequence!")

    def __str__(self):
        return self.strbases

    def __len__(self):
        if self.strbases == "NULL" or self.strbases == "ERROR":
            return 0
        else:
            return len(self.strbases)


#ex5
class Seq:
    def __init__(self, seq):
        self.seq = seq

    def count_base(self, base):
        if not self.seq or not all(char in 'ACTG' for char in self.seq):
            return 0
        return self.seq.count(base)


#ex6
class Seq:
    def __init__(self, seq):
        self.seq = seq

    def count_base(self, base):
        if not self.seq or not all(char in 'ACTG' for char in self.seq):
            return 0
        return self.seq.count(base)

    def count(self):
        if not self.seq or not all(char in 'ACTG' for char in self.seq):
            return {'A': 0, 'T': 0, 'C': 0, 'G': 0}

        counts = {'A': 0, 'T': 0, 'C': 0, 'G': 0}
        for base in self.seq:
            if base in counts:
                counts[base] += 1
        return counts


#ex7
class Seq:
    def __init__(self, seq):
        self.seq = seq if seq is not None else ""

    def count_bases(self):
        base_count = {'A': 0, 'T': 0, 'C': 0, 'G': 0}
        if self.seq == "":
            return base_count
        for base in self.seq:
            if base in base_count:
                base_count[base] += 1
        return base_count

    def reverse(self):
        if self.seq == "":
            return "NULL"
        else:
            return self.seq[::-1]