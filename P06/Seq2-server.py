import http.server
import socketserver
import termcolor
from pathlib import Path
from urllib.parse import parse_qs, urlparse
import jinja2 as j
# Define the Server's port
PORT = 8080


# -- This is for preventing the error: "Port already in use"
socketserver.TCPServer.allow_reuse_address = True
def read_html_file(filename):
    contents = Path("html/" + filename).read_text()
    contents = j.Template(contents)
    return contents


# Crear el diccionario
sequences_adn = {
    0: "ATCGATCGATCGATCGA",
    1: "TGCATCGATCGATCGAT",
    2: "CGTAGCATCGATCGATC",
    3: "TAGCTAGCTAGCTAGCT",
    4: "GATCGATCGATCGATCG"
}


# Imprimir el diccionario
# Class with our Handler. It is a called derived from BaseHTTPRequestHandler
# It means that our class inherits all his methods and properties
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
        elif path == "/ping":
            filename = "ping.html"
            contents = read_html_file(filename).render(context={})
        elif path == "/get":
            filename = "get.html"
            if "n" in arguments:
                n = arguments["n"][-1]
                seq = sequences_adn.get(int(n))
                if seq is not None:
                    contents = read_html_file(filename).render(context={"todisplay": seq, "seq": n})
        elif path == "/gene":
            genes = ["U5", "ADA", "FXN", "FRAT1", "RNU6_269P"]
            seq_fin = ""
            gene = arguments.get("base")[0]
            for i in range(0, 5):
                if gene == genes[i]:
                    filename = "../sequences/" + gene + ".txt"
                    sequence = Path(filename).read_text()
                    s = sequence.split("\n")[1:]
                    for i in s:
                        seq_fin += i
            contents = read_html_file("gene.html").render(context={"todisplay": arguments["base"][0], "sequence": seq_fin})
        elif path == "/operation":

        #else:
            contents = Path('html/error.html').read_text()


        # Generating the response message
        self.send_response(200)  # -- Status line: OK!

        # Define the content-type header:
        self.send_header('Content-Type', 'text/html')
        self.send_header('Content-Length', len(str.encode(contents)))

        # The header is finished
        self.end_headers()

        # Send the response message
        self.wfile.write(str.encode(contents))
        return


# ------------------------
# - Server MAIN program
# ------------------------
# -- Set the new handler
Handler = TestHandler

# -- Open the socket server
with socketserver.TCPServer(("", PORT), Handler) as httpd:

    print("Serving at PORT", PORT)

    # -- Main loop: Attend the client. Whenever there is a new
    # -- clint, the handler is called
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("")
        print("Stopped by the user")
        httpd.server_close()