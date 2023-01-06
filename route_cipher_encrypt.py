'''
get dummy words
get key
convert plaintext to all caps
replace codewords
'''


#--------------------------------------------------

# the sting to be encrypted (paste between quotes):
plaintext = '''We will run the batteries at Vicksburg the night of April 16
and proceed to Grand Gulf where we will reduce the forts. Be prepared to cross
the river on April 25 or 29. Admiral Porter'''

# matrix is 6 rows x 7 columns
# make up own dummy words
# key is [-1, 3, -2, 6, 5, -4]

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