import http.server
import socketserver
import termcolor
from urllib.parse import parse_qs, urlparse
import jinja2 as j
import requests
import json
from pathlib import Path
import http.client
from Seq1 import Seq

PORT = 8080
socketserver.TCPServer.allow_reuse_address = True

def read_html_file(filename):
    contents = Path("html/" + filename).read_text()
    contents = j.Template(contents)
    return contents

def fetch_json(file):  # renamed function
    SERVER = 'rest.ensembl.org'
    ENDPOINT = file
    PARAMS = "?content-type=application/json"

    conn = http.client.HTTPConnection(SERVER)

    try:
        conn.request("GET", ENDPOINT + PARAMS)
    except ConnectionRefusedError:
        print("ERROR! Cannot connect to the Server")
        exit()

    r1 = conn.getresponse()
    print(f"Response received!: {r1.status} {r1.reason}\n")
    data = r1.read().decode("utf-8")
    get_json = json.loads(data)
    return get_json

def info_response(seq):
    info = f"Total length: {seq.len()}<br>"
    for base in ["A", "C", "G", "T"]:
        count = seq.count_base(base)
        if seq.len() > 0:
            percentage = count / seq.len() * 100
        else:
            percentage = 0
        info += f"{base}: {count} ({percentage}  %)<br>"
    return info

def get_species_data(limit=None):
    url = "http://rest.ensembl.org/info/species"
    headers = {"Content-Type": "application/json"}
    response = requests.get(url, headers=headers)
    if response.status_code != 200:
        print("Error!")
        return
    data = response.json()
    species_list_1 = [species['display_name'] for species in data['species']]
    if limit is not None:
        species_list_2 = species_list_1[:int(limit)]
        return len(species_list_1), species_list_2
    else:
        return len(species_list_1)


def get_karyotype(species):
    url = f"https://rest.ensembl.org/info/assembly/{species}"
    headers = {"Content-Type": "application/json"}
    response = requests.get(url, headers=headers)
    if response.status_code != 200:
        print("Error!")
        return
    data = response.json()
    return data['karyotype']

def get_chromosome_length(species, chromo):
    url = f"https://rest.ensembl.org/info/assembly/{species}"
    headers = {"Content-Type": "application/json"}
    response = requests.get(url, headers=headers)
    if response.status_code != 200:
        print("Error!")
        return
    data = response.json()
    chromo_length = []
    for chromosome in data['top_level_region']:
        if chromo == chromosome["name"] and chromosome["coord_system"] == "chromosome":
            chromo_length.append(chromosome['length'])
        if chromo_length:
            return chromo_length[0]


class TestHandler(http.server.BaseHTTPRequestHandler):
    def do_GET(self):
        url_path = urlparse(self.path)
        path = url_path.path
        arguments = parse_qs(url_path.query)
        print(path, arguments)
        termcolor.cprint(self.requestline, 'green')

        if path == "/":
            contents = read_html_file("index.html").render()
        elif path == "/listSpecies":
            try:
                limit = arguments['limit'][-1] if 'limit' in arguments else None
                num_species, species = get_species_data(limit)
                contents = read_html_file("species.html").render(num_species=num_species, species=species, limit=limit)
            except KeyError:
                contents = read_html_file('html/error.html').read_text()
        elif path == "/karyotype":
            try:
                species = arguments['species'][-1]
                karyotype = get_karyotype(species)
                contents = read_html_file("karyotype.html").render(karyotype=karyotype)
            except KeyError:
                contents = read_html_file('html/error.html').read_text()
        elif path == "/chromosomeLength":
            try:
                species = arguments['species'][0]
                chromo = arguments['chromo'][0]
                chromo_length = get_chromosome_length(species, chromo)
                contents = read_html_file("chromolength.html").render(species=species, chromo=chromo, chromo_length=chromo_length)
            except KeyError:
                contents = Path('html/error.html').read_text()
        elif path == "/geneSeq":
            try:
                response = fetch_json("/lookup/symbol/homo_sapiens/" + arguments["gene"][0])
                get_id = response.get('id')
                seq = fetch_json("/sequence/id/" + get_id)
                geneinfo = ""
                geneinfo += (seq['seq']) + "<br>"
                contents = read_html_file("geneseq.html").render(context={"gene": arguments["gene"][0], "geneinfo": geneinfo})
            except KeyError:
                contents = Path('html/error.html').read_text()
        elif path == "/geneInfo":
            try:
                response = fetch_json("/lookup/symbol/homo_sapiens/" + arguments["gene"][0])
                get_id = response.get('id')
                seq = fetch_json("/sequence/id/" + get_id)
                geneinfo = f"Length: {len(seq['seq'])}" + "<br>"
                geneinfo += f"Start: {response['start']}" + "<br>"
                geneinfo += f"End: {response['end']}" + "<br>"
                geneinfo += f"id: {response['id']}" + "<br>"
                geneinfo += f"Chromosome: {response['seq_region_name']}" + "<br>"
                contents = read_html_file("geneinfo.html").render(context={"gene": arguments["gene"][0], "geneinfo": geneinfo})
            except KeyError:
                contents = Path('html/error.html').read_text()
        elif path == "/geneCalc":
            try:
                response = fetch_json("/lookup/symbol/homo_sapiens/" + arguments["gene"][0])
                get_id = response.get('id')
                seq_response = fetch_json("/sequence/id/" + get_id)
                seq = Seq(seq_response["seq"])
                contents = read_html_file("genecalc.html").render(context={"gene": arguments["gene"][0], "calculations": info_response(seq)})
            except KeyError:
                contents = Path('html/error.html').read_text()
        else:
            contents = Path('html/error.html').read_text()

        self.send_response(200)
        self.send_header('Content-Type', 'text/html')
        self.send_header('Content-Length', len(str.encode(contents)))
        self.end_headers()
        self.wfile.write(str.encode(contents))

with socketserver.TCPServer(("", PORT), TestHandler) as httpd:
    print("Serving at PORT", PORT, "...")
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("Stopped by gilillo")
        httpd.server_close()
