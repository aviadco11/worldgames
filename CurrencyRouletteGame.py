import os
import random
import requests
import json


def print_results(interval, rate, num_guess_user):
    print("rate exchange USD->ILS: {:.2f}".format(rate))
    print("Your Guess number: {:.2f}".format(num_guess_user))
    print("interval: ({:.2f}, {:.2f})".format(interval[0], interval[1]))


def get_exchange_rate():
    response = requests.get("https://anyapi.io/api/v1/exchange/convert?base=USD&to=ILS&amount=1&apiKey"
                            "=rk0e8a9lrmookc24emuvtg8brt9deu7kos1h39jor0dujqilb616t")
    return json.loads(response.content)["rate"]


def get_money_interval(currency_rate, difficulty, amount_usd):
    return float(currency_rate * amount_usd - (5 - difficulty)), float(currency_rate * amount_usd + (5 - difficulty))


def get_guess_from_user(amount_usd):
    return float(input("enter a guess of value ILS to a given amount of USD {0}: ".format(amount_usd)))


def play(difficulty):
    os.system('cls' if os.name == 'nt' else 'clear')
    print("Start Game Currency Roulette Game :")
    print("**************************************** :")
    amount_usd = random.randint(1, 100)
    num_guess_user = get_guess_from_user(amount_usd)
    rate = get_exchange_rate()
    interval = get_money_interval(rate, difficulty, amount_usd)
    print_results(interval, rate, num_guess_user)
    if interval[0] < num_guess_user < interval[1]:
        print("You Won !!!")
        return True
    else:
        print("You Lost !!!")
        return False
