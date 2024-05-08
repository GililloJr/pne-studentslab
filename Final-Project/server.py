import http.server
import socketserver
import termcolor
from urllib.parse import parse_qs, urlparse
import jinja2 as j
import requests
from pathlib import Path

PORT = 8080
socketserver.TCPServer.allow_reuse_address = True

def read_html_file(filename):
    contents = Path("html/" + filename).read_text()
    contents = j.Template(contents)
    return contents

def get_species_data(limit=None):
    url = "http://rest.ensembl.org/info/species"
    headers = {"Content-Type": "application/json"}
    response = requests.get(url, headers=headers)
    if response.status_code != 200:
        print("Error!")
        return
    data = response.json()
    species_list_1= [species['display_name'] for species in data['species']]

    if limit is not None:
        species_list_2 = species_list_1[:int(limit)]
    return len(species_list_1), species_list_2

def get_karyotype(species):
    url = f"https://rest.ensembl.org/info/assembly/{species}"
    headers= {"Content-Type": "application/json"}
    response = requests.get(url, headers=headers)
    if response.status_code != 200:
        print("Error!")
        return
    data = response.json()
    return data['karyotype']


def get_chromosome_length(species, chromo):
    url = f"https://rest.ensembl.org/info/assembly/{species}"
    headers= {"Content-Type": "application/json"}
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
            limit = arguments['limit'][-1] if 'limit' in arguments else None
            num_species, species = get_species_data(limit)
            contents = read_html_file("species.html").render(num_species=num_species, species=species, limit=limit)
        elif path == "/karyotype":
            species = arguments['species'][-1] if 'species' in arguments else None
            karyotype = get_karyotype(species)
            contents = read_html_file("karyotype.html").render(karyotype=karyotype)
        elif path == "/chromosomeLength":
            species = arguments['species'][0]
            chromo = arguments['chromosome'][0]
            chromo_length = get_chromosome_length(species, chromo)
            contents = read_html_file("chromolength.html").render(species=species, chromo=chromo, chromo_length=chromo_length)
        else:
            contents = Path('html/error.html').read_text()

        self.send_response(200)
        self.send_header('Content-Type', 'text/html')
        self.send_header('Content-Length', len(str.encode(contents)))
        self.end_headers()
        self.wfile.write(str.encode(contents))

with socketserver.TCPServer(("", PORT), TestHandler) as httpd:
    print("Serving at PORT", PORT)
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("Stopped by the user")
        httpd.server_close()
