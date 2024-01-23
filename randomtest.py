import random
from WordleDictionary import FIVE_LETTER_WORDS
from WordleGraphics import WordleGWindow, CORRECT_COLOR, PRESENT_COLOR, MISSING_COLOR, N_COLS, N_ROWS

#Selectong the random word
random_word = random.choice(FIVE_LETTER_WORDS)

#Breaking down a word into a list of characters
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
# Accessing and constructing the first guess
guess = ''
for row in range(N_ROWS):
    for col in range(N_COLS):
        guess += wordle_window.get_square_letter(row, col) 

guess_lower = guess.lower()

guess_lower = guess_lower.strip()

def enter_action(FIVE_LETTER_WORDS, guess_lower):
    
    if guess_lower in FIVE_LETTER_WORDS:
        msg = "Good try! This is a word!"
        wordle_window.show_message(msg, color="Black")
    else:
        msg = "Not in word list"
        wordle_window.show_message(msg, color="Black")

# Call the function with the actual list
enter_action(FIVE_LETTER_WORDS, guess_lower)

#gw = WordleGWindow()
#gw.add_enter_listener(enter_action)
