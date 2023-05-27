import os
import random


def print_list(l1, l2):
    print("List 1 -> {0}".format(l1))
    print("List 2 -> {0}".format(l2))


def generate_sequence(difficulty):
    l1 = []
    for i in range(difficulty):
        l1.append(random.randint(1, 101))
    return l1


def get_list_from_user(difficulty):
    l2 = []
    for i in range(difficulty):
        l2.append(int(input("Please add a number for list: ")))
    return l2


def is_list_equal(difficulty):
    l1 = generate_sequence(difficulty)
    l2 = get_list_from_user(difficulty)
    l1.sort()
    l2.sort()
    if l1 == l2:
        print_list(l1, l2)
        print("You Won !!!")
        return True
    else:
        print_list(l1, l2)
        print("You Lost !!!")
        return False


def play(difficulty):
    os.system('cls' if os.name == 'nt' else 'clear')
    print("Start Game Memory Game :")
    print("************************* :")
    if is_list_equal(difficulty):
        print("The two lists are identical !!")
    else:
        print("The two lists are different !!")
