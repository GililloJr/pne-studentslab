import http.server
import http.client
import socketserver
import termcolor
from pathlib import Path
from urllib.parse import parse_qs, urlparse
import jinja2 as j
import json

PORT = 8080
def read_html_file(filename):
    contents = Path("html/" + filename).read_text()
    contents = j.Template(contents)
    return contents
def list_species(limit=None):
    person = request.get("http://rest.ensembl.org/info/species", context={"Content-Type": "application/json"})
    if person.ok:
        datas = person.json()
        specie = [specie['display_name'] for specie in datas['species']]
        num_of_species = len(specie)
        if limit:
            specie = specie[:limit]
        return num_of_species, specie
    else:
        print("Error!")

def info_of_karyotype(specie):
    person = requests.get(f"https://rest.ensembl.org/info/assembly/{specie}", context={"Content-Type": "application/json"})
    if person.ok:
        datas = person.json
        return datas['karyotype']
    else:
        print("Error")

class TestHandler(http.server.BaseHTTPRequestHandler):
def do_GET(self):
    """This method is called whenever the client invokes the GET method
    in the HTTP protocol request"""
    url_path = urlparse(self.path)
    path = url_path.path  # we get it from here
    arguments = parse_qs(url_path.query)
    print(path, arguments)
    # Print the request line
    termcolor.cprint(self.requestline, 'green')

    if path == "/":
        filename = "index.html"
        contents = read_html_file(filename).render(context={})
    elif path == "/listSpecies":
        filename = "species.html"
        if 'limit' in arguments:
            limit = arguments['limit'][-1]
            num_of_species, specie = list_species(limit)
        else:
            limit = None