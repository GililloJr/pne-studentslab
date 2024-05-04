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
    response = requests.get("http://rest.ensembl.org/info/species", headers={"Content-Type": "application/json"})
    if response.ok:
        data = response.json()
        species = [species['display_name'] for species in data['species']]
        if limit:
            species = species[:int(limit)]
        return len(species), species
    else:
        print("Error!")

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
