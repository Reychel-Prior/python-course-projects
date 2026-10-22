import random

def number_guessing_game():

    number_to_guess = random.randint(0, 100)
    lives = 0

    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 0 and 100!")
    difficulty = input("Type 'easy' or 'hard': ").lower()
    if difficulty == "easy":
        lives = 10
    else:
        lives = 5

    print(f"NUMBER TO GUESS: {number_to_guess}")

    while lives > 0:

        print(f"You have {lives} attempts remaining to guess the number.")
        guess = int(input("Make a guess: "))

        if guess == number_to_guess:
            return True

        if guess > number_to_guess:
            print("Too high.")
        else:
            print("Too low.")
        print("Guess again.")

        lives -= 1
        if lives == 0:
            return False


if number_guessing_game():
    print("You won!")
else:
    print("You lose! You ran out of guesses!")




