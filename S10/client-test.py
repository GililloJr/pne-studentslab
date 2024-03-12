from Client0 import Client
IP = "127.0.0.1"
PORT = 8081
c = Client(IP, PORT)
print("* Testing PING...")
get_ping = c.talk("PING")
print(get_ping)

print("\n* Testing GET...")
for j in range(0, 4):
    get = c.talk(f"GET {j}")
    print(f"GET {j}: {get}")

sequence = c.talk("GET 0")

print("\n* Testing INFO...")
get_info = c.talk(f"INFO {sequence}")
print(get_info)

print("\n* Testing COMP...")
get_comp = c.talk(f"COMP {sequence}")
print(get_comp)

print("\n* Testing REV...")
get_rev = c.talk(f"REV {sequence}")
print(get_rev)

print("\n* Testing GENE...")
genes = ["ADA", "FRAT1", "FXN", "RNU6_269P", "U5"]
for gene in genes:
    get_gene = c.talk(f"GENE {gene}")
    print(get_gene)