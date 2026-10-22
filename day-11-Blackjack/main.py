import random

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]


def blackjack():
    user_play = input("Do you wanna play Blackjack? (Y/N)").lower()
    if user_play == "n":
        return False

    user_cards = []
    user_score = 0
    cpu_cards = []
    cpu_score = 0
    should_continue = True

    user_cards.append(random.choice(cards))
    cpu_cards.append(random.choice(cards))

    while should_continue:

        user_cards.append(random.choice(cards))

        print(f"    Your cards: {user_cards}, current score: {user_score}")
        print(f"    Computer's first card: {cpu_cards}")

        user_continue = input("Type 'y' to get another card, 'n' to pass: ").lower()

        if user_score > 21 and 11 in user_cards:
            index = user_cards.index("11")
            user_cards[index] = 1

        if user_score > 21 or user_continue == "n":
            should_continue = False

    while cpu_score < 17:
        pass

    return True

wanna_play = True

while wanna_play:
    blackjack()

print("Bye!")
