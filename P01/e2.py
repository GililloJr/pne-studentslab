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


def null_seqs():
    s1 = Seq()
    s2 = Seq("TATAC")

    print("Sequence 1:", s1)
    print("Sequence 2:", s2)

null_seqs()
