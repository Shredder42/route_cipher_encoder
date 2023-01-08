# Route Cipher Encoder
This is the challenge project from chapter 4 of the book *Impractical Python Projects* by Lee Vaughan.

## The challenge
This challenge places me in the shoes of a Union telegraph clerk during the American Civil War who needs to encrypt a message for the Union Army positioned near Vicksburg in April of 1863. The task is to use a route cipher to encrypt the message so if it falls into enemy hands, it won't be deciphered!

## The Route Cipher
The version of the Route Cipher used in this challenge was used during the American Civil war in which some of the words are substituted for code words. Additionally, some dummy words are added to the text to make it even more difficult to solve. Some more information about

The Route Cipher is encrypted by putting the text in a grid with predetermined dimensions. Then certain words are substituted for code words. Dummy words are also added to the bottom of the grid to futher obscure the message. Then, with all the code words substituted and the dummy words added, the message is rewritten (encrypted) following a key known to the clerk and the receiver of the message. They key may be a spiral shape, up certain columns and down others, or any other possible route to traverse the message. Therefore to decode the message, the recipient needs to know the code words and the key that indicates the route through the message.

The Route Cipher can be found [here](https://en.wikipedia.org/wiki/Transposition_cipher#Route_cipher).

## The Message
The message to be encrypted is:

*We will run the batteries at Vicksburg the night of April 16 and proceed to Grand Gulf where we will reduce the forts. Be prepared to cross the river on April 25 or 29. Admiral Porter*

## The details
These are the predetermined items needed to encrypt the message.

### The grid
The message is to be placed in a grid that is 7 rows by 6 columns.

### Code Words
These words will be substituted in the message.
    Batteries: HOUNDS
    Vicksburg: ODOR
    April: CLAYTON
    16: SWEET
    Grand: TREE
    Gulf: OWL
    Forts: BAILEY
    River: HICKORY
    25: MULTIPLY
    29: ADD
    Admiral: HERMES
    Porter: LANGFORD

### Dummy Words
These words are added as the bottom row of the message.
*angels
*crocodile
*cabin
*fire
*university
*spain

### The Key
The key specifies the route through the message for encryption. In this case the numbers signify the column. If the number is positive, the route goes down the column. If the number is negative, the route goes up the column.

Key = -1, 3. -2, 6, 5, -4

## The Code
The code from this challenge requires the clerk to input the message, the grid dimensions (rows and columns), dummy words, and the key.

Then it preps the code words and dictionary and validates the input from the user. Next, it takes in the message and removes punctuation and uppercases all the letters. Then it substitutes the code words and adds the dummy words to the end of the message. Finally, it places the message in a 7x6 grid and then rewrites the encrypted message following the key (i.e. begins by going up column 1, then down column 3, etc.).

## The Output

### The Substituted Message
The message with the code words substituted and dummy words added looks like this:

WE WILL RUN THE HOUNDS AT
ODOR THE NIGHT OF CLAYTON SWEET
AND PROCEED TO TREE OWL WHERE
WE WILL REDUCE THE BAILEY BE
PREPARED TO CROSS THE HICKORY ON
CLAYTON MULTIPLY OR ADD HERMES LANGFORD
ANGELS CROCODILE CABIN FIRE UNIVERSITY SPAIN

### The Encrypted Message
The final encrypted message:

ANGELS CLAYTON PREPARED WE AND ODOR WE RUN NIGHT TO REDUCE CROSS OR CABIN CROCODILE MULTIPLY TO WILL PROCEED THE WILL AT SWEET WHERE BE ON LANGFORD SPAIN HOUNDS CLAYTON OWL BAILEY HICKORY HERMES UNIVERSITY FIRE ADD THE THE TREE OF THE


