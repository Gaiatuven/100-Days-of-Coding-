import random


def intro():
    board = []
    EASY = 10
    HARD = 5
    word_list = ['apple', 'banana', 'strawberry']
    secret_word = random.choice(word_list)
    word_length = len(secret_word)
    print()
    print("Welcome to our Word Guessing Game\n"
          "Rules: Guess the secret Word\n")
    for _ in secret_word:
        board += "_"
    print(board)
    choice = input("Guess a letter: ")
    return choice


def difficulty():
    level = input("Select a difficulty level 'Easy' or 'Hard': ").lower()
    return level


def display(choice, level):
    board = []
    EASY = 10
    HARD = 5
    word_list = ['apple', 'banana', 'strawberry']
    secret_word = random.choice(word_list)
    word_length = len(secret_word)
    for _ in secret_word:
        board += "_"
    print(board)
    max_tries = EASY if level == 'easy' else HARD
    tries = 0
    print(f'You get {max_tries} to guess the Secret Word !!')
        while tries < max_tries == word_length:
            # if _ in " ".join(word_length):
            


intro()

