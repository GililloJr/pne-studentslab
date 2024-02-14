from pathlib import Path
file_contents = Path("../sequences/U5.txt").read_text()
line_j = file_contents.find('\n')
dna_code = file_contents[line_j:]
seq = dna_code.replace('\n', '')
from Seq0 import *
seq_complement(seq)
print("Gene U5:")
print(f"Frag: ", seq[0: 21])
complement_fragment = seq_complement(seq[0: 21])
print(f"Comp: {complement_fragment}")

