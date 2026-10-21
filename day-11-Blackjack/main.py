import random

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

user_cards = []
cpu_cards = []

def blackjack():
    user_continue = input("Do you wanna play Blackjack? (Y/N)").lower()
    if user_continue == "n":
        return False
    return True


wanna_play = True

while wanna_play:
    wanna_play = blackjack()