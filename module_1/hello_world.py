# The trivial Hello World programm
# Python naming conventions according to https://peps.python.org/pep-0008/

# To-do:
# Variable annotation https://peps.python.org/pep-0526/
# Type Hints https://peps.python.org/pep-0484/
# Documentation strings https://peps.python.org/pep-0257/


# dictionary definition
from typing import Dict


letters_dict = {
    "H": [1],
    "e": [2],
    "l": [3, 4, 10],
    "o": [5, 8],
    " ": [6],
    "w": [7],
    "r": [9],
    "d": [11],
    "!": [12]
}

def get_letter(the_dictionary={}, letter_number=0):
    if (the_dictionary is not None) and (letter_number>0):
        letter_cursor = letter_number

        for i in the_dictionary:
            for k in (the_dictionary[i]):
                if k == letter_cursor:
                    return i

        letter_cursor = letter_cursor + 1
    return ""



def simple_hello_world(the_dictionary={}):
    message_text = ""
    for i in range (1,len("Hello world!")+1):
          message_text = message_text + get_letter (the_dictionary, i)

    return message_text


print(simple_hello_world(letters_dict))