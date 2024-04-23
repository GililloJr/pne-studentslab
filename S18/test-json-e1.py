import json
import termcolor
from pathlib import Path

# Read the json file
jsonstring = Path("people-e1.json").read_text()

# Load the JSON data
people = json.loads(jsonstring)

# Print the total number of people
print()
termcolor.cprint("Total number of people: ", 'green', end="")
print(len(people))

# Iterate through each person in the list
for person in people:
    print()
    termcolor.cprint("Name: ", 'green', end="")
    print(person['Firstname'], person['Lastname'])
    termcolor.cprint("Age: ", 'green', end="")
    print(person['age'])

    # Get the phoneNumber list
    phoneNumbers = person['phoneNumber']

    # Print the number of elements in the list
    termcolor.cprint("Phone numbers: ", 'green', end='')
    print(len(phoneNumbers))

    # Print all the numbers
    for i, dictnum in enumerate(phoneNumbers):
        termcolor.cprint("  Phone " + str(i + 1) + ": ", 'blue')

        # The element num contains 2 fields: number and type
        termcolor.cprint("\t- Type: ", 'red', end='')
        print(dictnum['type'])
        termcolor.cprint("\t- Number: ", 'red', end='')
        print(dictnum['number'])

