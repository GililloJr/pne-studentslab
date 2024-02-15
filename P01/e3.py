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


def types_of_sequences():
    s1 = Seq()
    s2 = Seq("ACTGA")
    s3 = Seq("Invalid sequence")
    
    print("Sequence 1:", s1)
    print("Sequence 2:", s2)
    print("Sequence 3:", s3)

types_of_sequences()
