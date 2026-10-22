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
    new_card = 0
    should_continue = True

    new_card = random.choice(cards)
    user_cards.append(new_card)
    user_score += new_card

    new_card = random.choice(cards)
    cpu_cards.append(new_card)
    cpu_score += new_card

    while should_continue:

        new_card = random.choice(cards)
        user_cards.append(new_card)
        user_score += new_card

        print(f"    Your cards: {user_cards}, current score: {user_score}")
        print(f"    Computer's first card: {cpu_cards}")

        if user_score < 21:
            user_continue = input("Type 'y' to get another card, 'n' to pass: ").lower()
            if user_continue == "n":
                should_continue = False

        if user_score >= 21:
            if 11 in user_cards:
                index = user_cards.index(11)
                user_cards[index] = 1
            else:
                should_continue = False


    while cpu_score < 17:
        new_card = random.choice(cards)
        cpu_cards.append(new_card)
        cpu_score += new_card

    print(f"    Your final hand: {user_cards}, final score: {user_score}")
    print(f"    Computer's final hand: {cpu_cards}, final score: {cpu_score}")

    if user_score > 21:
        print("You went over 21, you lose!")
    elif user_score == cpu_score:
        print("It's a draw!")
    elif user_score < cpu_score:
        print("You lose!")
    else:
        print("You win!")

    return True

wanna_play = True

while wanna_play:
    blackjack()

print("Bye!")
