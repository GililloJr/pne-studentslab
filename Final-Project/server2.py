import http.server
import http.client
import socketserver
import termcolor
from pathlib import Path
from urllib.parse import parse_qs, urlparse
import jinja2 as j
import json


PORT = 8080
HTML_FOLDER = "html"
SERVER = "rest.ensembl.org"
ENDPOINT = '/listSpecies'
RESOURCE = "/info/species", "/info/assembly_info"
PARAMS = {'params': "content-type=application/json"}

print(f"\nConnecting to server: {SERVER}:{PORT}\n")

# Connect with the server
conn = http.client.HTTPConnection(SERVER, PORT)

# -- Send the request message, using the GET method. We are
# -- requesting the main page (/)
try:
    conn.request("GET", ENDPOINT + PARAMS)
except ConnectionRefusedError:
    print("ERROR! Cannot connect to the Server")
    exit()

# -- This is for preventing the error: "Port already in use"
socketserver.TCPServer.allow_reuse_address = True
def read_html_file(filename):
    contents = Path("html/" + filename).read_text()
    contents = j.Template(contents)
    return contents

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
        file_path = os.path.join(HTML_FOLDER, "index.html")
        contents = read_html_file(filename).render(context={})
    elif path == "/listSpecies":
        code, contents = list_species(endpoint, parameters)