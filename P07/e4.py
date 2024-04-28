import http.client
import json
from Seq1 import Seq
from pathlib import Path

genes = ["U5", "ADA", "FXN", "FRAT1", "RNU6_269P"]
def get_gene_data(gene_id):
    PORT = 80
    SERVER = 'rest.ensembl.org'
    ENDPOINT = '/sequence/id'
    PARAMS = '?content-type=application/json'
    URL = SERVER + ENDPOINT + '/' + gene_id + PARAMS

    print(f"Server: {SERVER}")
    print(f"URL: {URL}")

    print(f"\nConnecting to server: {SERVER}:{PORT}\n")

    conn = http.client.HTTPConnection(SERVER, PORT)
    try:
        conn.request("GET", ENDPOINT + '/' + gene_id + PARAMS)
    except ConnectionRefusedError:
        print("ERROR! Cannot connect to the Server")
        exit()

    r1 = conn.getresponse()
    data = r1.read().decode("utf-8")
    response = json.loads(data)

    if 'seq' in response and 'desc' in response:
        sequence = Seq(response['seq'])
        description = response['desc']
        return sequence, description
    else:
        print(f"Gene {gene_id} not found or no sequence/description available.")
        return None, None

def main():
    gene_id = input("Enter the gene ID: ")
    sequence, description = get_gene_data(gene_id)

    if sequence and description:
        print(f"Gene: {gene_id}")
        print(f"Description: {description}")
        print(f"Total length: {sequence.len()}")
        print(f"Bases: {sequence.strbases}")
        for base in ['A', 'C', 'G', 'T']:
            print(f"{base}: {sequence.count_base(base)} ({sequence.count_percent(base)}%)")
        print(f"Most frequent Base: {sequence.frequent_base()}")

if __name__ == "__main__":
    main()


