import random
from words import words
import string

def get_valid_word(words):
    word = random.choice(words)
    # print(word)
    while '-' in word or ' ' in word:
        word = random.choice(words)

    return word.upper()


def hangman():
    word = get_valid_word(words)
    word_letters = set(word) # letters in the word. 
    alphabet = set(string.ascii_uppercase)
    used_letters = set() # what user has guessed.

    # get user input:
    while len(word_letters) > 0:
        #letters used already
        print('You have guessed these letters: ', ' '.join(used_letters))

        #what the current word is with dashed for letters not guessed correctly yet.
        word_list = [letter if letter in used_letters else '-' for letter in word]
        print('Current Word: ', ' '.join(word_list))

        user_letter = input('Guess A Letter: ').upper()
        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter)

        elif user_letter in used_letters:
            print('You have already guessed this letter. Please try again.')
        
        else:
            print('Invalid character. Please try again.')


hangman()
