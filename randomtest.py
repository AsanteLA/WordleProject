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