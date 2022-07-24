"""
imports
"""
import random
from wordlist import easy_words, hard_words

"""
game
"""
guesses = []   
letter_guessed = "" 
tries = 6
# letter_guessed = leter_guessed + guess
# wrong_guess = 0

def title():
    """
    Print Hangwoman title
    """
    print("HANGWOMAN")
"""
imports
"""
import random
from wordlist import easy_words, hard_words

"""
game
"""
guesses = []
letter_guessed = ""
tries = 6
# letter_guessed = leter_guessed + guess
# wrong_guess = 0


def title():
    """
    Print Hangwoman title
    """
    print("HANGWOMAN")


def instructions():
    """
    Welcome and instructions
    """
    print("Welcome! Would you like instructions? Press Y for Yes and N for No.")
    instruction = input()
    while instruction.upper() not in ["Y", "N"]:
        print("Invalid input, choose between Y & N")
        instruction = input()
    if instruction.upper() == "Y":
        print(f"To play hangwoman, you need to guess the word one letter at a time."
              "Press a letter and hit enter. If correct it gets added to the word."
              "If your guess is wrong a part of the hangwoman image will be added."
              "Keep guessing until you get the whole word or you run out of tries.")
        print()


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


# while tries > 0:
#     guess = input("Enter a letter: ")

#     if guess in word:
#         print(f"YAY! There is one or more {guess} in the word.")
#     else:
#         tries -= 1
#         print(f"NOPE! No {guess} in the word. {tries} turn(s) left.")


def get_guess():
    print("Guess a letter")
    guess = input()
    while not guess.isalpha():
        print("Invalid input please choose a letter")
        guess = input()

    while guess.upper() in guesses:
        print("You already guessed this letter")
        guess = input()

    guesses.append(guess.upper())
    return guess.upper()


def validate_answer(word, guess):
    for letter in word:
        if letter = guess:
            return True
    return False


def display_word(word):
    display = ""
    for letter in word:
        if letter in letter_guessed:
            print(f"{letter}", end="")
        else:
            print(f"_", end="")
            wrong_guess += 1
        print("")
    if wrong_guess == 0:
        print(f"WOHO! The word was: {pick}. You win!")

        display = display + " " + letter
        print(display)
        # while tries > 0 and len(words) > 0:

        print("Sorry! Better luck next time.")


def hangman_img(tries):
    """
    Drawing of the hangman image.
    """
    stages = [
        """
            --------
            |      |
            |      o
            |     \\|/
            |      |
            |     / \\
            ---
            """,
        """
            --------
            |      |
            |      o
            |     \\|/
            |      |
            |     /
            ---
            """,
        """
            --------
            |      |
            |      o
            |     \\|/
            |      |
            |
            ---
            """,
        """
            --------
            |      |
            |      o
            |     \\|
            |      |
            |
            ---
            """,
        """
            --------
            |      |
            |      o
            |      |
            |      |
            |
            ---
            """,
        """
            --------
            |      |
            |      o
            |
            |
            |
            ---
            """,
        """
            --------
            |      |
            |
            |
            |
            |
            ---
            """,
    ]
    return stages[tries]


def replay():

    """
    image
    """
    pass


def game():
    """
    Method to contain the game loop
    """
    guesses = 0
    title()
    instructions()
    words = startup()
    pick = random.randint(0, len(words))
    word = words[pick]
    print(word)
    display_word(word)
    guess = get_guess()
    correct = validate_answer(word, guess)
    if not correct:
        tries +-1
    print(hangman_img(6-tries))

if __name__ == "__main__":
    game()


def instructions():
    """
    Welcome and instructions
    """
    print("Welcome! Would you like instructions? Press Y for Yes and N for No.")
    instruction = input()
    while instruction.upper() not in ["Y", "N"]:
        print("Invalid input, choose between Y & N")
        instruction = input()
    if instruction.upper() == "Y":
        print(f"To play hangwoman, you need to guess the word one letter at a time."
          "Press a letter and hit enter. If correct it gets added to the word."
          "If your guess is wrong a part of the hangwoman image will be added."
          "Keep guessing until you get the whole word or you run out of tries.")
        print()




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
    


# while tries > 0:
#     guess = input("Enter a letter: ")

#     if guess in word: 
#         print(f"YAY! There is one or more {guess} in the word.")
#     else:
#         tries -= 1
#         print(f"NOPE! No {guess} in the word. {tries} turn(s) left.")

#     

def get_guess():
    print("Guess a letter")
    guess = input()
    while not guess.isalpha():
        print("Invalid input please choose a letter")
        guess = input()

    while guess.upper() in guesses:
        print("You already guessed this letter")
        guess = input()

    guesses.append(guess.upper())
    return guess.upper()

def validate_answer(word, guess):
    for letter in word:
        if letter = guess:
            return True
    return False    

def display_word(word):
    display = ""
    for letter in word:
        if letter in letter_guessed:
            print(f"{letter}", end="")
        else:
            print(f"_", end="")
            wrong_guess += 1
        print("")
    if wrong_guess == 0:
        print(f"WOHO! The word was: {pick}. You win!")

        display = display + " " + letter
        print(display)
        # while tries > 0 and len(words) > 0:

        print("Sorry! Better luck next time.")


def hangman_img(tries):
    """
    Drawing of the hangman image.
    """
    stages = [
        """
            --------
            |      |
            |      o
            |     \\|/
            |      |
            |     / \\
            ---
            """,
        """
            --------
            |      |
            |      o
            |     \\|/
            |      |
            |     /
            ---
            """,
        """
            --------
            |      |
            |      o
            |     \\|/
            |      |
            |
            ---
            """,
        """
            --------
            |      |
            |      o
            |     \\|
            |      |
            |
            ---
            """,
        """
            --------
            |      |
            |      o
            |      |
            |      |
            |
            ---
            """,
        """
            --------
            |      |
            |      o
            |
            |
            |
            ---
            """,
        """
            --------
            |      |
            |
            |
            |
            |
            ---
            """,
    ]
    return stages[tries]


def replay():

    """
    image
    """
    pass



def game():
    """
    Method to contain the game loop
    """
    guesses = 0
    title()
    instructions()
    words = startup()
    pick = random.randint(0, len(words))
    word = words[pick]
    print(word)
    display_word(word)
    guess = get_guess()
    correct = validate_answer(word, guess)
    if not correct: 
        tries +- 1
    print(hangman_img(6-tries))

if __name__ == "__main__":
    game()