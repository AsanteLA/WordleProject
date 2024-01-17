import random
from WordleDictionary import FIVE_LETTER_WORDS

#Selectong the random word
random_word = random.choice(FIVE_LETTER_WORDS)

#Breaking down a word into a list of characters
charlist = list(random_word)

#Revelaing the cosen random word
print('Random Word:', random_word)

#Printing chatracterr list in array format
print(charlist)


# Sekected_Word = random.choice(FIVE_LETTER_WORDS)

# Breaking down a word into a list of characters
charlist = list(random_word)

# Creating a Wordle window
wordle_window = WordleGWindow()

# Revealing the chosen random word
print('Random Word:', random_word)

# Printing character list in array format
print(charlist)

# Loop to set each character in the Wordle window horizontally
for col, char in enumerate(charlist):
    # Set the character in row 0 (you can adjust the row as needed)
    wordle_window.set_square_letter(0, col, char)

# Wait for user interaction (optional)
input("Press Enter to exit")

# Accessing and constructing the first guess
guess = ''
for row in range(N_ROWS):
    for col in range(N_COLS):
        guess += wordle_window.get_square_letter(row, col) 

# Sekected_Word = random.choice(FIVE_LETTER_WORDS)
