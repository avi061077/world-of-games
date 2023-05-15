import requests
from datetime import date
import random

# from currency_converter import CurrencyConverter
# import py_currency_converter
from py_currency_converter import convert
# import py_currency_converter


def get_money_interval(difficulty, random_amount_usd):
    usd_to_nis = convert(base='USD', amount=random_amount_usd, to=['ILS'])['ILS']
    interval = ((usd_to_nis - (5 - difficulty)), (usd_to_nis + (5 - difficulty)))
    return interval


def get_guess_from_user(random_amount_usd):
    user_selected_number = input("How much Shekels is " + str(random_amount_usd) + "$? ")
    while not (user_selected_number.isdigit()):
        user_selected_number = (input("Type a number -  How much Shekels is " + str(random_amount_usd) + "$? "))
    return user_selected_number


def play(user_difficulty):
    print("======== Welcome to CurrencyRouletteGame =========")
    random_amount_usd = random.randint(1, 100)
    usd_to_nis = convert(base='USD', amount=random_amount_usd, to=['ILS'])['ILS']
    interval = get_money_interval(user_difficulty, random_amount_usd)
    user_selected_number = get_guess_from_user(random_amount_usd)
    if interval[0] < int(user_selected_number) < interval[1]:
        print("YOU WIN!!! The number was " + str(usd_to_nis))
        win = True
    else:
        print("Wrong guess! The number was " + str(usd_to_nis))
        win = False
    return win



