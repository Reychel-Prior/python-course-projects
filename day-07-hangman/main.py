import random

word_list = ["aardvark", "baboon", "camel"]
chosen_word = random.choice(word_list)

placeholder = ""
for letter in chosen_word:
    placeholder += "_"

guess = input("Make your guess: ").lower()

# TODO-2: Create a "display" that puts the guess letter in the right positions and _ in the rest of the string.

display = ""

for letter in chosen_word:
    if letter == guess:
        display += letter
    else:
        display += "_"
print(chosen_word)
print(display)