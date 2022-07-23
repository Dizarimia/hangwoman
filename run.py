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
    print("Would you like instructions? Press Y for Yes and N for No.")
    instruction = input()
    while instruction.upper() not in ["Y", "N"]:
        print("Invalid input, choose between Y & N")
    instruction = input()
    if instruction.upper() == "Y":
        return instructions()
    print("To play hangwoman, you need to guess the word one letter at a time."
    "Press a letter and hit enter. If it's correct it gets added to the word."
    "If your guess is wrong a part of the hangwoman image will be added."
    "Keep guessing until you get the whole word or you run out of tries")
    else:
        startup()




def startup():
    print("Welcome! Please choose difficulty: E for Easy or H for Hard")
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
    instructions()
    words = startup()
    pick = random.randint(0, len(words))
    word = words[pick]
    print(word)
    display_word(word)

if __name__ == "__main__":
    game()