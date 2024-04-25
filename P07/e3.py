import http.client
import json

PORT = 80
SERVER = 'rest.ensembl.org'
ENDPOINT = '/sequence/id'
PARAMS = '?content-type=application/json'
GENE_ID = 'ENSG00000207552'
URL = SERVER + ENDPOINT + '/' + GENE_ID + PARAMS

print(f"Server: {SERVER}")
print(f"URL: {URL}")

print(f"\nConnecting to server: {SERVER}:{PORT}\n")

# Connect with the server
conn = http.client.HTTPConnection(SERVER, PORT)

# Send the GET request for the specific gene ID
try:
    conn.request("GET", ENDPOINT + '/' + GENE_ID + PARAMS)
except ConnectionRefusedError:
    print("ERROR! Cannot connect to the Server")
    exit()

# Read the response message from the server
r1 = conn.getresponse()

# Print the status line
print(f"Response received!: {r1.status} {r1.reason}\n")

# Read the response's body
data = r1.read().decode("utf-8")

# Parse the JSON response
response = json.loads(data)

# Check if the response contains the sequence and description
if 'seq' in response and 'desc' in response:
    sequence = response['seq']
    description = response['desc']
    print(f"Gene: {GENE_ID}")
    print(f"Description: {description}")
    print(f"Bases: {sequence}")

else:
    print(f"Gene {GENE_ID} not found or no sequence/description available.")

