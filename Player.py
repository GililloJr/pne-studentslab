import socket
import sys

# Function to print colored messages
def print_colored(message, color):
    colors = {
        'red': '\033[91m',
        'green': '\033[92m',
        'yellow': '\033[93m',
        'blue': '\033[94m',
        'purple': '\033[95m',
        'cyan': '\033[96m',
    }
    end_color = '\033[0m'
    if color in colors:
        print(colors[color] + message + end_color)
    else:
        print(message)

# Server IP and port
SERVER_IP = "127.0.0.1"
SERVER_PORT = 8081

# Create a socket object
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    # Connect to the server
    client_socket.connect((SERVER_IP, SERVER_PORT))
    print("Connected to the server.")

    # Receive initial message from the server
    initial_message = client_socket.recv(2048).decode("utf-8")
    print(initial_message)

    # Start the game
    while True:
        # Get user input for the guess
        guess = input("Guess a number between 1 and 100: ")

        # Send the guess to the server
        client_socket.send(str.encode(guess))

        # Receive response from the server
        response = client_socket.recv(2048).decode("utf-8")

        # Check if the guess is correct
        if "won" in response:
            print_colored(response, 'green')
            break
        elif "Higher" in response:
            print_colored(response, 'red')
        elif "Lower" in response:
            print_colored(response, 'blue')

except KeyboardInterrupt:
    print("\nGame terminated by user.")

finally:
    # Close the socket
    client_socket.close()
