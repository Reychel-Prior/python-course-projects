import random

word_list = ["aardvark", "baboon", "camel"]
chosen_word = random.choice(word_list)

placeholder = ""
for letter in chosen_word:
    placeholder += "_"

is_end = False
guessed_letters = []

while not is_end:

    guess = input("Make your guess: ").lower()
    display = ""

    for letter in chosen_word:
        if letter in guessed_letters:
            display += letter
        elif letter == guess:
            display += letter
            guessed_letters.append(guess)
        else:
            display += "_"
    print(chosen_word)
    print(display)

    if "_" not in display:
        is_end = True
print("Out of the while loop")