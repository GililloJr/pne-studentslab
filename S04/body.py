from pathlib import Path
FILENAME = "sequences/U5.txt"
file_contents = Path(FILENAME).read_text()
line_j = file_contents.find('\n')
dna_code = file_contents[line_j:]
print(dna_code)