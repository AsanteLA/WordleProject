# File: Wordle.py

"""
This module is the starter file for the Wordle assignment.
BE SURE TO UPDATE THIS COMMENT WHEN YOU WRITE THE CODE.
"""

import random

from WordleDictionary import FIVE_LETTER_WORDS
from WordleGraphics import WordleGWindow, N_COLS, N_ROWS

def wordle(gw, guess_lower):
    def enter_action(FIVE_LETTER_WORDS, guess_lower):
        if guess_lower in FIVE_LETTER_WORDS:
            msg = "Good try! This is a word!"
            gw.show_message(msg, color="Black")
        else:
            msg = "Not in word list"
            gw.show_message(msg, color="Black")
    
    gw = WordleGWindow()
    gw.add_enter_listener(enter_action)

# Startup code

if __name__ == "__main__":
    #Selectong the random word
    random_word = random.choice(FIVE_LETTER_WORDS)

    #Breaking down a word into a list of characters
    charlist = list(random_word)

    #Revelaing the cosen random word
    print('Random Word:', random_word)

    #Printing chatracterr list in array format
    print(charlist)

    # Breaking down a word into a list of characters
    charlist = list(random_word)

    # Revealing the chosen random word
    print('Random Word:', random_word)

    # Printing character list in array format
    print(charlist)

    wordle_window = WordleGWindow()
    # Loop to set each character in the Wordle window horizontally
    for col, ch in enumerate(charlist):
        # Set the character in row 0 (you can adjust the row as needed)
        wordle_window.set_square_letter(0, col, ch)

    # Wait for user interaction (optional)
    input("Press Enter to exit")
    guess = ''
    for row in range(N_ROWS):
        for col in range(N_COLS):
            guess += wordle_window.get_square_letter(row, col) 

    guess_lower = guess.lower()

    guess_lower = guess_lower.strip()
    
    wordle(wordle_window, guess_lower)
