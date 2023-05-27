
from MemoryGame import play as play_memory
from GuessGame import play as play_guess_game
from CurrencyRouletteGame import play as play_roulette_game
from Score import add_score

def welcome(name):
    return "Hello {0} and welcome to the World of Games (WoG).\nHere you can find many cool games to play.".format(name)


def load_game():
    print("Please choose a game to play:")
    print("1. Memory Game - a sequence of numbers will appear for 1 second and you have to guess it back")
    print("2. Guess Game - guess a number and see if you chose like the computer")
    print("3. Currency Roulette - try and guess the value of a random amount of USD in ILS")
    user_game = int(input("Please choose game from 1 to 3: "))
    while user_game < 0 or user_game > 3:
        user_game = int(input("Please choose game from 1 to 3: "))
    user_difficult = int(input("Please choose game difficulty from 1 to 5: "))
    while user_difficult < 0 or user_difficult > 5:
        user_difficult = int(input("Please choose game difficulty from 1 to 5: "))
    if user_game == 1:
        if play_memory(user_difficult):
            add_score(user_difficult)
    elif user_game == 2:
        if play_guess_game(user_difficult):
            add_score(user_difficult)
    elif user_game == 3:
        if play_roulette_game(user_difficult):
            add_score(user_difficult)


load_game()