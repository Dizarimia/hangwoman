"""
imports
"""
import random
from wordlist import easy_words, hard_words

"""
game
"""


def title():
    """
    Print Hangwoman title
    """
    print("HANGWOMAN")


def instructions():
    """
    Welcome and instructions
    """

print("To play hangwoman, what you need to do is guess the word one letter at a time. Insert a letter and hit enter. If it is correct the letter gets added to the word. If your guess is wrong a part of the hangwoman image will be added. Keep guessing until you get the whole word or you run out of tries")


def startup():
    print("Welcome! Please choose difficulty: E Easy or H Hard")
    difficulty = input()
    while difficulty.upper() not in ["H", "E"]:
        print("Invalid input, choose between E & H")
        difficulty = input()
    if difficulty.upper() == "H": 
        return hard_words
    else:
        return easy_words


def replay():

    """
    image
    """
    pass

def display_word(word):
    display = ""
    for letter in word:
        display = display + " " + letter
    print(display)




def game():
    """
    Method to contain the game loop
    """
    title()
    words = startup()
    pick = random.randint(0, len(words))
    word = words[pick]
    print(word)
    display_word(word)

if __name__ == "__main__":
    game()