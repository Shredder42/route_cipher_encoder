'''
validate and convert plaintext to all caps
validate key and turn it to integers
replace codewords and convert to all caps
validate dummy words and convert to all caps
build matrix
encrypt and return encrypted message
'''


#--------------------------------------------------
# USER INPUT

# the sting to be encrypted (paste between quotes):
plaintext = '''We will run the batteries at Vicksburg the night of April 16
and proceed to Grand Gulf where we will reduce the forts. Be prepared to cross
the river on April 25 or 29. Admiral Porter'''

# or rows in the transposition matrix
ROWS = 6

# of columns in the transposition matrix
COLS = 7

# include dummy words separated by spaces equal to the number of columns (paste between quotes):
dummy_words = 'angels crocodile cabin fire university spain'

# key with spaces between numbers; negative to read UP column (ex = -1 2 -3 4):
key = '-1 3 -2 6 5 -4'

#--------------------------------------------------

code_words = {
    'Batteries': 'HOUNDS',
    'Vicksburg': 'ODOR',
    'April': 'CLAYTON',
    '16': 'SWEET',
    'Grand': 'TREE',
    'Gulf': "OWL",
    'Forts': 'BAILEY',
    'River': 'HICKORY',
    '25': 'MULTIPLY',
    '29': 'ADD',
    'Admiral': 'HERMES',
    'Porter': 'LANGFORD'
}

def main():
    pass



if __name__ == '__main__':
    main()