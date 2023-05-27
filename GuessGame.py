import os
import random


def print_number(gen_number, guess_from_user):
    print("Genrate number -> {0}".format(gen_number))
    print("Guess number from user -> {0}".format(guess_from_user))


def generate_number(difficulty):
    secret_number = random.randint(1, difficulty)
    return secret_number


def get_guess_from_user(difficulty):
    return int(input("Please choose number between 1 to {0}:".format(difficulty)))


def compare_results(difficulty):
    gen_number = generate_number(difficulty)
    guess_from_user = get_guess_from_user(difficulty)
    if gen_number == guess_from_user:
        print_number(gen_number, guess_from_user)
        return True
    else:
        print_number(gen_number, guess_from_user)
        return False


def play(difficulty):
    os.system('cls' if os.name == 'nt' else 'clear')
    print("Start Game Guess Game :")
    print("************************* :")
    if compare_results(difficulty):
        print("You Won !!!")
        return True
    else:
        print("You Lost !!!")
        return False
