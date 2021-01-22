import random
from words import words


def get_valid_word(words):
    word = random.choice(words)
    # print(word)
    while '-' in word or ' ' in word:
        word = random.choice(words)

    return word.upper()


