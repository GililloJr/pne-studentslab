import socket
import termcolor
from Seq1 import Seq

class SeqServer:
    def __init__(self):
        self.PORT = 8081
        self.IP = "127.0.0.1"
        self.ls = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.ls.bind((self.IP, self.PORT))
        self.ls.listen()
        print("SEQ server is configured!")

        try:
            while True:
                print("Waiting for clients to connect")
                (rs, address) = self.ls.accept()
                msg = rs.recv(2048).decode("utf-8")
                response = self.return_response(str(msg))
                send_bytes = str.encode(response)
                rs.send(send_bytes)
                rs.close()
        except KeyboardInterrupt:
            print("These clients have connected to the server:")

        self.ls.close()


    def return_response(self, msg):
        if msg.startswith("PING"):
            return self.ping_response()
        if msg.startswith("GET"):
            return self.get_response(msg)
        if msg.startswith("INFO"):
            return self.info_response(msg)
        if msg.startswith("COMP"):
            return self.comp_response(msg)
        if msg.startswith("REV"):
            return self.rev_response(msg)
        if msg.startswith("GENE"):
            return self.gene_response(msg)

    def ping_response(self):
        print("PING COMMAND")
        return "OK!\n"

    def get_response(self, msg):
        termcolor.cprint("GET", 'green')
        sequences = ["ATGCAGWA", "ATGGTCCG", "TGCAGTGT", "TTGACCTA"]
        for j in msg:
            if j.isdigit():
                if 0 <= int(j) <= 3:
                    b = sequences[int(j)]
                    print(b)
                    return b + "\n"
                else:
                    return "Not valid command"

    def info_response(self, msg):
        termcolor.cprint("INFO", 'green')
        seq = Seq(msg.replace("INFO", "").strip())
        info = f"Sequence: {seq}\n"
        info += f"Total length: {seq.len()}\n"
        for base in ["A", "C", "G", "T"]:
            count = seq.count_base(base)
            if seq.len() > 0:
                percentage = count / seq.len() * 100
            else:
                percentage = 0
            info += f"{base}: {count} ({percentage}%)\n"
        print(info)
        return info

    def comp_response(self, msg):
        termcolor.cprint("COMP", 'green')
        seq = Seq(msg.replace("COMP", "").strip())
        complement_seq = seq.complement()
        print(complement_seq)
        return f"Complement: {complement_seq}\n"

    def rev_response(self, msg):
        termcolor.cprint("REV", 'green')
        seq = Seq(msg.replace("REV", "").strip())
        reverse_seq = seq.reverse()
        print(reverse_seq)
        return f"Complement: {reverse_seq}\n"

    def gene_response(self, msg):
        termcolor.cprint("GENE", 'green')
        seq = Seq(msg.replace("GENE", "").strip())
        gene_name = msg.strip().split()[1]
        filename = f"../sequences/{gene_name}.txt"  # Assuming gene sequence files are in the ../sequences/ directory
        try:
            seq = Seq()
            gene_sequence = seq.read_fasta(filename)
            print(gene_sequence)  # Print the gene sequence
            return f"{gene_name} Sequence: {gene_sequence}\n"
        except FileNotFoundError:
            return f"Error: Gene {gene_name} not found\n"


server = SeqServer()


