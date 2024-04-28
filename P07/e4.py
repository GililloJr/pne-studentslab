import http.client
import json
from Seq1 import Seq
from pathlib import Path


PORT = 80
SERVER = 'rest.ensembl.org'
ENDPOINT = '/sequence/id'
PARAMS = '?content-type=application/json'
GENE_ID = 'ENSG00000207552'
URL = SERVER + ENDPOINT + PARAMS

print(f"Server: {SERVER}")
print(f"URL: {URL}")

print(f"\nConnecting to server: {SERVER}:{PORT}\n")

conn = http.client.HTTPConnection(SERVER, PORT)
try:
    conn.request("GET", ENDPOINT + PARAMS)
except ConnectionRefusedError:
    print("ERROR! Cannot connect to the Server")
    exit()

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

r1 = conn.getresponse()
data = r1.read().decode("utf-8")
response = json.loads(data)

if 'seq' in response and 'desc' in response:
    sequence = Seq(response['seq'])
    description = response['desc']
    print(f"Gene: {GENE_ID}")
    print(f"Description: {description}")
    print(f"Bases: {sequence}")

else:
    print(f"Gene {GENE_ID} not found or no sequence/description available.")

    print(f"Bases: {sequence.strbases}")
    for base in ['A', 'C', 'G', 'T']:
        print(f"{base}: {sequence.count_base(base)} ({sequence.count_percent(base)}%)")
    print(f"Most frequent Base: {sequence.frequent_base()}")



