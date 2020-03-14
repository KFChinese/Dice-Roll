from random import seed
from random import randint
from os import system, name
import time


def clear():

    # for windows
    if name == "nt":
        _ = system("cls")

    # for mac and linux(here, os.name is 'posix')
    else:
        _ = system("clear")


def intro():
    print("Welcome To Dice Roller.")
    time.sleep(2.5)


def get_amount():
    while True:
        clear()
        print("How many dice are you rolling?")
        amount = input("Enter amount: ")
        try:
            val = int(amount)
            if val >= 0:
                break
            else:
                clear()
                print("Amount can't be negative, try again")
        except ValueError:
            clear()
            print("Amount must be a number, try again")
    return val


def range_dice():
    while True:
        clear()
        print("How many sides does the dice have?")
        amount = input("Enter amount: ")
        try:
            val = int(amount)
            if val >= 0:
                break
            else:
                clear()
                print("Amount can't be negative, try again")
        except ValueError:
            clear()
            print("Amount must be a number, try again")
    return val


def roll(qty_die, die_rng):
    clear()
    print("Rolling...")
    seed(1)  # seed random number generator
    for _ in range(qty_die):
        print("The Dice rolled:", randint(1, die_rng), "\b!")


def main():
    clear()
    intro()
    qty_die = get_amount()
    die_rng = range_dice()
    roll(qty_die, die_rng)
    while input("Roll Again? (Y/N):").upper() == "Y":
        clear()
        intro()
        qty_die = get_amount()
        die_rng = range_dice()
        roll(qty_die, die_rng)


if __name__ == "__main__":
    main()
