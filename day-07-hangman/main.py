import random

stages = [r'''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', r'''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', r'''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']

word_list = ["aardvark", "baboon", "camel"]

lives = 6

chosen_word = random.choice(word_list)

placeholder = ""
for letter in chosen_word:
    placeholder += "_"

is_end = False
guessed_letters = []

while not is_end:

    print(stages[lives])
    print(f"Number of lives: {lives}")
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

    if guess not in chosen_word:
        lives -= 1

    if lives == 0:
        is_end = True
        print(stages[lives])
        print("You lose!")

    if "_" not in display:
        is_end = True
        print("You win!")