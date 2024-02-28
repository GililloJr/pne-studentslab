import socket

# SERVER IP, PORT
PORT = 8081
IP = "212.128.255.95" # depends on the computer the server is running

while True:
  # -- Ask the user for the message
    question = input("Enter a message please: ")
  # -- Create the socket
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
  # -- Establish the connection to the Server
    s.connect((IP, PORT))
  # -- Send the user message
    s.send(question.encode())
  # -- Close the socket
    s.close()