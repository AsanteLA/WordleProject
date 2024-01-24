# File: Wordle.py

"""
This module is the starter file for the Wordle assignment.
BE SURE TO UPDATE THIS COMMENT WHEN YOU WRITE THE CODE.
"""

import random
from WordleDictionary import FIVE_LETTER_WORDS
from WordleGraphics import WordleGWindow, N_COLS, N_ROWS, PRESENT_COLOR, CORRECT_COLOR, UNKNOWN_COLOR, MISSING_COLOR

def wordle():

    def enter_action(s, random_word):
        gw.show_message(random_word)
        
        if s.lower() in FIVE_LETTER_WORDS:
            for col, char in enumerate(random_word):
                if s[col].lower() == char.lower():
                    gw.set_square_color(gw.get_current_row(), col, CORRECT_COLOR)
                    gw.set_key_color(s[col].upper(), CORRECT_COLOR)
                elif s[col].lower() in random_word.lower():
                    gw.set_square_color(gw.get_current_row(), col, PRESENT_COLOR)
                    gw.set_key_color(s[col].upper(), PRESENT_COLOR)
                else:
                    gw.set_square_color(gw.get_current_row(), col, MISSING_COLOR)
                    gw.set_key_color(s[col].upper(), MISSING_COLOR)
                    
            if s.lower() == random_word.lower():
                gw.show_message("You win!")
                gw.close()
                
            next_row = gw.get_current_row() + 1
            if next_row < N_ROWS:
                gw.set_current_row(next_row)
        else:
            gw.show_message("Not in word list!")    
    
    random_word = random.choice(FIVE_LETTER_WORDS)       

    gw = WordleGWindow()
    gw.add_enter_listener(lambda s: enter_action(s, random_word))

# Startup code

if __name__ == "__main__":
    wordle()
