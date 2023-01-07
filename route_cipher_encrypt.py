'''
validate and convert plaintext to all caps
validate key and turn it to integers
replace codewords and convert to all caps
validate dummy words and convert to all caps
build matrix
encrypt and return encrypted message
'''

'''
grid for encryption:
WE WILL RUN THE BATTERIES AT
VICKSBURG THE NIGHT OF APRIL 16
AND PROCEED TO GRAND GULF WHERE
WE WILL REDUCE THE FORTS BE
PREPARED TO CROSS THE RIVER ON
APRIL 25 OR 29 ADMIRAL PORTER
D1 D2 D3 D4 D5 D6

encrypted message:
ANGELS CLAYTON PREPARED WE AND ODOR WE RUN NIGHT TO REDUCE CROSS OR CABIN
CROCODILE MULTIPLY TO WILL PROCEED THE WILL AT SWEET WHERE BE ON LANGFORD SPAIN
HOUNDS CLAYTON OWL BAILEY HICKORY HERMES UNIVERSITY FIRE ADD THE THE TREE OF THE

'''
import sys

#--------------------------------------------------
# USER INPUT

# the sting to be encrypted (paste between quotes):
plaintext = '''We will run the batteries at Vicksburg the night of April 16
and proceed to Grand Gulf where we will reduce the forts. Be prepared to cross
the river on April 25 or 29. Admiral Porter'''

# or rows in the transposition matrix
ROWS = 7

# of columns in the transposition matrix
COLS = 6

# include dummy words separated by spaces equal to the number of columns (paste between quotes):
dummy_words = 'angels crocodile cabin fire university spain'

# key with spaces between numbers; negative to read UP column (ex = -1 2 -3 4):
key = '-1 3 -2 6 5 -4'

#--------------------------------------------------

# Treating code words as if they are predefined (i.e. the user does not need to input them)
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

def validate_text_inputs(dummy_list, text_list):
    '''Validate all the user inputs for this cipher'''
    if len(dummy_list) != COLS:
        print('\nError - Number of dummy words does not match number of columns. Terminating program.', file=sys.stderr)
        sys.exit(1)
    if ROWS * COLS != len(dummy_list) + len(text_list):
        print('\nError - Message length does not match chosen grid. Terminating program.', file=sys.stderr)
        sys.exit(1)

def remove_punctuation_and_uppercase(word_list):
    '''Remove punctuation and uppercase dummy words and message.'''
    cleaned_list = []
    punc = '''!()-[];:'"\,<>./?@#$%^&*_~''' # list of punctuation to remove
    for word in word_list:
        for char in word:
            if char in punc:
                word = word.replace(char, '')
        word = word.upper()
        cleaned_list.append(word)
    return cleaned_list

def add_dummy_and_code_words():
    pass

def main():
    dummy_list = dummy_words.split()
    text_list = plaintext.split()
    validate_text_inputs(dummy_list, text_list)
    clean_dummys = remove_punctuation_and_uppercase(dummy_list)
    clean_message = remove_punctuation_and_uppercase(text_list)
    add_dummy_and_code_words()

if __name__ == '__main__':
    main()