"""
This module is the starter file for the Wordle assignment.
BE SURE TO UPDATE THIS COMMENT WHEN YOU WRITE THE CODE.
"""

import random
import tkinter
from WordleDictionary import FIVE_LETTER_WORDS
from WordleGraphics import WordleGWindow, N_COLS, N_ROWS, PRESENT_COLOR, CORRECT_COLOR, UNKNOWN_COLOR, MISSING_COLOR, MISSING_COLOR_BLD, CORRECT_COLOR_BLD, PRESENT_COLOR_BLD

def wordle():
    def enter_action(s, random_word):
        #gw.show_message(random_word)

        if s.lower() in FIVE_LETTER_WORDS:
            print(s.lower())
            print(random_word)
            for col, char in enumerate(random_word):
                if not any (char in s for char in gw.hardmode_list):
                    print("Must use guess letters!")
                    break
                if s[col].lower() == char.lower() and s[col].lower() in gw.hardmode_list:
                    print(f"Colorblind mode: {gw._colorblind_mode}")  # Print colorblind mode status
                    if gw._colorblind_mode:
                        gw.set_square_color(gw.get_current_row(), col, CORRECT_COLOR_BLD)
                        gw.set_key_color(s[col].upper(), CORRECT_COLOR_BLD)
                        print("Colorblind mode1: Setting square color to CORRECT_COLOR")
                        gw.hardmode_list.append(s[col].lower())

                    else:
                        gw.set_square_color(gw.get_current_row(), col, CORRECT_COLOR)
                        print("Colorblind mode2: Setting square color to CORRECT_COLOR")
                        gw.set_key_color(s[col].upper(), CORRECT_COLOR)
                        gw.hardmode_list.append(s[col].lower())

                elif s[col].lower() in random_word.lower():
                    if gw._colorblind_mode:
                        gw.set_square_color(gw.get_current_row(), col, PRESENT_COLOR_BLD)
                        gw.set_key_color(s[col].upper(), PRESENT_COLOR_BLD)
                        print("Colorblind mode3: Setting square color to PRESENT_COLOR")
                        gw.hardmode_list.append(s[col].lower())

                    else:
                        gw.set_square_color(gw.get_current_row(), col, PRESENT_COLOR)
                        print("Colorblind mode4: Setting square color to PRESENT_COLOR")
                        gw.set_key_color(s[col].upper(), PRESENT_COLOR)
                        gw.hardmode_list.append(s[col].lower())
                        print(gw.hardmode_list)

                else:
                    if gw._colorblind_mode:
                        gw.set_square_color(gw.get_current_row(), col, MISSING_COLOR_BLD)
                        gw.set_key_color(s[col].upper(), MISSING_COLOR_BLD)
                        print("Colorblind mode5: Setting square color to MISSING_COLOR")
                    else:
                        gw.set_square_color(gw.get_current_row(), col, MISSING_COLOR)
                        print("Colorblind mode6: Setting square color to MISSING_COLOR")
                        gw.set_key_color(s[col].upper(), MISSING_COLOR)

            if s.lower() == random_word.lower():
                gw.show_message("You win! Wordle in " + str(gw.get_current_row() + 1))
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
    
    