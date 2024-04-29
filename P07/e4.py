import http.client
import json
from Seq1 import Seq

genes = {
    "FRAT1": "ENSG00000165879",
    "ADA": "ENSG00000196839",
    "FXN": "ENSG00000165060",
    "RNU6_269P": 'ENSG00000212379',
    "MIR633": 'ENSG00000207552',
    "TTTY4C": 'ENSG00000228296',
    "RBMY2YP": "ENSG00000227633",
    "FGFR3": "ENSG00000068078",
    "KDR": "ENSG00000128052",
    "ANK2": "ENSG00000145362"
}

def info_response(seq):
    info = f"Total length: {seq.len()}\n"
    for base in ["A", "C", "G", "T"]:
        count = seq.count_base(base)
        if seq.len() > 0:
            percentage = count / seq.len() * 100
        else:
            percentage = 0
        info += f"{base}: {count} ({percentage:.2f}%)\n"
    return info

gene_code = input("Enter a gene name (e.g., FRAT1, ADA, FXN): ")
if gene_code in genes:
    SERVER = 'rest.ensembl.org'
    ENDPOINT = f'/sequence/id/{genes[gene_code]}'
    PARAMS = '?content-type=application/json'
    URL = SERVER + ENDPOINT + PARAMS

    print()
    print(f"Server: {SERVER}")
    print(f"URL: {URL}")

    conn = http.client.HTTPConnection(SERVER)

    try:
        conn.request("GET", ENDPOINT + PARAMS)
    except ConnectionError:
        print("ERROR! Cannot connect to the server")
        exit()

    r1 = conn.getresponse()
    print(f"Response received!: {r1.status} {r1.reason}\n")
    data = r1.read().decode("utf-8")
    response = json.loads(data)
    print(f"Gene: {gene_code}")
    print(f"Description: {response['desc']}")
    sequence = response['seq']
    seq = Seq(sequence)
    print(info_response(seq))
    base_count = sequence.count()
    most_frequent = max(base_count, key=base_count.get)
    print(f"Most frequent base is: {most_frequent}")
else:
    print("No valid gene.")






